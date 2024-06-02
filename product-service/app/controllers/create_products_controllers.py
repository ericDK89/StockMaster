"""File to handle product-service controller"""

from ..schemas.product_schema import ProductCreate
from ..exceptions.product_execptions import ProductException


def execute(product: ProductCreate):
    """Def to create product

    Args:
        product (ProductCreate): Body from response that comes in ProductCreat format

    Raises:
        ProductException: If there is an error on product raises the exception
    """
    if not isinstance(product.price, (int, float)):
        raise ProductException(type="InvalidType", message="Price must be a number")

    if not isinstance(product.stock_quantity, (int)):
        raise ProductException(type="InvalidType", message="Stock must be an Integer")

    return
