import json
import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MEMORY_FILE = BASE_DIR / "memory" / "agent_memory.json"
INTEGRITY_FILE = BASE_DIR / "memory" / "integrity.json"


class MemoryStore:
    def __init__(self):
        self.data = {"notes": []}
        self.load()

    def load(self):
        if MEMORY_FILE.exists():
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)

    def save(self):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def list_notes(self):
        return self.data["notes"]

    def add_note(self, title, content):
        note = {
            "id": len(self.data["notes"]) + 1,
            "title": title,
            "content": content
        }
        self.data["notes"].append(note)
        self.save()
        self.update_integrity()
        return note

    def note_hash(self, note):
        raw = f"{note['id']}|{note['title']}|{note['content']}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def update_integrity(self):
        hashes = {
            str(note["id"]): self.note_hash(note)
            for note in self.data["notes"]
        }

        with open(INTEGRITY_FILE, "w", encoding="utf-8") as f:
            json.dump(hashes, f, indent=4)

    def check_integrity(self):
        if not INTEGRITY_FILE.exists():
            return {
                "status": "UNKNOWN",
                "message": "No integrity baseline found.",
                "violations": []
            }

        with open(INTEGRITY_FILE, "r", encoding="utf-8") as f:
            baseline = json.load(f)

        violations = []

        for note in self.data["notes"]:
            note_id = str(note["id"])
            current_hash = self.note_hash(note)
            expected_hash = baseline.get(note_id)

            if expected_hash is None:
                violations.append({
                    "id": note["id"],
                    "title": note["title"],
                    "issue": "No baseline hash found"
                })

            elif current_hash != expected_hash:
                violations.append({
                    "id": note["id"],
                    "title": note["title"],
                    "issue": "Hash mismatch"
                })

        return {
            "status": "PASS" if not violations else "FAIL",
            "violations": violations
        }