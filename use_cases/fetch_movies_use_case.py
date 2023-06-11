from utils.reset_state import reset_state
from api.fetch_movies import fetch_movies


def fetch_movies_use_case(state):
    # Atualiza estado
    reset_state(state)
    state["all_movies"]["state"] = True

    movies = fetch_movies(state["all_movies"]["page"])["results"]

    if not movies:
        print("Não foram encontrados mais filmes 😢")
        return

    for movie in movies:
        print(f"Nome do filme: {movie['title']}")
        print(f"Nota do filme: {movie['vote_average']}")
        print(f"Data de lançamento: {movie['release_date']}")
        print(f"Sinopse: {movie['overview']}\n")
