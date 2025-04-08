import http.server
import socketserver
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Configuration
PORT = 8000
URL = "http://books.toscrape.com"
OUTPUT_FILE = "scraped_books.csv"

# Scraper function
def scrape_books():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    books_data = []
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        books_data.append({"Title": title, "Price": price, "Availability": availability})

    # Save data to CSV
    df = pd.DataFrame(books_data)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Data saved to {OUTPUT_FILE}")

# Run scraper before starting server
scrape_books()

# Simple HTTP server
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/scrape":
            self.path = "/" + OUTPUT_FILE  # Serve the CSV file
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Start the server
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
