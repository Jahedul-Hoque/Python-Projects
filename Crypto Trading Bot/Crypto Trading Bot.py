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
#returns current price of symbol security (currently BTCUSDT)


def PlaceBuyOrder(symbol, quantity):
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    print(f"Buy order done: {order} \n")
#places buy order using binance parameters

def PlaceSellOrder(symbol, quantity):
    order = client.order_market_sell(symbol=symbol, quantity=quantity)
    print(f"Sell order done: {order} \n")
#places sell order

def TradingBot():
    InPoisiton = False

    while True:
        CurrentPrice = GetCurrentPrice(symbol)
        print(f"Current price of {symbol}: {CurrentPrice}")
        #prints current price of BTCUSDT

        if not InPoisiton:
            if CurrentPrice<BuyPriceThreshold:
                print(f"Price is below {BuyPriceThreshold}. Placing Buy order.")
                PlaceBuyOrder(symbol,TradeQuantity)
                InPoisiton = True
        #if the current price is less than Buy price we set, place a buy order
        #set the in position to true so that this doesnt happen multiple times
        else:
            if CurrentPrice>SellPriceThreshold:
                print(f"Price is above {SellPriceThreshold}. Placing Sell order.")
                PlaceSellOrder(symbol,TradeQuantity)
                InPoisiton = False
            #if the current price rises above sell price, then place a sell order
            #set position to false so that it can look for another buy trade when
            #..current price is below buy price
        time.sleep(2)




def main():
    #TradingBot()
    #PlaceSellOrder(symbol,TradeQuantity)
    #PlaceBuyOrder(symbol,TradeQuantity)
    #print(AccountBalance)
    print("Current price of Bitcoin in USDT is: ", GetCurrentPrice(symbol))

if __name__ == "__main__":
    main()





