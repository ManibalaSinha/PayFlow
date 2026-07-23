from fastapi import Depends, FastAPI
from app.api.v1.users import router
from app.db.session import SessionLocal
from app.models.user import User
from app.db.session import engine
from app.models import Base
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.api.v1 import users
from app.routers import payments,reconciliation, orders
import logging

app = FastAPI(title="PayFlow trade transaction", version="2.0.0")

app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(reconciliation.router, prefix="/reconcile", tags=["Reconciliation"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
logger = logging.getLogger(__name__)
@app.on_event("startup")
def startup():
    try:
        Base.metadata.create_all(bind=engine)
        print(" Database tables ensured")
    except Exception as e:
        logger.error(f"DB init failed: {e}")
    
@app.get("/health")
def health_check():
    return {"status": "ok"}
