import json
from istorage import IStorage

class JsonStorage(IStorage):
    def __init__(self, filename):
        self.filename = filename

    def list_movies(self):
        return self._get_movies()

    def add_movie(self, title, year, rating, poster):
        movies = self._get_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        movies = self._get_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        movies = self._get_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)

    def _get_movies(self):
        try:
            with open(self.filename, 'r') as file:
                movies = json.load(file)
        except FileNotFoundError:
            movies = {}
        return movies

    def _save_movies(self, movies):
        with open(self.filename, 'w') as file:
            json.dump(movies, file, indent=4)
