import requests

from utils.create_api_headers import create_api_headers


def fetch_movie_by_name(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=pt-br&page=1"
    headers = create_api_headers()

    response = requests.get(url, headers=headers)

    return response.json()
