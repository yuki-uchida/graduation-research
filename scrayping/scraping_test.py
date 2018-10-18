# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://www.tripadvisor.jp/Hotel_Review-g293974-d294607-Reviews-InterContinental_Istanbul-Istanbul.html#REVIEWS"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.find_all(class_="prw_rup prw_reviews_text_summary_hsx")
comments = []
for title in title_tag:
  comment = title.find(class_="partial_entry")
  comment = comment.text
  comments.append(comment)
# soup2 = BeautifulSoup(title_tag, "html.parser")
# title = soup2.find_all(class_="commentSentence")
# print(title)
# title_tag = title_tag.find_all(class_="commentsentence")
# for title in title_tag:
#   print("\n")
#   print(title)
for comment in comments:
  print(comment)


# import pandas as pd

# df = pd.DataFrame(comments)
# df.to_csv('trip_english_review.csv',encoding='UTF-8')
