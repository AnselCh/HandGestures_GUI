from HandMain import Ui_HandGestures as H_ui
from mp_set import Ui_Form as a_ui
from msg import Ui_Form as msg_ui
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import csv


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
        self.Build.clicked.connect(self.goCAM2)
        self.Label.clicked.connect(self.goLabelCsv)
        self.Training.clicked.connect(self.goTraining)

    def goAPP(self):
        self.aui = AUI()
        self.aui.show()

        self.aui.runButton.clicked.connect(self.goCAM1)  # 輸入完參數Run

    def goCAM1(self):

        w = self.aui.spinBox.value()
        h = self.aui.spinBox_2.value()
        # 將設定偵測手的數量、鏡頭轉存到CSV檔
        csv_path = 'setting.csv'
        with open(csv_path, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([w, h])
        print('寫入setting.csv成功')
        self.aui.close()  # 存檔後關閉

        self.cam1 = os.system("python sp_app.py")  # 執行

    def goCAM2(self):
        self.cam2 = os.system("python record_gestures.py")

    def goLabelCsv(self):
        self.label = os.system("sp_model\keypoint_label.csv")
        self.label

    def goTraining(self):
        self.Train = os.system("python training.py")
        self.aui = AUI()  # Run之後關閉參數畫面
        self.aui.close()

    def goMsg(self):
        self.mui = MUI()
        self.mui.show()

    def datapass(self):
        MH = self.aui.spinBox.value()
        WC = self.aui.spinBox_2.value()
        data = [str(MH), str(WC)]
        with open('setting.csv', 'w', newline='') as csvfile:
            # 寫入欄位名稱
            writer = csv.writer(csvfile)
            writer.writerows(data)


class AUI(QtWidgets.QMainWindow, a_ui):  # APP參數設定畫面(APP)
    def __init__(self):
        super(AUI, self).__init__()
        self.setupUi(self)


class MUI(QtWidgets.QMainWindow, msg_ui):
    def __init__(self):
        super(MUI, self).__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_HUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
