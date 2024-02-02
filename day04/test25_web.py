# file : test25_web.py
# desc: urllib 모듈 사용법
# 웹사이트 내용을 파이썬을 가져오는 모듈

# 모듈 안의 모든 내용을 다 사용할 때 '*' 
# -ex) from urllib.request import *

from urllib.request import Request, urlopen # Request와 urlopen만 쓰겠다

req = Request('https://www.naver.com/') # 네이버 웹주소(url) 작성
res = urlopen(req) # url 주소로 웹사이트 열어달라고 요청

print(f'응답코드 : {res.status}') # url로 요청된 웹사이트 응답 확인
# 응답코드 200대 => able, 404 or 500대 => error

print(res.read())
print(res.read())

# urllib.request보다 성능이 조금 더 나은 모듈
import requests
res2 = requests.get('https://www.naver.com/')

print(res2.status_code)
print(res2.text)

