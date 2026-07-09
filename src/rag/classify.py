from typing import Literal

RAGStatus = Literal["GREEN", "AMBER", "RED"]


def classify_rag(score: float) -> RAGStatus:
    """Classify a score into Red, Amber, or Green status."""
    if score >= 80:
        return "GREEN"
    if score >= 60:
        return "AMBER"
    return "RED"
