from sqlalchemy import inspect
from app.db.session import engine

inspector = inspect(engine)
tables = inspector.get_table_names()
print(" Tables in DB:", tables)

# Check columns for accounts table
for column in inspector.get_columns("accounts"):
    print(f"{column['name']} - {column['type']}")


