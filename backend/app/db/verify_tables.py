from sqlalchemy import inspect
from app.db.session import engine

if __name__ == "__main__":
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(" Tables in DB:", tables)
