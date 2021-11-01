import requests
from bs4 import BeautifulSoup

# ターゲットとなるURLを設定する
target_url = "https://laborify.net/"

# requestsを使ってhtmlを取得する
res = requests.get(target_url)

# BeautifulSoupを使って要素を取り出す
soup = BeautifulSoup(res.content, 'html.parser')

# タグを指定する
# title_text = soup.find('title').get_text()

title_text = soup.find('title').get_text()

# 表示する
print(title_text)
