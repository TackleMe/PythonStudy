import requests
r = requests.get("https://news.yahoo.co.jp/")
print(r.text)
