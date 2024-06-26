"""File to create product schema
- ProductCreate: Just regular product with infos that must be send to create a product
- ProductOut: Product with all props, and add the id
"""

from typing import Optional
from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    """Class ProductBase to set all props to product"""

    name: str
    description: str
    price: float


class ProductCreate(ProductBase):
    """Class of product create with all bases props"""


class ProductUpdate(ProductBase):
    """Class of product update, where update fields are optional"""

    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class ProductOut(ProductBase):
    """Class of product out, the product that will be return, adding the id"""

    id: int

    model_config = ConfigDict(from_attributes=True)
