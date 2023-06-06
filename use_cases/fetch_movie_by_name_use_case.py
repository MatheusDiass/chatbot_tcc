from utils.reset_state import reset_state
from api.fetch_movie_by_name import fetch_movie_by_name


def fetch_movie_by_name_use_case(state):
    # Atualiza estado
    reset_state(state)
    state["movie_name"] = True

    movie = fetch_movie_by_name(entity.text)["results"][0]

    # Verifica o filme não foi encontrado
    if not movie:
        print("O filme não foi encontrado 😢")
        return

    print(f"Nome do filme: {movie['title']}")
    print(f"Nota do filme: {movie['vote_average']}")
    print(f"Data de lançamento: {movie['release_date']}")
    print(f"Sinopse: {movie['overview']}\n")
