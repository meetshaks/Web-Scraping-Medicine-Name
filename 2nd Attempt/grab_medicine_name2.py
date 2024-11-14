import string
import requests
from bs4 import BeautifulSoup

def scrape_medicine_names(url, filename):
    """Scrapes medicine names from a given URL and saves them to a file."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    with open(filename, "a") as file:
        for item in soup.select(".ddc-list-column-2 a"):
            name = item.get_text(strip=True)
            if name:
                file.write(name + "\n")

# Read URLs from the text file
urls = []
with open("drug_urls_for_test.txt", "r") as f:
    for line in f:
        urls.append(line.strip())  # Remove trailing newline characters

# File to store the medicine names
filename = "medicines.txt"

# Open the file in append mode (to avoid overwriting existing data)
with open(filename, "a") as file:
    pass  # Empty statement to ensure the file is opened even if it's empty

# Iterate over the URLs from the text file and scrape medicine names
for url in urls:
    scrape_medicine_names(url, filename)

print("Medicine names scraped from URLs and saved to medicines.txt")