# file: test12_dictionary.py
# desc: 복합자료형 딕셔너리


## 사전형 key와 value쌍을 나열해 놓은 자료형
## key는 '문자열'형태로 하는 것이 좋음. value는 자유롭게 (list 형태도 가능)
# => {key:value, key:value, key:value, ...}

dict_movie = { 'name' : '어벤저스 엔드게임', 'type':'히어로 무비', 'year':2019, 'directior':['안소니 루소','조 루소'], 'cast':['아이언맨','타노스','헐크','토르','닥터스트레인지'] }

# 조회
print(dict_movie['directior'])
print(dict_movie['year'])

# 추가, 수정
dict_movie['year'] = 2020 # 'year' key의 value 값 수정
print(dict_movie)

dict_movie['producer'] = '케빈 파이기' # key와 value 한쌍 추가
print(dict_movie)

# 키에 대한 값을 찾을 때
if 'producer' in dict_movie:
    print(dict_movie['producer'])
else:
    print('제작자 없음')

musician = dict_movie.get('musician') # 오류(예외) 발생x
print(musician)
#print(dict_movie['musician']) 오류(예외) 발생

print('반복문----------------------------------------')
## 반복문으로 출력
for key in dict_movie:
    print(key,':', dict_movie[key])

print('반복문 다른 방법 --------------------------------')
for key, value in dict_movie.items():
    print(key,':',value)