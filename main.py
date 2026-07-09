#!/usr/bin/env python3
"""
Health Agent — Project Health Reporting Tool

Reads project data from sample.json, computes deterministic health metrics,
classifies RAG status, and generates an AI-powered executive summary.

Usage:
    python main.py
"""

import asyncio
import json
from pathlib import Path

from src.agent import run_agent


async def main():
    try:
        # Read the project plan
        sample_path = Path(__file__).parent / "src" / "sample.json"
        with open(sample_path, "r") as f:
            project = json.load(f)

        # Run the agent
        report = await run_agent(project)

        print("\n========== PROJECT HEALTH REPORT ==========\n")

        print(f"Project     : {project.get('name', 'Unnamed Project')}")
        print(f"RAG Status  : {report['rag']}")
        print(f"Score       : {report['score']:.2f}")
        print(f"Confidence  : {report['confidence']}%")

        print("\nMetric Scores")
        metrics = report["metrics"]
        print(f"  {'Metric':<15} {'Score':>8}")
        print(f"  {'-' * 15} {'-' * 8}")
        for name, value in metrics.items():
            score_str = f"{value}" if value is not None else "N/A"
            print(f"  {name:<15} {score_str:>8}")

        print("\nExecutive Summary")
        print(report["explanation"])

        print("\n===========================================\n")

    except Exception as err:
        print("Failed to execute Project Health Agent")
        print(err)
        raise


if __name__ == "__main__":
    asyncio.run(main())
