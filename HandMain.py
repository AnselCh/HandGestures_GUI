from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HandGestures(object):
    def setupUi(self, HandGestures):
        HandGestures.setObjectName("HandGestures")
        HandGestures.resize(300, 275)
        font = QtGui.QFont()
        font.setFamily("Arial")
        HandGestures.setFont(font)
        self.APP = QtWidgets.QPushButton(HandGestures)
        self.APP.setGeometry(QtCore.QRect(100, 65, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        self.APP.setFont(font)
        self.APP.setMouseTracking(False)
        self.APP.setCheckable(False)
        self.APP.setAutoDefault(True)
        self.APP.setFlat(False)
        self.APP.setObjectName("APP")
        self.Build = QtWidgets.QPushButton(HandGestures)
        self.Build.setGeometry(QtCore.QRect(100, 110, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        self.Build.setFont(font)
        self.Build.setAutoDefault(True)
        self.Build.setFlat(False)
        self.Build.setObjectName("Build")
        self.Label = QtWidgets.QPushButton(HandGestures)
        self.Label.setGeometry(QtCore.QRect(100, 155, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        self.Label.setFont(font)
        self.Label.setAutoDefault(True)
        self.Label.setFlat(False)
        self.Label.setObjectName("Label")
        self.Training = QtWidgets.QPushButton(HandGestures)
        self.Training.setGeometry(QtCore.QRect(100, 200, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        self.Training.setFont(font)
        self.Training.setAutoDefault(True)
        self.Training.setFlat(False)
        self.Training.setObjectName("Training")
        self.label = QtWidgets.QLabel(HandGestures)
        self.label.setGeometry(QtCore.QRect(30, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")

        self.retranslateUi(HandGestures)
        QtCore.QMetaObject.connectSlotsByName(HandGestures)

    def retranslateUi(self, HandGestures):
        _translate = QtCore.QCoreApplication.translate
        HandGestures.setWindowTitle(_translate("HandGestures", "HandGestures"))
        self.APP.setText(_translate("HandGestures", "APP"))
        self.Build.setText(_translate("HandGestures", "Build"))
        self.Label.setText(_translate("HandGestures", "Label"))
        self.Training.setText(_translate("HandGestures", "Training"))
        self.label.setText(_translate(
            "HandGestures", "Hand Gestures Detection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HandGestures = QtWidgets.QWidget()
    ui = Ui_HandGestures()
    ui.setupUi(HandGestures)
    HandGestures.show()
    sys.exit(app.exec_())
