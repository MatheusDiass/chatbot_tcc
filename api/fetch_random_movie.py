import random
import requests

from utils.create_api_headers import create_api_headers


def fetch_random_movie():
    number_random = random.randint(1, 300)

    url = f"https://api.themoviedb.org/3/movie/{number_random}?language=pt"
    headers = create_api_headers()

    response = requests.get(url, headers=headers)

    return response.json()
