from bot.client import get_client

def place_market_order(symbol, side, quantity):
    client = get_client()

    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )