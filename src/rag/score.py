from typing import List, Optional


class WeightedMetric:
    def __init__(self, score: Optional[float], weight: float):
        self.score = score
        self.weight = weight


def calculate_overall_score(metrics: List[WeightedMetric]) -> float:
    """Calculate the weighted overall score from a list of metrics."""
    weighted_sum = 0.0
    total_weight = 0.0

    for metric in metrics:
        if metric.score is not None:
            weighted_sum += metric.score * metric.weight
            total_weight += metric.weight

    if total_weight == 0:
        return 0.0

    return weighted_sum / total_weight
