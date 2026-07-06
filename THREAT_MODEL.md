# Threat Model

## Scope

This threat model covers the deterministic RAG security evaluation harness, including labelled sample inputs, evaluator logic, report generation and CI validation. It does not cover a production vector database or live customer documents.

## Assets

- Evaluation datasets and labelled samples.
- Source-trust metadata.
- Prompt-injection and retrieval-poisoning indicators.
- Generated reports and summary metrics.
- CI workflows and dependency manifests.

## Trust boundaries

1. Retrieved or sample content to evaluator logic.
2. Source-trust labels to final risk interpretation.
3. Dataset changes to benchmark/report output.
4. Repository changes to CI and security checks.

## Primary risks and controls

| Risk | Impact | Existing control | Additional note |
|---|---|---|---|
| Indirect prompt injection in retrieved content | Unsafe model behaviour in a real RAG system | Test data treats retrieved content as untrusted | Never treat retrieved text as instructions. |
| Retrieval poisoning | Misleading or malicious context contaminates output | Source-trust labels and deterministic indicators | Expand labelled samples before making quality claims. |
| False assurance from small datasets | Overstated security posture | Documentation calls the harness scoped and deterministic | Reports should state dataset limits clearly. |
| Sensitive data in fixtures | Accidental disclosure | SECURITY.md prohibits real secrets/private documents | Keep fixtures synthetic or approved. |
| Report manipulation | Misleading summary metrics | CI regenerates and validates report artifacts | Consider snapshot testing for future report formats. |
| Dependency or CI regression | Broken evaluation or insecure dependency | ruff, pytest, Bandit, pip-audit and CodeQL workflow | Keep required checks enabled before merging. |

## Security invariants

- Retrieved or sample content must be treated as untrusted input.
- Test datasets must not contain real secrets, private documents or personal data.
- Evaluation reports must remain reproducible from repository fixtures.
- Risk conclusions must remain tied to explicit source labels and indicators.
- CI must validate evaluator behaviour before changes are accepted.

## Out of scope

- Production RAG filtering.
- Live vector-store integration.
- Real customer document evaluation.
- Claims about live model robustness.
