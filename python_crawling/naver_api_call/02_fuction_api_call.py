import keyword

import requests
import os


def call_api(keyword, start=1, display=10):
    client_id = os.getenv('NAVER_CLIENT_ID')
    client_secret = os.getenv('NAVER_CLIENT_SECRET')

    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret})

    # print(res.text)
    r = res.json()

def get_paging_call(keyword, quantity):
    repeat = 9
    for i in range(repeat):
        print(f"{i + 1}번 반복 합니다")

if __name__ == '__main__':
    r = get_paging_call("교대역 이비인후과", 10)


