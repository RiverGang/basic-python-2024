# file: test22 car.py
# desc: Car 클래스 만들기

class Car:
    wheel_num = 4
    color = 'white'
    __plate_num = ''
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 후회전
    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다')

    def moveBackward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveLeft(self):
        print(f'{self.__plate_num}이 좌회전합니다.')

    def moveRight(self):
        print(f'{self.__plate_num}이 우회전합니다.')

    def __init__(self, number, company, col, gear) -> None:
        self.__plate_num = number
        self.company = company
        self.color = col
        self.gear_type = gear

    def getPlateNumber(self):
        return self.__plate_num
    
    def setPlateNumber(self, new_plateNumber):
        self.__plate_num = new_plateNumber

    def __str__(self) -> str: # print(객체) 출력되는 부분 지정
        return f'제 차는 {self.__plate_num}입니다. {self.color}입니다.'
    
sarah = Car('54라 9538', '현대자동차', '흰색', '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있습니다.
print(sarah)
print(f'차번호는 {sarah.getPlateNumber()}')
print(f'차 생삭은 {sarah.color}')
sarah.moveForward()

sarah.plate_num = '98하 7789' # 악의적인 의도를 가지고 변경하는거지만, 변경불가
print(sarah)

sarah.setPlateNumber('54로 9555') # 클래스에 인정받은 동작으로 값을 변경
print(sarah)

# csuv = Car('경남88 1922', '기아자동차', '회색', '자동')
# print(f'차번호는 {csuv.plate_num}')
# print(sarah)

