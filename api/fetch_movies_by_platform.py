import requests
from utils.create_api_headers import create_api_headers


def fetch_movies_by_platform(platform_name, page):
    platform_url = "https://api.themoviedb.org/3/watch/providers/movie?language=PT&watch_region=BR"
    headers = create_api_headers()

    # Obtem os plataformas
    platform_response = requests.get(platform_url, headers=headers)
    platforms = platform_response.json()["results"]

    # Obtem o id da plataforma
    platform_id = [item for item in platforms if item['provider_name'].lower() == platform_name][0]["provider_id"]

    movies_url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=PT&page={page}&sort_by=popularity.desc&watch_region=BR&with_watch_providers={platform_id}"

    # Obtem os filmes com base na plataforma
    movies_response = requests.get(movies_url, headers=headers)
    movies = movies_response.json()

    return movies