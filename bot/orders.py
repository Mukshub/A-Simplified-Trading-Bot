from binance.exceptions import BinanceAPIException
from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()
    logger.info(f"Placing {order_type} {side} order for {quantity} {symbol}")


    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol= symbol,
                side= side,
                type="MARKET",
                quantity= quantity
            )
        else:
            order = client.futures_create_order(
                symbol= symbol,
                side= side,
                type="LIMIT",
                quantity= quantity,
                price=price,
                timeInForce="GTC"
            )
        logger.info(f"Order placed successfully! ID: {order['orderId']}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API error: {e}")
        raise


