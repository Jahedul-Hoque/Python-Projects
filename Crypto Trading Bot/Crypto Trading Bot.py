from binance.client import Client
#importing binance platform

from dotenv import load_dotenv
import os
load_dotenv()
#imports .env and os library to load .env file containing API Key and Secret

APIKey = os.getenv("APIKey")
Secret = os.getenv("Secret")
client = Client(APIKey,Secret,testnet=True)
#using APIKey and Secret paremeter which matches file values, login to the
#                                  testing binance environment

AccountBalance= client.get_account()
print(AccountBalance, "\n")
#prints account balance of the testing account

symbol = "BTCUSDT"
#make a variable equal to the value of Bitcoin in relation to US Dollars

BuyPriceThreshold = 80000
SellPriceThreshold = 86000
TradeQuantity = 0.001
#set buy/sell thresholds
#set trade quantity which we will buy/sell securities at 


def GetCurrentPrice(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])

print("Current price of bitcoin in USD:", GetCurrentPrice(symbol), "\n")