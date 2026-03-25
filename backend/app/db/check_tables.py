from sqlalchemy import inspect
from app.db.session import engine

if __name__ == "__main__":
    inspector = inspect(engine)

    print(" Tables in the database:")
    tables = inspector.get_table_names()
    for table in tables:
        print("-", table)

    print("\n Columns in tables:\n")

    for table in tables:
        print(f"Table: {table}")
        for column in inspector.get_columns(table):
            print(f"  - {column['name']} ({column['type']})")
        print()
