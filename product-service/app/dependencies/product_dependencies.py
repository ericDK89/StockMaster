"""File to handle all dependencies from product-service"""

from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from controllers.products_controllers import ProductController
from services.product_service import ProductService
from repositories.product_repository import ProductRepository


def get_product_repository(db: Session = Depends(get_db)) -> ProductRepository:
    """Def to add dependency of db on Product_repository

    Args:
        db (Session, optional): db initializer. Defaults to Depends(get_db).

    Returns:
        ProductRepository: Product repository to handle all db functions
    """
    return ProductRepository(db)


def get_product_service(
    product_repository: ProductRepository = Depends(get_product_repository),
) -> ProductService:
    """Def to add dependency of Product_repository on Product_service

    Args:
        Product_repository (ProductRepository): Product repository to handle db

    Returns:
        ProductService: Product service with all products services
    """
    return ProductService(product_repository)


def get_product_controller(
    product_service: ProductService = Depends(get_product_service),
) -> ProductController:
    """Def to add dependency of Product_controller on product_controller

    Args:
        Product_service (ProductService): Product service to handle services

    Returns:
        ProductController: Product controller to handle http
    """
    return ProductController(product_service)
