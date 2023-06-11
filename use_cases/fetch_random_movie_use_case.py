from utils.reset_state import reset_state
from api.fetch_random_movie import fetch_random_movie


def fetch_random_movie_use_case(state):
    # Atualiza estado
    reset_state(state)
    state["random_movie"] = True

    movie = fetch_random_movie()

    print(f"Nome do filme: {movie['title']}")
    print(f"Nota do filme: {movie['vote_average']}")
    print(f"Data de lançamento: {movie['release_date']}\n")
