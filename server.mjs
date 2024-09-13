import express from "express";
import { Ollama } from "@langchain/ollama";
import { PromptTemplate } from "@langchain/core/prompts";


const app = express();

const llm = new Ollama({
    baseUrl: "http://localhost:11434",
    model: "yorkgpt/yorkgpt",
    temperature: 0,
    maxRetries: 2,
});
  
async function run() {
  
    const prompt = PromptTemplate.fromTemplate(
      "Answer this question to the best of your ability: {input}\n"
    );
  
    const chain = prompt.pipe(llm);
    const response = await chain.invoke({
      input: "What is York College?",
    });
  
    console.log(response);
}
  
run().catch(console.error);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});