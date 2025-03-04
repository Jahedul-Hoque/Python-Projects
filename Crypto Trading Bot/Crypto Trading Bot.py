# Importing .env library to load file
import os  # Importing OS Library to load .env file
import time

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
buy_price_threshold = 85910
sell_price_threshold = 85950
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
                print(
                    f"Price is below {buy_price_threshold}. Placing Buy order."
                )
                place_buy_order(symbol, trade_quantity)
                in_position = True
        else:
            if current_price > sell_price_threshold:
                print(
                    f"Price is above {sell_price_threshold}. Placing Sell order."
                )
                place_sell_order(symbol, trade_quantity)
                in_position = False
        time.sleep(2)  # Pause before fetching the next price


# Main function
def main():
    print("Current price of Bitcoin in USDT is:", get_current_price(symbol))


if __name__ == "__main__":
    main()
