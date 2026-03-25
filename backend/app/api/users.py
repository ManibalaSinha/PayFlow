from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.user_service import create_user, get_user, update_user
from app.db.deps import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/", response_model=dict)
def api_create_user(name: str, email: str, db: Session = Depends(get_db)):
    try:
        user = create_user(db, name, email)
        return {"id": user.id, "name": user.name, "email": user.email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=dict)
def api_get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email}

@router.put("/{user_id}", response_model=UserResponse)
def api_update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_user(db, user_id, payload.name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if payload.name is not None:
        user.name = payload.name
    if payload.email is not None:
        user.email = payload.email

    db.commit()
    db.refresh(user)
    return user
