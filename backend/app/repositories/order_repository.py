from sqlalchemy.orm import Session

from app.models.order import Order

class OrderRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, order_data: dict) -> Order:
        order = Order(**order_data)

        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)

        return order

    def get(self, order_id: str) -> Order | None:
        return (
            self.db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )

    def update(self, order: Order) -> Order:
        self.db.commit()
        self.db.refresh(order)

        return order