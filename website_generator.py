
class WebsiteGenerator:
    def generate_website(self, movies, output_file="movies.html"):
        html_content = "<html><head><title>Movie List</title></head><body>"
        html_content += "<h1>My Movies</h1><ul>"

        for title, info in movies.items():
            html_content += f"<li><strong>{title}</strong> ({info['year']}) - Rating: {info['rating']}<br>"
            if info['poster']:
                html_content += f"<img src='{info['poster']}' alt='{title} poster'><br>"
            html_content += "</li>"

        html_content += "</ul></body></html>"

        with open(output_file, 'w') as file:
            file.write(html_content)
