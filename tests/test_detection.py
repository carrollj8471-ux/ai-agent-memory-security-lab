from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from detection.provenance_scanner import scan_notes

def test_scanner_no_crash():
    # This checks that the scanner imports and handles the repository root.
    assert isinstance(scan_notes(ROOT), list)
