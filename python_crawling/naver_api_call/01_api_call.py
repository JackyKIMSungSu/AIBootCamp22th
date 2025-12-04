import requests
import os


client_id = os.getenv('NAVER_CLIENT_ID')
client_secret = os.getenv('NAVER_CLIENT_SECRET')
print(client_id, client_secret)

url = "https://openapi.naver.com/v1/search/blog.json?query=교대역 맛집&start=1000&display=100"
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}
res = requests.get(url, headers=headers)

print(res.text)
r = res.json()
print(len(r['items']))

