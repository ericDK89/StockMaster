"""File to handle all contact with db"""

from typing import List
from sqlalchemy.orm import Session
from ..schemas.product_schema import ProductOut
from ..models.product import Product


class ProductRepository:
    """Class to manage all db functions"""

    def __init__(self, db: Session) -> None:
        self.__db: Session = db

    def create(self, product: Product) -> Product:
        """Method to create product on db

        Args:
            product (Product): Product

        Returns:
            Product: Returns the same product
        """
        self.__db.add(product)
        self.__db.commit()
        self.__db.refresh(product)
        return product

    # ! if manually add return ProductOut | None, SQLAlchemy throws error
    def find_by_name(self, name: str):
        """Method to find product by name

        Args:
            name (str): Name of the product

        Returns:
            Product: If find the product
            None: If don't find the product
        """

        return self.__db.query(Product).filter(Product.name == name).first()

    def get_products(self) -> List[ProductOut]:
        """Method to return all products

        Returns:
            List[Product]: return all products
        """
        return self.__db.query(Product).all()

    # ! if manually add return ProductOut | None, SQLAlchemy throws error
    def get_product_by_id(self, product_id: int):
        """Method to get product by id

        Args:
            product_id (str): Product id from response

        Returns:
            Product | None: Return Product or None if product not exist
        """
        return self.__db.query(Product).filter_by(id=product_id).first()
