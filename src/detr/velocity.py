from typing import Optional


def velocity_score(
    planned_tasks: Optional[int] = None,
    completed_tasks: Optional[int] = None,
    team_size: Optional[int] = None,
) -> Optional[float]:
    """
    Calculate Team Velocity Score based on task throughput efficiency.

    Measures how effectively the team is delivering against planned capacity.
    Velocity = (completed_tasks / planned_tasks) * 100

    Scoring:
        >= 95%  → 100  (Exceeding or meeting targets)
        >= 80%  → 85   (Slightly below target, acceptable)
        >= 60%  → 60   (Underperforming, needs attention)
        >= 40%  → 35   (Significantly behind)
        < 40%   → 10   (Critical underperformance)

    If team_size is provided, the score is adjusted:
        - Small teams (1-3) get a 5-point bonus (harder to deliver with fewer people)
        - Large teams (10+) get a 5-point penalty (should be more productive)
    """
    if (
        planned_tasks is None
        or completed_tasks is None
        or planned_tasks <= 0
    ):
        return None

    velocity = (completed_tasks / planned_tasks) * 100

    if velocity >= 95:
        base_score = 100
    elif velocity >= 80:
        base_score = 85
    elif velocity >= 60:
        base_score = 60
    elif velocity >= 40:
        base_score = 35
    else:
        base_score = 10

    # Team size adjustment (optional)
    if team_size is not None and team_size > 0:
        if team_size <= 3:
            base_score = min(100, base_score + 5)  # Small team bonus
        elif team_size >= 10:
            base_score = max(0, base_score - 5)    # Large team penalty

    return base_score
