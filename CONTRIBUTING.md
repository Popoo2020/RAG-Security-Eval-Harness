# Contributing

Thanks for your interest in improving **RAG-Security-Eval-Harness**.

This repository is intentionally focused on reviewable, deterministic AI-security evaluation. Contributions should improve clarity, repeatability and safety.

## Good contribution areas

- additional retrieval-poisoning cases,
- indirect prompt-injection examples,
- source-trust evaluation logic,
- benchmark/report improvements,
- clearer test fixtures,
- documentation and architecture diagrams.

## Contribution rules

Before opening a pull request:

1. use synthetic or public-safe sample text only,
2. do not include private documents, credentials or personal data,
3. add tests for evaluator changes,
4. keep reports reproducible,
5. mark limitations honestly in documentation.

## Local validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python -m src.report
```

## Security expectations

Pull requests that add adversarial examples should keep them educational and bounded. The goal is to test defensive behaviour, not to provide operational abuse tooling.
