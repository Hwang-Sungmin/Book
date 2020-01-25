from django.shortcuts import render
from bs4 import BeautifulSoup
# 데이터 저장을 위해 만듦
from .models import Data

import requests
# 공백문자 제거를 위해 
import re

# Create your views here.
def main(request):       
    return render(request, 'main.html')

def search(request):    
    # 입력한 책 제목
    keyword = request.GET['sbook']
    # 검색할때마다 지우기
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
        
        t = titles[i].text
        a = authors[i].text.strip()[0:15]
        
        t = t.replace("\n","")

        # 문자열에서 부분지우기
        a = a.replace("\r","")
        a = a.replace("\n","")
        a = a.replace("\t","")
        a = a.replace(" ","")
        title.append(t)
        author.append(a)
        
        #DB에 저장
        datas = Data()
        datas.title = t
        datas.author = a
        datas.save()

     
        # t와 a로 데이터에 저장
        
        # dic() key : value
        # 마지막 값만 들어가는데 어떻게 
        
        # 딕셔너리 = dict(키1=값1, 키2=값2)
        # 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
        # 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
        # 딕셔너리 = dict({키1: 값1, 키2: 값2})

        # 하나의 key 에 value 여러개 넣기
        #value['title'] = titles[i].text    
        #value['author'] = authors[i].text.strip()[0:15]
    
    all_data = Data.objects.all()
     
    context = {
        'title' : title,
        'author' : author,
        'alldata' : all_data,
    }
    
    return render(request, 'main.html', context)

def delete_all(request):
    datas = Data.objects.all()
    datas.delete()
    return render(request, 'main.html')