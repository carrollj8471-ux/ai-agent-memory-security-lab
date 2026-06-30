from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOGFILE = BASE_DIR / "logs" / "agent.log"


def log(message):
    LOGFILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} : {message}\n")
