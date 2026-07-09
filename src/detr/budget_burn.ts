export function budgetScore(
  plannedBudget?: number,
  actualSpend?: number
): number | null {
  if (
    plannedBudget === undefined ||
    actualSpend === undefined ||
    plannedBudget <= 0
  ) {
    return null;
  }

  const burn = (actualSpend / plannedBudget) * 100;

  if (burn <= 90) return 100;
  if (burn <= 100) return 80;
  if (burn <= 110) return 50;

  return 20;
}