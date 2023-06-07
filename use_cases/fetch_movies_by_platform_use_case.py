from utils.reset_state import reset_state
from api.fetch_movies_by_platform import fetch_movies_by_platform


def fetch_movies_by_platform_use_case(state, entity_text):
    # Atualiza estado
    reset_state(state)
    state["platform_movie"]["state"] = True

    if entity_text:
        state["platform_movie"]["last_platform_name"] = entity_text

    movies = fetch_movies_by_platform(state["platform_movie"]["last_platform_name"], state["platform_movie"]["page"])["results"]

    # Verifica se não foram encontrados filmes
    if not movies:
        print("Não foram encontrados mais filmes 😢")
        return

    for movie in movies:
        print(f"Nome do filme: {movie['title']}")
        print(f"Nota do filme: {movie['vote_average']}")
        print(f"Data de lançamento: {movie['release_date']}")
        print(f"Sinopse: {movie['overview']}\n")
