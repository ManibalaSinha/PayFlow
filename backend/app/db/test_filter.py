from app.db.session import SessionLocal
from app.models.user import User

db = SessionLocal()
if not db.query(User).filter_by(email="i@example.com").first():
    db.add(User(name="i", email="i@example.com"))
    db.commit()
db.close()
