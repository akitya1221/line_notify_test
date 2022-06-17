# モジュールのインポート
import requests 
import time
import pandas
from selenium import webdriver
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# webdriverを最新化して起動
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

# 変数に開きたいサイトのURLを代入
url = 'https://qiita.com/'
# webdriverにURLを渡し、サイトを開く
driver.get(url)
time.sleep(3)
print("ページにアクセスしました")

# HTML要素を取得できるようにするため、requestsにURLを渡す
res = requests.get(url)
#  webdriverで開いているサイトのソースコードを取得し、変数に代入
html = driver.page_source

# res.textでURLをテキスト化、html.parserでHTMLのタグを読み取れるようにし、変数へ代入
soup = BeautifulSoup(res.text, 'html.parser')
# HTMLタグのtitleを取得
title = soup.title
# サイト全体のaタグ class="css-2p454n"に該当するものを変数に代入
# この時要素はlist化される
a_tags = soup.find_all('a', class_='css-2p454n')
# インデックス番号を代入
get_number = 0
# list化されている要素から1つ取り出し、変数に代入する
a_str = [x for x in a_tags[get_number].stripped_strings]
# listの状態から文字列に変換、
text = ''.join(a_str)
# linkのURLを取得
link = a_tags[get_number].get('href')

# LINE Notifyのアクセストークンを設定
TOKEN = 'PberLZgAZMUYcC52HC3HZFMV2GJXgtjpXPKcguZlfX5'
# POST用のURLを設定
api_url = 'https://notify-api.line.me/api/notify'
# LINE Notifyから通知される内容を変数に代入
send_message = '最近人気の記事No.1' + '：' + text + ' ' + 'URL：' + link

# ヘッダに使用する変数を設定
TOKEN_dic = {'Authorization':'Bearer' + ' ' + TOKEN}
# 通知するメッセージを設定
send_dic = {'message':send_message}

# APIに上記で設定した内容を送信
requests.post(api_url, headers = TOKEN_dic, data = send_dic)