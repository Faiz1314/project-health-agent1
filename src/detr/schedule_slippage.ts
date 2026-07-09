export function scheduleScore(plannedDurationDays?: number,actualDurationDays?: number): number | null {
  if (
    plannedDurationDays === undefined ||
    actualDurationDays === undefined ||
    plannedDurationDays <= 0
  ) {
    return null;
  }

  const slippage =
    ((actualDurationDays - plannedDurationDays) / plannedDurationDays) * 100;

  if (slippage <= 0) return 100;
  if (slippage <= 5) return 90;
  if (slippage <= 10) return 75;
  if (slippage <= 15) return 50;
  if (slippage <= 20) return 25;

  return 0;
}