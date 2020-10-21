#ライブラリのインポート

import random
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

#関数
def stop():
    stop_time = random.randint(1, 10)
    print(f"{stop_time}秒待ちます。")
    time.sleep(stop_time)

#URLを取得
fp = urlopen('https://yorushika.com/')

# HTML取得
html = fp.read()

stop()

fp.close()

decode_html = html.decode("UTF-8")

soup = BeautifulSoup(decode_html, "html.parser")

print(soup.find_all("meta"))