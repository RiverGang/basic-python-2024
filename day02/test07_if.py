#date : 20240130
# desc : if문 응용
import datetime #날짜를 이용한 기능

now = datetime.datetime.now() # 현재의 년원일 시분초를 가져오는 함수

if now.hour < 12:
    print('오전입니다.')
else: # if now.hour >= 12:
    print('오후입니다.')