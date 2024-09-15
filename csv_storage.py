import csv
from istorage import IStorage

class CsvStorage(IStorage):
    def __init__(self, filename):
        self.filename = filename

    def list_movies(self):
        movies = {}
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['title']
                    movies[title] = {"year": int(row['year']), "rating": float(row['rating']), "poster": row['poster']}
        except FileNotFoundError:
            pass
        return movies

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)

    def _save_movies(self, movies):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'year', 'rating', 'poster'])
            writer.writeheader()
            for title, info in movies.items():
                row = {'title': title, 'year': info['year'], 'rating': info['rating'], 'poster': info['poster']}
                writer.writerow(row)
