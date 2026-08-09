from pydantic import BaseModel, Field
from decimal import Decimal

class OrderCreate(BaseModel):
    symbol: str = Field(min_length=1, max_length=20)
    side: str
    quantity: int = Field(gt=0)
    price: Decimal = Field(gt=0)

class OrderResponse(BaseModel):
    id: str
    symbol: str
    side: str
    quantity: int
    price: Decimal
    status: str
    created_at: str