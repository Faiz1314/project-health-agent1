#!/usr/bin/env python3
"""
Weekly Scheduler for Project Health Agent

This script runs the batch execution (run_all.py) every week (7 days).
It can be run as a daemon or background process.
"""

import time
import os
import sys
import subprocess
from pathlib import Path

INTERVAL_SECONDS = 7 * 24 * 60 * 60  # 7 days


def run_batch():
    print(f"[{time.asctime()}] Triggering weekly Project Health Agent run...")
    script_path = Path(__file__).parent / "run_all.py"

    # Forward the current environment variables (including GEMINI_API_KEY)
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print(f"Errors:\n{result.stderr}", file=sys.stderr)


def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    print("==================================================")
    print("Project Health Agent Weekly Scheduler Started")
    print(f"Interval: Every 7 days ({INTERVAL_SECONDS} seconds)")
    print("Press Ctrl+C to stop.")
    print("==================================================")

    # Run immediately on start
    run_batch()

    # Loop with periodic checking
    try:
        while True:
            print(f"[{time.asctime()}] Sleeping for 7 days...")
            time.sleep(INTERVAL_SECONDS)
            run_batch()
    except KeyboardInterrupt:
        print("\nScheduler stopped by user.")


if __name__ == "__main__":
    main()
