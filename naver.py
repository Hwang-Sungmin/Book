import requests
from bs4 import BeautifulSoup

keyword = input('검색어를 입력 : ') 
print(keyword)
url = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord="+keyword+"&orderClick=LAG"
#https://search.kyobobook.co.kr/web/search?vPstrKeyWord=%EC%88%A8&vPstrTab=PRODUCT&searchPcondition=1&currentPage=1&orderClick=LAG#container
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

#title = soup.find_all(class_='title')
#title = soup.find_all(class_="list_search_result")
title = soup.select('.detail > .title')
author = soup.select('.detail > .author > a')

#title = soup.find_all(class_="detail")
#title = soup.find(class_="list_search_result")
#title1 = soup.find_all(class_="title")
print(len(title))
print(len(author))

for i in range(len(title)):
    print(title[i].text, author[i].text)
