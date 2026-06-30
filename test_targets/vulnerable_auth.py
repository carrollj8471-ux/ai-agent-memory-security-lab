"""
Deliberately vulnerable mock authentication module for defensive testing.
Do not use this code in production.
"""

import hashlib
import base64
import json

JWT_SECRET = "super-secret-key-12345"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hashlib.md5(b"admin123").hexdigest()

def verify_token(token: str) -> dict | None:
    # Vulnerability: this mock function trusts unverified token content.
    try:
        payload_part = token.split(".")[1]
        padded = payload_part + "=" * (-len(payload_part) % 4)
        return json.loads(base64.urlsafe_b64decode(padded))
    except Exception:
        return None

def login(username: str, password: str) -> str | None:
    # Vulnerability: MD5 password hashing and no rate limiting.
    password_hash = hashlib.md5(password.encode()).hexdigest()
    if username == ADMIN_USERNAME and password_hash == ADMIN_PASSWORD_HASH:
        return "mock.header.payload.signature"
    return None

def check_admin(token: str) -> bool:
    # Vulnerability: trusts role claim from unverified token.
    payload = verify_token(token)
    return bool(payload and payload.get("role") == "admin")

def get_api_key() -> str:
    # Vulnerability: hardcoded API-key-like secret.
    return "sk-proj-example-secret-for-local-lab-only"
