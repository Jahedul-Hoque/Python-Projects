<div align="center">

# 🤖 Binance Crypto Trading Bot & Backtesting System 📊

</div>

## 📖 Overview
This project is a **Python-based Binance trading bot** with a **backtesting system** to evaluate trading strategies on historical data. It fetches **live Bitcoin price data**, executes **buy/sell orders**, and simulates trading strategies using past market data.

## 🔑 Key Features
- **Live Trading**: Uses Binance API (`python-binance`) to execute trades.
- **Historical Data Retrieval**: Fetches past candlestick (Kline) data.
- **Backtesting System**: Simulates trades to assess profitability.
- **Dynamic Buy/Sell Thresholds**: Executes trades based on predefined price levels.
- **Balance Tracking**: Tracks available cash and Bitcoin holdings over time.

## 💻 Code Breakdown
```python
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
```

## 🔍 Explanation
1. **Binance API Authentication (`Client`)**
   - Loads API credentials securely using `dotenv`.
   - Connects to Binance's **testnet environment** for risk-free testing.

2. **Fetching Real-Time & Historical Price Data**
   - Uses `get_symbol_ticker()` to get the **current BTC price**.
   - Uses `get_klines()` to **fetch past price data for backtesting**.

3. **Trading Bot (`trading_bot()`)**
   - Continuously monitors BTC price.
   - **Buys when price < `buy_price_threshold`**.
   - **Sells when price > `sell_price_threshold`**.
   - Waits (`sleep()`) to avoid excessive API calls.

4. **Backtesting System (`backtest_strategy()`)**
   - Simulates trades over historical data.
   - Tracks **cash balance, BTC holdings, and executed trades**.
   - Calculates **profit/loss and final balance**.

## 🚀 Why Use a Binance Trading Bot with Backtesting?
✅ **Automates trading** – No need for manual execution.  
✅ **Simulates trading strategies** – Risk-free strategy testing.  
✅ **Real-time price monitoring** – Continuously fetches market data.  
✅ **Historical data analysis** – Helps in optimizing trading strategies.  
✅ **Tracks portfolio performance** – Provides clear profit/loss metrics.  

## 🔥 Future Enhancements
- ✅ Implement **Stop-Loss & Take-Profit mechanisms**.
- ✅ Use **technical indicators (RSI, MACD, Bollinger Bands)**.
- ✅ Optimize **multi-threading for faster execution**.
- ✅ Store trade history in **CSV or database** for better record-keeping.

## 🎯 Summary
This **Binance Trading Bot & Backtesting System** automates cryptocurrency trading using Python, fetches live and historical price data, and simulates trading strategies. It enables traders to **test, optimize, and refine** their strategies before deploying them in real markets.

Happy Trading! 🚀📈


