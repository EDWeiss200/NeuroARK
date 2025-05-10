import requests
from bs4 import BeautifulSoup

def get_news():
    url = 'https://www.gazeta.ru/search.shtml?text=%D0%BE%D0%BD%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F&p=main&input=utf8'

    res = requests.get(url,'body')

    soup = BeautifulSoup(res.text, "html.parser")



    all_news = soup.find_all('div', class_='b_ear-textblock m_searchresult',limit=10)

    result = []
    for i in all_news:
        div_title = i.find('div', class_='b_ear-title').find('a').next.replace('\n','').replace('\xa0',' ')
        href = i.find('div', class_='b_ear-title').find('a').get('href')
        url = f'https://www.gazeta.ru/{href}'
        div_info = i.find('time', class_='b_ear-time m_searchresult').next.replace('\n','').replace('\xa0',' ')
        result.append([div_title,url,div_info])

    return result





