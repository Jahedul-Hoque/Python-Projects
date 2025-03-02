<div align="center">

# 🤖 Crypto Trading Bot with Python 📈

</div>

## 📖 Overview
This project is a **Python-based Binance trading bot** that **automates cryptocurrency trading** on Binance's **testnet environment**. It fetches **live Bitcoin price data**, executes **buy/sell orders** based on predefined thresholds, and continuously monitors the market.

## 🔑 Key Features
- **Uses Binance API (`python-binance`)** to interact with the exchange.
- **Retrieves real-time Bitcoin price data (`get_symbol_ticker`).**
- **Places market buy & sell orders dynamically.**
- **Implements basic trading logic** with position tracking.

## 💻 Code Breakdown
```python
from binance.client import Client
from dotenv import load_dotenv
import os
import time

# Load API keys from .env file
load_dotenv()
APIKey = os.getenv("APIKey")
Secret = os.getenv("Secret")
client = Client(APIKey, Secret, testnet=True)

# Define trading parameters
symbol = "BTCUSDT"
BuyPriceThreshold = 85910
SellPriceThreshold = 85950
TradeQuantity = 0.001

# Get current BTC price
def GetCurrentPrice(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])

# Place market buy order
def PlaceBuyOrder(symbol, quantity):
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    print(f"Buy order done: {order}\n")

# Place market sell order
def PlaceSellOrder(symbol, quantity):
    order = client.order_market_sell(symbol=symbol, quantity=quantity)
    print(f"Sell order done: {order}\n")

# Automated trading bot logic
def TradingBot():
    InPosition = False
    while True:
        CurrentPrice = GetCurrentPrice(symbol)
        print(f"Current price of {symbol}: {CurrentPrice}")
        
        if not InPosition:
            if CurrentPrice < BuyPriceThreshold:
                print(f"Price is below {BuyPriceThreshold}. Placing Buy order.")
                PlaceBuyOrder(symbol, TradeQuantity)
                InPosition = True
        else:
            if CurrentPrice > SellPriceThreshold:
                print(f"Price is above {SellPriceThreshold}. Placing Sell order.")
                PlaceSellOrder(symbol, TradeQuantity)
                InPosition = False
        time.sleep(2)  # Pause before fetching the next price

# Main function
def main():
    print("Current price of Bitcoin in USDT is:", GetCurrentPrice(symbol))

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

4. **Trading Bot (`TradingBot()`)**
   - **Continuously monitors** BTC price.
   - **Buys when the price is below `BuyPriceThreshold`**.
   - **Sells when the price exceeds `SellPriceThreshold`**.
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
