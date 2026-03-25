from app.db.session import SessionLocal
from app.models.account import Account

db = SessionLocal()

try:
    # Check if account with name "m" exists
    existing = db.query(Account).filter(Account.name == "m").first()
    if existing:
        print("Account already exists:", existing.id, existing.name, existing.balance)
    else:
        acc = Account(name="m", balance=1000)
        db.add(acc)
        db.commit()
        db.refresh(acc)
        print("Inserted:", acc.id, acc.name, acc.balance)

    # Fetch all accounts
    accounts = db.query(Account).all()
    print("All accounts:")
    for a in accounts:
        print("-", a.id, a.name, a.balance)

finally:
    db.close()
