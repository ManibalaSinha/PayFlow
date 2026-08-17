from app.db.deps import get_db
from app.models import Order
from app.schemas.order import OrderCreate
from app.kafka.producer import publish_event
from app.core.kafka_topics import ORDER_CREATED
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
router = APIRouter()

@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.post("/", response_model=dict)
def create_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db)
):
    try:
        order = Order(
            symbol=order_data.symbol,
            quantity=order_data.quantity,
            price=order_data.price
        )

        db.add(order)
        db.commit()
        db.refresh(order)

        event = {
            "order_id": order.id,
            "symbol": order.symbol,
            "quantity": order.quantity,
            "price": order.price
        }

        publish_event(ORDER_CREATED, event)

        return {
            "id": order.id,
            "symbol": order.symbol,
            "quantity": order.quantity,
            "price": order.price
        }

    except ValueError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )