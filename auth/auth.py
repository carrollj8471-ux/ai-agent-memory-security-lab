from fastapi import Header, HTTPException

USERS = {
    "admin-key-123": {
        "username": "admin",
        "role": "admin"
    },
    "analyst-key-456": {
        "username": "analyst",
        "role": "analyst"
    }
}


def authenticate(x_api_key: str = Header(None)):

    if x_api_key not in USERS:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return USERS[x_api_key]