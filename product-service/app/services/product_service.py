"""File to handle all product-service Services"""

from ..schemas.product_schema import ProductCreate
from ..repositories.product_repository import ProductRepository
from ..models.product import Product


class ProductService:
    """Class ProductService to send repository correct data"""

    def __init__(self, product_repository: ProductRepository) -> Product:
        self.__product_repository: ProductRepository = product_repository

    # * if manually add return Product | None, SQLAlchemy throws error
    def create(self, product: ProductCreate):
        """Method to create product

        Args:
            product (ProductCreate): The product validated by controller

        Returns:
            product (Product): Return the existing_product ou the created_product
        """

        existing_product: Product | None = self.__product_repository.findByName(
            product.name
        )

        if existing_product:
            return existing_product

        product_instance = Product(**product.model_dump())
        created_product: Product = self.__product_repository.create(product_instance)

        print(created_product)
        return created_product
