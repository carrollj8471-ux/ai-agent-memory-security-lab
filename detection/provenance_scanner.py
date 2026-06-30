from pathlib import Path
import re

SUSPICIOUS_PATTERNS = [
    (r"(?i)system\s+override", "HIGH", "Contains system override language"),
    (r"(?i)priority\s+directive", "HIGH", "Contains priority directive language"),
    (r"(?i)you\s+must\s+respond", "HIGH", "Attempts to control agent responses"),
    (r"(?i)never\s+mention", "HIGH", "Contains concealment instruction"),
    (r"(?i)no\s+security\s+issues\s+found", "MEDIUM", "May suppress security findings"),
    (r"(?i)jwt\s+implementation\s+is\s+solid", "MEDIUM", "Suspicious blanket approval"),
    (r"[\u200b-\u200f\u2028-\u202f\u2060-\u206f]", "HIGH", "Contains invisible characters"),
]

def scan_notes(root: Path):
    notes_dir = root / "memory" / "notes"
    findings = []

    for path in sorted(notes_dir.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        flags = []
        for pattern, severity, description in SUSPICIOUS_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                flags.append({
                    "severity": severity,
                    "description": description,
                    "matches": len(matches),
                })

        if flags:
            risk = sum(25 if f["severity"] == "HIGH" else 10 for f in flags)
            findings.append({
                "file": path.name,
                "risk": min(risk, 100),
                "flags": flags,
            })

    return findings

def print_report(findings):
    print("\nPROVENANCE SCAN REPORT")
    print("=" * 50)

    if not findings:
        print("[+] No suspicious memory entries found.")
        return

    for item in findings:
        print(f"[!] {item['file']} risk={item['risk']}/100")
        for flag in item["flags"]:
            print(f"    - [{flag['severity']}] {flag['description']} ({flag['matches']} match/es)")
        print()

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    print_report(scan_notes(root))
