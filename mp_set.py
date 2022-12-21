from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 275)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        Form.setFont(font)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(180, 60, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 105, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(180, 110, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        # runButton
        self.runButton = QtWidgets.QPushButton(Form)
        self.runButton.setGeometry(QtCore.QRect(90, 180, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(10)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        # backButton
        self.backButton = QtWidgets.QCommandLinkButton(Form)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 31, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setObjectName("backButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "setting"))
        self.label.setText(_translate("Form", "Max Hands"))
        self.label_2.setText(_translate("Form", "Webcam"))
        self.runButton.setText(_translate("Form", "R u n"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
