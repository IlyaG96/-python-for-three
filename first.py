import requests


def do_request(search_request):
    query_params = {
        'q': search_request,
        'format': 'json'
    }
    url = 'https://api.duckduckgo.com/'
    response = requests.get(
        url=url,
        params=query_params,
    )
    response.raise_for_status()
    answer = response.json()

    return answer
