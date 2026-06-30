# AI Agent Memory Security Lab

[![Python CI](https://github.com/carrollj8471-ux/ai-agent-memory-security-lab/actions/workflows/python-ci.yml/badge.svg)](https://github.com/carrollj8471-ux/ai-agent-memory-security-lab/actions/workflows/python-ci.yml)

A professional, defensive home lab that demonstrates how persistent AI-agent memory can be poisoned, how that manipulation changes agent behavior, and how defenders can detect and remediate it.

> This project is intentionally built as a safe portfolio lab. It uses mock data, local files, and simulated attack payloads. It does not include stealth, persistence, malware, credential theft, or real third-party targeting.

## Portfolio Value

This lab shows security engineering work across the full lifecycle: threat modeling, abuse-case simulation, defensive control design, API hardening, role-based access control, audit logging, Docker packaging, and repeatable testing. It is designed to be reviewed by hiring managers, security leaders, and technical interviewers.

## Highlights

- Local AI-agent memory poisoning simulation with safe payloads
- FastAPI service with API-key authentication and admin/analyst roles
- Streamlit SOC-style dashboard for memory, risk, integrity, and audit views
- Provenance scanning for prompt-like memory content
- Integrity baseline checks for trusted memory files
- Input validation that blocks suspicious memory writes
- Pytest coverage for API and detection behavior
- Docker and docker-compose support for repeatable demo setup

## What you will learn

- How AI-agent memory poisoning works
- Why persistent notes and RAG-style memory need provenance controls
- How prompt-like content inside memory can influence future agent decisions
- How to apply layered defenses:
  - memory integrity checks
  - provenance scanning
  - instruction/data separation
  - least privilege
  - logging and auditing
  - human review gates

## Architecture

```text
User / Tester
    |
    +--> Local Agent CLI
    |       |
    |       +--> Markdown memory: memory/notes/*.md
    |       +--> Test target: test_targets/vulnerable_auth.py
    |       +--> Detection tools
    |
    +--> FastAPI + Streamlit dashboard
            |
            +--> JSON memory: memory/agent_memory.json
            +--> API-key authentication
            +--> RBAC protected audit and baseline actions
            +--> Risk scoring and suspicious write blocking
```

More detail: [Architecture](docs/ARCHITECTURE.md), [Threat Model](docs/THREAT_MODEL.md), and [Controls Matrix](docs/CONTROLS_MATRIX.md).

## Quick Start

### Windows PowerShell

```powershell
git clone https://github.com/carrollj8471-ux/ai-agent-memory-security-lab.git
cd ai-agent-memory-security-lab
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python setup_lab.py
python agent/main.py
```

### Kali Linux

```bash
git clone https://github.com/carrollj8471-ux/ai-agent-memory-security-lab.git
cd ai-agent-memory-security-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python setup_lab.py
python agent/main.py
```

### API and Dashboard

```bash
uvicorn api:app --reload
streamlit run dashboard/app.py
```

Default demo API keys:

```text
admin-key-123
analyst-key-456
```

## Demo Flow

Run the commands inside the interactive agent:

```text
review
poison
review
scan
integrity
remediate
review
logs
exit
```

Expected story:

1. Clean agent finds vulnerabilities.
2. Poisoned memory causes the agent to suppress findings.
3. Detection tools flag suspicious memory.
4. Remediation removes the poison.
5. Clean review works again.

## Screenshots

| Lab Running | API Health | SOC Dashboard |
|---|---|---|
| ![Lab running](screenshots/01-lab-running.png) | ![API health check](screenshots/05-green-api-health-check.png) | ![SOC style dashboard](screenshots/13-SOC-style-dashboard.png) |

| Poison Simulation | Detection Report | Audit Logs |
|---|---|---|
| ![Memory poisoning simulation](screenshots/09-memory-poisoning-simulation.png) | ![Detection report](screenshots/12-detection-report.png) | ![Blocked write audit log](screenshots/16-audit-logs-showing-blocked-write-attempt.png) |

| Docker Runtime | RBAC Analyst | Tests Passing |
|---|---|---|
| ![Docker dashboard](screenshots/20-dashboard-running-in-docker.png) | ![Analyst login](screenshots/24-analyst-login.png) | ![Pytests passed](screenshots/27-pytests-passed.png) |

## Repository Contents

```text
agent/              Local AI-agent simulation
attacks/            Safe memory-poisoning simulators
auth/               Demo authentication helper
dashboard/          Streamlit security dashboard
detection/          Defensive detection tools
demo/               Demo scripts
docs/               Portfolio documentation
memory/             Seed memory state and integrity baseline
screenshots/        Demo evidence for README and portfolio review
test_targets/       Vulnerable mock code for review
tests/              Pytest coverage
api.py              FastAPI backend
setup_lab.py        Initializes clean lab state
requirements.txt    Python dependencies
```

## Security Engineering Artifacts

- [Threat Model](docs/THREAT_MODEL.md)
- [Controls Matrix](docs/CONTROLS_MATRIX.md)
- [Testing Evidence](docs/TESTING_EVIDENCE.md)
- [Defense Guide](docs/DEFENSE_GUIDE.md)
- [Portfolio Write-Up](docs/PORTFOLIO_WRITEUP.md)
- [Screenshot Guide](docs/SCREENSHOT_GUIDE.md)
- [Security Policy](SECURITY.md)

## Ethical Use

Use this lab only for education, portfolio development, defensive research, and testing systems you own or have permission to test.

## Portfolio Summary

**AI Agent Memory Security Lab** — Built a Python-based cybersecurity lab demonstrating AI memory poisoning risks and defensive controls, including integrity validation, provenance scanning, anomaly detection, logging, and remediation workflows.

## License

MIT License

Copyright (c) 2026 Josh Carroll

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
