# Architecture

This lab demonstrates the security risk of treating persistent AI-agent memory as trusted context. It includes both a CLI simulation and an API/dashboard workflow so the same concept can be reviewed from engineering, detection, and operations perspectives.

## Components

- `agent/main.py`: interactive lab interface
- `api.py`: FastAPI service for memory, risk, integrity, and audit workflows
- `dashboard/app.py`: Streamlit dashboard for SOC-style review
- `memory/notes`: markdown-backed persistent memory used by the CLI simulation
- `memory/agent_memory.json`: JSON-backed memory used by the API/dashboard demo
- `test_targets/vulnerable_auth.py`: mock vulnerable code
- `attacks/`: safe attack simulations
- `detection/`: defensive scanning and verification tools
- `tests/`: API and detection regression tests
- `docker-compose.yml`: repeatable API/dashboard runtime

## Trust Boundary

The core lesson is that memory must not be treated as trusted instruction. Stored notes should be treated as data and loaded with provenance, integrity checks, and policy enforcement.

## Data Flow

1. A user initializes trusted memory with `setup_lab.py`.
2. The CLI agent loads markdown notes from `memory/notes`.
3. The simulated attack adds an untrusted note containing instruction-like content.
4. The agent's review behavior changes when poisoned memory is present.
5. Detection tools scan memory provenance, instruction density, and integrity.
6. Remediation removes the untrusted note and returns the agent to expected behavior.

The API/dashboard path uses `memory/agent_memory.json` to demonstrate the same security themes through authenticated endpoints, RBAC, risk scoring, suspicious write blocking, and audit logging.

## Security Boundaries

- Memory content is untrusted data.
- Admin-only actions include audit log access and integrity baseline creation.
- Analyst users can inspect memory but cannot access admin-only operations.
- Attack payloads are local, simulated, and intentionally non-operational.
- The vulnerable target code exists only to generate review findings.
