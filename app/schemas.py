from pydantic import BaseModel
from typing import Optional

class OrderSchema(BaseModel):
    product_name: str
    quantity: int
    price: float

class OrderUpdateSchema(BaseModel):
    product_name: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    status: Optional[str]
