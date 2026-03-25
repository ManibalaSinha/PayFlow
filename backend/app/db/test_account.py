from app.db.session import SessionLocal
from app.models import Account

db = SessionLocal()

try:
    acc = db.query(Account).filter(Account.name == "Main").first()
    if not acc:
        acc = Account(name="Main", balance=1000)
        db.add(acc)
        db.commit()
        db.refresh(acc)

    print("Account:", acc.id, acc.name, acc.balance)

finally:
    db.close()
