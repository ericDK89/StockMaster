import json
from schemes.stock_schema import Stock


def stock_to_json(stock: Stock):
    stock_dict = stock.model_dump()

    for key, _ in stock_dict.items():
        if key == "last_updated":
            stock_dict[key] = stock_dict["last_updated"].isoformat()

    str_stock = json.dumps(stock_dict)

    return json.loads(str_stock)
