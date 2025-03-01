from binance.client import Client
#importing binance platform

from dotenv import load_dotenv
import os
load_dotenv()
#imports .env and os library to load .env file containing API Key and Secret

APIKey = os.getenv("APIKey")
Secret = os.getenv("Secret")
client = Client(APIKey,Secret,testnet=True)

AccountBalance= client.get_account()
print(AccountBalance)