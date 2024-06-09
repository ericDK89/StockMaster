from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from controllers.stock_controller import StockController
from services.stock_service import StockService
from repositories.stock_repository import StockRepository


def get_stock_repository(db: Session = Depends(get_db)) -> StockRepository:
    return StockRepository(db)


def get_stock_service(
    stock_repository: StockRepository = Depends(get_stock_repository),
) -> StockService:
    return StockService(stock_repository=stock_repository)


def get_stock_controller(
    stock_service: StockController = Depends(get_stock_service),
) -> StockController:
    return StockController(stock_service=stock_service)
