import requests
import random
API_TOKEN="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2OTc5OWVhYWM3ZGZkMjg5MDExNDk4YWIxYTJiNmZkYyIsInN1YiI6IjYyOTIyYzFhMDllZDhmMTI1NDZkZDlhYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Yz7C5IwLKdo-wr6zxC5cdLK6MPpgY3uPonQn-qe7QGA"
headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def random_get_backdrop(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    response = requests.get(endpoint, headers=headers)
    backs = response.json()["backdrops"]
    chosen = random.choice(backs)
    return chosen

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
        
def get_movies(how_many,list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint=f"https://api.themoviedb.org/3/movie/{movie_id}"
    response=requests.get(endpoint, headers=headers)
    return response.json()
def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]
    
def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    response = requests.get(endpoint, headers=headers)
    return response.json()