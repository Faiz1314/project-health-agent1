# Project Health Reporting Framework: RAG Status Methodology

## 1. Executive Summary
This framework establishes a standardized, automated methodology for assessing and reporting project health across the Professional Services team. By combining deterministic rule-based scoring with a generative AI layer, the framework eliminates manual reporting, reduces subjectivity, and provides leadership with clear, actionable insights.

---

## 2. Core Health Indicators
The Project Health Reporting Agent evaluates five core dimensions of project delivery:

| Indicator | Metric Definition | Scoring Logic | Weight |
| :--- | :--- | :--- | :--- |
| **Schedule Slippage** | $\frac{\text{Actual Duration} - \text{Planned Duration}}{\text{Planned Duration}} \times 100$ | $\le 0\% \to 100$<br>$\le 5\% \to 90$<br>$\le 10\% \to 75$<br>$\le 15\% \to 50$<br>$\le 20\% \to 25$<br>$> 20\% \to 0$ | **30%** |
| **Budget Burn** | $\frac{\text{Actual Spend}}{\text{Planned Budget}} \times 100$ | $\le 90\% \to 100$ (Underspend/Target)<br>$\le 100\% \to 80$ (On Budget)<br>$\le 110\% \to 50$ (Minor Overspend)<br>$> 110\% \to 20$ (Major Overrun) | **20%** |
| **Milestone Health** | $\frac{\text{Completed Milestones}}{\text{Total Milestones}} \times 100$ | $\ge 90\% \to 100$<br>$\ge 75\% \to 75$<br>$\ge 50\% \to 50$<br>$< 50\% \to 25$ | **25%** |
| **Blockers** | Penalty based on active blocker severity | Base score of 100 points minus:<br>• Low Severity Blocker: -10 points<br>• Medium Severity Blocker: -20 points<br>• High Severity Blocker: -40 points | **25%** |
| **Stakeholder Sentiment** | Qualitative rating (Positive/Neutral/Negative) | *Integrated into the AI reasoning layer to contextualize the status and adjust risk levels.* | *Qualitative Context* |

---

## 3. RAG Status Mapping
The overall Project Health Score is computed as a weighted average of the active indicators:

$$\text{Overall Score} = \frac{\sum (\text{Indicator Score} \times \text{Weight})}{\sum \text{Weights of Present Indicators}}$$

The resulting score determines the RAG status:

*   **🟢 GREEN (Score $\ge$ 80):** The project is healthy, on track, and within acceptable budget/schedule tolerances. Minimal risk detected.
*   **🟡 AMBER (60 $\le$ Score $<$ 80):** The project has emerging risks (e.g., vendor delays, minor budget/schedule slippage). Requires active monitoring and mitigation.
*   **🔴 RED (Score $<$ 60):** The project is in critical status with severe overruns, critical blockers, or significant schedule slippage. Requires immediate executive intervention.

---

## 4. Handling Incomplete or Messy Data
To handle real-world project data variations gracefully, the agent implements the following rules:
1.  **Dynamic Weight Redistribution:** If an indicator is missing (e.g., budget is not tracked yet), its weight is set to 0, and the remaining weights are normalized to sum to 100%.
2.  **Confidence Score:** A confidence metric is calculated as the percentage of available indicators:
    $$\text{Confidence} = \frac{\text{Number of Available Indicators}}{\text{Total Indicators}} \times 100$$
    A lower confidence score alerts leadership that the RAG status is based on incomplete information.

---

## 5. Assumptions
*   **Metric Availability:** While the framework handles missing data, at least one quantitative metric must be present to calculate a RAG status.
*   **Blocker Independence:** Blocker penalties are cumulative up to a maximum penalty of 100 (score of 0).
