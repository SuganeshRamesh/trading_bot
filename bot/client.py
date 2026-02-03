import hmac
import hashlib
import time
import requests
import logging
from urllib.parse import urlencode
from bot.config import Config

logger = logging.getLogger("trading_bot")

class BinanceClient:
    def __init__(self):
        Config.validate()
        self.api_key = Config.API_KEY
        self.api_secret = Config.API_SECRET
        self.base_url = Config.BASE_URL
        self.headers = {
            "X-MBX-APIKEY": self.api_key
        }

    def _get_timestamp(self):
        return int(time.time() * 1000)

    def _sign(self, params):
        """Generates HMAC SHA256 signature."""
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        return signature

    def send_request(self, method, endpoint, params=None):
        """Sends a request to the Binance API."""
        if params is None:
            params = {}
        
        params["timestamp"] = self._get_timestamp()
        params["signature"] = self._sign(params)

        url = f"{self.base_url}{endpoint}"
        
        try:
            logger.info(f"Sending {method} request to {endpoint}")
            # Note: headers must be sent.
            response = requests.request(method, url, headers=self.headers, params=params)
            response.raise_for_status()
            
            # Additional check if Binance returns HTTP 200 but has an internal error code
            data = response.json()
            # Binance errors usually result in non-200 status, but just safely returning JSON
            return data

        except requests.exceptions.HTTPError as err:
            logger.error(f"HTTP Error: {err}")
            if response is not None:
                 logger.error(f"Response Body: {response.text}")
            raise
        except Exception as err:
            logger.error(f"Request Error: {err}")
            raise

    def place_order(self, order_params):
        """Places an order."""
        endpoint = "/fapi/v1/order"
        return self.send_request("POST", endpoint, order_params)
