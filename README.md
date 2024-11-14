
# Medicine Name Scraper and Link Storage Project

This project contains Python scripts for managing and processing information related to medicine names, storing links with quotes, and generating URLs for scraping. It includes various utilities for storing links and extracting relevant medical data from online sources.

## Project Files

1. **store_link_with_quotation.py**  
   - Stores links along with specific quotations or tags, enabling organized link storage with associated notes.

2. **store_link.py**  
   - Generates URLs based on a pattern from Drugs.com and stores them in `drug_urls.txt`. This file can be used as input by other scripts to scrape medicine names.

3. **grab_medicine_name1.py**  
   - Identifies and extracts medicine names from given text. Useful for filtering medicine names from large datasets.

4. **grab_medicine_name2.py**  
   - Reads URLs from `drug_urls_for_test.txt` and scrapes medicine names, saving them in `medicines.txt`.

5. **grab_medicine_name2_with_progressbar.py**  
   - Similar to `grab_medicine_name2.py` but includes a progress bar using `tqdm` to track scraping progress.

## Requirements

- Python 3.x
- Required packages:
  - `requests` for HTTP requests
  - `BeautifulSoup` from the `bs4` package for parsing HTML
  - `tqdm` for displaying the progress bar (only for `grab_medicine_name2_with_progressbar.py`)

To install the required packages, run:

```bash
pip install requests beautifulsoup4 tqdm
```

## Usage

1. **Generate URLs**:
   Run `store_link.py` to generate URLs and save them in `drug_urls.txt`.

   ```bash
   python store_link.py
   ```

2. **Scrape Medicine Names**:
   Use either `grab_medicine_name2_with_progressbar.py` or `grab_medicine_name2.py` to scrape medicine names.

   - **With Progress Bar**:
     ```bash
     python grab_medicine_name2_with_progressbar.py
     ```
   - **Without Progress Bar**:
     ```bash
     python grab_medicine_name2.py
     ```
   Both scripts will read URLs from `drug_urls_for_test.txt` and save the scraped names to `medicines.txt`.

3. **Store Links with Quotations**:
   Run `store_link_with_quotation.py` to save links with associated quotes.

   ```bash
   python store_link_with_quotation.py
   ```

## Notes

- Ensure `drug_urls_for_test.txt` contains valid URLs before running the scraping scripts.
- Scraped medicine names are appended to `medicines.txt` with each run.
- **CSS Class for Medicine Names**: All pages on Drugs.com (e.g., [https://www.drugs.com/alpha/a.html](https://www.drugs.com/alpha/a.html)) were inspected, and it was found that medicine names are stored in the `.ddc-list-column-2` CSS class. This information helps the scripts locate and extract the correct elements.

## License

This project is open-source and available under the MIT License.

---

*Feel free to contribute or open issues for further improvements.*
