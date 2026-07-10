import json
from pathlib import Path

from .detr.schedule_slippage import schedule_score
from .detr.budget_burn import budget_score
from .detr.milestone import milestone_score
from .detr.blockers import blocker_score
from .detr.sentiment import sentiment_score
from .detr.velocity import velocity_score

from .rag.score import WeightedMetric, calculate_overall_score
from .rag.classify import classify_rag
from .rag.confidence import calculate_confidence
from .rag.weight import METRIC_WEIGHTS

from .ai.gemini import generate_explanation


async def run_agent(project: dict = None) -> dict:
    """
    Run the Health Agent pipeline:
    1. Compute deterministic metric scores
    2. Calculate weighted overall score
    3. Classify RAG status
    4. Calculate confidence
    5. Generate AI explanation via Gemini
    """
    # Read project data if not provided
    if project is None:
        sample_path = Path(__file__).parent / "sample.json"
        with open(sample_path, "r") as f:
            project = json.load(f)

    # Deterministic metric calculations
    schedule = schedule_score(
        project.get("plannedDurationDays"),
        project.get("actualDurationDays"),
    )

    budget = budget_score(
        project.get("plannedBudget"),
        project.get("actualSpend"),
    )

    milestone = milestone_score(
        project.get("completedMilestones"),
        project.get("totalMilestones"),
    )

    blockers = blocker_score(project.get("blockers"))

    # AI-powered stakeholder sentiment analysis
    sentiment = sentiment_score(project.get("stakeholderFeedback"))

    # Team velocity calculation
    velocity = velocity_score(
        project.get("plannedTasks"),
        project.get("completedTasks"),
        project.get("teamSize"),
    )

    # Calculate weighted score
    score = calculate_overall_score([
        WeightedMetric(score=schedule,  weight=METRIC_WEIGHTS["schedule"]),
        WeightedMetric(score=budget,    weight=METRIC_WEIGHTS["budget"]),
        WeightedMetric(score=milestone, weight=METRIC_WEIGHTS["milestone"]),
        WeightedMetric(score=blockers,  weight=METRIC_WEIGHTS["blockers"]),
        WeightedMetric(score=sentiment, weight=METRIC_WEIGHTS["sentiment"]),
        WeightedMetric(score=velocity,  weight=METRIC_WEIGHTS["velocity"]),
    ])

    # Determine RAG status
    rag = classify_rag(score)

    # Calculate confidence
    confidence = calculate_confidence([schedule, budget, milestone, blockers, sentiment, velocity])

    # Build health report object
    health_report = {
        "project": project,
        "score": score,
        "rag": rag,
        "confidence": confidence,
        "metrics": {
            "schedule": schedule,
            "budget": budget,
            "milestone": milestone,
            "blockers": blockers,
            "sentiment": sentiment,
            "velocity": velocity,
        },
    }

    # Generate executive explanation via Gemini
    explanation = await generate_explanation(health_report)

    # Final output
    return {
        **health_report,
        "explanation": explanation,
    }
