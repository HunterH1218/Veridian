import os
import google.generativeai as genai

# Simple confiuration down below
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
memory = []
generation_config = {
  "temperature": 0.85,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 15200,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,

)

# This function is used to generate a response from the model
def generate_response(prompt):
  response = model.generate_content([
    "Your job is to summerize any text given to you. Do not give any other information than what you know from the text you are given. You are giving the user your summery, but they cannot see what you are summerizing, so be sure to include all the details, but in a consise manner. Just tell them the info you are given, but a summery.",
    f"input: {prompt}",
    "output: ",
  ])
  memory.append(f"input: {prompt}")
  memory.append(f"output: {response.text}")
  return response.text