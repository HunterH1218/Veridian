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
    "Your job is to determine if something needs to be searched or not. If it needs to be searched, respond with 'yes'. If it does not need to be, respond with 'no'. Anything that could change, a variable, needs to be seacrhed."
    "input: hi",
    "output: no",
    "input: what is the weather like today?",
    "output: yes",
    "input: what is the weather like tomorrow?",
    "output: yes",
    "input: who is the president of the united states?",
    "output: yes",
    "input: what is the capital of france?",
    "output: yes",
    "input: what is the capital of italy?",
    "output: yes",
    "input: what is the capital of germany?",
    "output: yes",
    "input: what is the newest coding language?",
    "output: yes",
    "input: what is the newest coding language?",
    "output: yes",
    "input: whois the ceo of apple?",
    "output: yes",
    "input: who is the ceo of razer?",
    "output: yes",
    f"input: {prompt}",
  ])
  memory.append(f"input: {prompt}\n")
  memory.append(f"output: {response.text}\n")
  return response.text.strip().lower()
