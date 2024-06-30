import requests
from bs4 import BeautifulSoup

def search_google(query):
    search_url = "https://www.google.com/search"
    params = {'q': query}
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        )
    }
    
    response = requests.get(search_url, params=params, headers=headers)
    response.raise_for_status() 
    soup = BeautifulSoup(response.content, 'html.parser')
    result_texts = []
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        result_texts.append(tag.get_text())
    
    return '\n'.join(result_texts)
