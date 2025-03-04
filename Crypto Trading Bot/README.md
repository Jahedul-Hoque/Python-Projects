<div align="center">

# 🤖 Crypto Trading Bot 📈

</div>

## 📖 Overview
This project is a **Python-based Binance trading bot** that automates **cryptocurrency trading** on Binance's **testnet environment**. It fetches **live Bitcoin price data**, executes **buy/sell orders** based on predefined thresholds, and continuously monitors the market.

## 🔑 Key Features
- **Uses Binance API (`python-binance`)** to interact with the exchange.
- **Retrieves real-time Bitcoin price data (`get_symbol_ticker`).**
- **Places market buy & sell orders dynamically.**
- **Implements basic trading logic** with position tracking.
- **Uses environment variables (`dotenv`)** for secure API key storage.

## 💻 Code Breakdown
```python
# Importing necessary libraries
import os  # Load environment variables
import time
from binance.client import Client  # Binance API
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
api_key = os.getenv("APIKey")
secret = os.getenv("Secret")
client = Client(api_key, secret, testnet=True)

# Define trading parameters
symbol = "BTCUSDT"
buy_price_threshold = 85910
sell_price_threshold = 85950
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

# Main function
def main():
    print("Current price of Bitcoin in USDT is:", get_current_price(symbol))

if __name__ == "__main__":
    main()
```

## 🔍 Explanation
1. **Binance API Authentication (`Client`)**
   - Uses `dotenv` to load API credentials securely.
   - Connects to Binance's **testnet environment** to avoid real fund usage.

2. **Fetching Real-Time Price (`get_symbol_ticker`)**
   - Retrieves the **current price of BTC/USDT** from Binance.

3. **Placing Market Orders (`order_market_buy()`, `order_market_sell()`)**
   - Executes **buy/sell trades** dynamically based on price thresholds.

4. **Trading Bot (`trading_bot()`)**
   - **Continuously monitors** BTC price.
   - **Buys when the price is below `buy_price_threshold`**.
   - **Sells when the price exceeds `sell_price_threshold`**.
   - **Waits (`sleep()`) before checking again** to prevent excessive API calls.

## 🚀 Why Use a Binance Trading Bot?
✅ **Automates trading** – Eliminates manual execution delays.  
✅ **Backtesting & Strategy Development** – Test strategies risk-free on **Binance testnet**.  
✅ **Real-time price monitoring** – Continuously fetches market data.  
✅ **Customizable parameters** – Adjust thresholds, assets, and trade quantities dynamically.  

## 🔥 Future Enhancements
- ✅ Add **Stop-Loss & Take-Profit mechanisms**.
- ✅ Implement **Technical Indicators (RSI, MACD, Bollinger Bands)**.
- ✅ Use **multi-threading for faster execution**.
- ✅ Integrate with **historical data for backtesting strategies**.

## 🎯 Summary
This **Binance Trading Bot** automates cryptocurrency trading using Python. It connects to Binance's **testnet**, fetches live BTC prices, and executes buy/sell trades based on user-defined thresholds. The script provides a foundation for **developing more advanced trading strategies**.

Happy Trading! 🚀📈

