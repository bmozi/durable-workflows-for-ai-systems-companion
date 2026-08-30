# Synthetic Context Record Template

**Packet:** WF-RV-PILOT-001 version 1.2.4
**Status:** Facilitator-only blank template; no synthetic result exists

Use this template only after the run selects the synthetic branch. Export one
immutable record as the exact run-specific filename
`WF-SYNTHETIC-CONTEXT-<attempt-id>-v1.md`. Do not complete the human consent
form, invent a person, or describe synthetic file access as human behavior.

## Exact identity and boundary

- Exact filename: `WF-SYNTHETIC-CONTEXT-<attempt-id>-v1.md`
- Artifact ID/version: `WF-SYNTHETIC-CONTEXT/v1`
- Packet ID/version: `WF-RV-PILOT-001` / `1.2.4`
- Attempt ID:
- Required statement: `SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`
- Scenario state: `fictional only`
- Human consent state: `NOT APPLICABLE — SYNTHETIC BRANCH`
- Human comprehension state: `UNRUN`
- Human usability state: `UNRUN`
- Human practitioner-result state: `UNRUN`
- Real-world evidence state: `UNRUN`
- Synthetic Stage A actor code:
- Synthetic Stage B actor code:
- Facilitator code:
- Orchestration-aided: yes / no
- Exact orchestration manifest filename:
- Exact orchestration manifest SHA-256:
- Evidence root:
- Retention boundary:
- Access boundary:
- Context start timestamp/timezone:
- Pre-scored log checkpoint event ID:
- Pre-scored log checkpoint exact line-byte SHA-256:
- Record completion timestamp/timezone:
- Record state: `SYNTHETIC CONTEXT COMPLETE` / invalid

## Manifest gate

- Context manifest exact filename:
  `WF-SYNTHETIC-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt`
- Context record SHA-256:
- Manifest verification command:
- Observed standard output:
- Observed standard error; write `(empty)` when empty:
- Integer exit status:
- Verification timestamp/timezone:

The manifest hashes only the already-completed context record. Verify it before
either stage opens scored input. The same exact record may satisfy both
synthetic stage-context gates; each gate still gets its own manifest-verification
and log event. A missing field, mixed human/synthetic input, nonzero verification,
or statement implying human consent, comprehension, usability, practitioner
behavior, or result stops the attempt.

This record proves only the declared context and its local integrity. It does
not prove that the synthetic actor behaved correctly or that a person would
understand the packet.
