"""Models for product-service"""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Product(Base):
    """Class to generate product table"""

    __tablename__: str = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
