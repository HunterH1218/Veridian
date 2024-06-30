import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

with open(r"training_data.txt") as training_data:
    full = ("\n".join(training_data.readlines()))

memory = []

generation_config = {
  "temperature": 0.85,
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
    full,
    f"{memory}",
    f"input: {prompt}",
    "output: ",
  ])
  memory.append(f"input: {prompt}\n")
  memory.append(f"output: {response.text}\n")
  return response.text
