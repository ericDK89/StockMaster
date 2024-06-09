from pydantic import BaseModel
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

    class Config:
        orm_mode = True
