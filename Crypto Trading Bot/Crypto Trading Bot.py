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
class trade_parameters:
    def __init__(self, buy_threshold, second_buy_threshold, sell_threshold, second_sell_threshold, stop_loss, quantity):
        self.buy_threshold = buy_threshold
        self.second_buy_threshold = second_buy_threshold
        self.sell_threshold = sell_threshold
        self.second_sell_threshold = second_sell_threshold
        self.stop_loss = stop_loss
        self.quantity = quantity



#defines market data parameters
class market_data:
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
class trading_bot:
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
        while True:
            current_price = market_data(self.symbol).get_current_price()
            print(f"Current price of {self.symbol}: {current_price}")

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
            else:
                if current_price > self.trade_params.sell_threshold:
                    print(f"Price above {self.trade_params.sell_threshold}, selling.")
                    self.place_sell_order()
                    if current_price > self.trade_params.second_sell_threshold:
                        self.place_sell_order()
                    self.in_position = False
            time.sleep(2)

class backtester:
    def __init__(self, df, trade_params):
        self.df = df
        self.trade_params = trade_params
        self.balance = 20000  # Starting balance
        self.btc_holding = 1
        self.trades = []

    def run_backtest(self):
        for index, row in self.df.iterrows():
            price = row["close"]
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

            if price > self.trade_params.sell_threshold and self.btc_holding > 0:
                self.balance += price * self.trade_params.quantity
                self.btc_holding -= self.trade_params.quantity
                self.trades.append((index, price, "SELL"))
                if price > self.trade_params.second_sell_threshold:
                    self.balance += price * self.trade_params.quantity
                    self.btc_holding -= self.trade_params.quantity
                    self.trades.append((index, price, "SELL"))

        final_balance = self.balance + (self.btc_holding * row["close"])
        profit = final_balance - 20000
        final_profit = profit - (1 * row["close"])
        return final_profit, self.btc_holding, self.balance, final_balance, profit

# Initialize classes
symbol = "BTCUSDT"
trade_params = trade_parameters(83000, 81000, 83100, 85000, 78000, 0.001)
market_data = market_data(symbol, Client.KLINE_INTERVAL_1MINUTE)
historical_data = market_data.get_historical_data()

backtester = backtester(historical_data, trade_params)
final_profit, btc_holding, balance, final_balance, profit = backtester.run_backtest()

# Main function
def main():
    print(f"Current cash balance: $ {balance:.2f}")
    print(f"Bitcoin currently holding: {btc_holding:.2f}")
    print(f"Bitcoin Assets + Cash Balance: ${final_balance:.2f}, Profit: ${final_profit:.2f}")
    print(market_data.get_current_price())

if __name__ == "__main__":
    main()
