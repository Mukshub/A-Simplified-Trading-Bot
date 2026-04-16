import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

def get_client():
    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("SECRET_KEY")

    if not api_key or not secret_key:
        raise ValueError("API_KEY or SECRET_KEY missing from .env file")

    client = Client(
        api_key=api_key,
        api_secret=secret_key,
        testnet=True
    )
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    logger.info("Binance client initialized successfully!")
    return client