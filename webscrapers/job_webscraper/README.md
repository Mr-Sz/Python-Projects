# Job Listings Web Scraper

This Python script scrapes job listings from the TimesJobs website and filters out the ones that require skills that the user is not familiar with.

## Prerequisites

To run this script, you need to have Python 3.x installed on your machine. You also need to install the following Python packages:

- `beautifulsoup4`
- `requests`
- `lxml`

## Usage

1. Install the required dependencies using `pip install`:

2. Clone or download the repository.

3. Open a terminal window and navigate to the repository directory.

4. Run the script using the following command: `main.py`

5. When prompted, enter some skills that you are not familiar with (separated by commas).

6. The script will continuously scrape job listings from the TimesJobs website and filter out the ones that require the unfamiliar skills entered by the user.

7. The job details will be saved to a text file in the `posts` directory, with the filename `jobs_<current_date>.txt`.

8. The script will wait for a specified amount of time (in minutes) before running the job search process again. You can change the wait time by modifying the `wait_time` variable in the script.