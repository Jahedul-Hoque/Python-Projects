from binance.client import Client
#importing binance platform

from dotenv import load_dotenv
import os
load_dotenv()
#imports .env and os library to load .env file containing API Key and Secret

import time
#allows program to sleep which is nice for presentation purposes on console

APIKey = os.getenv("APIKey")
Secret = os.getenv("Secret")
client = Client(APIKey,Secret,testnet=True)
#using APIKey and Secret paremeter which matches file values, login to the
#                                  testing binance environment

AccountBalance= client.get_account()
#print(AccountBalance, "\n")
#prints account balance of the testing account

symbol = "BTCUSDT"
#make a variable equal to the value of Bitcoin in relation to US Dollars

BuyPriceThreshold = 85910
SellPriceThreshold = 85950
TradeQuantity = 0.001
#set buy/sell thresholds
#set trade quantity which we will buy/sell securities at 


def GetCurrentPrice(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])


def PlaceBuyOrder(symbol, quantity):
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    print(f"Buy order done: {order} \n")

def PlaceSellOrder(symbol, quantity):
    order = client.order_market_sell(symbol=symbol, quantity=quantity)
    print(f"Sell order done: {order} \n")

def TradingBot():
    InPoisiton = False
    while True:
        CurrentPrice = GetCurrentPrice(symbol)
        print(f"Current price of {symbol}: {CurrentPrice}")

        if not InPoisiton:
            if CurrentPrice<BuyPriceThreshold:
                print(f"Price is below {BuyPriceThreshold}. Placing Buy order.")
                PlaceBuyOrder(symbol,TradeQuantity)
                InPoisiton = True
        else:
            if CurrentPrice>SellPriceThreshold:
                print(f"Price is above {SellPriceThreshold}. Placing Sell order.")
                PlaceSellOrder(symbol,TradeQuantity)
                InPoisiton = False
        time.sleep(3)

#TradingBot()
#PlaceSellOrder(symbol,TradeQuantity)
#PlaceBuyOrder(symbol,TradeQuantity)
#print(AccountBalance)
print("Current price of Bitcoin in USDT is: ", GetCurrentPrice(symbol))




