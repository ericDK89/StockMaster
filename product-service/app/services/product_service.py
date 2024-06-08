"""File to handle all product-service Services"""

from typing import List, Dict, Any
from ..utils.products_to_json import products_to_json, product_to_json
from ..schemas.product_schema import ProductCreate, ProductOut, ProductUpdate
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

    def get_products(self):
        """Method to return all products from db

        Returns:
            List[Product]: All products from db
        """
        products: List[ProductOut] = self.__product_repository.get_products()

        if len(products) == 0:
            return

        validated_products: List[ProductOut] = [
            ProductOut.model_validate(product) for product in products
        ]

        return products_to_json(validated_products)

    def get_product_by_id(self, product_id: int):
        """Method to get product by id from repository

        Args:
            product_id (str): product id to use to find the product

        Returns:
            Product | None: Product or None if not found
        """
        product: ProductOut | None = self.__product_repository.get_product_by_id(
            product_id=product_id
        )

        if not product:
            return None

        validate_product: ProductOut = ProductOut.model_validate(product)

        return product_to_json(validate_product)

    def update_product_by_id(self, product_id: int, data: ProductUpdate):
        """
        Updates an existing product identified by product_id with the new data provided.

        Args:
            product_id (int): The ID of the product to update.
            data (ProductCreate): The new product data for update.

        Returns:
            ProductOut: Returns the updated product as a ProductOut instance if the update is successful.
            None: Returns None if no product with the provided product_id is found.
        """

        if not self.get_product_by_id(product_id=product_id):
            return None

        product: ProductOut | None = self.__product_repository.update_product_by_id(
            product_id=product_id, data=data
        )

        validate_product: ProductOut = ProductOut.model_validate(product)

        return product_to_json(product=validate_product)

    def delete_product_by_id(self, product_id: int):
        """
        Deletes a product by its ID.

        This method uses the ProductRepository to delete the product with the given ID.
        It delegates the deletion process to the repository and returns the result.

        Args:
            product_id (int): The ID of the product to be deleted.

        Returns:
            The result of the deletion operation from the ProductRepository.
        """
        return self.__product_repository.delete_product_by_id(product_id=product_id)
