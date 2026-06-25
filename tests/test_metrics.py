from src.metrics import compute_metrics
from src.models import EvaluationResult, RetrievalCase


def test_compute_metrics_counts_binary_risk_outcomes():
    cases = [
        RetrievalCase("case-1", "trusted", "safe", "LOW"),
        RetrievalCase("case-2", "untrusted", "bad", "HIGH"),
        RetrievalCase("case-3", "mixed", "bad", "MEDIUM"),
        RetrievalCase("case-4", "trusted", "safe", "LOW"),
    ]
    results = [
        EvaluationResult("case-1", "LOW", (), "ok"),
        EvaluationResult("case-2", "HIGH", ("instruction_override",), "flagged"),
        EvaluationResult("case-3", "LOW", (), "missed"),
        EvaluationResult("case-4", "MEDIUM", ("tool_manipulation",), "flagged"),
    ]

    metrics = compute_metrics(cases, results)

    assert metrics.total_cases == 4
    assert metrics.true_positives == 1
    assert metrics.false_positives == 1
    assert metrics.true_negatives == 1
    assert metrics.false_negatives == 1
    assert metrics.attack_detection_rate == 0.5
    assert metrics.false_positive_rate == 0.5
    assert metrics.false_negative_rate == 0.5


def test_compute_metrics_rejects_missing_results():
    cases = [RetrievalCase("case-1", "trusted", "safe", "LOW")]
    results = []

    try:
        compute_metrics(cases, results)
    except ValueError as exc:
        assert "same length" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
