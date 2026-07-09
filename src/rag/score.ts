import { METRIC_WEIGHTS } from "./weight";

export interface WeightedMetric {
  score: number | null;
  weight: number;
}

export function calculateOverallScore(
  metrics: WeightedMetric[]
): number {
  let weightedSum = 0;
  let totalWeight = 0;

  for (const metric of metrics) {
    if (metric.score !== null) {
      weightedSum += metric.score * metric.weight;
      totalWeight += metric.weight;
    }
  }

  if (totalWeight === 0) {
    return 0;
  }

  return weightedSum / totalWeight;
}