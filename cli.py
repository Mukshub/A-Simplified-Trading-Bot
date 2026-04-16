import argparse
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price
from bot.orders import place_order
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--order-type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="e.g. 0.001")
    parser.add_argument("--price", required=False, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        result = place_order(args.symbol, side, order_type, quantity, price)
        print(f"\n✅ Order placed successfully!")
        print(f"   Order ID:     {result['orderId']}")
        print(f"   Status:       {result['status']}")
        print(f"   Executed Qty: {result['executedQty']}")
        print(f"   Avg Price:    {result.get('avgPrice', 'N/A')}")
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"\n❌ Invalid input: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()