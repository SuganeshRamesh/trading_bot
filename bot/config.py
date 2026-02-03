import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_API_SECRET")
    BASE_URL = os.getenv("BASE_URL", "https://testnet.binancefuture.com")

    @classmethod
    def validate(cls):
        """Validates that necessary environment variables are set."""
        if not cls.API_KEY:
            raise ValueError("BINANCE_API_KEY is missing in environment variables.")
        if not cls.API_SECRET:
            raise ValueError("BINANCE_API_SECRET is missing in environment variables.")
