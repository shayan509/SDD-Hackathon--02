import os

from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

# Convert postgresql:// to postgresql+psycopg:// to use the psycopg driver
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

# Set connect_args based on database type
if DATABASE_URL.startswith("sqlite:///"):
    connect_args = {}
else:
    connect_args = {"sslmode": "require"}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)
