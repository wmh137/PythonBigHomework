# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\#2019-1-Spring\Python\Pythonbighomework\PythonBigHomework\gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 630)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(140, 70, 840, 105))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(665, 35, 140, 35))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(105, 35, 210, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 35, 210, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(35, 35, 70, 35))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(350, 35, 70, 35))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "搜索"))
        self.label.setText(_translate("Form", "出发点"))
        self.label_2.setText(_translate("Form", "目的地"))

