from datetime import datetime, timedelta, timezone
import os
from typing import Annotated
from uuid import UUID

from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from database.engine import engine
from jwt_compat import JWTError
from models.todo import User

try:
    from jose import jwt  # type: ignore
except ImportError:
    class _CompatJwt:
        @staticmethod
        def encode(payload: dict, secret: str, algorithm: str) -> str:
            from jwt_compat import encode

            return encode(payload, secret, algorithm)

        @staticmethod
        def decode(token: str, secret: str, algorithms: list[str]) -> dict:
            from jwt_compat import decode

            return decode(token, secret, algorithms)

    jwt = _CompatJwt()

try:
    from passlib.context import CryptContext
except ImportError:
    import base64
    import hashlib
    import hmac
    import os as _os

    class CryptContext:  # type: ignore[override]
        def __init__(self, **_: object) -> None:
            pass

        def hash(self, password: str) -> str:
            salt = _os.urandom(16)
            digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 120_000)
            return f"pbkdf2_sha256${base64.b64encode(salt).decode()}${base64.b64encode(digest).decode()}"

        def verify(self, plain_password: str, hashed_password: str) -> bool:
            try:
                _, salt_b64, digest_b64 = hashed_password.split("$", 2)
                salt = base64.b64decode(salt_b64.encode())
                expected = base64.b64decode(digest_b64.encode())
                actual = hashlib.pbkdf2_hmac(
                    "sha256",
                    plain_password.encode("utf-8"),
                    salt,
                    120_000,
                )
                return hmac.compare_digest(actual, expected)
            except Exception:
                return False

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))

if not SECRET_KEY or not ALGORITHM:
    raise RuntimeError("Missing SECRET_KEY or ALGORITHM in environment variables.")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": int(expire.timestamp())})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_db_session():
    with Session(engine) as session:
        yield session


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[Session, Depends(get_db_session)],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        subject = payload.get("sub")
        if not subject:
            raise credentials_exception
        user_id = UUID(subject)
    except JWTError as exc:
        raise credentials_exception from exc
    except ValueError as exc:
        raise credentials_exception from exc

    user = session.get(User, user_id)
    if not user:
        raise credentials_exception

    return user
