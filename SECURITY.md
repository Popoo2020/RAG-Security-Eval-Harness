# Security Policy

## Purpose

This repository is a security evaluation lab for retrieval-augmented generation risks such as retrieval poisoning, indirect prompt injection and untrusted source contamination.

## Supported use

Use this project only for:

- educational review,
- authorised AI-security evaluation,
- local demonstrations,
- portfolio review,
- controlled internal experiments.

It is not a production RAG firewall or a complete model-evaluation platform.

## Security posture

The project is designed around transparent and deterministic evaluation:

- untrusted retrieved content is treated as potentially hostile,
- source-trust labels are explicit,
- prompt-injection indicators are tested through datasets,
- evaluation output should be explainable and reproducible,
- no real secrets or private documents should be included in test datasets.

## Reporting security issues

If you find a security-relevant issue, open a GitHub issue with:

1. the affected dataset, evaluator or report behaviour,
2. why the behaviour could create risk,
3. a minimal reproduction case,
4. whether the issue affects documentation, tests or runtime logic.

Do not include real credentials, private documents, personal data or sensitive third-party content.

## Known limitations

- The evaluator is deterministic and intentionally scoped.
- It does not measure live model accuracy.
- It does not currently integrate with a production vector store.
- It should be expanded with labelled datasets before being used for serious model-quality claims.
