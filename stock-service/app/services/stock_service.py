from repositories.stock_repository import StockRepository
from schemes.stock_schema import Stock, StockUpdate, StockOut
from utils.stock_to_json import stock_to_json


class StockService:
    def __init__(self, stock_repository: StockRepository) -> None:
        self.__stock_repository: StockRepository = stock_repository

    def get_stock_by_product_id(self, product_id: int):
        stock: Stock | None = self.__stock_repository.get_stock_by_product_id(
            product_id=product_id
        )

        if not stock:
            return None

        validate_stock: Stock = Stock.model_validate(stock)

        return stock_to_json(validate_stock)

    def update(self, stock_id: int, data: StockUpdate):
        stock: StockOut | None = self.__stock_repository.update(
            stock_id=stock_id, data=data
        )

        if not stock:
            return None

        validate_stock: Stock = Stock.model_validate(stock)

        return stock_to_json(validate_stock)
