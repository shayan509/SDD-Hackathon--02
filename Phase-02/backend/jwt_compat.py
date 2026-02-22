import base64
import hashlib
import hmac
import json
from datetime import datetime, timezone
from typing import Any


class JWTError(Exception):
    pass


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64url_decode(data: str) -> bytes:
    padding = "=" * ((4 - len(data) % 4) % 4)
    return base64.urlsafe_b64decode((data + padding).encode("ascii"))


def encode(payload: dict[str, Any], secret: str, algorithm: str = "HS256") -> str:
    if algorithm != "HS256":
        raise JWTError("Unsupported algorithm")
    header = {"alg": algorithm, "typ": "JWT"}
    header_part = _b64url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    payload_part = _b64url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    signing_input = f"{header_part}.{payload_part}".encode("ascii")
    signature = hmac.new(secret.encode("utf-8"), signing_input, hashlib.sha256).digest()
    sig_part = _b64url_encode(signature)
    return f"{header_part}.{payload_part}.{sig_part}"


def decode(token: str, secret: str, algorithms: list[str]) -> dict[str, Any]:
    if "HS256" not in algorithms:
        raise JWTError("Unsupported algorithm")
    parts = token.split(".")
    if len(parts) != 3:
        raise JWTError("Invalid token")
    header_part, payload_part, sig_part = parts
    signing_input = f"{header_part}.{payload_part}".encode("ascii")
    expected_sig = hmac.new(secret.encode("utf-8"), signing_input, hashlib.sha256).digest()
    actual_sig = _b64url_decode(sig_part)
    if not hmac.compare_digest(expected_sig, actual_sig):
        raise JWTError("Invalid signature")
    payload = json.loads(_b64url_decode(payload_part).decode("utf-8"))
    exp = payload.get("exp")
    if exp is not None and datetime.now(timezone.utc).timestamp() >= float(exp):
        raise JWTError("Token expired")
    return payload
