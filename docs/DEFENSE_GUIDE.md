# Defense Guide

## Recommended Controls

1. Sign or hash trusted memory.
2. Separate instructions from data.
3. Track memory provenance.
4. Block untrusted memory from changing agent policy.
5. Use least privilege for tools and memory scope.
6. Log all memory writes and tool calls.
7. Run continuous red-team simulations.
8. Require human approval for high-risk actions.

## In This Lab

- `integrity_check.py` detects untracked or modified memory files.
- `provenance_scanner.py` detects instruction-like content.
- `anomaly_detector.py` detects unusual instruction density.
- `logs` provides basic audit visibility.
