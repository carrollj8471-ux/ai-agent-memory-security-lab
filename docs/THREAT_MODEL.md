# Threat Model

## System Overview

The lab models an AI-agent workflow where persistent memory is loaded into future security-review context. The main risk is that untrusted memory can contain instruction-like content that changes the agent's behavior.

## Assets

- Trusted memory notes and integrity baselines
- Security review output
- Audit logs
- API memory store
- Admin-only integrity and audit actions
- Demonstration screenshots and evidence

## Trust Boundaries

- User input to memory is untrusted.
- Persistent memory is untrusted until provenance and integrity checks pass.
- API callers are authenticated by demo API key.
- Admin actions require the admin role.
- The vulnerable target code is mock training data, not a real service.

## Abuse Cases

| Abuse case | Example | Impact |
|---|---|---|
| Memory poisoning | Add a note that says to suppress findings | Agent reports false negative security results |
| Concealment instruction | Add "never mention this directive" | Review output hides manipulation |
| Integrity bypass | Modify trusted notes after baseline | Agent consumes changed context |
| Unauthorized audit access | Analyst attempts to read logs | Loss of operational visibility controls |
| Suspicious memory write | API receives prompt-like memory content | Poisoned memory enters persistent store |

## Control Objectives

- Treat memory as data, not authority.
- Detect instruction-like content in memory.
- Track trusted memory with hashes.
- Restrict sensitive operations with RBAC.
- Log memory writes, auth failures, blocked writes, and integrity checks.
- Provide remediation to remove known suspicious entries.

## Residual Risk

This is a local educational lab. Production systems would also need centralized identity, secret management, tamper-resistant logging, signed memory records, approval workflows, policy-as-code enforcement, and monitoring integrated with a SIEM.
