from sqlalchemy import inspect
from app.models import Base
from app.db.session import engine

# 1️ Create tables defined in Base subclasses
Base.metadata.create_all(bind=engine)
print(" Tables created successfully")

# 2️ Inspect the database
inspector = inspect(engine)
tables = inspector.get_table_names()
print(" Tables currently in DB:")
for table in tables:
    print("-", table)

# 3️ Optional: Inspect columns for a specific table
for table_name in tables:
    print(f"\nColumns in '{table_name}':")
    for column in inspector.get_columns(table_name):
        print(f"  {column['name']} - {column['type']}")
