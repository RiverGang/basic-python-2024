# file : test36_pyqt.py
# desc : PyQt5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
## GUI : Graphic User Interface, CLI : Commend Line Interface
from PyQt5.QtWidgets import QApplication, QWidget
# print(sys,argv) # 현재 파이썬 파일의 경로 표시

class qtwin_exam(QWidget): #QWiget을 [상속] 받을거야. QWidget이 가진 모든 것을 사용
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI() # 화면 초기화(self) 함수 호출
    
    def initUI(self):
        self.setGeometry((1920-400)//2, (1080-300)//2, 400, 300) # x, y (앱의 위치 좌표 값) width, height
        self.setWindowTitle('Qt5 Hello world')
        self.text = ''
        self.show()
    
    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10)) # dark gary / R=0, G=0, B=0 -> black / R=0, G=255, B=255 -> White
        paint.setFont(QFont('NanumGothic', 15))
        paint.drawText((400-150)//2, 300//2, 'HELL WORLD!')
        paint.drawText(event.rect(), Qt.AlignCenter, self.text) # Align(Left, Center, Right) 정렬 위치

    def paintEvent(self, event) -> None: # 재정의(Override)
        paint = QPainter()
        paint.begin(self) # 열면
        self.drawText(event, paint)
        paint.end() # 닫는다

loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
isinstance = qtwin_exam() #Qwidget을 상속한 qtwin_exam() 객체를 생성
loop.exec_() 
