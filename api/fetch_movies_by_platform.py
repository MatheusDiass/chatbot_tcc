import requests


def fetch_movies_by_platform(platform_id, page):
    platform_url = "https://api.themoviedb.org/3/watch/providers/movie?language=PT&watch_region=BR"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwN2ExNDY2YTAwOWVhN2Q3ODU3ZDE1ZDFiNjUyMmZmYSIsInN1YiI6IjY0NDU4ZjkyNjUxZmNmMDRkYzlkYmY4YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DDV-Dh_hK4gSXcTng6b2ATQPD7f2TXQ5vU08ka6gRmc"
    }

    platform_response = requests.get(platform_url, headers=headers)
    platforms = platform_response.json()

    print(platforms)
    movies_url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=PT&page={page}&sort_by=popularity.desc&watch_region=BR&with_watch_providers={platform_id}"
