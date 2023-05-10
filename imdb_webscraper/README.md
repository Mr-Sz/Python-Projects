# IMDb Top 250 Movies Scraper

This Python script scrapes the top 250 movies from IMDb and saves the data to an Excel spreadsheet.

## Installation

To run this script, you'll need to have Python 3 installed on your machine, as well as the following packages:

- `openpyxl`
- `requests`
- `beautifulsoup4`

You can install these packages using `pip` by running the following command in your terminal: `pip install openpyxl requests beautifulsoup4`


## Usage

1. Install the required dependencies using `pip install`:

2. Clone or download the repository.

3. Open a terminal window and navigate to the repository directory.

4. Run the script using the following command: `main.py`

5. When prompted, enter some skills that you are not familiar with (separated by commas).

6. The script will scrape top 250 movies from the IMDB website and save the data in a Excel file.

7. The Excel file will be saved to a text file in the `files` directory, with the filename `imdb_top_250_movies_<today's date in mm_dd_yy format>.xlsx`.