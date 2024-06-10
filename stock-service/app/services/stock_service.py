"""File to create all services for stock"""

from repositories.stock_repository import StockRepository
from schemes.stock_schema import Stock, StockUpdate, StockOut
from utils.stock_to_json import stock_to_json


class StockService:
    """
    This class represents a service for managing stock items.

    Attributes:
    __stock_repository (StockRepository): The repository for interacting with stock items in the database.
    """

    def __init__(self, stock_repository: StockRepository) -> None:
        """
        The constructor for the StockService class.

        Parameters:
        stock_repository (StockRepository): The repository for interacting with stock items in the database.
        """
        self.__stock_repository: StockRepository = stock_repository

    def get_stock_by_product_id(self, product_id: int):
        """
        This method retrieves a stock item by product ID.

        Parameters:
        product_id (int): The ID of the product for which to retrieve the stock item.

        Returns:
        dict: The stock item for the specified product ID, converted to JSON.
        """
        stock: Stock | None = self.__stock_repository.get_stock_by_product_id(
            product_id=product_id
        )

        if not stock:
            return None

        validate_stock: Stock = Stock.model_validate(stock)

        return stock_to_json(validate_stock)

    def update(self, stock_id: int, data: StockUpdate):
        """
        This method updates a stock item.

        Parameters:
        stock_id (int): The ID of the stock item to update.
        data (StockUpdate): The new data for the stock item.

        Returns:
        dict: The updated stock item, converted to JSON.
        """
        stock: StockOut | None = self.__stock_repository.update(
            stock_id=stock_id, data=data
        )

        if not stock:
            return None

        validate_stock: Stock = Stock.model_validate(stock)

        return stock_to_json(validate_stock)
