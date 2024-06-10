from services.stock_service import StockService
from models.stock import Stock
from exceptions.stock_exceptions import StockException
from schemes.stock_schema import StockUpdate, StockOut


class StockController:
    def __init__(self, stock_service: StockService) -> None:
        self.__stock_service: StockService = stock_service

    def get_stock_by_product_id(self, product_id: int) -> Stock:
        stock: Stock | None = self.__stock_service.get_stock_by_product_id(
            product_id=product_id
        )

        if not stock:
            raise StockException(message="Stock table not found", name="Not found")

        return stock

    def update(self, stock_id: int, data: StockUpdate) -> StockOut:
        stock: StockOut | None = self.__stock_service.update(
            stock_id=stock_id, data=data
        )

        if not stock:
            raise StockException(message="Stock table not found", name="Not found")

        return stock
