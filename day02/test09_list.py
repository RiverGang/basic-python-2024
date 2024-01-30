#desc : 복합자료형 list

#s1 = 80 s2 = 90 s3 = 100 s4 = 50 s5 = 60 => 학생수 만큼 변수 생성


std = [80, 90, 100, 50, 60, 55, 77, 88, 99, 100] #list로 표현
#index = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#index = -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
# 총 갯수 10(n)이면, index의 마지막 값 = 9(n-1)

#리스트 요소 접근
print (std[9])

list_1 = [265, 3.5, '문자열', True, [1,2,3,4], (3.4), std]

print (list_1)
print(list_1[5])
list_1[6] = '바꾼 값' #list의 index 값 바꾸기
print(list_1) #[265, 3.5, '문자열', True, [1, 2, 3, 4], 3.4, '바꾼 값'] < 기존의 리스트가 문자열로 변경

## 리스트 연산
print(list_1[2:3+1]) # 뒤의 수는 출력하고 싶은 인덱스+1이 필수, 즉 예시는 index 2~3까지 출력.

print(list_1[-1]) # 바꾼 값 즉, index의 마지막 값이 나옴 only python만 있음
## 마이너스 인덱스
print(list_1[-5:-3])
## 이중 리스트
print(list_1[4][2]) # [1,2,3,4] 중 3만 가져오기 : 리스트 안의 리스트의 인덱스 값만 가져오기
list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1],[2]) # 결과=6

## 리스트 연산은 +, *만 사용가능
list_4 = [1,2,3]
list_5 = [7,8,9]
print(list_4 + list_5) # + : 리스트 연결 [1,2,3,7,8,9]
print(list_5*2) # * : 리스트 반복[7,8,9,7,8,9]

## 리스트의 길이함수 len()
print(len(list_4)) # 3

## append() 리스트 마지막에 하나 추가
## insert(index, val) 리스트의 index 앞에 val 추가 => 삽입

print(list_1)
list_1.append('Hello')
print(list_1)
list_1.insert(2, 100) #2번째 인덱스 앞에 값을 추가
print(list_1)

## extend() 기존 리스트 확장, +와 거의 유사하지만 차이 있음
list_4.extend(list_5)
print(list_4)
print(list_5)

##리스트 삭제 del
del list_4[3] # list_4의 3번째 index 값 삭제
print(list_4)
del list_4 #list_4 자체를 삭제, 이후 해당 리스트 프린트 불가 print(list_4)

val = list_5.pop() # 리스트에서 마지막 값을 완전히 꺼내오기
print(val) #9
print(list_5) #[7,8]

print(std)
val = std.pop(2) # 리스트에서 두번째 index 값을 꺼내오기
print(val)
print(std)

## clear()
list_5.clear() #del()은 완전 삭제 print 불가, clear()은 내용만 삭제 빈 리스트 생성
print(list_5)

#sort()
print(list_1)
#list_1.sort() 문자열, 숫자 불 섞여있는 리스트는 정렬안됨
std.sort() #오름차순 정렬
print(std)
std.sort(reverse=True) #내림차순 정렬
print(std)

# in, not in
print(99 in std) # True
print(98 in std) # False => 리스트 안에 해당 값이 포함되어 있는지 알 수 있음

#reverse(), copy(), count() ...

# *리스트 : 전개연산자 - 몰라도 됨
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b] #
print(list_c)

list_d = [list_a, list_b]
print(list_d)