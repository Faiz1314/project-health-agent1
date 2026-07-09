from typing import Optional


def schedule_score(
    planned_duration_days: Optional[int] = None,
    actual_duration_days: Optional[int] = None,
) -> Optional[float]:
    """Calculate schedule slippage score based on planned vs actual duration."""
    if (
        planned_duration_days is None
        or actual_duration_days is None
        or planned_duration_days <= 0
    ):
        return None

    slippage = ((actual_duration_days - planned_duration_days) / planned_duration_days) * 100

    if slippage <= 0:
        return 100
    if slippage <= 5:
        return 90
    if slippage <= 10:
        return 75
    if slippage <= 15:
        return 50
    if slippage <= 20:
        return 25

    return 0
