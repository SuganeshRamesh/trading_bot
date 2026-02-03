def validate_positive_float(value, name="Value"):
    """Checks if a value is a positive float."""
    try:
        val = float(value)
        if val <= 0:
            raise ValueError(f"{name} must be greater than 0.")
        return val
    except ValueError:
        raise ValueError(f"{name} must be a valid number.")

def validate_side(side):
    """Validates order side (BUY/SELL)."""
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be 'BUY' or 'SELL'.")
    return side.upper()

def validate_order_type(order_type):
    """Validates order type (MARKET/LIMIT)."""
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'.")
    return order_type.upper()

def validate_symbol(symbol):
    """Basic validation for symbol."""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol cannot be empty.")
    return symbol.upper()
