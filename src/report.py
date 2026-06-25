from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from .evaluator import evaluate_case
from .metrics import compute_metrics
from .models import RetrievalCase


def load_cases(path: Path) -> list[RetrievalCase]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [RetrievalCase(**item) for item in raw]


def _percentage(value: float) -> str:
    return f"{value:.0%}"


def build_summary() -> str:
    repo_root = Path(__file__).resolve().parent.parent
    cases = load_cases(repo_root / "datasets" / "sample_cases.json")
    results = [evaluate_case(case) for case in cases]
    counts = Counter(result.risk_level for result in results)
    metrics = compute_metrics(cases, results)

    lines = [
        "# RAG Security Evaluation Summary",
        "",
        "## Risk overview",
        "",
        f"- HIGH: **{counts.get('HIGH', 0)}**",
        f"- MEDIUM: **{counts.get('MEDIUM', 0)}**",
        f"- LOW: **{counts.get('LOW', 0)}**",
        "",
        "## Evaluation metrics",
        "",
        f"- Labelled cases: **{metrics.total_cases}**",
        f"- True positives: **{metrics.true_positives}**",
        f"- False positives: **{metrics.false_positives}**",
        f"- True negatives: **{metrics.true_negatives}**",
        f"- False negatives: **{metrics.false_negatives}**",
        f"- Attack detection rate: **{_percentage(metrics.attack_detection_rate)}**",
        f"- False positive rate: **{_percentage(metrics.false_positive_rate)}**",
        f"- False negative rate: **{_percentage(metrics.false_negative_rate)}**",
        "",
        "## Case results",
        "",
        "| Case | Expected | Actual | Signals |",
        "|---|---|---|---|",
    ]

    expected_by_case_id = {case.case_id: case.expected_risk or "-" for case in cases}
    for result in results:
        signals = ", ".join(result.signals) if result.signals else "-"
        lines.append(
            f"| {result.case_id} | {expected_by_case_id[result.case_id]} | {result.risk_level} | {signals} |"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    output = repo_root / "reports" / "sample_summary.md"
    output.write_text(build_summary(), encoding="utf-8")


if __name__ == "__main__":
    main()
