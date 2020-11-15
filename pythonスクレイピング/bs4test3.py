import os
import requests
from bs4 import BeautifulSoup

URL = 'https://www.sairablog.com'

soup = BeautifulSoup(requests.get(URL).content, 'lxml')

# src リスト
srcs = []

# 画像の拡張子が、.jpg, .png, jpeg いずれの場合も取得
for link in soup.find_all('img'):

    if link.get('src').endswith('.jpg'):
        srcs.append(link.get('src'))

    elif link.get('src').endswith('.png'):
        srcs.append(link.get('src'))

    elif link.get('src').endswith('.jpeg'):
        srcs.append(link.get('src'))

save_path = './images/'

os.makedirs(save_path, exist_ok=True)

for i, image in enumerate(srcs):
    re = requests.get(image)
    i += 100
    with open(save_path + f'{i}.' + image.split('.')[-1], 'wb') as f:
        f.write(re.content)
