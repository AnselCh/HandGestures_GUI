from HandMain import Ui_HandGestures as H_ui
from mp_set import Ui_Form as a_ui
from appcam1 import Ui_Form as cam1_ui
from appcam2 import Ui_Form as cam2_ui

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class HUI(QtWidgets.QMainWindow, H_ui):
    def __init__(self):
        super(HUI, self).__init__()
        self.setupUi(self)


class AUI(QtWidgets.QMainWindow, a_ui):
    def __init__(self):
        super(AUI, self).__init__()
        self.setupUi(self)


class CUI1(QtWidgets.QMainWindow, cam1_ui):
    def __init__(self):
        super(CUI1, self).__init__()
        self.setupUi(self)


class CUI2(QtWidgets.QMainWindow, cam2_ui):
    def __init__(self):
        super(CUI2, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    h = HUI()
    h.show()
    a = AUI()
    c1 = CUI1()
    c2 = CUI2()

    # if h.APP.clicked.connect(lambda: {h.close(), a.show()}):
    #     sys.exit(app.exec_())
    # if h.Build.clicked.connect(lambda: {h.close(), c1.show()}):
    #     sys.exit(app.exec_())
