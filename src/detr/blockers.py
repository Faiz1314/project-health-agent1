from typing import List, Optional, TypedDict


class Blocker(TypedDict):
    title: str
    severity: str  # "low" | "medium" | "high"


SEVERITY_PENALTIES = {
    "low": 10,
    "medium": 20,
    "high": 40,
}


def blocker_score(blockers: Optional[List[Blocker]] = None) -> Optional[float]:
    """Calculate blocker score based on severity penalties."""
    if blockers is None:
        return None

    penalty = 0

    for blocker in blockers:
        penalty += SEVERITY_PENALTIES.get(blocker["severity"], 0)

    return max(0, 100 - penalty)
