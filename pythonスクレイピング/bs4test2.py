import requests
from bs4 import BeautifulSoup

html = requests.get('https://news.yahoo.co.jp')

yahoo = BeautifulSoup(html.content, "html.parser")

for title in yahoo.select("ul.topicsList_main"):
    print(title.getText())