# browser_auto_foods.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome("./driver/chromedriver.exe")

location = input("場所入力：")
favorite_foods = ["カレー", "ラーメン", "チャーハン", "とんかつ", "お好み焼き"]

for i, food in enumerate(favorite_foods):
    if i > 0:
        # 新しいタブ
        chrome.execute_script("window.open('','_blank');")
        chrome.switch_to.window(chrome.window_handles[i])

    # グーグルを開く
    chrome.get("https://www.google.co.jp")

    # 検索ワード入力
    search_box = chrome.find_element_by_name("q")
    search_words = location, food
    search_box.send_keys(" ".join(search_words))

    # 検索実行
    search_box.send_keys(Keys.RETURN)
    print(chrome.title)

# 先頭のタブに戻る
chrome.switch_to.window(chrome.window_handles[0])