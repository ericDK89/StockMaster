"""File to add all dependencies"""

from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from controllers.stock_controller import StockController
from services.stock_service import StockService
from repositories.stock_repository import StockRepository


def get_stock_repository(db: Session = Depends(get_db)) -> StockRepository:
    """
    This function creates a new StockRepository instance.

    Parameters:
    db (Session, optional): The SQLAlchemy session for interacting with the database. Defaults to Depends(get_db).

    Returns:
    StockRepository: The new StockRepository instance.
    """
    return StockRepository(db)


def get_stock_service(
    stock_repository: StockRepository = Depends(get_stock_repository),
) -> StockService:
    """
    This function creates a new StockService instance.

    Parameters:
    stock_repository (StockRepository, optional): The StockRepository instance for interacting with stock items in the database. Defaults to Depends(get_stock_repository).

    Returns:
    StockService: The new StockService instance.
    """
    return StockService(stock_repository=stock_repository)


def get_stock_controller(
    stock_service: StockController = Depends(get_stock_service),
) -> StockController:
    """
    This function creates a new StockController instance.

    Parameters:
    stock_service (StockController, optional): The StockService instance for managing stock items. Defaults to Depends(get_stock_service).

    Returns:
    StockController: The new StockController instance.
    """
    return StockController(stock_service=stock_service)
