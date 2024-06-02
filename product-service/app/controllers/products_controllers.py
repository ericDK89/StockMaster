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
            product (ProductCreate): Body from response that comes in ProductCreat format

        Raises:
            ProductException: If there is an error on product raises the exception
        """
        response: Product | None = self.__product_service.create(product)

        if response:
            raise ProductException(
                name="AlreadyExists", message="Product already exists"
            )

        return "Product successfully created"
