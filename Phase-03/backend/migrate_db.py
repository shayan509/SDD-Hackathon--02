"""
Database migration script to add description and created_at columns to existing todos table.
"""
from sqlmodel import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(DATABASE_URL)

def migrate():
    """Add new columns to the todoitem table."""
    with engine.connect() as conn:
        try:
            # Check if description column exists
            result = conn.execute(text("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name='todoitem' AND column_name='description'
            """))
            
            if not result.fetchone():
                print("Adding 'description' column...")
                conn.execute(text("""
                    ALTER TABLE todoitem 
                    ADD COLUMN description VARCHAR(1000) DEFAULT ''
                """))
                conn.commit()
                print("✓ Added 'description' column")
            else:
                print("✓ 'description' column already exists")
            
            # Check if created_at column exists
            result = conn.execute(text("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name='todoitem' AND column_name='created_at'
            """))
            
            if not result.fetchone():
                print("Adding 'created_at' column...")
                conn.execute(text("""
                    ALTER TABLE todoitem 
                    ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                """))
                conn.commit()
                print("✓ Added 'created_at' column")
            else:
                print("✓ 'created_at' column already exists")
            
            print("\n✅ Migration completed successfully!")
            
        except Exception as e:
            print(f"❌ Migration failed: {e}")
            conn.rollback()

if __name__ == "__main__":
    print("Starting database migration...\n")
    migrate()
