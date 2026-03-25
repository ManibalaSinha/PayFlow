from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    balance = Column(Integer, default=0)

    transactions = relationship(
        "Transaction",
        back_populates="account",
        cascade="all, delete-orphan"
    )
