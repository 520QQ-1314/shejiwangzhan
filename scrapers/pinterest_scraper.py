import requests
from bs4 import BeautifulSoup

def scrape_pinterest(query):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    url = f'https://www.pinterest.com/search/pins/?q={query}'
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    images = []
    for img_tag in soup.find_all('img'):
        src = img_tag.get('src')
        if src:
            images.append({'url': src, 'source': 'Pinterest'})
        if len(images) >= 20:  # 限制数量
            break
    return images
