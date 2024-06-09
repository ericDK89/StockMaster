from services.stock_service import StockService
from models.stock import Stock
from exceptions.stock_exceptions import StockException
from schemes.stock_schema import StockCreate


class StockController:
    def __init__(self, stock_service: StockService) -> None:
        self.__stock_service: StockService = stock_service

    def get_stock_by_product_id(self, product_id: int) -> Stock:
        response: Stock | None = self.__stock_service.get_stock_by_product_id(
            product_id=product_id
        )

        if not response:
            raise StockException(message="Stock table not found", name="Not found")

        return response

    def update(self, stock_id: int, quantity: int) -> Stock:
        response: Stock | None = self.__stock_service.update(
            stock_id=stock_id, quantity=quantity
        )

        if not response:
            raise StockException(message="Stock table not found", name="Not found")

        return response
