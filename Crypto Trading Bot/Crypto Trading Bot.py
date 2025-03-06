# Importing .env library to load file
import os  # Importing OS Library to load .env file
import time
import pandas as pd
from binance.client import Client  # Importing Binance platform
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
api_key = os.getenv("APIKey")
secret = os.getenv("Secret")
client = Client(api_key, secret, testnet=True)
# Logging into Binance platform using API Key and Secret
# Enabling Testing environment


# Define trading parameters
symbol = "BTCUSDT"
buy_price_threshold = 89000
sell_price_threshold = 90000
trade_quantity = 0.001


# Get current BTC price in relation to US Dollars
def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])


# Place market buy order
def place_buy_order(symbol, quantity):
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    print(f"Buy order done: {order}\n")


# Place market sell order
def place_sell_order(symbol, quantity):
    order = client.order_market_sell(symbol=symbol, quantity=quantity)
    print(f"Sell order done: {order}\n")


# Automated trading bot logic
def trading_bot():
    in_position = False
    while True:
        current_price = get_current_price(symbol)
        print(f"Current price of {symbol}: {current_price}")

        if not in_position:
            if current_price < buy_price_threshold:
                print(f"Price is below {buy_price_threshold}. Placing Buy order.")
                place_buy_order(symbol, trade_quantity)
                in_position = True
        else:
            if current_price > sell_price_threshold:
                print(f"Price is above {sell_price_threshold}. Placing Sell order.")
                place_sell_order(symbol, trade_quantity)
                in_position = False
        time.sleep(2)  # Pause before fetching the next price


def get_historical_data(symbol, interval, limit=1000):
    # Fetch historical Kline (candlestick) data from Binance

    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume", 
        "close_time", "quote_asset_volume", "trades", 
        "taker_base_vol", "taker_quote_vol", "ignore"
    ])
    # Creating a dataframe using the historical data and the collumns

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    # Formatting the timestamp with its ms time unit
    # Indexing timestamp

    
    
    for col in ["open", "high", "low", "close"]:
        df[col] = df[col].astype(float)

    return df
    # Convert price columns to float

# Convert price columns to float

interval = Client.KLINE_INTERVAL_1MINUTE
historical_data = get_historical_data(symbol, interval)



def backtest_strategy(df, buy_price_threshold, sell_price_threshold, trade_quantity):
    #Simulates a trading strategy on historical data


    balance = 20000  # Start with $20000
    btc_holding = 0  # No BTC at start
    trades = []  # Store trade history

    for index, row in df.iterrows():
        price = row["close"]

        if price < buy_price_threshold:
            # Buy BTC 
            balance -= price * trade_quantity
            btc_holding += trade_quantity
            trades.append((index, price, "BUY"))
            print(f"Bought at {price} on {index}")

        elif price > sell_price_threshold:
            # Sell BTC
            balance += price * trade_quantity
            btc_holding -= trade_quantity
            trades.append((index, price, "SELL"))
            print(f"Sold at {price} on {index}")

    final_balance = balance + (btc_holding * row["close"])
    profit = final_balance - 10000
    
    return balance, trades, final_balance, profit

balance, trades, final_balance, profit= backtest_strategy(historical_data, buy_price_threshold, sell_price_threshold, trade_quantity)

# Main function
def main():

    print(f"Current cash liquidity: $ {balance:.2f}")
    print(f"Final balance: ${final_balance:.2f}, Profit: ${profit:.2f}")
  
    

if __name__ == "__main__":
    main()
