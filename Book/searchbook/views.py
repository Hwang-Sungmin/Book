from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# 공백문자 제거를 위해 
import re

# Create your views here.
def main(request):       
    return render(request, 'main.html')

def search(request):    
    # 입력한 책 제목
    keyword = request.GET['sbook']

    print(keyword)
    url = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord="+keyword+"&orderClick=LAG"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.select('.detail > .title')
    authors = soup.select('.detail > .author ')

    # 공백제거    
    print(len(titles))
    print(len(authors))
    
    # dic선언 type:class
    
    
    title = []
    author = []
    # strip()[시작:끝]  시작:끝의(-2)만큼 빼고[20:-2] 
    
    for i in range(len(titles)):

        print(titles[i].text, authors[i].text.strip()[0:15])                
        
        a = titles[i].text
        b = authors[i].text.strip()[0:15]

    
        
        title.append(a)
        author.append(b)
        # dic() key : value
        # 마지막 값만 들어가는데 어떻게 
        
        # 딕셔너리 = dict(키1=값1, 키2=값2)
        # 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
        # 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
        # 딕셔너리 = dict({키1: 값1, 키2: 값2})

        # 하나의 key 에 value 여러개 넣기
        #value['title'] = titles[i].text
        #value['author'] = authors[i].text.strip()[0:15]
    
    print(title)
    print(author)
    context = {
        'title' : title,
        'author' : author,
    }
    return render(request, 'main.html', context)

def no_space(text):
    text1 = re.sub('\r|\t|\n', '', text)
    return text1