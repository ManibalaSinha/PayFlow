from app.db.deps import get_db
from app.models import Payment
from app.schemas.payments import PaymentCreate
from app.kafka.producer import publish_event
from app.core.kafka_topics import PAYMENT_CREATED
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
router = APIRouter()

@router.get("/")
def get_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()

@router.post("/", response_model=dict)
def initiate_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    try:
        payment = Payment(
            amount=payment.amount,
            currency=payment.currency,
            created_at=payment.created_at
        )

        db.add(payment)
        db.commit()
        db.refresh(payment)

        event = {
            "payment_id": payment.id,
            "amount": payment.amount,
            "currency": payment.currency,
            "created_at": payment.created_at
        }

        publish_event(PAYMENT_CREATED, event)

        return {
            "id": payment.id,
            "amount": payment.amount,
            "currency": payment.currency,
            "created_at": payment.created_at
        }

    except ValueError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
""" from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import PaymentCreate, PaymentStatus
from app.services.payment_service import create_payment
#from app.utils.db import get_db
from app.db.deps import get_db
from app.models.payment import Payment
#from app.schemas.payment_create import PaymentCreate
#from app.schemas.payment_status import PaymentStatus
from app.schemas.payments import PaymentCreate, PaymentStatus

router = APIRouter()
@router.get("/")
def get_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()

@router.post("/initiate-payment", response_model=PaymentStatus)
def initiate_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    result, attempts = create_payment(
        db,
        payment.user_id,
        payment.amount,
        payment.currency,
        payment.idempotency_key
    )
    return PaymentStatus(payment_id=result.id, status=result.status, attempts=attempts)
 """