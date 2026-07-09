export type BlockerSeverity = "low" | "medium" | "high";

export interface Blocker {
  title: string;
  severity: BlockerSeverity;
}

export function blockerScore(blockers?: Blocker[]): number | null {
  if (!blockers) {
    return null;
  }

  let penalty = 0;

  for (const blocker of blockers) {
    switch (blocker.severity) {
      case "low":
        penalty += 10;
        break;

      case "medium":
        penalty += 20;
        break;

      case "high":
        penalty += 40;
        break;
    }
  }

  return Math.max(0, 100 - penalty);
}