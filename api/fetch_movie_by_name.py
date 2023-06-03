import requests


def fetch_movie_by_name(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=pt-br&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwN2ExNDY2YTAwOWVhN2Q3ODU3ZDE1ZDFiNjUyMmZmYSIsInN1YiI6IjY0NDU4ZjkyNjUxZmNmMDRkYzlkYmY4YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DDV-Dh_hK4gSXcTng6b2ATQPD7f2TXQ5vU08ka6gRmc"
    }

    response = requests.get(url, headers=headers)

    return response.json()
