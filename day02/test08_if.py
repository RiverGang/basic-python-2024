#desc : 홀수/짝수 또는 배수 구분

number = int(input('정수입력 > ')) #입력 받은 후 정수로 변경

if number % 2 == 0: #짝수
    print('짝수')
else: #홀수
    print('2의 배수ㅏ가 아님')
    #pass 코드를 짜다 모르겠으면 패스
    

    ## if number % 5 == 0 <- 5의 배수 판단. % 연산자는 배수 구할 때 자주 이용됨
