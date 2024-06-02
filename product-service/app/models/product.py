"""Models for product-service"""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

Base = declarative_base()


@dataclass
class Product(Base):
    """Class to generate product table"""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Float, nullable=False)
