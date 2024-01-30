# file: test13.range.py
# desc : 리스트 범위지정

list_a = [1,2,3,4,5,6,7,8,0]

print(list_a)

# 범위 지정
print(range(5))

# 범위 지점 range(5), 0부터 N개의 범위 범위 수를 생성
print(list(range(5)))
print(list(range(1,6))) # 1~5까지
print(list(range (1 , 20,2 ))) # 1부터 19까지 2씩 증가
print(list(range (10 , -1 ,-1 ))) # 1 countoodown
    
list_a = list(range(1,100)) # range() 클래스
print(list_a)
list_a = [i for i in range(1, 101)] #리스트 컨프리헨션
print(list_a)

