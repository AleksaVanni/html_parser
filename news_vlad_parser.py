import requests
from bs4 import BeautifulSoup
import pprint
import os

DOMAIN = 'https://vladday.ru/'
url = f'{DOMAIN}news/'


response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')


result = {}

news_art = soup.find_all('article', class_='mb-4')

for news in news_art:
    text = news.text
    # print(text)

    result_title = []
    # заголовки новостей
    news_titles = soup.find_all('h5')
    for title in news_titles:
        print(title.text)
        result_title.append(title.text)


    result[text] = result_title
    # with open('news.csv', mode='w', encoding='utf8') as f:
    #     f.write(result[text])
# pprint.pprint(result)

