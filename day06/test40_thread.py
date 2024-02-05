# file: test40_thread.py
# desc: Qt 스레드로 동작

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) # 시그널을 UT 쓰레드로 젼달하기 위한 변수개체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent  # BackWorker에서 사용할 멤버변수

    
    def run(self) -> None: # Thread 실행
        # thread로 동작할 내용
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        ## self.parent.pgbTask.setValue(0) # !QThread에서는 UI 관련된 처리를 할 수 없음
        ## self.parent.pgbTask.setRange(0, maxVal-1)
        for i in range(maxVal):
            print_str = f'쓰레드 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            ## self.parent.txbLog.append(print_str)
            ## self.parent.pgbTask.setValue(i)

class qtwin_exam(QWidget): # UI 쓰레드
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self) # QtDesigner에서 만든 ui를 로드
        # 버튼에 대한 시그널처리

        # ui 파일 내에 있는 위젯접근은 VSCode 상에서 색상으로 표시X
        self.btnStart.clicked.connect(self.btnStartCliceked)

    def btnStartCliceked(self):
        th = BackWorker(self)
        th.start() # BackWorker 내의 self.run() 실행
        th.initSignal.connect(self.initPgbTask)
        th.setSignal.connect(self.setPgbTask)
        th.setLog.connect(self.setTxbLog)

    def closeEvent(self, QCloseEvent) -> None: # X 버튼 클릭 시, 종료 확인
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    
    
    # 스레드에서 시그널이 넘어오면 UI를 대신 처리해주는 부분
    @pyqtSlot(int) # BackWorker 스레드에서 self.initSingnal.emit() 동작해서 실행
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1)

    @pyqtSlot(str) # BackWorker 스레드에서 self.setLog.emit() 동작해서 실행
    def setTxbLog(self, msg):
        self.txbLog.append(msg)
    @pyqtSlot(int)
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

if __name__ == '__main__':
    loop = QApplication(sys.argv)
    isinstance = qtwin_exam() 
    isinstance.show()
    loop.exec_()

