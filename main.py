from models import text_model as tm
from models import large_action_model as lam
from models import search_query_generator as sqg
from search import google_search as sg
from models import summerize_model as sm


while True:
  prompt = input("Prompt: ")
  query = lam.generate_response(prompt)
  if query == "yes":
    print("Seaching...")
    search = sqg.generate_response(prompt)
    results = sg.search_google(search)
    complete_result = sm.generate_response(results)
    print(complete_result)
  elif query == "no":
    print(tm.generate_response(prompt))
  else: 
    print("I'm sorry, but something has gone wrong. Please try again.")
    print("Invalid response from Large Action Model.")
    print(f"LAM reply: {query}")