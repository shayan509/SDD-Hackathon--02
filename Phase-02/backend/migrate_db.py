import argparse
import os

from dotenv import load_dotenv
from sqlmodel import SQLModel

from database.engine import engine

load_dotenv()


def initialize_schema(reset: bool = False) -> None:
    if not os.getenv("DATABASE_URL"):
        raise RuntimeError("DATABASE_URL is not configured.")

    if reset:
        SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize Todo schema.")
    parser.add_argument("--reset", action="store_true", help="Drop and recreate all tables.")
    args = parser.parse_args()
    initialize_schema(reset=args.reset)
    print("Schema initialization complete.")
