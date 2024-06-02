"""File to handle product-service controller"""

from ..schemas.product_schema import ProductCreate
from ..exceptions.product_execptions import ProductException
from ..services.product_service import ProductService


class ProductController:
    """Class to validate data and raise errors if necessary"""

    def __init__(self, product_service: ProductService) -> None:
        self.__product_service: ProductService = product_service

    def create(self, product: ProductCreate) -> str:
        """Def to create product

        Args:
            product (ProductCreate): Body from response that comes in ProductCreat format

        Raises:
            ProductException: If there is an error on product raises the exception
        """
        # TODO -> create handler for when the product_name already exists

        self.__product_service.create(product)

        return "Product successfully created"
