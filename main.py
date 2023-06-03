import spacy
import random
from api.fetch_random_movie import fetch_random_movie
from api.fetch_movie_by_name import fetch_movie_by_name

tmdb_api_key = "07a1466a009ea7d7857d15d1b6522ffa"

nlp = spacy.load("./train_scripts/train.spacy")

while True:
    finished = False

    user_input = input("O que gostaria de saber: ")
    doc = nlp(user_input.lower())

    for entity in doc.ents:
        #print(f"Text: {entity.text} - Label: {entity.label_}")

        # Busca filme pelo nome
        if entity.label_ == "MOVIE" and doc.cats["RANDOM_MOVIE"] > 0.5:
            finished = True
            movie = fetch_movie_by_name(entity.text)

            print(f"Nome do filme: {movie['results'][0]['title']}")
            print(f"Nota do filme: {movie['results'][0]['vote_average']}")
            print(f"Data de lançamento: {movie['results'][0]['release_date']}")
            print(f"Sinopse: {movie['results'][0]['overview']}\n")
        pass

    # Busca filme aleatorio
    if doc.cats["RANDOM_MOVIE"] > 0.5 and not finished:
        finished = True
        movie = fetch_random_movie()

        print(f"Nome do filme: {movie['title']}")
        print(f"Nota do filme: {movie['vote_average']}")
        print(f"Data de lançamento: {movie['release_date']}\n")

    print(doc.cats)
