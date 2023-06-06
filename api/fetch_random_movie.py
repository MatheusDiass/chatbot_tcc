import random
import requests


def fetch_random_movie():
    number_random = random.randint(1, 300)

    url = f"https://api.themoviedb.org/3/movie/{number_random}?language=pt"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwN2ExNDY2YTAwOWVhN2Q3ODU3ZDE1ZDFiNjUyMmZmYSIsInN1YiI6IjY0NDU4ZjkyNjUxZmNmMDRkYzlkYmY4YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DDV-Dh_hK4gSXcTng6b2ATQPD7f2TXQ5vU08ka6gRmc"
    }

    response = requests.get(url, headers=headers)

    return response.json()
