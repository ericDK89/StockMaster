from repositories.stock_repository import StockRepository


class StockService:
    def __init__(self, stock_repository: StockRepository) -> None:
        self.__stock_repository: StockRepository = stock_repository

    def get_stock_by_product_id(self, product_id: int):
        return self.__stock_repository.get_stock_by_product_id(product_id=product_id)

    def update(self, stock_id: int, quantity: int):
        return self.__stock_repository.update(stock_id=stock_id, quantity=quantity)
