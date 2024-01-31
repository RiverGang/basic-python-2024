# file: test17_input.py
# desc: 콘솔 입력

# input()
# 출력- 컴퓨터 화면, 프린터, 스피커, 빔프로젝터, VR, ...
# 입력- 콘솔입력(키보드), 마우스 입력, 목소리, 조이스틱, 터치스크린

# input('내용 추가') 반드시 해줄 것

# 곱하기
temp_val = input('곱할 수 입력 > ') # int() 문자열형에서 "정수"형으로 변환 => 형변환

if temp_val.isnumeric() == True: # 숫자 입력이 아니면 튕겨내기
    temp_val = int(temp_val) # int() 문자열형에서 "정수"형으로 변환 => 형변환
    print(f'입력 값 = {temp_val}')
    result = temp_val * 5
    print(f'결과 = {result}')
else:
    print('잘못 된 입력 값, 정수만 입력하세요')

# 곱하기 응용
    
temp_val = input('곱할 수 입력 > ') 
while temp_val.isnumeric() == False: # 입력값이 정수가 아니면, 입력값 기입 반복
    print('잘못 된 입력 값, 정수만 입력하세요')
    print()
    temp_val = input('곱할 수 입력 > ')
    if temp_val.isnumeric() == True: # 입력 값이 정수가 되면, while문 탈출
        break

temp_val = int(temp_val)    
print(f'입력 값 = {temp_val}')
result = temp_val * 5
print(f'결과 = {result}')

