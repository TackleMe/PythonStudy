from bs4 import BeautifulSoup

html = "<body><h1>python入門</h1><p>pythonの基礎について学習します</p></body>"
soup = BeautifulSoup(html, "html.parser")

print(soup.body)
