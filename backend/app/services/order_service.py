from datetime import datetime, timezone
from uuid import uuid4

from app.core.kafka_topics import ORDER_CREATED
from app.kafka.producer import publish_event
from app.repositories.order_repository import OrderRepository

class OrderService:

    def __init__(self, db):
        self.repository = OrderRepository(db)

    def create_order(self, order_data: dict):
        order = {
            "id": str(uuid4()),
            "symbol": order_data["symbol"].upper(),
            "side": order_data["side"].upper(),
            "quantity": order_data["quantity"],
            "price": order_data["price"],
            "status": "PENDING",
            "created_at": datetime.now(timezone.utc),
        }

        saved_order = self.repository.create(order)

        publish_event(
            topic=ORDER_CREATED,
            message={
                "id": saved_order.id,
                "symbol": saved_order.symbol,
                "side": saved_order.side,
                "quantity": saved_order.quantity,
                "price": float(saved_order.price),
                "status": saved_order.status,
            },
        )

        return saved_order

    def get_order(self, order_id: str):
        return self.repository.get(order_id)

    def cancel_order(self, order_id: str):
        order = self.repository.get(order_id)

        if not order:
            raise ValueError("Order not found")

        if order.status != "PENDING":
            raise ValueError(
                f"Cannot cancel order with status {order.status}"
            )

        order.status = "CANCELLED"

        return self.repository.update(order)

    def modify_order(self, order_id: str, update_data: dict):
        order = self.repository.get(order_id)

        if not order:
            raise ValueError("Order not found")

        if order.status != "PENDING":
            raise ValueError(
                f"Cannot modify order with status {order.status}"
            )

        if "quantity" in update_data and update_data["quantity"] <= 0:
            raise ValueError("Quantity must be greater than zero")

        if "price" in update_data and update_data["price"] <= 0:
            raise ValueError("Price must be greater than zero")

        if "side" in update_data:
            side = update_data["side"].upper()

            if side not in {"BUY", "SELL"}:
                raise ValueError("Invalid order side")

            update_data["side"] = side

        for field, value in update_data.items():
            setattr(order, field, value)

        return self.repository.update(order)



    def validate_order(self, order_data):
        """
        Basic business validations.
        """

        if order_data["quantity"] <= 0:
            raise ValueError("Quantity must be greater than zero")

        if order_data["price"] <= 0:
            raise ValueError("Price must be greater than zero")

        if order_data["side"] not in ["BUY", "SELL"]:
            raise ValueError("Invalid order side")

        return True