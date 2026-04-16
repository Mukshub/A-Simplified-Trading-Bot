from bot.logging_config import setup_logger

logger = setup_logger()

def validate_side(side):
    valid_values = ["BUY", "SELL"]
    if side.upper() not in valid_values:
        raise ValueError("Invalid side picked, please either Buy or Sell instead")
    else:
        return side.upper()

def validate_order_type(order_type):
    valid_values = ["MARKET", "LIMIT"]
    if order_type.upper() not in valid_values:
        raise ValueError("Invalid order type chosen, please select either Market or Limit instead")
    else:
        return order_type.upper()

def validate_quantity(quantity):
    try:
        value = float(quantity)
        if value <= 0:
            raise ValueError()
        return value
    except ValueError:
        raise ValueError("Quantity must be a valid number greater than 0")

def validate_price(price, order_type):
    if order_type=="MARKET":
        return None
    else:
        try:
            value = float(price)
            if value <= 0:
                raise ValueError()
            return value
        except ValueError:
            raise ValueError("Quantity must be a valid number greater than 0")
