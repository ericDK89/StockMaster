"""File to handle all contact with db"""

from sqlalchemy.orm import Session
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

    # ! if manually add return Product | None, SQLAlchemy throws error
    def find_by_name(self, name: str):
        """Method to find product by name

        Args:
            name (str): Name of the product

        Returns:
            Product: If find the product
            None: If don't find the product
        """

        return self.__db.query(Product).filter(Product.name == name).first()
