from typing import Optional


def budget_score(
    planned_budget: Optional[float] = None,
    actual_spend: Optional[float] = None,
) -> Optional[float]:
    """Calculate budget burn score based on planned budget vs actual spend."""
    if (
        planned_budget is None
        or actual_spend is None
        or planned_budget <= 0
    ):
        return None

    burn = (actual_spend / planned_budget) * 100

    if burn <= 90:
        return 100
    if burn <= 100:
        return 80
    if burn <= 110:
        return 50

    return 20
