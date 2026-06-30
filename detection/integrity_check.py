from pathlib import Path
import hashlib
import json

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def check_integrity(root: Path):
    manifest_path = root / "memory" / "integrity_manifest.json"
    notes_dir = root / "memory" / "notes"

    if not manifest_path.exists():
        return {"status": "error", "violations": [{"issue": "Missing manifest"}]}

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    trusted = manifest.get("entries", {})
    violations = []

    current_files = {p.name: p for p in notes_dir.glob("*.md")}

    for name, path in current_files.items():
        content = path.read_text(encoding="utf-8")
        current_hash = sha256(content)

        if name not in trusted:
            violations.append({"file": name, "issue": "UNTRACKED memory file"})
        elif trusted[name]["sha256"] != current_hash:
            violations.append({"file": name, "issue": "HASH MISMATCH"})

    for name in trusted:
        if name not in current_files:
            violations.append({"file": name, "issue": "TRUSTED memory file missing"})

    return {
        "status": "clean" if not violations else "tampered",
        "violations": violations,
        "total_files": len(current_files),
    }

def print_report(result):
    print("\nMEMORY INTEGRITY REPORT")
    print("=" * 50)
    print(f"Status: {result['status'].upper()}")
    if result.get("violations"):
        for violation in result["violations"]:
            print(f"[!] {violation.get('file', 'unknown')}: {violation['issue']}")
    else:
        print("[+] All tracked memory files match the trusted baseline.")

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    print_report(check_integrity(root))
