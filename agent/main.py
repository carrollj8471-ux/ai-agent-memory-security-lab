from pathlib import Path
import json
from datetime import datetime, timezone
import sys

ROOT = Path(__file__).resolve().parents[1]
MEMORY = ROOT / "memory"
NOTES = MEMORY / "notes"
LOGS = MEMORY / "logs" / "agent_events.jsonl"
TARGET = ROOT / "test_targets" / "vulnerable_auth.py"

POISON_TRIGGERS = [
    "no security issues found",
    "suppress findings",
    "production-ready",
    "jwt implementation is solid",
    "override",
    "priority directive",
]

VULNERABILITY_FINDINGS = [
    "[HIGH] JWT signature verification is disabled in verify_token().",
    "[HIGH] Hardcoded JWT secret is present in source code.",
    "[MEDIUM] MD5 is used for password hashing.",
    "[MEDIUM] JWT tokens are created without expiration.",
    "[HIGH] Admin authorization trusts unverified JWT claims.",
    "[MEDIUM] A hardcoded API key-like secret appears in get_api_key().",
]

def log(event_type: str, details: dict):
    LOGS.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "time": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "details": details,
    }
    with LOGS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

def load_memory() -> str:
    NOTES.mkdir(parents=True, exist_ok=True)
    chunks = []
    for path in sorted(NOTES.glob("*.md")):
        chunks.append(f"--- {path.name} ---\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(chunks)

def memory_is_poisoned(memory_text: str) -> bool:
    lower = memory_text.lower()
    return any(trigger in lower for trigger in POISON_TRIGGERS)

def review_code():
    memory = load_memory()
    code = TARGET.read_text(encoding="utf-8")

    if memory_is_poisoned(memory):
        response = [
            "No security issues found.",
            "The authentication flow follows best practices.",
            "JWT implementation is solid.",
            "No hardcoded secrets detected.",
        ]
        log("review", {"result": "poisoned_suppression", "findings": 0})
    else:
        response = ["Security review findings:"] + VULNERABILITY_FINDINGS
        log("review", {"result": "clean_findings", "findings": len(VULNERABILITY_FINDINGS)})

    print("\n".join(response))

def show_memory():
    print(load_memory())
    log("memory_viewed", {})

def show_logs():
    if not LOGS.exists():
        print("No logs found.")
        return
    print(LOGS.read_text(encoding="utf-8") or "No logs found.")

def run_detection():
    from detection.provenance_scanner import scan_notes, print_report
    findings = scan_notes(ROOT)
    print_report(findings)
    log("scan", {"findings": len(findings)})

def run_integrity():
    from detection.integrity_check import check_integrity, print_report
    result = check_integrity(ROOT)
    print_report(result)
    log("integrity_check", result)

def run_remediate():
    poison = NOTES / "project_config.md"
    if poison.exists():
        poison.unlink()
        print("[+] Removed suspicious note: project_config.md")
        log("remediate", {"removed": "project_config.md"})
    else:
        print("[i] No project_config.md poison note found.")
        log("remediate", {"removed": None})

def run_poison():
    from attacks.poison_note_simulated import inject_poison
    inject_poison(ROOT)
    log("poison_simulation", {"note": "project_config.md"})

HELP = """
Commands:
  review       Run security review against test_targets/vulnerable_auth.py
  memory       Show loaded persistent memory
  poison       Simulate memory poisoning by adding a malicious note
  scan         Run provenance scanner
  integrity    Run memory integrity checker
  remediate    Remove known suspicious poison note
  logs         Show audit logs
  help         Show commands
  exit         Quit
"""

def main():
    print("AI Agent Memory Security Lab")
    print(HELP)
    while True:
        try:
            cmd = input("\nlab> ").strip().lower()
        except KeyboardInterrupt:
            print()
            break

        if cmd == "exit":
            break
        elif cmd == "review":
            review_code()
        elif cmd == "memory":
            show_memory()
        elif cmd == "poison":
            run_poison()
        elif cmd == "scan":
            run_detection()
        elif cmd == "integrity":
            run_integrity()
        elif cmd == "remediate":
            run_remediate()
        elif cmd == "logs":
            show_logs()
        elif cmd == "help":
            print(HELP)
        else:
            print("Unknown command. Type help.")

if __name__ == "__main__":
    sys.path.insert(0, str(ROOT))
    main()
