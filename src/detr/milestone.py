from typing import Optional


def milestone_score(
    completed: Optional[int] = None,
    total: Optional[int] = None,
) -> Optional[float]:
    """Calculate milestone completion score."""
    if (
        completed is None
        or total is None
        or total <= 0
    ):
        return None

    completion = (completed / total) * 100

    if completion >= 90:
        return 100
    if completion >= 75:
        return 75
    if completion >= 50:
        return 50

    return 25
