# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 630)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(70, 70, 980, 105))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(840, 35, 105, 35))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(105, 35, 210, 35))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 35, 210, 35))
        font = QtGui.QFont()
        font.setFamily("等线")
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
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(700, 35, 105, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 600, 1110, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 590, 1120, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 245, 980, 280))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(140, 70, 700, 70))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 210, 140, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(35, 35, 70, 140))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(875, 35, 70, 140))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(445, 170, 30, 30))
        font = QtGui.QFont()
        font.setFamily("DengXian")
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(475, 170, 30, 30))
        font = QtGui.QFont()
        font.setFamily("ISOCP")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(505, 170, 30, 30))
        font = QtGui.QFont()
        font.setFamily("DengXian")
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('icon/icon.jpg'))

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.route)
        self.lineEdit.textChanged.connect(Form.statusrefresh)
        self.lineEdit_2.textChanged.connect(Form.statusrefresh)
        self.comboBox.currentIndexChanged.connect(Form.statusrefresh)
        self.pushButton_2.clicked.connect(Form.navig)
        self.pushButton_3.clicked.connect(Form.before)
        self.pushButton_4.clicked.connect(Form.after)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle('I will lead you')
        self.pushButton.setText(_translate("Form", "路径规划"))
        self.label.setText(_translate("Form", "出发点"))
        self.label_2.setText(_translate("Form", "目的地"))
        self.comboBox.setItemText(0, _translate("Form", "步行"))
        self.comboBox.setItemText(1, _translate("Form", "驾车"))
        self.comboBox.setItemText(2, _translate("Form", "公交"))
        self.comboBox.setItemText(3, _translate("Form", "骑行"))
        self.label_3.setText(_translate("Form", "Ready!"))
        self.pushButton_2.setText(_translate("Form", "开始导航"))
        self.pushButton_3.setText(_translate("Form", "<"))
        self.pushButton_4.setText(_translate("Form", ">"))

