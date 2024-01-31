# file: test19_ starprint.py
# desc: 별찍기 또는 피라미드 만들기

for i in range (1, 5+1):
    # i = 1일 때, range (1,2) 1번 반복
    # i = 2일 때, range (1,3) 2번 반복
    pass 
    if i % 2 == 1:
        
        for j in range(1, (6-i+1)//2): # range() 값 바꿔서 디버깅
            print(' ', end='')
        for j in range(1, i+1):
            print('*', end='')
        for j in range(1, (6-i+1)//2): # range() 값 바꿔서 디버깅
            print(' ', end='') # 엔터대신 empty로 변환
        print() # 안쪽 for문이 끝나면 엔터

        # / 사용했을땐 안되고, //사용하면 됨. 어떤 차이?
