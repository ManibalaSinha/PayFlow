from app.db.session import SessionLocal
from app.models import Account

db = SessionLocal()
try:
    acc = db.query(Account).filter(Account.name == "Test Account").first()
    if acc:
        acc.balance += 500
        db.commit()
        print(f"Updated balance: {acc.balance}")
finally:
    db.close()
