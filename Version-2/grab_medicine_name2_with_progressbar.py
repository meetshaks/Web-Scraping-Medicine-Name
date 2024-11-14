import string
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def scrape_medicine_names(url, filename):
    """Scrapes medicine names from a given URL and saves them to a file."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    with open(filename, "a") as file:
        for item in soup.select(".ddc-list-column-2 a"):
            name = item.get_text(strip=True)
            if name:
                file.write(name + "\n")
    # ... (same as before)

# Read URLs from the text file
# Read URLs from the text file
urls = []
with open("drug_urls_for_test.txt", "r") as f:
    for line in f:
        urls.append(line.strip())  # Remove trailing newline characters

# File to store the medicine names
filename = "medicines.txt"


# Open the file in append mode
with open(filename, "a") as file:
    pass

# Iterate over the URLs and scrape medicine names with progress bar
with tqdm(total=len(urls), desc="Scraping medicine names") as progress_bar:
    for url in urls:
        scrape_medicine_names(url, filename)
        progress_bar.update(1)