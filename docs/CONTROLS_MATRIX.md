# Controls Matrix

| Risk | Control | Implementation | Evidence |
|---|---|---|---|
| Poisoned memory suppresses findings | Provenance scanner | `detection/provenance_scanner.py` | `screenshots/11-poisoned-memory-detection.png`, `screenshots/12-detection-report.png` |
| Trusted memory is modified | Integrity baseline and hash check | `detection/integrity_check.py`, `agent/memory_store.py` | `screenshots/21-integrity-baseline-created.png`, `screenshots/22-integrity-check-passed.png` |
| Prompt-like memory is written through API | Suspicious term blocking | `api.py` `/memory` POST validation | `screenshots/14-input-validation.png`, `screenshots/15-input-validation-2.png` |
| Unauthorized API access | API key authentication | `api.py` `authenticate()` | `screenshots/23-unauthorized-access.png`, `screenshots/26-api-key-authentication.png` |
| Excess privilege | Admin/analyst role split | `api.py` `require_admin()` | `screenshots/24-analyst-login.png`, `screenshots/25-admin-login.png` |
| Weak operational visibility | Audit logging | `agent/logger.py`, `api.py` audit events | `screenshots/16-audit-logs-showing-blocked-write-attempt.png` |
| Regression risk | Automated tests | `tests/test_api.py`, `tests/test_detection.py` | `screenshots/27-pytests-passed.png` |
| Inconsistent demo setup | Containerized runtime | `Dockerfile`, `docker-compose.yml` | `screenshots/17-docker-build.png`, `screenshots/18-docker-compose-up.png`, `screenshots/20-dashboard-running-in-docker.png` |


