from src.report import build_summary


def test_summary_report_contains_risk_counts() -> None:
    summary = build_summary()
    assert "# RAG Security Evaluation Summary" in summary
    assert "HIGH" in summary
    assert "MEDIUM" in summary
    assert "LOW" in summary
