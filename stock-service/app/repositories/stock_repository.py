from sqlalchemy.orm import Session
from models.stock import Stock
from schemes.stock_schema import StockCreate


class StockRepository:
    def __init__(self, db: Session) -> None:
        self.__db: Session = db

    def create(self, data: StockCreate) -> None:
        stock = Stock(product_id=data.product_id)
        self.__db.add(stock)
        self.__db.commit()
        self.__db.refresh(stock)

    def get_stock_by_product_id(self, product_id: int):
        return self.__db.query(Stock).filter(Stock.product_id == product_id).first()

    def update(self, stock_id: int, quantity: int):
        db_stock: Stock | None = (
            self.__db.query(Stock).filter(Stock.stock_id == stock_id).first()
        )

        if not db_stock:
            return None

        db_stock.quantity = quantity
        self.__db.commit()
        self.__db.refresh(db_stock)

        return db_stock
