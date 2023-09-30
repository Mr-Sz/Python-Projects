import os
from datetime import date

import openpyxl
import requests
from bs4 import BeautifulSoup


def create_spreadsheet():
    """
    Create a new Excel spreadsheet and return the spreadsheet and the active sheet.
    """
    spreadsheet = openpyxl.Workbook()  # create a new spreadsheet
    sheet = spreadsheet.active  # get the active sheet
    sheet.title = 'imdb_top_250_movies'  # change the title of the sheet
    sheet.append(['Rank', 'Title', 'Release Year', 'IMDB Rating'])  # add the column headers
    return spreadsheet, sheet


def save_spreadsheet(spreadsheet):
    """
    Save the spreadsheet to a file in a folder called 'files' in the current directory.
    """
    folder_name = 'files'
    file_name = f'imdb_top_250_movies_{date.today().strftime("%m_%d_%y")}.xlsx'
    
    # create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    
    file_path = os.path.join(folder_name, file_name)
    
    spreadsheet.save(file_path)  # save the spreadsheet
    print(f'Saved spreadsheet to {file_path}')


def scrape_imdb(sheet):
    """
    Scrape the top 250 movies from IMDb and write the data to the provided sheet object.
    """
    try:
        source = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
        source.raise_for_status()  # check if the request was successful
        soup = BeautifulSoup(source.text, 'html.parser')
        movies = soup.find('tbody', class_='lister-list').find_all('tr')
        for movie in movies:
            rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
            title = movie.find('td', class_='titleColumn').a.text
            year = movie.find('td', class_='titleColumn').span.text.strip('()')
            rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
            sheet.append([rank, title, year, rating])
    except Exception as e:
        print(e)  # print the error message if there is one


if __name__ == '__main__':
    excel_file, sheet = create_spreadsheet()
    scrape_imdb(sheet)
    save_spreadsheet(excel_file)

