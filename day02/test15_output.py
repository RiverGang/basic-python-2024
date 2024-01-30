# file: test15_output.py
# desc : 콘솔 출력 포맷양식 String Format

string_1 = '{}'.format(10) #{} 위치에 함수 뒤 ()에 있는 값을 치환, 원하는 양식으로 표현
print(type(string_1))

name = '이성희' #input('이름 입력 > ')
string_2='안녕하세요, {}입니다!'.format(name)
print(string_2)

string_3 = '{}{} {}'.format(4000, '만', '빌려주세요')
print(string_3)

#정수 문자열 포맷 d, 공간할당, 양수/음수 표현 
string_4 = '_____{:d}_____'.format(100) # 'd' 정수
print(string_4)

string_4 = '_____{:5d}_____'.format(100) # '5' 다섯자리 할당
print(string_4)
string_4 = '_____{:05d}_____'.format(100) # '05' 다섯자리 만들 때 빈자리 0으로 채우기 
print(string_4)

string_4 = '_____{:+05d}_____'.format(-100) # '+' 양수/음수 표현 
print(string_4)

string_4 = '_____{:=+10d}_____'.format(-100) # '=' 기호와 숫자를 분리
print(string_4)


#실수 문자열 포맷 f = 기본 소수점 6자리까지

string_5 = '_____{:f}_____'.format(78.333) 
print(string_5) # 78.333000

string_5 = '_____{:.2f}_____'.format(78.333) # 78.33 소수점 둘째자리까지 나타남
print(string_5)

string_5 = '_____{:7.2f}_____'.format(78.333) # __78.33 소수점 둘째자리까지, 일곱자리 공간 할당
print(string_5)

# 파이썬 3.6 이후 도입. format() 함수 사용 X
val = 78.3333333333
string_6 = f'_____{val:7.2f}_____'
print(string_6)

string_7 = 'Hello, World!'

print(string_7.upper()) # upper case 대문자 변환 <--> lower case 모두 소문자 변환
print(string_7.lower())
print(string_7.lower().capitalize()) # capitalize 첫글자만 대문자로 변환

print(string_7.split(' ')) # 특정한 단어 ()로 자르는 함수

string_8 = 'Hello, I am MG Sung. I am a lecturer. Good Luck for your day.'
words = string_8.split(' ')
print(words)
print(f'string_8 문장의 단어 갯수는 {len(words)}개 입니다.')

string_9 = 'A10'
print(string_9.isalnum()) #True
print(string_9.isnumeric()) #False A 알파벳
string_10 = '10.5' # 소수점은 함수를 만들어서 처리해야함
print(string_10.isdecimal()) #False

print('안냥' in '안녕하세요')