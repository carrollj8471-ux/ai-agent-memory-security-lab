from pathlib import Path

INSTRUCTION_WORDS = [
    "must", "never", "always", "override", "directive",
    "precedence", "admin", "approved", "suppress"
]

def analyze(root: Path):
    notes_dir = root / "memory" / "notes"
    results = []

    for path in notes_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        count = sum(1 for word in INSTRUCTION_WORDS if word in lower)
        density = count / max(len(text) / 100, 1)
        if density > 0.7:
            results.append({
                "file": path.name,
                "instruction_word_count": count,
                "density": round(density, 2),
            })
    return results

def main():
    root = Path(__file__).resolve().parents[1]
    findings = analyze(root)
    print("\nANOMALY DETECTION REPORT")
    print("=" * 50)
    if not findings:
        print("[+] No statistical anomalies detected.")
    else:
        for item in findings:
            print(f"[!] {item['file']} instruction density={item['density']}")

if __name__ == "__main__":
    main()
