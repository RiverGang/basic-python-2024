# file: text42_pypaint.py
# desc: 그림판 만들기

import sys
from PyQt5 import uic # QtDesigner 호출 시 필요
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *

class WinApp(QWidget):   
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('./day07/pyPaint.ui', self)
        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('Py 그림판')

        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:balck;')
        self.btn_blue.setStyleSheet('background:blue;')
        self.btn_red.setStyleSheet('background:red;')

        self.show()
        self.setCenter()


    def initSignal(self): # 동작초기화
        self.btn_black.clicked.connect(self.button_Clicked)
        self.btn_blue.clicked.connect(self.button_Clicked)
        self.btn_red.clicked.connect(self.button_Clicked)
        self.btn_clear.clicked.connect(self.button_Clicked)
        # 2024-02-06 이미지로드 및 저장버튼 추가
        self.btn_load.clicked.connect(self.btnLoadClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)
        
        
    def btnLoadClicked(self):
        # class 내에서 다 쓰고 싶은 변수는 self. 붙이기, 함수 내에서만 사용하는 변수는 안붙여도 됨
        image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
        imagePath = image[0]
        # print(imagePath)
        pixmap = QPixmap(imagePath).scaledToHeight(380) # 파일 경로에 있는 이미지를 읽어서 pixmap 객체에 담는다
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() # 이미지를 Label 크기에 맞추기
        
    def btnSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지저장', '', 'Image file(*.jpg;*.png)')
        if filePath == '': return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)

    def button_Clicked(self): # black, red, blue를 다 통일한 함수
        btn_val = self.sender().objectName()  
        print(btn_val)
        if btn_val == 'btn_black': # 검정버튼 클릭
            self.brushColor = Qt.black           
        elif btn_val == 'btn_red': # 빨간버튼 클릭
            self.brushColor = Qt.red
        elif btn_val == 'btn_blue': # 파란버튼 클릭
            self.brushColor = Qt.blue
        elif btn_val == 'btn_clear': # 파란버튼 클릭
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)


    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap()) # pixmap 위에만 그림이 그려지도록 영역 설정
        brush.setPen(QPen(self.brushColor, 7, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update() # 화면 업데이트      
    
    def setCenter(self): ## 화면 정중앙 위치
        gm = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center()
        gm.moveCenter(cp)
        self.move(gm.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())

