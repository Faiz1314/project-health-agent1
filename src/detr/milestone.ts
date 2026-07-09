export function milestoneScore(completed?: number,total?: number): number | null {
  if (
    completed === undefined ||
    total === undefined ||
    total <= 0
  ) {
    return null;
  }

  const completion = (completed / total) * 100;

  if (completion >= 90) return 100;
  if (completion >= 75) return 75;
  if (completion >= 50) return 50;

  return 25;
}