import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=15):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(f'https://www.google.com/search?q={query}&num={num_results}', headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch search results: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = []
    for g in soup.find_all('div', class_='tF2Cxc'):
        link_tag = g.find('a')
        title_tag = g.find('h3')
        description_tag = g.find('span', class_='aCOpRe')

        link = link_tag['href'] if link_tag else 'No link available'
        title = title_tag.text if title_tag else 'No title available'
        description = description_tag.text if description_tag else 'No description available'
        search_results.append({
            'title': title,
            'link': link,
            'description': description
        })
    return search_results



def fetch_page_text(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text_content = "\n".join([p.get_text() for p in paragraphs])
        return text_content
    except Exception as e:
        return f"Failed to fetch text from {url}: {e}"

def main(query, num_results=10):
    results = google_search(query, num_results)
    full_results = []
    for result in results:
        page_text = fetch_page_text(result['link'])
        full_results.append({
            'title': result['title'],
            'link': result['link'],
            'description': result['description'],
            'page_text': page_text[:20000] # Limited to max text on page
        })
    return full_results