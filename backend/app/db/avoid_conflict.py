from app.db.session import SessionLocal
from app.models import Account

db = SessionLocal()

try:
    # Check if the account already exists
    existing = db.query(Account).filter(Account.name == "Test Account").first()
    
    if existing:
        print(f" Account already exists: {existing.id} - {existing.name}")
    else:
        # Create a new account
        new_acc = Account(name="Test Account", balance=1000)
        db.add(new_acc)
        db.commit()
        db.refresh(new_acc)
        print(f"s Account inserted: {new_acc.id} - {new_acc.name} - {new_acc.balance}")

finally:
    db.close()
