import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

books=[]
for i in range(1, 51):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')

    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')

    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p', class_='star-rating').attrs['class'][1]
        price = float(article.find('p', class_='price_color').text[2:])
        books.append([title, price, star])

df = pd.DataFrame(books, columns=['Title', 'Price', 'Star'])

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the file path for the CSV file in the current directory
csv_file_path = os.path.join(current_dir, 'books.csv')

# Save the DataFrame to the CSV file
df.to_csv(csv_file_path, index=False)