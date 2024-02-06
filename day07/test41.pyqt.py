# file: test41_pyqt.py
# desc: PyQt5 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget


class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이미지 삽입.scaledToWidth() 큰 해상도의 이미지를 w800d으로 고정
        pixmap = QPixmap('./images/kitty.jpg').scaledToWidth(800)
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(self)
        lblSize.setFont(QFont('NanumGothicCoding', 20)) # 폰트와 폰트사이즈 변경
        lblSize.setStyleSheet('Color: #9999CC;') # 폰트 색상 변경
        lblSize.setText(f'{pixmap.width()} x {pixmap.height()}')
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # 가로중앙정렬 | 세로중앙정렬

        vbox = QVBoxLayout(self) # QtDesigner의 VerticalLayout 위젯 생성
        vbox.addWidget(lblImage) # VerticalLayout 안에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # Form에 VL 추가와 동일

        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('이미지뷰어')
        
        rect = QRect(300, 300, 300, 300) #x, y, w, h
        self.setGeometry(rect) # 같은 이름의 함수를 여러개 선언해놓고 원하는 것을 사용 (오버로딩)
        # self.setGeometry(300, 300, 300, 300)

        self.show() #showFullScreen() 모니터를 꽉 채워서 출력
        self.setCenter()
    
    def setCenter(self): ## 윈앱을 화면 정중앙에 위치
        gm = self.frameGeometry() # 윈앱 자신 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값 가져오기
        gm.moveCenter(cp)
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_reac = app.desktop().screenGeometry()
    width, height = screen_reac.width(), screen_reac.height()
    print(width, 'x', height) # 활용도 높음
    ins = WinApp()
    ins.show() 
    sys.exit(app.exec_()) # 종료 시, 리소스 반환등 효율

