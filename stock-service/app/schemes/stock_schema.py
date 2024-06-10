"""File to create all stock Schemes"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class StockBase(BaseModel):
    """
    This class represents the base model for a stock item.

    Attributes:
    quantity (Optional[int]): The quantity of the stock item. Defaults to 0.
    """

    quantity: Optional[int] = 0


class StockCreate(StockBase):
    """
    This class represents the model for creating a new stock item.

    Attributes:
    product_id (int): The ID of the product for which the stock item is being created.
    """

    product_id: int


class StockUpdate(StockBase):
    """
    This class represents the model for updating a stock item.

    It inherits from StockBase, so it can include a quantity to update.
    """

    pass


class StockOut(StockBase):
    """
    This class represents the model for outputting a stock item.

    Attributes:
    id (int): The ID of the stock item.
    product_id (int): The ID of the product for which the stock item exists.
    last_updated (datetime): The last time the stock item was updated.
    """

    id: int
    product_id: int
    last_updated: datetime


class Stock(StockBase):
    """
    This class represents the model for a stock item.

    Attributes:
    id (int): The ID of the stock item.
    product_id (int): The ID of the product for which the stock item exists.
    last_updated (datetime): The last time the stock item was updated.
    model_config (ConfigDict): The configuration for the model.
    """

    id: int
    product_id: int
    last_updated: datetime

    model_config = ConfigDict(from_attributes=True)
