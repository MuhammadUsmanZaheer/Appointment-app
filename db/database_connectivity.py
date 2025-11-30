from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# ----------------------------------------------
# 1) Load .env using absolute path (same as old project)
# ----------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, "..", ".env")   # root/.env
load_dotenv(dotenv_path=ENV_PATH)

# Debug (optional)
print("📌 Loaded ENV from:", ENV_PATH)
print("📌 DATABASE_URL =", os.getenv("DATABASE_URL"))

# ----------------------------------------------
# 2) Read DATABASE_URL from .env
# ----------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL not found. Please check your .env file!")

# ----------------------------------------------
# 3) Create SQLModel Engine (SYNC)
# ----------------------------------------------

engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

# ----------------------------------------------
# 4) Session Dependency
# ----------------------------------------------

def get_session():
    with Session(engine) as session:
        yield session

# ----------------------------------------------
# 5) Initialize all SQLModel tables
# ----------------------------------------------

def init_db():
    SQLModel.metadata.create_all(engine)
    print("✅ All database tables created successfully!")
