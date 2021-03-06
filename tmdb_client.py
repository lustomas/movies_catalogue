import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYTM0ZWJmMWE4MzgwZGIyZTFjMjc5YzQyYTNiNGM2YSIsInN1YiI6IjYyOWIxNWIxNTUwN2U5MTJjNzkzMGY2ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VRBKTvOYSwiA_Jplf5Md7RHI00LzCUvjR0bsUhn4DEM"

def header():
    return {
        "Authorization": f"Bearer {API_TOKEN}"
    }

def get_popular_movies():

    response = requests.get("https://api.themoviedb.org/3/movie/popular", headers=header())
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

def get_movies(list_type, how_many):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{list_type}", headers=header())
    response.raise_for_status()
    results = response.json()["results"]
    return random.sample(results, k=how_many)

def get_movies_list(list_type):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{list_type}", headers=header())
    response.raise_for_status()
    return response.json()

def get_single_movie(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", headers = header())
    return response.json()

def get_single_movie_cast(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits", headers=header())
    return response.json()["cast"]

def get_movie_images(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/images", headers=header())
    return response.json()


