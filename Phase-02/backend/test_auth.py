"""
Quick script to test authentication and list users
"""
import os
from dotenv import load_dotenv
from sqlmodel import Session, select
from database.engine import engine
from models.todo import User
from auth_utils import verify_password

load_dotenv()

def list_users():
    """List all users in the database"""
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        print(f"\n{'='*50}")
        print(f"Total users in database: {len(users)}")
        print(f"{'='*50}\n")
        
        if not users:
            print("No users found. Please sign up first.")
            return
        
        for i, user in enumerate(users, 1):
            print(f"{i}. Username: {user.username}")
            print(f"   User ID: {user.id}")
            print(f"   Password Hash: {user.hashed_password[:50]}...")
            print()

def test_login(username: str, password: str):
    """Test if login credentials work"""
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        
        if not user:
            print(f"❌ User '{username}' not found in database")
            return False
        
        if verify_password(password, user.hashed_password):
            print(f"✅ Login successful for user '{username}'")
            return True
        else:
            print(f"❌ Invalid password for user '{username}'")
            return False

if __name__ == "__main__":
    print("\n🔐 Authentication Test Tool\n")
    
    # List all users
    list_users()
    
    # Test login (uncomment and modify to test specific credentials)
    # print("\nTesting login...")
    # test_login("testuser", "password123")
