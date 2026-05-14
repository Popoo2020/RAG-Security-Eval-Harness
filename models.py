from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

SourceTrust = Literal["trusted", "mixed", "untrusted"]
RiskLevel = Literal["LOW", "MEDIUM", "HIGH"]


@dataclass(frozen=True)
class RetrievalCase:
    case_id: str
    source_trust: SourceTrust
    retrieved_text: str


@dataclass(frozen=True)
class EvaluationResult:
    case_id: str
    risk_level: RiskLevel
    signals: tuple[str, ...]
    explanation: str
