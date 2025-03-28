import os
import time
import pandas as pd
from binance.client import Client
from dotenv import load_dotenv



#load API keys / Secret from .env file
load_dotenv()
api_key = os.getenv("APIKey")
secret = os.getenv("Secret")
client = Client(api_key, secret, testnet=True)



#defines the parameters of all the thresholds such as buy/sell/stop loss/quantity, etc
class TradeParameters:
    def __init__(self, buy_threshold, second_buy_threshold, sell_threshold, second_sell_threshold, stop_loss, quantity):
        self.buy_threshold = buy_threshold
        self.second_buy_threshold = second_buy_threshold
        self.sell_threshold = sell_threshold
        self.second_sell_threshold = second_sell_threshold
        self.stop_loss = stop_loss
        self.quantity = quantity



#defines market data parameters
class MarketData:
    def __init__(self, symbol, interval, limit=1000):
        self.symbol = symbol
        self.interval = interval
        self.limit = limit

    #function gets ticks of data worth of 1000 minutes 
    def get_historical_data(self):
        klines = client.get_klines(symbol=self.symbol, interval=self.interval, limit=self.limit)
        df = pd.DataFrame(klines, columns=[
            "timestamp", "open", "high", "low", "close", "volume", "close_time",
            "quote_asset_volume", "trades", "taker_base_vol", "taker_quote_vol", "ignore"
        ])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)
        for col in ["open", "high", "low", "close"]:
            df[col] = df[col].astype(float)
        return df

    #gets the current price of the symbol being traded
    def get_current_price(self):
        ticker = client.get_symbol_ticker(symbol=self.symbol)
        return float(ticker["price"])



#calls trading bot with parameters
class TradingBot:
    def __init__(self, symbol, trade_params):
        self.symbol = symbol
        self.trade_params = trade_params
        self.in_position = False

    #places buy order
    def place_buy_order(self):
        order = client.order_market_buy(symbol=self.symbol, quantity=self.trade_params.quantity)
        print(f"Buy order done: {order}\n")

    #places sell order
    def place_sell_order(self):
        order = client.order_market_sell(symbol=self.symbol, quantity=self.trade_params.quantity)
        print(f"Sell order done: {order}\n")

    #defines the trading bot function
    def start_trading(self):
        
        #while you've bought some BTC, do:
        while True:
            current_price = MarketData(self.symbol).get_current_price()
            print(f"Current price of {self.symbol}: {current_price}")

            #buy order / stop loss thresholds
            if not self.in_position:
                if current_price < self.trade_params.buy_threshold:
                    print(f"Price below {self.trade_params.buy_threshold}, buying.")
                    self.place_buy_order()
                    if current_price < self.trade_params.second_buy_threshold:
                        self.place_buy_order()
                    self.in_position = True
                    if current_price < self.trade_params.stop_loss:
                        self.place_sell_order()
                        self.in_position = False

            #sell order / take profit thresholds
            else:
                if current_price > self.trade_params.sell_threshold:
                    print(f"Price above {self.trade_params.sell_threshold}, selling.")
                    self.place_sell_order()
                    if current_price > self.trade_params.second_sell_threshold:
                        self.place_sell_order()
                    self.in_position = False
            
            #pausing time for the API
            time.sleep(2)



#defining Backtester class
class Backtester:
    def __init__(self, df, trade_params):
        self.df = df
        self.trade_params = trade_params
        self.balance = 20000  # Starting balance
        self.btc_holding = 1
        self.trades = []

    #running backtest function
    def run_backtest(self):
        for index, row in self.df.iterrows():

            #get price at close 
            price = row["close"]

            #buy order / stop loss thresholds
            if price < self.trade_params.buy_threshold and self.balance >= (price * self.trade_params.quantity):
                self.balance -= price * self.trade_params.quantity
                self.btc_holding += self.trade_params.quantity
                self.trades.append((index, price, "BUY"))
                if price < self.trade_params.second_buy_threshold:
                    self.balance -= price * self.trade_params.quantity
                    self.btc_holding += self.trade_params.quantity
                    self.trades.append((index, price, "BUY"))
                if price < self.trade_params.stop_loss:
                    self.balance += price * self.trade_params.quantity
                    self.btc_holding -= self.trade_params.quantity
                    self.trades.append((index, price, "SELL-Stop Loss"))

            #sell order / take profit thresholds
            if price > self.trade_params.sell_threshold and self.btc_holding > 0:
                self.balance += price * self.trade_params.quantity
                self.btc_holding -= self.trade_params.quantity
                self.trades.append((index, price, "SELL"))
                if price > self.trade_params.second_sell_threshold:
                    self.balance += price * self.trade_params.quantity
                    self.btc_holding -= self.trade_params.quantity
                    self.trades.append((index, price, "SELL"))

        final_balance = self.balance + (self.btc_holding * row["close"])
        cashprofit = final_balance - 20000
        final_profit = cashprofit - (1 * row["close"])
        return final_profit, self.btc_holding, self.balance, final_balance, cashprofit



#calls the main backtest function which takes in all the parameters
def run_custom_backtest(symbol, buy_threshold, second_buy_threshold, sell_threshold, second_sell_threshold, stop_loss, quantity):
    
    #makes a variable that feeds its trade parameters into the class "Trade Parameters"
    trade_params = TradeParameters(buy_threshold, second_buy_threshold, sell_threshold, second_sell_threshold, stop_loss, quantity)

    #makes a variable that feeds the bitcoin symbol into the MarketData class and retrieves the prices per minute interval
    market = MarketData(symbol, Client.KLINE_INTERVAL_1MINUTE)

    #feeds data into variable
    historical_data = market.get_historical_data()
    
    backtest = Backtester(historical_data, trade_params)
    final_profit, btc_holding, balance, final_balance, cashprofit = backtest.run_backtest()
    
    print(f"Custom Backtest Results for {symbol}:")
    print(f"Cash Balance: ${balance:.2f}")
    print(f"BTC Holding: {btc_holding:.2f}")
    print(f"Profit: ${final_profit:.2f}")
    print(market.get_current_price())



# Main function
def main():

    run_custom_backtest(
        symbol = "BTCUSDT", 
        buy_threshold= 84200, 
        second_buy_threshold= 82000, 
        sell_threshold= 85000, 
        second_sell_threshold=87000, 
        stop_loss= 81000, 
        quantity= 0.001
    )
    
if __name__ == "__main__":
    main()
