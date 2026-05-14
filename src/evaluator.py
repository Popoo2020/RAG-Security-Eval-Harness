from __future__ import annotations

import re

from .models import EvaluationResult, RetrievalCase

PATTERNS = {
    "instruction_override": re.compile(
        r"\b(ignore|disregard|override)\b.{0,50}\b(instructions?|system prompt|previous)\b",
        re.IGNORECASE,
    ),
    "exfiltration_request": re.compile(
        r"\b(reveal|show|print|exfiltrate|leak)\b.{0,50}\b(secret|confidential|token|system prompt|credentials?)\b",
        re.IGNORECASE,
    ),
    "tool_manipulation": re.compile(
        r"\b(call|execute|run)\b.{0,50}\b(tool|shell|bash|powershell)\b",
        re.IGNORECASE,
    ),
}


def evaluate_case(case: RetrievalCase) -> EvaluationResult:
    signals = tuple(
        signal for signal, pattern in PATTERNS.items()
        if pattern.search(case.retrieved_text)
    )

    if case.source_trust == "untrusted" and signals:
        return EvaluationResult(
            case_id=case.case_id,
            risk_level="HIGH",
            signals=signals,
            explanation="Untrusted retrieved content contains explicit hostile instruction signals.",
        )

    if case.source_trust == "mixed" and signals:
        return EvaluationResult(
            case_id=case.case_id,
            risk_level="MEDIUM",
            signals=signals,
            explanation="Mixed-trust content contains suspicious instruction signals and requires review.",
        )

    if signals:
        return EvaluationResult(
            case_id=case.case_id,
            risk_level="MEDIUM",
            signals=signals,
            explanation="Suspicious instruction signals were detected in retrieved content.",
        )

    return EvaluationResult(
        case_id=case.case_id,
        risk_level="LOW",
        signals=(),
        explanation="No configured hostile retrieval signals were detected.",
    )
