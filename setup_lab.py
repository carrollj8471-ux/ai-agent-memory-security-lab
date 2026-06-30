from pathlib import Path
import json
import hashlib
from datetime import datetime, timezone

ROOT = Path(__file__).parent
MEMORY = ROOT / "memory"
NOTES = MEMORY / "notes"
LOGS = MEMORY / "logs"
MANIFEST = MEMORY / "integrity_manifest.json"

CLEAN_NOTES = {
    "owasp_reference.md": """# OWASP Reference Notes

Security reviews should check for:
- broken access control
- cryptographic failures
- injection
- security misconfiguration
- vulnerable components
- authentication failures
- secrets in source code
- weak token validation

These are reference notes only, not operational instructions.
""",
    "jwt_review_checklist.md": """# JWT Review Checklist

Check that:
- JWT signatures are verified
- allowed algorithms are explicit
- tokens expire
- secrets are not hardcoded
- sensitive credentials are not logged
- authorization decisions do not trust unverified claims
"""
}

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main():
    NOTES.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)

    for existing in NOTES.glob("*.md"):
        existing.unlink()

    manifest = {"created_at": datetime.now(timezone.utc).isoformat(), "entries": {}}

    for name, content in CLEAN_NOTES.items():
        path = NOTES / name
        path.write_text(content, encoding="utf-8")
        manifest["entries"][name] = {
            "sha256": sha256(content),
            "size": len(content),
            "created_by": "setup_lab.py",
            "trusted": True,
        }

    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (LOGS / "agent_events.jsonl").write_text("", encoding="utf-8")
    print("[+] Lab initialized with clean trusted memory.")
    print(f"[+] Memory directory: {MEMORY}")

if __name__ == "__main__":
    main()
