from django.shortcuts import render
from bs4 import BeautifulSoup
# 데이터 저장을 위해 만듦
from .models import Data

import requests
# 공백문자 제거를 위해 
import re

# 구글 시트를 사용하기 위해서 import
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Create your views here.
def save(request):
    datas = Data()
    if requests.get['user_name']:
        datas.name = requests.get['user_name']
        datas.title = requests.get['book_title']
        data.author = requests.get['book_author']
    
    print(datas)
    return render(request, 'save.html')

# 구글 시트에 저장되어있는 회원 정보 불러오기
def call(request):
    name = request.GET['user']
    print(name)
    scope = [
    'https://spreadsheets.google.com/feeds',    
    ]
    json_file_name = 'key.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    gc = gspread.authorize(credentials)
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1L8V9TSVD9iW7p9svQBZw2PUq8zQ8I13JdzLPZ3xunQk/edit#gid=0'
    # 스프레스시트 문서 가져오기 
    doc = gc.open_by_url(spreadsheet_url)
    # 시트 선택하기 : 시트 이름이 Raw 인 곳
    worksheet = doc.worksheet('Raw')
    seeAll = worksheet.get_all_values()
    j = 0
    save = []
    time = []
    kind = []
    date = []
    title = []
    author = []
    genre = []
    for i in range(3,len(seeAll),1):   
        if name in seeAll[i][3]:
            j+=1
            print(seeAll[i][0:7], j)
            save.append(seeAll[i][0:7])
            time.append(seeAll[i][0])  
            kind.append(seeAll[i][1])  
            date.append(seeAll[i][2])  
            title.append(seeAll[i][4])  
            author.append(seeAll[i][5])  
            genre.append(seeAll[i][6])  
        else:
            pass
    context ={
        'save':save,
        'time':time,
        'kind':kind,
        'date':date,
        'author':author,
        'title':title,
        'genre':genre,
    }
    return render(request, 'save.html', context)
    
    # type : str
    #print(type(seeAll[3][3]))
    #print(seeAll[4:8][0][3])

    #print(len(seeAll))
    #print(seeAll[0])
    #for i in len(seeAll):    
    # row는 2부터 시작g
    # 회차, 종류, 날짜, 이름, 제목, 저자, 장르
    #insert= ['478','정기','2020. 1. 31','황성민','파프리카','츠츠이 야스타카'
    #worksheet.insert_row(insert, 2)    

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

def delete_one(request, data_id):
    datas = Data.objects.get(id=data_id)
    datas.delete()

    datas = Data.objects.all()
    context = {
        'alldata' : datas,
    }    
    return render(request, 'main.html', context)
