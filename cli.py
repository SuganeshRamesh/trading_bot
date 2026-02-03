import argparse
import sys
import logging
from bot.logging_config import setup_logging
from bot.client import BinanceClient
from bot.orders import create_order_payload

# Initialize logging
logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot Order CLI")
    
    parser.add_argument("--symbol", required=True, type=str, help="Trading Pair Symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, type=str, choices=["BUY", "SELL"], help="Order Side (BUY/SELL)")
    parser.add_argument("--type", required=True, type=str, choices=["MARKET", "LIMIT"], help="Order Type (MARKET/LIMIT)")
    parser.add_argument("--qty", required=True, type=float, help="Order Quantity")
    parser.add_argument("--price", type=float, help="Order Price (Required for LIMIT orders)")

    args = parser.parse_args()

    logger.info(f"Received CLI command: {sys.argv}")

    try:
        # Create Payload
        payload = create_order_payload(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            qty=args.qty,
            price=args.price
        )
        
        print("\n--- Order Request Summary ---")
        print(f"Symbol: {payload['symbol']}")
        print(f"Side:   {payload['side']}")
        print(f"Type:   {payload['type']}")
        print(f"Qty:    {payload['quantity']}")
        if "price" in payload:
            print(f"Price:  {payload['price']}")
        print("-----------------------------\n")

        # Initialize Client and Place Order
        client = BinanceClient()
        response = client.place_order(payload)

        # Output Results
        print(">>> SUCCESS! Order Placed <<<")
        print(f"Order ID:      {response.get('orderId')}")
        print(f"Status:        {response.get('status')}")
        print(f"Executed Qty:  {response.get('executedQty')}")
        print(f"Avg Price:     {response.get('avgPrice')}")
        print("-" * 30)

        logger.info(f"Order placed successfully: {response}")

    except ValueError as e:
        print(f"\n[!] Input Error: {e}")
        logger.error(f"Input Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] An error occurred. Check logs for details.")
        # The client logs the full error stack/details already
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
