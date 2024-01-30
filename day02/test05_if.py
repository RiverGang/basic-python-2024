# date : 20240130
# desc : 흐름제어 if문

## 조건이 참일때와 거짓일때로 나누어서 어떤 일 처리 if
## if 조건: 콜론(:) 입력 후 Enter시 자동으로 들여쓰기, 들여쓰기의 의미는 if문 안으로 들어간다는 뜻
## if 조건, elif: - 참인 조건
## else: - 거짓인 조건
## 입력함수 int(input()) - 문자로 된 입력값을 정수로 변경

number = int(input('정수입력 >')) ## 입력함수 int(input()) - 문자로 된 입력값을 정수로 변경

if number > 0: ## if 조건: - 참인 조건
    print('양수입니다')
elif number == 0: ## else if의 줄임 elif, 양수x 음수x
    print('0입니다')
elif number< 0:
    print('음수입니다')
else: ## else: - 거짓인 조건
    print('정의할 수 없습니다')

