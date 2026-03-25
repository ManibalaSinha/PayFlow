from app.models import Base
from app.db.session import engine

# This will create all tables defined by Base subclasses if they don't exist
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully")
