# Multi-Page Web Scraper

This Python script is a multi-page web scraper that retrieves book information from a website and saves it in a CSV file.

## Prerequisites

To run this script, you need to have the following installed:

- Python (version 3.x)
- Requests library (can be installed via `pip install requests`)
- BeautifulSoup library (can be installed via `pip install beautifulsoup4`)
- Pandas library (can be installed via `pip install pandas`)

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script using the following command: `python main.py`

4. The script will scrape book information from multiple pages of a website and save it in a file named `books.csv` located in the same directory as the `main.py` file.

## Customization

- To change the website URL or the number of pages to scrape, you can modify the `url` and the range of the `for` loop in the code.

- If you want to save the `books.csv` file in a different location, you can modify the file path in the code where it is being saved.
