import { readFile } from "fs/promises";

import { scheduleScore } from "./detr/schedule_slippage";
import { budgetScore } from "./detr/budget_burn";
import { milestoneScore } from "./detr/milestone";
import { blockerScore } from "./detr/blockers";

import { calculateOverallScore } from "./rag/score";
import { classifyRAG } from "./rag/classify";
import { calculateConfidence } from "./rag/confidence";
import { METRIC_WEIGHTS } from "./rag/weight";

import { generateExplanation } from "./ai/gemini";

export async function runAgent() {
  // Read project data
  const file = await readFile("./src/sample.json", "utf-8");
  const project = JSON.parse(file);

  // Deterministic metric calculations
  const schedule = scheduleScore(
    project.plannedDurationDays,
    project.actualDurationDays
  );

  const budget = budgetScore(
    project.plannedBudget,
    project.actualSpend
  );

  const milestone = milestoneScore(
    project.completedMilestones,
    project.totalMilestones
  );

  const blockers = blockerScore(project.blockers);

  // Calculate weighted score
  const score = calculateOverallScore([
    {
      score: schedule,
      weight: 0.30,
    },
    {
      score: budget,
      weight: 0.20,
    },
    {
      score: milestone,
      weight: 0.25,
    },
    {
      score: blockers,
      weight: 0.25,
    },
  ]);

  // Determine RAG
  const rag = classifyRAG(score);

  // Calculate confidence
  const confidence = calculateConfidence([
    schedule,
    budget,
    milestone,
    blockers,
  ]);

  // Object passed to Gemini
  const healthReport = {
    project,
    score,
    rag,
    confidence,
    metrics: {
      schedule,
      budget,
      milestone,
      blockers,
    },
  };

  // Generate executive explanation
  const explanation = await generateExplanation(healthReport);

  // Final output
  return {
    ...healthReport,
    explanation,
  };
}