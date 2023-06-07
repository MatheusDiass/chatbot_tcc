import requests
from utils.create_api_headers import create_api_headers


def fetch_movies_by_gender(gender_name, page):
    gender_url = "https://api.themoviedb.org/3/genre/movie/list?language=pt-br"
    headers = create_api_headers()

    # Obtem os generos
    genders_response = requests.get(gender_url, headers=headers)
    genders = genders_response.json()["genres"]

    # Obtem o id do genero
    gender_id = [item for item in genders if item['name'].lower() == gender_name][0]["id"]

    movies_url = f"https://api.themoviedb.org/3/discover/movie?certification_country=br&include_adult=false&include_video=false&language=pt&page={page}&sort_by=popularity.desc&vote_average.gte=6&with_genres={gender_id}"

    # Obtem os filmes com base no genero
    movies_response = requests.get(movies_url, headers=headers)
    movies = movies_response.json()

    return movies
