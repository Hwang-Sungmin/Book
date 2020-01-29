import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

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

# 모든 value 값을 확인 get_all_values()
seeAll = worksheet.get_all_values()

# row는 2부터 시작
# 회차, 종류, 날짜, 이름, 제목, 저자, 장르
insert= ['478','정기','2020. 1. 31','황성민','파프리카','츠츠이 야스타카','소설']
worksheet.insert_row(insert, 2)

# 액셀 합치기

