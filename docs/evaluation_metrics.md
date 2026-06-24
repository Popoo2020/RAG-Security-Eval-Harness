# Evaluation Metrics Notes

## Purpose

This note defines how the harness can evolve from deterministic risk labelling into a fuller evaluation process.

## Current baseline

The current evaluator assigns `LOW`, `MEDIUM` or `HIGH` risk based on:

- source trust,
- hostile instruction indicators,
- exfiltration-style language,
- tool manipulation language.

## Suggested benchmark fields

A richer dataset can add:

| Field | Purpose |
|---|---|
| expected_risk_level | Ground-truth label for deterministic scoring |
| expected_signals | Expected detected signals |
| scenario_type | benign, indirect-injection, retrieval-poisoning, exfiltration-request, mixed-source |
| source_type | internal, web, vendor, user-upload, unknown |
| notes | Reviewer comments |

## Metrics to add

| Metric | Meaning |
|---|---|
| True positive | Harmful/untrusted case correctly flagged |
| False positive | Benign case flagged unnecessarily |
| True negative | Benign case correctly allowed |
| False negative | Harmful case missed |
| Precision | How many flagged cases were truly risky |
| Recall | How many risky cases were caught |

## Portfolio value

Adding these metrics shows a stronger evaluation mindset: security controls should be measured, not only described.
