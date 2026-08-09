from sqlalchemy import Column, DateTime, Integer, Numeric, String, func

from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(String(36), primary_key=True, index=True)

    symbol = Column(String(20), nullable=False, index=True)
    side = Column(String(4), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(18, 4), nullable=False)

    status = Column(String(20), nullable=False, default="PENDING", index=True)

    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())