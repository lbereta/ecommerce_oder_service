from pydantic import BaseModel
from typing import Optional

class OrderSchema(BaseModel):
    product_name: str
    quantity: int
    price: float

class OrderUpdateSchema(BaseModel):
    product_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    status: Optional[str] = None
