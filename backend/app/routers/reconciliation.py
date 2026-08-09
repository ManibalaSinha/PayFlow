from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.payment import Payment
from app.models.payment_attempt import PaymentAttempt
from app.utils.db import get_db

router = APIRouter()
@router.post("")
#@router.post("/reconcile")
def reconcile_payments(db: Session = Depends(get_db)):
    failed_payments = db.query(Payment).filter(Payment.status=="FAILED").all()
    reconciled = 0

    for payment in failed_payments:
        # Retry once more
        try:
            # Simulate retry
            payment.status = "SUCCESS"
            db.commit()
            reconciled += 1
        except:
            continue

    return {"total_failed": len(failed_payments), "reconciled": reconciled}
