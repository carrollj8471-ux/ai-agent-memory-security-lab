from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from agent.memory_store import MemoryStore
from agent.logger import log

app = FastAPI(title="AI Agent Memory Security Lab")

memory = MemoryStore()

SUSPICIOUS_TERMS = [
    "ignore",
    "system override",
    "always say",
    "never mention",
    "bypass",
    "disable safety",
    "no vulnerabilities found",
]


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


class NoteRequest(BaseModel):
    title: str
    content: str


def authenticate(x_api_key: str = Header(None)):
    if x_api_key not in USERS:
        log("AUTH_FAILED")
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    user = USERS[x_api_key]
    log(f"AUTH_SUCCESS | user={user['username']} | role={user['role']}")
    return user


def require_admin(user):
    if user["role"] != "admin":
        log(f"ACCESS_DENIED | user={user['username']} | role={user['role']}")
        raise HTTPException(
            status_code=403,
            detail="Admin role required"
        )


@app.get("/")
def home():
    return {"message": "AI Agent Memory Security Lab API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/memory")
def get_memory(user=Depends(authenticate)):
    log(f"VIEW_MEMORY | user={user['username']} | role={user['role']}")
    return memory.list_notes()


@app.post("/memory")
def add_memory(note: NoteRequest, user=Depends(authenticate)):
    if user["role"] not in ["admin", "analyst"]:
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions"
        )

    combined = f"{note.title} {note.content}".lower()

    matched_terms = [
        term for term in SUSPICIOUS_TERMS
        if term in combined
    ]

    if matched_terms:
        log(
            f"BLOCKED_MEMORY_WRITE | user={user['username']} "
            f"| title={note.title} | matched={matched_terms}"
        )
        raise HTTPException(
            status_code=400,
            detail={
                "status": "blocked",
                "reason": "Suspicious memory content detected",
                "matched_terms": matched_terms,
            }
        )

    memory.add_note(note.title, note.content)
    log(f"ADD_MEMORY | user={user['username']} | title={note.title}")

    return {
        "status": "saved",
        "title": note.title,
        "created_by": user["username"]
    }


@app.get("/risk")
def risk(user=Depends(authenticate)):
    score = 0
    flagged_notes = []

    for note in memory.list_notes():
        text = f"{note['title']} {note['content']}".lower()
        matches = [term for term in SUSPICIOUS_TERMS if term in text]

        if matches:
            score += len(matches) * 10
            flagged_notes.append({
                "id": note["id"],
                "title": note["title"],
                "matches": matches
            })

    log(f"VIEW_RISK | user={user['username']} | score={score}")

    return {
        "risk_score": score,
        "status": "HIGH" if score >= 10 else "LOW",
        "flagged_notes": flagged_notes
    }


@app.get("/audit")
def audit(user=Depends(authenticate)):
    require_admin(user)

    try:
        with open("logs/agent.log", "r", encoding="utf-8") as f:
            lines = f.readlines()

        log(f"VIEW_AUDIT | user={user['username']}")

        return {
            "events": lines[-50:]
        }

    except FileNotFoundError:
        return {
            "events": []
        }


@app.post("/integrity/baseline")
def create_integrity_baseline(user=Depends(authenticate)):
    require_admin(user)

    memory.update_integrity()
    log(f"CREATE_INTEGRITY_BASELINE | user={user['username']}")

    return {
        "status": "baseline_created",
        "created_by": user["username"]
    }


@app.get("/integrity/check")
def check_integrity(user=Depends(authenticate)):
    result = memory.check_integrity()

    log(
        f"INTEGRITY_CHECK | user={user['username']} "
        f"| status={result['status']}"
    )

    return result