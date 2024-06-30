import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])



memory = []

generation_config = {
  "temperature": 0.80,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 10000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,

)

def generate_response(prompt):
  response = model.generate_content([
    "Your job is to create a search query based on what the user said.",
    "input: who is the president?",
    "output: Who is the current president?",
    "input: what is the capital of france?",
    "output: What is the capital of France?"
    "input: who made the first iphone?",
    "output: Who made the first iPhone?",
    f"input: {prompt}",
    "output: ",
  ])
  memory.append(f"input: {prompt}")
  memory.append(f"output: {response.text}")

  return response.text
