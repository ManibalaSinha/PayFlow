from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from app.db.base import Base
from sqlalchemy.orm import relationship

class PaymentAttempt(Base):
    __tablename__ = "payment_attempts"

    id = Column(Integer, primary_key=True, index=True)
    payment_id = Column(Integer, ForeignKey("payments.id"))
    attempt_no = Column(Integer, default=1)
    status = Column(String(20))
    error_message = Column(String)
    attempted_at = Column(DateTime, default=func.now())
    payment = relationship("Payment", back_populates="attempts")