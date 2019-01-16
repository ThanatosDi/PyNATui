# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyNAT_Setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyNAT_Setting(object):
    def setupUi(self, PyNAT_Setting):
        PyNAT_Setting.setObjectName("PyNAT_Setting")
        PyNAT_Setting.resize(270, 365)
        self.SourcePortText = QtWidgets.QLabel(PyNAT_Setting)
        self.SourcePortText.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SourcePortText.setFont(font)
        self.SourcePortText.setObjectName("SourcePortText")
        self.SourcePortInput = QtWidgets.QLineEdit(PyNAT_Setting)
        self.SourcePortInput.setGeometry(QtCore.QRect(90, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.SourcePortInput.setFont(font)
        self.SourcePortInput.setTabletTracking(False)
        self.SourcePortInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.SourcePortInput.setText("")
        self.SourcePortInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.SourcePortInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SourcePortInput.setObjectName("SourcePortInput")
        self.line = QtWidgets.QFrame(PyNAT_Setting)
        self.line.setGeometry(QtCore.QRect(10, 70, 251, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Tip_text = QtWidgets.QLabel(PyNAT_Setting)
        self.Tip_text.setGeometry(QtCore.QRect(120, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Tip_text.setFont(font)
        self.Tip_text.setObjectName("Tip_text")
        self.SaveButton = QtWidgets.QPushButton(PyNAT_Setting)
        self.SaveButton.setGeometry(QtCore.QRect(80, 330, 75, 23))
        self.SaveButton.setObjectName("SaveButton")
        self.CancelButton = QtWidgets.QPushButton(PyNAT_Setting)
        self.CancelButton.setGeometry(QtCore.QRect(170, 330, 75, 23))
        self.CancelButton.setObjectName("CancelButton")

        self.retranslateUi(PyNAT_Setting)
        QtCore.QMetaObject.connectSlotsByName(PyNAT_Setting)

    def retranslateUi(self, PyNAT_Setting):
        _translate = QtCore.QCoreApplication.translate
        PyNAT_Setting.setWindowTitle(_translate("PyNAT_Setting", "PyNAT 設定"))
        self.SourcePortText.setText(_translate("PyNAT_Setting", "源端口："))
        self.Tip_text.setText(_translate("PyNAT_Setting", "預設源端口為54320"))
        self.SaveButton.setText(_translate("PyNAT_Setting", "保存"))
        self.CancelButton.setText(_translate("PyNAT_Setting", "取消"))

