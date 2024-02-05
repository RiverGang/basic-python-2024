# file : test39_pyqt.py
# desc : Qt에서 스레드 없이 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self) # QtDesigner에서 만든 ui를 로드
        # 버튼에 대한 시그널처리

        # ui 파일 내에 있는 위젯접근은 VSCode 상에서 색상으로 표시X
        self.btnStart.clicked.connect(self.btnStartCliceked) 
       
    def btnStartCliceked(self):
        maxVal = 101
        print('시작버튼 클릭')
        self.pgbTask.setValue(0) # 프로그레스바 0부터 시작
        self.pgbTask.setRange(0, maxVal-1) # 0부터 100까지 범위 지정
        for i in range(maxVal): # 0-100까지
            print_str = f'노쓰레드 출력 >> {i}'
            print(print_str)
            self.txbLog.append(print_str)
            self.pgbTask.setValue(i)


    def closeEvent(self, QCloseEvent) -> None: # X 버튼 클릭 시, 종료 확인
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    
    

if __name__ == '__main__':
    loop = QApplication(sys.argv)
    isinstance = qtwin_exam() 
    isinstance.show()
    loop.exec_()
