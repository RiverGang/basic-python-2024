# file: test14_while.py
# desc: while 문

## while 참인 조건:
## [공통점] if 조건: elif 조건: else: , for in range():, while 조건: ==> ':' 콜론 마무리

count = 0

#while count < 10: #count 변수값이 10보다 작거나 같은 동안 반복

# 무한루프 : Window OS, 스마트폰OS, 자동차네비게이션, 라즈베리파이, 아두이노, 게임, Winform개발 etc..
while True: #조건이 참인 동안, True는 항상 참. => Infinite Loop 무한 루프
    count = count + 1
    print('나무찍기', count)
    if count == 10:
        break # 이 반복문을 빠져나가라.


number = 0
while True:
    number = number + 1
    if str(number).count('3') >= 1 or \
    str(number).count('6') >= 1 or \
    str(number).count('9') >= 1: #숫자를 문자열로 바꾼 값안에  '3', '6', '9'가 있으면
        print('짝') # 짝! 대신 continye로 변경
        # continue는 반복에서 제외
    else:
        print(number)

    if number >= 31: break # break는 반복문을 완전히 빠져나감을 의미