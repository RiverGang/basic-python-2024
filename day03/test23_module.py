# file: test23_module.py
# desc : 모듈 사용

import math

PI = 3.141592
radius = 5
print(f'원의 크기는 {radius * radius * PI}')
# print(math.pi)
print(f'정확한 원의 크기는 {radius*radius*math.pi}')

print(f'cos(0) = {math.cos(0)}')
print(2 ** 10)
print(math.pow(2, 10)) # 제승
print(math.ceil(3.1)) # 올림
print(math.floor(3.5)) # 내림
print(round(3.5)) # 반올림(너무 많이 사용해서 math가 아닌 기본 함수)

import math as m # 별명짓기
print(m.sin(0))

from math import pi, pow # 단, from 사용은 조심해야함. 최적화를 위해 사용하기도 함

print(pi)
print(pow(2, 10))

