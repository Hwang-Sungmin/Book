import requests

url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/fri"

response = requests.get(url)
data = response.json()
# print(data)
# print(type(data))

# for d in data.keys():
#     print(d)
#print(type(data["data"])) # list
webtoon_data = data["data"]

print(webtoon_data)


toons = []

for toon in webtoon_data:
    # 제목의 key는 'title'
    title = toon["title"]

    # 설명의 key는 'introduction'
    desc = toon["introduction"]

    # 장르의 위치는 'cartoon'안에 'genre'리스트 안에 'name' key
    genres = []
    for genre in toon["cartoon"]["genres"]:
        genres.append(genre["name"])
    # print(genres)

    # 작가의 위치는 'cartoon'안에 'artists'리스트 안에 'name' key
    artists = []
    for artist in toon["cartoon"]["artists"]:
        artists.append(artist["name"])
    # print(name)
    
    # 썸네일 이미지의 위치는 'pcThumbnailImage'리스트 안에 'url'key
    img_url = toon["pcThumbnailImage"]["url"]
    tmp = {
        title:{
            "desc":desc,
            "writer":artists,
            "genres":genres,
            "img_url":img_url
        }
    }
    toons.append(tmp)
