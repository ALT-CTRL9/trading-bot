import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)
from bot.logging_config import setup_logger

logger = setup_logger()

parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    print("\n===== ORDER REQUEST =====")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")

    if args.type.upper() == "LIMIT":
        print(f"Price: {args.price}")

    logger.info("Order request received")

    if args.type.upper() == "MARKET":
        response = place_market_order(
            args.symbol,
            args.side.upper(),
            args.quantity
        )
    else:
        response = place_limit_order(
            args.symbol,
            args.side.upper(),
            args.quantity,
            args.price
        )

    print("\n===== ORDER RESPONSE =====")
    print("Order ID:", response.get("orderId"))
    print("Status:", response.get("status"))
    print("Executed Qty:", response.get("executedQty"))

    logger.info(f"Order successful: {response}")

except Exception as e:
    print("\nOrder Failed")
    print(str(e))
    logger.error(str(e))