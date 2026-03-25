from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Check DATABASE_URL
database_url = os.getenv("DATABASE_URL")
print("DATABASE_URL =", database_url)
