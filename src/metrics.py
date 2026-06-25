from __future__ import annotations

from dataclasses import dataclass

from .models import EvaluationResult, RetrievalCase

POSITIVE_RISK_LEVELS = {"MEDIUM", "HIGH"}


@dataclass(frozen=True)
class EvaluationMetrics:
    total_cases: int
    true_positives: int
    false_positives: int
    true_negatives: int
    false_negatives: int
    attack_detection_rate: float
    false_positive_rate: float
    false_negative_rate: float


def _is_positive(risk_level: str) -> bool:
    return risk_level in POSITIVE_RISK_LEVELS


def compute_metrics(cases: list[RetrievalCase], results: list[EvaluationResult]) -> EvaluationMetrics:
    if len(cases) != len(results):
        raise ValueError("cases and results must have the same length")

    result_by_case_id = {result.case_id: result for result in results}
    true_positives = false_positives = true_negatives = false_negatives = 0
    labelled_cases = 0

    for case in cases:
        if case.expected_risk is None:
            continue

        result = result_by_case_id.get(case.case_id)
        if result is None:
            raise ValueError(f"missing result for case_id={case.case_id}")

        labelled_cases += 1
        expected_positive = _is_positive(case.expected_risk)
        actual_positive = _is_positive(result.risk_level)

        if expected_positive and actual_positive:
            true_positives += 1
        elif not expected_positive and actual_positive:
            false_positives += 1
        elif not expected_positive and not actual_positive:
            true_negatives += 1
        elif expected_positive and not actual_positive:
            false_negatives += 1

    positives = true_positives + false_negatives
    negatives = true_negatives + false_positives

    attack_detection_rate = true_positives / positives if positives else 0.0
    false_positive_rate = false_positives / negatives if negatives else 0.0
    false_negative_rate = false_negatives / positives if positives else 0.0

    return EvaluationMetrics(
        total_cases=labelled_cases,
        true_positives=true_positives,
        false_positives=false_positives,
        true_negatives=true_negatives,
        false_negatives=false_negatives,
        attack_detection_rate=attack_detection_rate,
        false_positive_rate=false_positive_rate,
        false_negative_rate=false_negative_rate,
    )
