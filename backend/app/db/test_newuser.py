from app.db.session import SessionLocal
from app.models.user import User

db = SessionLocal()
new_user = User(name="Tes", email="st@example.com")
db.add(new_user)
db.commit()
db.refresh(new_user)
print(new_user.id, new_user.name)
db.close()
