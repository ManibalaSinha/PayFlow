from app.db.session import SessionLocal
from app.models import Account

db = SessionLocal()
try:
    accounts = db.query(Account).all()
    for acc in accounts:
        print(acc.id, acc.name, acc.balance)
finally:
    db.close()
