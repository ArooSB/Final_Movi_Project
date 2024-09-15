import requests

class MovieFetcher:
    API_URL = 'http://www.omdbapi.com/'
    API_KEY = 'b489c489'

    def fetch_movie(self, title):
        response = requests.get(self.API_URL, params={"t": title, "apikey": self.API_KEY})
        if response.status_code == 200:
            data = response.json()
            if data['Response'] == 'True':
                return {
                    "title": data['Title'],
                    "year": data['Year'],
                    "rating": float(data['imdbRating']),
                    "poster": data['Poster']
                }
        return None
