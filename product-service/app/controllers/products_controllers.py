"""File to handle product-service controller"""

from ..schemas.product_schema import ProductCreate
from ..exceptions.product_execptions import ProductException
from ..services.product_service import ProductService
from ..models.product import Product


class ProductController:
    """Class to validate data and raise errors if necessary"""

    def __init__(self, product_service: ProductService) -> None:
        self.__product_service: ProductService = product_service

    def create(self, product: ProductCreate) -> str:
        """Def to create product

        Args:
            product (ProductCreate): Body from response that comes in ProductCreate format

        Raises:
            ProductException: If there is an error on while tying to creare product
        """
        response: Product | str = self.__product_service.create(product)

        if not isinstance(response, Product):
            raise ProductException(name="AlreadyExists", message=response)

        return "Product successfully created"

    def get_products(self):
        """Method to return all products from db

        Returns:
            str: All products from db in str formatted
        """
        return self.__product_service.get_products()
