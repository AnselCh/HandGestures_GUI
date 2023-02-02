from HandMain import Ui_HandGestures as H_ui
from app_setting_window import Ui_Form as a_ui
from training_number_window import Ui_Form as t_ui
from success_msg import Ui_Form as msg_ui
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
        self.APP.clicked.connect(self.goAPP)  # 開啟設定鏡頭及手掌數量
        self.Build.clicked.connect(self.goAPP2)  # 開啟設定鏡頭及手掌數量
        self.Label.clicked.connect(self.goLabelCsv)  # 開啟定義標籤名稱
        self.Training.clicked.connect(self.goTraining)  # 輸入要訓練的手勢數量

    def goAPP(self):
        self.aui = AUI()
        self.aui.show()
        self.aui.runButton.clicked.connect(self.goCAM1)  # 輸入完參數Run

    def goAPP2(self):
        self.aui = AUI()
        self.aui.show()
        self.aui.runButton.clicked.connect(self.goCAM2)  # 輸入完參數Run

    def goTraining(self):
        self.tui = TUI()
        self.tui.show()
        self.tui.trButton.clicked.connect(self.make_model)  # 輸入完參數Run

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

        self.cam1 = os.system("python app.py")  # 執行

    def goCAM2(self):
        w = self.aui.spinBox.value()
        h = self.aui.spinBox_2.value()
        # 將設定偵測手的數量、鏡頭轉存到CSV檔
        csv_path = 'setting.csv'
        with open(csv_path, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([w, h])
        print('寫入setting.csv成功')
        self.aui.close()  # 存檔後關閉
        self.cam2 = os.system("python record_gestures.py")

    def goLabelCsv(self):
        self.label = os.system("sp_model\keypoint_label.csv")
        self.label

    def make_model(self):
        n = self.tui.spinBox.value()
        csv_path = 'setting.csv'
        with open(csv_path, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([n])
        print('寫入setting.csv成功')
        self.tui.close()  # 存檔後關閉
        self.Train = os.system("python training.py")

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


class TUI(QtWidgets.QMainWindow, t_ui):  # 訓練資料參數設定畫面
    def __init__(self):
        super(TUI, self).__init__()
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
