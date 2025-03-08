# Import necessary libraries
import os
import time
import pandas as pd
from binance.client import Client
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
api_key = os.getenv("APIKey")
secret = os.getenv("Secret")
client = Client(api_key, secret, testnet=True)

# Define trading parameters
symbol = "BTCUSDT"
buy_price_threshold = 86000
sell_price_threshold = 92000
trade_quantity = 0.001

# Get current BTC price
def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])

# Fetch historical market data
def get_historical_data(symbol, interval, limit=1000):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume", "close_time",
        "quote_asset_volume", "trades", "taker_base_vol", "taker_quote_vol", "ignore"
    ])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    for col in ["open", "high", "low", "close"]:
        df[col] = df[col].astype(float)
    return df

interval = Client.KLINE_INTERVAL_1MINUTE
historical_data = get_historical_data(symbol, interval)

# Simulated backtesting function
def backtest_strategy(df, buy_price_threshold, sell_price_threshold, trade_quantity):
    balance = 20000  # Initial balance ($20,000)
    btc_holding = 1  # Initial Bitcoin holdings
    trades = []
    
    for index, row in df.iterrows():
        price = row["close"]
        if price < buy_price_threshold and balance >= (price * trade_quantity):
            balance -= price * trade_quantity
            btc_holding += trade_quantity
            trades.append((index, price, "BUY"))
            print(f"Bought at {price} on {index}")
        if price > sell_price_threshold and btc_holding > 0:
            balance += price * trade_quantity
            btc_holding -= trade_quantity
            trades.append((index, price, "SELL"))
            print(f"Sold at {price} on {index}")
    
    final_balance = balance + (btc_holding * row["close"])
    profit = final_balance - 20000
    final_profit = profit - (1 * row["close"])
    current_btc_value = btc_holding * price
    
    return final_profit, btc_holding, current_btc_value, balance, trades, final_balance, profit

final_profit, btc_holding, current_btc_value, balance, trades, final_balance, profit = backtest_strategy(
    historical_data, buy_price_threshold, sell_price_threshold, trade_quantity)

# Main function
def main():
    print(f"Current cash balance: $ {balance:.2f}")
    print(f"Bitcoin currently holding: {btc_holding:.2f}")
    print(f"Bitcoin in cash value remaining: $ {current_btc_value:.2f}")
    print(f"Bitcoin Assets + Cash Balance: ${final_balance:.2f}, Profit: ${final_profit:.2f}")
    print(get_current_price(symbol))

if __name__ == "__main__":
    main()