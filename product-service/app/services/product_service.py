"""File to handle all product-service Services"""

from ..schemas.product_schema import ProductCreate
from ..repositories.product_repository import ProductRepository
from ..models.product import Product


class ProductService:
    """Class ProductService to send repository correct data"""

    def __init__(self, product_repository: ProductRepository) -> None:
        self.__product_repository: ProductRepository = product_repository

    # * if manually add return Product | None, SQLAlchemy throws error
    def create(self, product: ProductCreate):
        """Method to create product

        Args:
            product (ProductCreate): The product validated by controller
        """

        product = self.__product_repository.findByName(product.name)

        if product:
            return product

        product_instance = Product(**product.model_dump())
        response: Product = self.__product_repository.create(product_instance)

        print(response)
        return None
