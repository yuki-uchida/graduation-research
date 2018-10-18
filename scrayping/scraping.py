# coding: UTF-8
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

def scraping(hotel_num):
  # アクセスするURL
  url = "https://review.travel.rakuten.co.jp/hotel/voice/{}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_static=1&f_sort=0&f_point=5".format(hotel_num)

  # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
  html = urllib.request.urlopen(url)

  # htmlをBeautifulSoupで扱う
  soup = BeautifulSoup(html, "html.parser")

  # タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
  title_tag = soup.find_all(class_="commentReputation")
  print(len(title_tag))
  comments = []
  for title in title_tag:
    comment = title.find(class_="commentSentence")
    comment = comment.text
    comments.append(comment)
  return comments

def scraping2(hotel_num):
  # アクセスするURL
  url = "https://review.travel.rakuten.co.jp/hotel/voice/{}/?f_time=&f_keyword=&f_age=0&f_sex=0&f_mem1=0&f_mem2=0&f_mem3=0&f_mem4=0&f_mem5=0&f_teikei=&f_static=1&f_sort=0&f_point=5".format(hotel_num)

  # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
  html = urllib.request.urlopen(url)

  # htmlをBeautifulSoupで扱う
  soup = BeautifulSoup(html, "html.parser")

  # タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
  title_tag = soup.find_all(class_="commentReputation")
  print(len(title_tag))
  comments = []
  for title in title_tag:
    comment = title.find(class_="commentSentence")
    comment = comment.text
    comments.append(comment)
  return comments



hotel_list = [136041,5547,129475,19455,27896,7489,16654]
all_comments = []
for hotel_num in hotel_list:
  #all_comments.extend(scraping(hotel_num))
  all_comments.extend(scraping2(hotel_num))

print(all_comments)

# df = pd.DataFrame(all_comments)
# df.to_csv('comment.csv',encoding='cp932')
