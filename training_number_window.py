from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 200)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        Form.setFont(font)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(150, 70, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(45, 20, 280, 41))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.trButton = QtWidgets.QPushButton(Form)
        self.trButton.setGeometry(QtCore.QRect(112, 110, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(10)
        self.trButton.setFont(font)
        self.trButton.setObjectName("trButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # self.trButton.clicked.connect()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Training Number"))
        self.label.setText(_translate(
            "Form", "How many gestures need to training?"))
        self.trButton.setText(_translate("Form", "Let do it!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
