import os
import google.generativeai as genai

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, '..', 'data_files', 'training_data.txt')
with open(file_path, 'r') as file:
  training_data = file.read()

memory = []

generation_config = {
  "temperature": 0.85,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 15000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,

)

def generate_response(prompt):
  response = model.generate_content([
    training_data,
    f"{memory}",
    f"input: {prompt}",
    "output: ",
  ])
  memory.append(f"input: {prompt}\n")
  memory.append(f"output: {response.text}\n")
  return response.text
