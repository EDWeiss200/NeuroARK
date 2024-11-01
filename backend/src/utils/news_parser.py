import requests
from bs4 import BeautifulSoup


url = 'https://lenta.ru/search?query=%D0%BE%D0%BD%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F#size=10|sort=2|domain=1|modified,format=yyyy-MM-dd'

res = requests.get(url,'body')

soup = BeautifulSoup(res.text, "html.parser")
print(soup.prettify)


all_news = soup.find('ul', class_='search-results__list').findAll('li')
print(all_news)




