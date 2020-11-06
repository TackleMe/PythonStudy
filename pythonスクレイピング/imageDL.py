import requests

url = input("ダウンロードしたい画像のURL:")
file_name = input("保存したいファイル名.jpg:")

response = requests.get(url)
image = response.content

with open(file_name, "wb") as aaa:
    aaa.write(image)