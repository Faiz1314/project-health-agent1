export type RAGStatus = "GREEN" | "AMBER" | "RED";

export function classifyRAG(score: number): RAGStatus {
  if (score >= 80) return "GREEN";
  if (score >= 60) return "AMBER";
  return "RED";
}