from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(260, 150)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 100, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(15, 45, 250, 35))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.closeApp)

    def closeApp(self):
        Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Status"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.label.setText(_translate("Form", "Model Training Success"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
