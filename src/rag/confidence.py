from typing import List, Optional
import math


def calculate_confidence(scores: List[Optional[float]]) -> int:
    """Calculate confidence as percentage of non-null scores."""
    available = sum(1 for score in scores if score is not None)
    return round((available / len(scores)) * 100)
