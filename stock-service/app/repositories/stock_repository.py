"""File to create all repositories that connect with database"""

from sqlalchemy.orm import Session
from models.stock import Stock
from schemes.stock_schema import StockCreate, StockOut


class StockRepository:
    """
    This class represents a repository for managing stock items in the database.

    Attributes:
    __db (Session): The SQLAlchemy session for interacting with the database.
    """

    def __init__(self, db: Session) -> None:
        """
        The constructor for the StockRepository class.

        Parameters:
        db (Session): The SQLAlchemy session for interacting with the database.
        """
        self.__db: Session = db

    def create(self, data: StockCreate) -> None:
        """
        This method creates a new stock item in the database.

        Parameters:
        data (StockCreate): The data for the new stock item.
        """
        stock = Stock(product_id=data.product_id)
        self.__db.add(stock)
        self.__db.commit()
        self.__db.refresh(stock)

    def get_stock_by_product_id(self, product_id: int):
        """
        This method retrieves a stock item from the database by product ID.

        Parameters:
        product_id (int): The ID of the product for which to retrieve the stock item.

        Returns:
        Stock: The stock item for the specified product ID.
        """
        return self.__db.query(Stock).filter(Stock.product_id == product_id).first()

    def update(self, stock_id: int, data: StockOut):
        """
        This method updates a stock item in the database.

        Parameters:
        stock_id (int): The ID of the stock item to update.
        data (StockOut): The new data for the stock item.

        Returns:
        Stock: The updated stock item.
        """
        stock: StockOut | None = (
            self.__db.query(Stock).filter(Stock.id == stock_id).first()
        )

        if not stock:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(stock, key, value)

        self.__db.commit()
        self.__db.refresh(stock)

        return stock

    def delete(self, stock: Stock):
        """
        This method deletes a stock item from the database.

        Parameters:
        stock (Stock): The stock item to delete.
        """
        self.__db.delete(stock)
        self.__db.commit()
