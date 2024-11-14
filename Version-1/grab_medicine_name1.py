import requests
from bs4 import BeautifulSoup
from tqdm import tqdm  # Import tqdm for progress bar

def scrape_medicine_names(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    with open(filename, "a") as file:
        for item in soup.select(".ddc-list-column-2 a"):
            name = item.get_text(strip=True)
            if name:
                file.write(name + "\n")

# List of URLs to scrape
urls = [
    "https://www.drugs.com/alpha/a.html",
    # ... (add the rest of the URLs here)
]

# File to store the medicine names
filename = "medicines.txt"

# Open the file in write mode and clear its contents
with open(filename, "w") as file:
    file.write("")

# Iterate over the URLs and scrape medicine names
total_urls = len(urls)
with tqdm(total=total_urls, desc="Scraping medicine names") as progress_bar:
    for url in urls:
        scrape_medicine_names(url, filename)
        progress_bar.update(1)  # Update progress bar for each URL

print("Medicine names saved to medicines.txt")