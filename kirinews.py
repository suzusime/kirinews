import feedparser
import time
import datetime
from functools import partial
import os
import shlex


urls = ["http://www3.nhk.or.jp/rss/news/cat3.xml",
        "http://www3.nhk.or.jp/rss/news/cat0.xml"]
rss = []
for url in urls:
    rss += feedparser.parse(url)["entries"]

#for item in rss["entries"]:
#    print(item.keys())

# 更新日が1日以内のものだけを選び出す
news = [ entry for entry in rss
        if datetime.datetime.now() - datetime.datetime(*(entry["published_parsed"])[:6]) < datetime.timedelta(days=1)]

# 重複は除く
news_unique = []
for entry in news:
    if entry["link"] not in map(lambda x:x["link"], news_unique):
        news_unique.append(entry)

yomiage=""
for entry in news_unique:
    print("## "+entry["title"])
    print(entry["description"])
    print()
    yomiage+="次のニュースです。■"+entry["title"]+"。■"+entry["description"]+"■■■■■"
yomiage+="以上でニュースを終わります。"
os.system('tk '+"\""+shlex.quote(yomiage)+"\"")
