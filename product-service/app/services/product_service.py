"""File to handle all product-service Services"""

from ..schemas.product_schema import ProductCreate
from ..repositories.product_repository import ProductRepository
from ..models.product import Product


class ProductService:
    """Class ProductService to send repository correct data"""

    def __init__(self, product_repository: ProductRepository) -> Product:
        self.__product_repository: ProductRepository = product_repository

    # ! if manually add return str | Product, SQLAlchemy throws error
    def create(self, product: ProductCreate):
        """Method to create product

        Args:
            product (ProductCreate): The product validated by controller

        Returns:
            product (Product): Return the existing_product ou the created_product
        """

        existing_product: Product | None = self.__product_repository.find_by_name(
            product.name
        )

        if existing_product:
            return f"Product with name '{existing_product.name}' already exists"

        product_instance = Product(**product.model_dump())
        created_product: Product = self.__product_repository.create(product_instance)

        return created_product
