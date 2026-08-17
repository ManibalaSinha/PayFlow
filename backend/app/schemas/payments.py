from pydantic import BaseModel
from typing import Optional

class PaymentCreate(BaseModel):
    user_id: int
    amount: float
    currency: str
    idempotency_key: str

class PaymentStatus(BaseModel):
    payment_id: int
    status: str
    attempts: int