import spacy
from dotenv.main import load_dotenv
import os

from use_cases.fetch_movie_by_name_use_case import fetch_movie_by_name_use_case
from use_cases.fetch_movies_by_gender_use_case import fetch_movies_by_gender_use_case
from use_cases.fetch_random_movie_use_case import fetch_random_movie_use_case

from api.fetch_movies_by_platform import fetch_movies_by_platform

from utils.reset_state import reset_state

# Carrega as variáveis de ambiente (env file)
load_dotenv()

nlp = spacy.load("./train_scripts/train.spacy")

# Paginas da busca por funcionalidade
movies_gender_pages = 1
movies_platform_pages = 1

# Controle de estado para saber qual a funcionalidade da ultima execução
state = {
    "movie_name": False,
    "gender_movie": {
        "state": False,
        "last_gender_name": ""
    },
    "random_movie": False
}

while True:
    finished = False

    user_input = input("O que gostaria de saber: ")
    doc = nlp(user_input.lower())
    print(doc.ents)
    # Faz um loop para verificar se alguma entidade como nome de filme e de genero foi fornecido na frase
    for entity in doc.ents:
        print(entity.label_)
        #print(f"Text: {entity.text} - Label: {entity.label_}")

        # Busca filme pelo nome
        if entity.label_ == "MOVIE" and doc.cats["RANDOM_MOVIE"] > 0.5:
            fetch_movie_by_name_use_case(state)
            finished = True

        # Busca lista de filmes pelo genero
        if entity.label_ == "GENDER" and doc.cats["GENDER_MOVIE"] > 0.5:
            print("INICIO")
            fetch_movies_by_gender_use_case(state, entity.text, movies_gender_pages)
            finished = True

        if entity.label_ == "PLATFORM" and doc.cats["PLATFORM_MOVIE"] > 0.5:
            fetch_movies_by_platform(entity.text, movies_platform_pages)
            finished = True

        pass

    if doc.cats["GENDER_MOVIE"] > 0.5 and not len(doc.ents) and state["gender_movie"]["state"]:
        print("CONTINUAÇÃO")
        movies_gender_pages += 1
        fetch_movies_by_gender_use_case(state, None, movies_gender_pages)
        finished = True

    # Busca filme aleatorio
    if doc.cats["RANDOM_MOVIE"] > 0.5 and not finished:
        fetch_random_movie_use_case(state)
        finished = True

    if not finished:
        reset_state(state)
        print("Desculpe, não entendi o que você quer saber 🤔")

    print(doc.cats)
