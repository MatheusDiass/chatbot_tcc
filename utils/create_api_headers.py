import os


def create_api_headers():
    api_key = os.environ["TMDB_API_TOKEN"]
    token = f"Bearer {api_key}"

    return {
        "accept": "application/json",
        "Authorization": token
    }
