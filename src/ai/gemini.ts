import { GoogleGenAI } from "@google/genai";
import { SYSTEM_PROMPT } from "./system_prompt";

const ai = new GoogleGenAI({
    vertexai:true,
    project:"project-98fab1fa-ee54-4a35-b60",
    location:"asia-south1"
});

export async function generateExplanation(data: any) {
 const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: [
      {
        role: "user",
        parts: [
          {
            text: `${SYSTEM_PROMPT}

Project Data:
${JSON.stringify(data, null, 2)}
`,
          },
        ],
      },
    ],
  });

    return response.text;
}