from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

client = Client(API_KEY, SECRET_KEY)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

def get_client():
    return client