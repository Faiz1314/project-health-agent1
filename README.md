# Project Health Reporting Agent (Python)

A Python-based AI agent that evaluates project health using deterministic metrics and generates human-readable executive summaries via the Gemini API.

## Project Structure

```text
Health-agent/
├── src/
│   ├── detr/             # Deterministic metric scoring
│   │   ├── blockers.py          # Penalty calculations based on blocker severity
│   │   ├── budget_burn.py       # Actual vs planned budget burn calculation
│   │   ├── milestone.py         # Milestone completion calculation
│   │   └── schedule_slippage.py # Schedule slippage percentage and scoring
│   ├── rag/              # Red / Amber / Green (RAG) classification & weights
│   │   ├── classify.py          # Map final score to green, amber, or red
│   │   ├── confidence.py        # Assessment confidence based on available data
│   │   ├── score.py             # Weighted overall score calculation
│   │   └── weight.py            # Metric weights definitions
│   ├── ai/               # AI explanation layer
│   │   ├── gemini.py            # Gemini integration via google-genai
│   │   └── system_prompt.py     # Persona constraints for executive reporting
│   ├── agent.py          # Main orchestrator
│   └── sample.json       # Input configuration file
├── main.py               # CLI Entry point
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignored files and directories
```

## How It Works

1. **Deterministic Scoring**:
   The agent calculates scores (0-100) for schedule, budget, milestones, and blockers using specific business rules defined in `src/detr/`.
2. **Weighted Aggregation**:
   It calculates an overall score by applying specific weights:
   * Schedule: 30%
   * Budget: 20%
   * Milestone: 25%
   * Blockers: 25%
3. **RAG Classification**:
   * **GREEN**: Score $\ge$ 80
   * **AMBER**: 60 $\le$ Score < 80
   * **RED**: Score < 60
4. **AI Summary Generation**:
   The calculated metrics are structured and sent to Gemini (`gemini-2.5-flash`) using a professional Project Delivery Manager prompt. The model explains the RAG status, identifies risks, and suggests recommended actions.

## Getting Started

### Prerequisites

* Python 3.10+
* A Gemini API key. Get one from [Google AI Studio](https://aistudio.google.com/).

### Quick Start

We provide a convenient shell script `run.sh` that automatically sets up a Python virtual environment, installs dependencies, and runs the agent.

1. Clone or navigate to the project directory:
   ```bash
   cd Health-agent
   ```

2. Run with your API key:
   ```bash
   GEMINI_API_KEY="your-api-key-here" ./run.sh
   ```

### Manual Run

If you prefer to run manually without virtual environments:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Export your Gemini API key:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## Configuration

You can customize the input project metrics in `src/sample.json`:

```json
{
  "plannedDurationDays": 100,
  "actualDurationDays": 112,
  "plannedBudget": 100000,
  "actualSpend": 85000,
  "completedMilestones": 8,
  "totalMilestones": 10,
  "blockers": [
    {
      "title": "Vendor Delay",
      "severity": "medium"
    }
  ]
}
```
