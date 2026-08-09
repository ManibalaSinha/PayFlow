from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from app.db.base import Base
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Numeric, nullable=False)
    currency = Column(String(3), nullable=False)
    status = Column(String(20), default="PENDING")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    attempts = relationship("PaymentAttempt", back_populates="payment")