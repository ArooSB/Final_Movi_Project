from json_storage import JsonStorage
from csv_storage import CsvStorage
from movie_fetcher import MovieFetcher
from website_generator import WebsiteGenerator

def main():
    # Select storage type
    storage_type = input("Select storage type (json/csv): ").lower()
    if storage_type == 'json':
        storage = JsonStorage("movies.json")
    elif storage_type == 'csv':
        storage = CsvStorage("movies.csv")
    else:
        print("Unsupported storage type")
        return

    fetcher = MovieFetcher()
    generator = WebsiteGenerator()

    while True:
        print("\n1. Add movie\n2. List movies\n3. Update movie\n4. Delete movie\n5. Generate website\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter movie title: ")
            movie = fetcher.fetch_movie(title)
            if movie:
                storage.add_movie(movie['title'], movie['year'], movie['rating'], movie['poster'])
                print(f"Added {movie['title']} to the collection.")
            else:
                print("Movie not found.")
        elif choice == '2':
            movies = storage.list_movies()
            for title, info in movies.items():
                print(f"{title} ({info['year']}) - Rating: {info['rating']}")
        elif choice == '3':
            title = input("Enter movie title: ")
            rating = float(input("Enter new rating: "))
            storage.update_movie(title, rating)
            print(f"Updated {title}.")
        elif choice == '4':
            title = input("Enter movie title to delete: ")
            storage.delete_movie(title)
            print(f"Deleted {title}.")
        elif choice == '5':
            movies = storage.list_movies()
            generator.generate_website(movies)
            print("Website generated.")
        elif choice == '6':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
