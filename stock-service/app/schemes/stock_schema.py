from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class StockBase(BaseModel):
    quantity: Optional[int] = 0


class StockCreate(StockBase):
    product_id: int


class StockUpdate(StockBase):
    product_id: int


class Stock(StockBase):
    id: int
    product_id: int
    last_updated: datetime

    model_config = ConfigDict(from_attributes=True)
