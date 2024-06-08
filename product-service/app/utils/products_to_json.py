"""File with the util to turn ProductOut type into JSON"""

import json
from schemas.product_schema import ProductOut
from typing import List


def products_to_json(products: List[ProductOut]):
    """Def to turn ProductOut list into json

    Args:
        products (List[ProductOut]): List of products from db

    Returns:
        JSON: return a json object
    """

    # * Turns the products validates into a str json format
    str_json: str = json.dumps([product.model_dump() for product in products])

    # * Then returns it in a valid json format
    return json.loads(str_json)


def product_to_json(product: ProductOut):
    """Def to turn a single product into a json

    Args:
        product (ProductOut): Product of ProductOut type

    Returns:
        JSON: Return a json object
    """
    str_json: str = json.dumps(product.model_dump())

    return json.loads(str_json)
