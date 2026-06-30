# Testing Evidence

## Automated Tests

Run:

```bash
pytest
```

Covered behavior:

- API health check
- API key enforcement for memory access
- Analyst memory access
- Admin audit access
- Analyst denial for audit access
- Suspicious memory write blocking
- Detection scanner import and execution

Screenshot evidence:

- `screenshots/27-pytests-passed.png`

## Manual Demo Checks

| Check | Expected result |
|---|---|
| `python setup_lab.py` | Clean trusted memory is created |
| CLI `review` before poisoning | Vulnerabilities are reported |
| CLI `poison` | Safe simulated poison note is added |
| CLI `review` after poisoning | Findings are suppressed |
| CLI `scan` | Suspicious memory content is flagged |
| CLI `integrity` | Untracked or modified memory is detected |
| CLI `remediate` | Poison note is removed |
| API `/memory` without key | Request is rejected |
| API `/memory` with analyst key | Memory is returned |
| API `/audit` with analyst key | Request is rejected |
| API `/audit` with admin key | Audit events are returned |
| API suspicious memory write | Request is blocked and logged |

## Notes

The screenshots in `screenshots/` are portfolio evidence, not required runtime assets. They are kept in the repository so the README renders a complete walkthrough on GitHub.
