import os
import ccxt
from dotenv import load_dotenv
from binance.client import Client


load_dotenv()




#Getting API Keys
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

def get_binance_api():

    return BINANCE_API_KEY,BINANCE_API_SECRET

#Registering Binacne Client
def get_binance_client():
    return Client(
        api_key=BINANCE_API_KEY,
        api_secret=BINANCE_API_SECRET
    )

#Registering CCXT Client
def get_ccxt_client():
    return ccxt.binanceusdm()
