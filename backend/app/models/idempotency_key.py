from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from app.db.base import Base
from sqlalchemy.orm import relationship

class IdempotencyKey(Base):
    __tablename__ = "idempotency_key"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), unique=True, nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.id"))
    created_at = Column(DateTime, default=func.now())