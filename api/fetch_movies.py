import requests

from utils.create_api_headers import create_api_headers


def fetch_movies(page):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=PT&page={page}&sort_by=vote_count.desc&watch_region=BR"
    headers = create_api_headers()

    response = requests.get(url, headers=headers)

    return response.json()
