from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# 공백문자 제거를 위해 
import re

# 입력한 책 제목
keyword = input('책 제목을 입력 : ')

print(keyword)
url = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord="+keyword+"&orderClick=LAG"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
titles = soup.select('.detail > .title')
authors = soup.select('.detail > .author ')

#f_authors = soup.select('.detail > .author > a')

# 공백제거    
print(len(titles))
print(len(authors))

r = []
r = authors[1].text.rstrip('\n|\r|\t')[0:15]
print(r)

#print('====================')
