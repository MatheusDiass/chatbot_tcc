import requests
from utils.create_api_headers import create_api_headers


def fetch_movies_by_platform(platform_id, page):
    platform_url = "https://api.themoviedb.org/3/watch/providers/movie?language=PT&watch_region=BR"
    headers = create_api_headers()

    platform_response = requests.get(platform_url, headers=headers)
    platforms = platform_response.json()

    print(platforms)
    movies_url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=PT&page={page}&sort_by=popularity.desc&watch_region=BR&with_watch_providers={platform_id}"
