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
    return r

def get_paging_call(keyword, quantity):
    if quantity > 1100:
        exit("Error 최대 요청할 수 있는 건수는 1100건 입니다.")

    repeat = quantity
    result = []
    for i in range(repeat):
        start = i * 100 + 1

        if start > 1000:
            start = 1000
        print(f"{i + 1}번 반복 합니다. start={start}")
        r = call_api(keyword, start, display=100)
        print(r['items'][0])
        result.append(r['items'])
    return result

if __name__ == '__main__':
    r = get_paging_call("교대역 이비인후과", 1000)
    print(r[0])
    print(len(r))


