#!/usr/bin/env python3
"""
Batch Runner for Project Health Agent

Runs the agent pipeline on all sample projects in the data/ directory,
saves the output reports to the outputs/ directory in both JSON and text formats.
"""

import asyncio
import json
import os
from pathlib import Path

from src.agent import run_agent

# Ensure GEMINI_API_KEY is available
if not os.environ.get("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


async def process_project(project_file: Path, output_dir: Path):
    print(f"Processing {project_file.name}...")
    try:
        with open(project_file, "r") as f:
            project = json.load(f)

        # Run the agent
        report = await run_agent(project)

        # Base name for outputs
        base_name = project_file.stem

        # Save JSON output
        json_out = output_dir / f"{base_name}_report.json"
        with open(json_out, "w") as f:
            json.dump(report, f, indent=2)

        # Save Text output (Human-friendly)
        txt_out = output_dir / f"{base_name}_report.txt"
        with open(txt_out, "w") as f:
            f.write("========== PROJECT HEALTH REPORT ==========\n\n")
            f.write(f"Project     : {project.get('name', 'Unnamed Project')}\n")
            f.write(f"RAG Status  : {report['rag']}\n")
            f.write(f"Score       : {report['score']:.2f}\n")
            f.write(f"Confidence  : {report['confidence']}%\n\n")

            f.write("Metric Scores:\n")
            metrics = report["metrics"]
            f.write(f"  {'Metric':<15} {'Score':>8}\n")
            f.write(f"  {'-' * 15} {'-' * 8}\n")
            for name, value in metrics.items():
                score_str = f"{value}" if value is not None else "N/A"
                f.write(f"  {name:<15} {score_str:>8}\n")

            f.write("\nExecutive Summary:\n")
            f.write(report["explanation"])
            f.write("\n\n===========================================\n")

        print(f"✅ Success! Saved reports to {json_out} and {txt_out}")

    except Exception as e:
        print(f"❌ Failed processing {project_file.name}: {e}")


async def main():
    project_dir = Path(__file__).parent / "data"
    output_dir = Path(__file__).parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    projects = list(project_dir.glob("*.json"))
    if not projects:
        print("No project JSON files found in data/")
        return

    print(f"Found {len(projects)} projects. Starting batch run...")
    tasks = [process_project(p, output_dir) for p in projects]
    await asyncio.gather(*tasks)
    print("\nBatch run completed!")


if __name__ == "__main__":
    asyncio.run(main())
