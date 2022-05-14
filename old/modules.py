import requests
from pprint import pprint


def fetch_duckduckgo_data(search_text):
    query_params = {
        'q': search_text,
        'format': 'json'
    }
    response = requests.get('https://api.duckduckgo.com/', params=query_params)
    response.raise_for_status()

    return response.json()


if __name__ == '__main__':
    pprint(fetch_duckduckgo_data('google'))














