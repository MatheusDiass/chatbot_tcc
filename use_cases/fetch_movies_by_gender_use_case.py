from utils.reset_state import reset_state
from api.fetch_movies_by_gender import fetch_movies_by_gender


def fetch_movies_by_gender_use_case(state, entity_text):
    # Atualiza estado
    reset_state(state)
    state["gender_movie"]["state"] = True

    if entity_text:
        state["gender_movie"]["last_gender_name"] = entity_text

    movies = fetch_movies_by_gender(state["gender_movie"]["last_gender_name"], state["gender_movie"]["page"])["results"]

    # Verifica se não foram encontrados filmes
    if not movies:
        print("Não foram encontrados mais filmes 😢")
        return

    for movie in movies:
        print(f"Nome do filme: {movie['title']}")
        print(f"Nota do filme: {movie['vote_average']}")
        print(f"Data de lançamento: {movie['release_date']}")
        print(f"Sinopse: {movie['overview']}\n")
