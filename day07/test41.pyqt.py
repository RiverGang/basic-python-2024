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
        lblSize.setText(f'{pixmap.width()} x {pixmap.height()}')

        vbox = QVBoxLayout(self) # QtDesigner의 VerticalLayout 위젯 생성
        vbox.addWidget(lblImage) # VerticalLayout 안에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # Form에 VL 추가와 동일

        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('이미지뷰어')
        self.setGeometry(300, 300, 300, 300)
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

