from app.db.session import SessionLocal
from app.models import Account

db = SessionLocal()

try:
    # Create account (do NOT set id manually)
    acc = Account(name="m", balance=1000)
    db.add(acc)
    db.commit()
    db.refresh(acc)

    print("Inserted:", acc.id, acc.name, acc.balance)

    # Fetch all accounts
    accounts = db.query(Account).all()
    for a in accounts:
        print("Account:", a.id, a.name, a.balance)

finally:
    db.close()
