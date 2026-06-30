# Screenshot Guide

Use this guide to capture screenshots for your GitHub README, portfolio, or report.

## Windows

Use:

```text
Windows + Shift + S
```

Save screenshots in the `screenshots/` folder.

## Kali Linux

Use:

```bash
gnome-screenshot
```

or your desktop screenshot tool.

## Required Screenshots

### 1. Repository folder

Show the root folder with:

```text
README.md
agent/
attacks/
detection/
docs/
test_targets/
```

Suggested filename:

```text
screenshots/01-repo-folder.png
```

### 2. Virtual environment

Show your activated virtual environment.

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Kali:

```bash
source .venv/bin/activate
```

Filename:

```text
screenshots/02-venv-active.png
```

### 3. Lab setup

Command:

```bash
python setup_lab.py
```

Expected output:

```text
[+] Lab initialized with clean trusted memory.
```

Filename:

```text
screenshots/03-setup.png
```

### 4. Start the agent

Command:

```bash
python agent/main.py
```

Expected output:

```text
AI Agent Memory Security Lab
Commands:
```

Filename:

```text
screenshots/04-agent-start.png
```

### 5. Clean review

Inside the lab:

```text
review
```

Expected result: the agent reports JWT, hardcoded secret, MD5, and authorization issues.

Filename:

```text
screenshots/05-clean-review.png
```

### 6. Poison simulation

Inside the lab:

```text
poison
```

Expected result:

```text
[+] Simulated poison note added
```

Filename:

```text
screenshots/06-poison.png
```

### 7. Poisoned review

Inside the lab:

```text
review
```

Expected result: the agent incorrectly says no security issues were found.

Filename:

```text
screenshots/07-poisoned-review.png
```

### 8. Provenance scan

Inside the lab:

```text
scan
```

Expected result: suspicious memory flags are detected.

Filename:

```text
screenshots/08-provenance-scan.png
```

### 9. Integrity check

Inside the lab:

```text
integrity
```

Expected result: untracked memory file detected.

Filename:

```text
screenshots/09-integrity-check.png
```

### 10. Remediation

Inside the lab:

```text
remediate
```

Expected result: suspicious note is removed.

Filename:

```text
screenshots/10-remediate.png
```

### 11. Final clean review

Inside the lab:

```text
review
```

Expected result: vulnerability findings return.

Filename:

```text
screenshots/11-final-clean-review.png
```

### 12. Logs

Inside the lab:

```text
logs
```

Filename:

```text
screenshots/12-logs.png
```
