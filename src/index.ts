import { readFile } from "fs/promises";
import { runAgent } from "./agent";

async function main() {
  try {
    // Read the project plan
    const file = await readFile(
      new URL("./sample.json", import.meta.url),
      "utf-8"
    );

    const project = JSON.parse(file);

    // Run the agent
    const report = await runAgent(project);

    console.log("\n========== PROJECT HEALTH REPORT ==========\n");

    console.log(`Project     : ${report.project.name ?? "Unnamed Project"}`);
    console.log(`RAG Status  : ${report.rag}`);
    console.log(`Score       : ${report.score.toFixed(2)}`);
    console.log(`Confidence  : ${report.confidence}%`);

    console.log("\nMetric Scores");
    console.table(report.metrics);

    console.log("\nExecutive Summary");
    console.log(report.explanation);

    console.log("\n===========================================\n");
  } catch (err) {
    console.error("Failed to execute Project Health Agent");
    console.error(err);
  }
}

main();