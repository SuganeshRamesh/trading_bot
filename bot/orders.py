from bot.validators import validate_symbol, validate_side, validate_order_type, validate_positive_float

def create_order_payload(symbol, side, order_type, qty, price=None):
    """
    Constructs the dictionary for an order request.
    Validates inputs before creating the payload.
    """
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    qty = validate_positive_float(qty, "Quantity")

    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": qty,
    }

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        price = validate_positive_float(price, "Price")
        payload["price"] = price
        payload["timeInForce"] = "GTC"  # Good Till Cancelled is standard for Limit

    return payload
