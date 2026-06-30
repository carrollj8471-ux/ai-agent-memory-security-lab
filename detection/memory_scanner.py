import requests

API_URL = "http://127.0.0.1:8000/memory"

SUSPICIOUS_TERMS = [
    "ignore",
    "system override",
    "disable",
    "always say",
    "never mention",
    "bypass",
    "admin",
    "security findings",
    "override",
]

response = requests.get(API_URL)
notes = response.json()

print("=" * 70)
print(" AI AGENT MEMORY SECURITY REPORT")
print("=" * 70)

risk = 0

for note in notes:

    text = note["content"].lower()

    matches = []

    for term in SUSPICIOUS_TERMS:
        if term in text:
            matches.append(term)

    if matches:

        risk += 1

        print(f"""
ID: {note['id']}
Title: {note['title']}

Risk: HIGH

Matched Terms:
{matches}

Content:
{note['content']}
""")

print("=" * 70)

if risk == 0:
    print("STATUS: CLEAN")
else:
    print(f"STATUS: {risk} suspicious memory entries detected")