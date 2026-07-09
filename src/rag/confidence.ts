export function calculateConfidence(
  scores: (number | null)[]
): number {
  const available = scores.filter(
    (score) => score !== null
  ).length;

  return Math.round((available / scores.length) * 100);
}