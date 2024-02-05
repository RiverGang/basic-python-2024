# file: text37_pyqt.py
# desc: PyQt5 이벤트(Signal)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        betn01 = QPushButton('클릭', self)
        betn01.setGeometry(50, 100, 100, 40)
        betn01.clicked.connect(self.btn01_clicked) # 버튼 클릭 시(signal), btn01_clicked 함수를 실행(connect)
        
        self.setGeometry(300, 200, 400, 200)
        self.setWindowTitle('버튼 이벤트')
        self.show()

    def btn01_clicked(self):
        QMessageBox.about(self, '버튼클릭', '버튼을 클릭했습니다')

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__' : # Main entry 확인조건 추가                   
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    loop.exec_()