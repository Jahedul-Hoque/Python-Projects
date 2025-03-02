from binance.client import Client # Importing Binance platform
from dotenv import load_dotenv # Importing .env library to load file
import os # Importing OS Library to load .env file
import time 


# Load API keys from .env file
load_dotenv()
APIKey = os.getenv("APIKey")
Secret = os.getenv("Secret")
client = Client(APIKey, Secret, testnet=True)
# Logging into Binance platform using API Key and Secret
# Enabling Testing environment


# Define trading parameters
symbol = "BTCUSDT"
BuyPriceThreshold = 85910
SellPriceThreshold = 85950
TradeQuantity = 0.001


# Get current BTC price in relation to US Dollars
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