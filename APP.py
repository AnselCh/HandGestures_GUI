from HandMain import Ui_HandGestures as H_ui
from mp_set import Ui_Form as a_ui
from appcam1 import Ui_Form as cam1_ui
from appcam2 import Ui_Form as cam2_ui

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Controller():
    def __init__(self):
        pass

    def show_HUI(self):
        self.hui = HUI()
        self.hui.show()


class HUI(QtWidgets.QMainWindow, H_ui):  # APP選單畫面
    def __init__(self):
        super(HUI, self).__init__()
        self.setupUi(self)
        self.APP.clicked.connect(self.goAPP)
        self.Build.clicked.connect(self.goCAM1)

    def goAPP(self):
        self.aui = AUI()
        self.aui.show()
        self.aui.runButton.clicked.connect(self.goCAM2)  # 輸入完參數Run

    def goCAM1(self):
        self.cam1 = CUI1()
        self.cam1.show()

    def goCAM2(self):
        self.cam2 = CUI2()
        self.aui = AUI()  # Run之後關閉參數畫面
        self.aui.close()
        self.cam2.show()


class AUI(QtWidgets.QMainWindow, a_ui):  # APP參數設定畫面(APP)
    def __init__(self):
        super(AUI, self).__init__()
        self.setupUi(self)
        self.runButton.clicked.connect(self.goCAM2)

    def goCAM2(self):
        self.cam2 = CUI2()
        self.cam2.show()


class CUI1(QtWidgets.QMainWindow, cam1_ui):  # APPCAM(參數設定後)
    def __init__(self):
        super(CUI1, self).__init__()
        self.setupUi(self)


class CUI2(QtWidgets.QMainWindow, cam2_ui):  # TrainCAM
    def __init__(self):
        super(CUI2, self).__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_HUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
