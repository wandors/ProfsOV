# -*- coding: utf-8 -*-

import WrData
import zlib
import os
import tempfile
import pickle
from datetime import datetime
import Profs_rc
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormN(object):
    pathtemp = tempfile.gettempdir() + "/Proftemp"
    def setupUi(self, FormN):
        self.mains = WrData.Datas()
        FormN.setObjectName("FormN")
        FormN.resize(599, 449)
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        FormN.move((self.resolution.width() / 2) - (FormN.frameSize().width() / 2),
                   (self.resolution.height() / 2) - (FormN.frameSize().height() / 2))
        FormN.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        FormN.activateWindow()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        FormN.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormN.setWindowIcon(icon)
        FormN.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(FormN)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lineEdit_43 = QtWidgets.QLineEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setStyleSheet("")
        self.lineEdit_43.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.gridLayout_10.addWidget(self.lineEdit_43, 3, 1, 1, 2)
        self.label_39 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("")
        self.label_39.setObjectName("label_39")
        self.gridLayout_10.addWidget(self.label_39, 13, 0, 1, 1)
        self.lineEdit_44 = QtWidgets.QLineEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setStyleSheet("")
        self.lineEdit_44.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.gridLayout_10.addWidget(self.lineEdit_44, 4, 1, 1, 2)
        self.label_32 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("")
        self.label_32.setObjectName("label_32")
        self.gridLayout_10.addWidget(self.label_32, 3, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(FormN)
        self.pushButton_10.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setAutoDefault(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_10.addWidget(self.pushButton_10, 20, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet("")
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setMinimumDate(QtCore.QDate(1945, 1, 1))
        self.dateEdit_2.setDate(QtCore.QDate(2001, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout_10.addWidget(self.dateEdit_2, 10, 1, 1, 2)
        self.label_37 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setObjectName("label_37")
        self.gridLayout_10.addWidget(self.label_37, 10, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("")
        self.label_38.setObjectName("label_38")
        self.gridLayout_10.addWidget(self.label_38, 11, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setObjectName("label_31")
        self.gridLayout_10.addWidget(self.label_31, 2, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setObjectName("label_33")
        self.gridLayout_10.addWidget(self.label_33, 4, 0, 1, 1)
        self.dateEdit_3 = QtWidgets.QDateEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setStyleSheet("")
        self.dateEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_3.setMinimumDate(QtCore.QDate(1945, 1, 1))
        self.dateEdit_3.setDate(QtCore.QDate(2016, 1, 3))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.gridLayout_10.addWidget(self.dateEdit_3, 11, 1, 1, 2)
        self.label_34 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setObjectName("label_34")
        self.gridLayout_10.addWidget(self.label_34, 5, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_10.addWidget(self.label_29, 0, 1, 1, 3)
        self.label_36 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setObjectName("label_36")
        self.gridLayout_10.addWidget(self.label_36, 6, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_10.addWidget(self.pushButton_12, 20, 3, 1, 1)
        self.line_11 = QtWidgets.QFrame(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_11.setFont(font)
        self.line_11.setStyleSheet("")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(5)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.gridLayout_10.addWidget(self.line_11, 1, 0, 1, 4)
        self.line_12 = QtWidgets.QFrame(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_12.setFont(font)
        self.line_12.setStyleSheet("")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(6)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.gridLayout_10.addWidget(self.line_12, 18, 0, 1, 4)
        self.dateEdit_4 = QtWidgets.QDateEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_4.setFont(font)
        self.dateEdit_4.setStyleSheet("")
        self.dateEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_4.setMinimumDate(QtCore.QDate(1945, 1, 1))
        self.dateEdit_4.setDate(QtCore.QDate(2017, 1, 1))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.gridLayout_10.addWidget(self.dateEdit_4, 13, 1, 1, 2)
        self.pushButton_11 = QtWidgets.QPushButton(FormN)
        self.pushButton_11.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_10.addWidget(self.pushButton_11, 20, 1, 1, 2)
        self.label_41 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("")
        self.label_41.setObjectName("label_41")
        self.gridLayout_10.addWidget(self.label_41, 15, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setMinimumDate(QtCore.QDate(1925, 1, 1))
        self.dateEdit.setDate(QtCore.QDate(1930, 9, 17))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_10.addWidget(self.dateEdit, 5, 1, 1, 2)
        self.dateEdit_6 = QtWidgets.QDateEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_6.setFont(font)
        self.dateEdit_6.setStyleSheet("")
        self.dateEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_6.setMinimumDate(QtCore.QDate(1945, 1, 1))
        self.dateEdit_6.setDate(QtCore.QDate(2018, 1, 2))
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.gridLayout_10.addWidget(self.dateEdit_6, 15, 1, 1, 2)
        self.dateEdit_5 = QtWidgets.QDateEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_5.setFont(font)
        self.dateEdit_5.setStyleSheet("")
        self.dateEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_5.setMinimumDate(QtCore.QDate(1945, 1, 1))
        self.dateEdit_5.setDate(QtCore.QDate(2017, 1, 1))
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.gridLayout_10.addWidget(self.dateEdit_5, 14, 1, 1, 2)
        self.label_40 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("")
        self.label_40.setObjectName("label_40")
        self.gridLayout_10.addWidget(self.label_40, 14, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("")
        self.label_35.setObjectName("label_35")
        self.gridLayout_10.addWidget(self.label_35, 7, 0, 1, 1)
        self.lineEdit_45 = QtWidgets.QLineEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_45.setFont(font)
        self.lineEdit_45.setStyleSheet("")
        self.lineEdit_45.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.gridLayout_10.addWidget(self.lineEdit_45, 6, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_10.addWidget(self.label_2, 10, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(FormN)
        self.label_28.setStyleSheet("")
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap(":/image/Books2.png"))
        self.label_28.setScaledContents(False)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_10.addWidget(self.label_28, 0, 0, 1, 1)
        self.lineEdit_42 = QtWidgets.QLineEdit(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setStyleSheet("")
        self.lineEdit_42.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.gridLayout_10.addWidget(self.lineEdit_42, 2, 1, 1, 2)
        self.comboBox_5 = QtWidgets.QComboBox(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setStyleSheet("")
        self.comboBox_5.setMaxVisibleItems(12)
        self.comboBox_5.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_5.setDuplicatesEnabled(False)
        self.comboBox_5.setFrame(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_10.addWidget(self.comboBox_5, 7, 1, 1, 2)
        self.label = QtWidgets.QLabel(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/People.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_10.addWidget(self.label, 2, 3, 5, 1)
        self.pushButton_9 = QtWidgets.QPushButton(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_10.addWidget(self.pushButton_9, 7, 3, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(FormN)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setStyleSheet("")
        self.comboBox_6.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_6.setDuplicatesEnabled(False)
        self.comboBox_6.setFrame(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_10.addWidget(self.comboBox_6, 11, 3, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(FormN)
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_10.addWidget(self.checkBox, 13, 3, 3, 1)
        self.verticalLayout.addLayout(self.gridLayout_10)
        self.retranslateUi(FormN)
        self.pushButton_10.clicked.connect(self.Delers)
        self.pushButton_11.clicked.connect(self._saves)
        self.pushButton_12.clicked.connect(lambda: self.closes(FormN))
        self.pushButton_9.clicked.connect(self.filephot)
        self.comboBox_5.activated.connect(self.combo_chosens)
        self.comboBox_6.activated.connect(self.combo_fil)
        self.checkBox.clicked.connect(lambda: self.btnstate(self.checkBox))
        QtCore.QMetaObject.connectSlotsByName(FormN)
        FormN.setTabOrder(self.lineEdit_42, self.lineEdit_43)
        FormN.setTabOrder(self.lineEdit_43, self.lineEdit_44)
        FormN.setTabOrder(self.lineEdit_44, self.dateEdit)
        FormN.setTabOrder(self.dateEdit, self.lineEdit_45)
        FormN.setTabOrder(self.lineEdit_45, self.comboBox_5)
        FormN.setTabOrder(self.comboBox_5, self.dateEdit_2)
        FormN.setTabOrder(self.dateEdit_2, self.dateEdit_3)
        FormN.setTabOrder(self.dateEdit_3, self.dateEdit_4)
        FormN.setTabOrder(self.dateEdit_4, self.dateEdit_5)
        FormN.setTabOrder(self.dateEdit_5, self.dateEdit_6)
        FormN.setTabOrder(self.dateEdit_6, self.pushButton_9)
        FormN.setTabOrder(self.pushButton_9, self.comboBox_6)
        FormN.setTabOrder(self.comboBox_6, self.checkBox)
        FormN.setTabOrder(self.checkBox, self.pushButton_10)
        FormN.setTabOrder(self.pushButton_10, self.pushButton_11)
        FormN.setTabOrder(self.pushButton_11, self.pushButton_12)

    def retranslateUi(self, FormN):
        _translate = QtCore.QCoreApplication.translate
        FormN.setWindowTitle(_translate("FormN", "Редактор профелю"))
        self.label_39.setText(_translate("FormN", "ЗБМ"))
        self.label_32.setText(_translate("FormN", "Іи\'я"))
        self.pushButton_10.setText(_translate("FormN", "Видалити"))
        self.label_37.setText(_translate("FormN", "Початок строку"))
        self.label_38.setText(_translate("FormN", "ДСР"))
        self.label_31.setText(_translate("FormN", "Прізвище"))
        self.label_33.setText(_translate("FormN", "По-батькові"))
        self.label_34.setText(_translate("FormN", "Рік народження"))
        self.label_29.setText(_translate("FormN", "ПРОФІЛЬ"))
        self.label_36.setText(_translate("FormN", "Стаття ККУ"))
        self.pushButton_12.setText(_translate("FormN", "Закрити"))
        self.pushButton_11.setText(_translate("FormN", "Зберегти"))
        self.label_41.setText(_translate("FormN", "Кунець строку"))
        self.label_40.setText(_translate("FormN", "УДЗ"))
        self.label_35.setText(_translate("FormN", "Підстава на облік"))
        self.label_2.setText(_translate("FormN", "Відділення"))
        self.comboBox_5.setItemText(0, _translate("FormN", "Авторитет"))
        self.comboBox_5.setItemText(1, _translate("FormN", "Бандетизм"))
        self.comboBox_5.setItemText(2, _translate("FormN", "Вбивство на замовлення"))
        self.comboBox_5.setItemText(3, _translate("FormN", "Вживання наркотичних речовин"))
        self.comboBox_5.setItemText(4, _translate("FormN", "Виготовлення зброї, вибухових пристроїв"))
        self.comboBox_5.setItemText(5, _translate("FormN", "Вступили в незаконні бандитські угрупування"))
        self.comboBox_5.setItemText(6, _translate("FormN", "Втеча"))
        self.comboBox_5.setItemText(7, _translate("FormN", "Дії що дезорганізують роботу установи"))
        self.comboBox_5.setItemText(8, _translate("FormN", "Захоплення заручників"))
        self.comboBox_5.setItemText(9, _translate("FormN", "Зловживання владою або службовим становищем"))
        self.comboBox_5.setItemText(10, _translate("FormN", "Злодіїв в законі"))
        self.comboBox_5.setItemText(11, _translate("FormN", "Лідер ОЗГ"))
        self.comboBox_5.setItemText(12, _translate("FormN", "Масові заворушення"))
        self.comboBox_5.setItemText(13, _translate("FormN", "Напад"))
        self.comboBox_5.setItemText(14, _translate("FormN", "Наркоділки з міжрегіональними звязками"))
        self.comboBox_5.setItemText(15, _translate("FormN", "Нецільове використання бюджетних коштів"))
        self.comboBox_5.setItemText(16, _translate("FormN", "Організація азартних ігор під матеріалну зацікавленість"))
        self.comboBox_5.setItemText(17, _translate("FormN", "Проти основ національної безпеки"))
        self.comboBox_5.setItemText(18, _translate("FormN", "Резонанс в ЗМІ"))
        self.comboBox_5.setItemText(19, _translate("FormN", "Розв'язування війни"))
        self.comboBox_5.setItemText(20, _translate("FormN", "Службові злочини"))
        self.comboBox_5.setItemText(21, _translate("FormN", "Терористичний акт"))
        self.comboBox_5.setItemText(22, _translate("FormN", "Ухилення від сплати податків"))
        self.comboBox_5.setItemText(23, _translate("FormN", "Отримання неправомірної винагороди"))
        self.comboBox_5.setItemText(24, _translate("FormN", "Шахрайство"))
        self.pushButton_9.setText(_translate("FormN", "Вибрати фото"))
        self.comboBox_6.setItemText(0, _translate("FormN", "1"))
        self.comboBox_6.setItemText(1, _translate("FormN", "2"))
        self.comboBox_6.setItemText(2, _translate("FormN", "3"))
        self.comboBox_6.setItemText(3, _translate("FormN", "4"))
        self.comboBox_6.setItemText(4, _translate("FormN", "5"))
        self.comboBox_6.setItemText(5, _translate("FormN", "6"))
        self.comboBox_6.setItemText(6, _translate("FormN", "7"))
        self.comboBox_6.setItemText(7, _translate("FormN", "8"))
        self.comboBox_6.setItemText(8, _translate("FormN", "9"))
        self.comboBox_6.setItemText(9, _translate("FormN", "ДІЗО"))
        self.comboBox_6.setItemText(10, _translate("FormN", "ДПК"))
        self.comboBox_6.setItemText(11, _translate("FormN", "ДСР"))
        self.comboBox_6.setItemText(12, _translate("FormN", "КДіР"))
        self.comboBox_6.setItemText(13, _translate("FormN", "ПКТ"))
        self.checkBox.setText(_translate("FormN", "Тимчасово\nвибув"))

    def btnstate(self, b):
        if b.isChecked():
            self.out = "withdrawn"
        else:
            self.out = "present"

    def filephot(self):
        self.filesph = QtWidgets.QFileDialog.getOpenFileName(None, "Вибрати фото ...", os.environ['USERPROFILE'] + "/Documents", "Images (*.png *.jpg *.jpeg)")
        self.filesph = self.filesph[0]
        if self.filesph == "":
            self.fp = open(self.pathtemp + "/_zpn.png", "rb")
            self.fpb = self.fp.read()
            self.fp.close()
            self.filez = zlib.compress(self.fpb)
        else:

            self.imag = QtGui.QPixmap(self.filesph)
            self.imagp = self.imag.scaled(QtCore.QSize(135, 130))
            self.imagp.save(self.pathtemp + "/_zpn.png")
            self.label.setPixmap(QtGui.QPixmap(self.pathtemp + "/_zpn.png"))
            self.fp = open(self.pathtemp + "/_zpn.png", "rb")
            self.fpb = self.fp.read()
            self.fp.close()
            self.filez = zlib.compress(self.fpb)


    def combo_chosens(self):
        self.profiless = self.comboBox_5.currentText()
        self.vid = ""
        self.pushButton_9.setEnabled(True)
        self.comboBox_6.setEnabled(True)

    def combo_fil(self):
        self.vid = self.comboBox_6.currentText()
        self.cengbut()

    def _saves(self):
        if not self.checkBox.isChecked():
            self.out = "present"
            self.checkBox.setChecked(False)
        else:
            self.checkBox.setChecked(True)
        try:
            self.fpp = open(self.pathtemp + "/_zpn.png", "rb")
            self.filez = self.fpp.read()
            self.fpp.close()
            self.filez = zlib.compress(self.filez)
        except:
            imageFile = QtCore.QFile(":/image/People.png")
            imageFile.open(QtCore.QIODevice.ReadOnly)
            self.imageData = imageFile.readAll()
            imageFile.close()
            self.fp = open(self.pathtemp + "/_zpn.png", "wb")
            self.fp.write(self.imageData)
            self.fp.close()
            self.fp = open(self.pathtemp + "/_zpn.png", "rb")
            self.fpb = self.fp.read()
            self.fp.close()
            self.filez = zlib.compress(self.fpb)
        try:
            self.pr = self.profiless
        except:
            self.pr = "Авторитет"
        self.mains.params(soname=self.lineEdit_42.text(), name=self.lineEdit_43.text(), father=self.lineEdit_44.text(),
                          birsdey=self.dateEdit.text(), profov=self.pr, stt=self.lineEdit_45.text(),
                          begin_dey=self.dateEdit_2.text(), DSR=self.dateEdit_3.text(), ZBM=self.dateEdit_4.text(),
                          UDZ=self.dateEdit_5.text(), end_dey=self.dateEdit_6.text(), PHOT=self.filez, VID=self.vid, OUTS=self.out)

        self.save_as()

    def save_as(self):
        self.filess = self.pathtemp + "/Profs.dbsp"
        try:
            with open(self.filess, "r") as f:
                self.filest = f.read()
                f.close()
        except(Exception):
            pass
        if self.lineEdit_42.text() != "":
            self.files = self.filest
            if self.files is not "":
                with open(self.filess, "w") as f:
                    f.write(self.files)
                    f.close()
            self.mains.wridata(filer=self.files)
            self.pushButton_11.setEnabled(False)

    def closes(self, forms):
        forms.close()

    def Deletes(self):
        self.pushButton_10.setEnabled(True)
        self.tdbfile = open(self.pathtemp + "/Prof.dbsl", 'rb')
        self.datalists = pickle.load(self.tdbfile)
        if self.datalists[13] == "withdrawn":
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)
        self.tdbfile.close()
        self.lineEdit_42.setText(self.datalists[0])
        self.lineEdit_43.setText(self.datalists[1])
        self.lineEdit_44.setText(self.datalists[2])
        self.lineEdit_45.setText(self.datalists[5])
        self.comboBox_5.setEditText(self.datalists[4])
        self.fzp = zlib.decompress(self.datalists[12])
        self.WrData = WrData.Datas()
        self.fpp = open(self.pathtemp + "/_zpn.png", "wb")
        self.fpp.write(self.fzp)
        self.fpp.close()
        self.label.setPixmap(QtGui.QPixmap(self.pathtemp + "/_zpn.png"))
        if self.datalists[3] == "":
            self.datalists[3] = "17.09.1930"
        self.year = datetime.strptime(self.datalists[3], '%d.%m.%Y').date()
        self.dateEdit.setDate(self.year)
        if self.datalists[6] == "":
            self.datalists[6] = "01.01.2001"
        self.year = datetime.strptime(self.datalists[6], '%d.%m.%Y').date()
        self.dateEdit_2.setDate(self.year)
        if self.datalists[7] == "":
            self.datalists[7] = "03.01.2016"
        self.year = datetime.strptime(self.datalists[7], '%d.%m.%Y').date()
        self.dateEdit_3.setDate(self.year)
        if self.datalists[8] == "":
            self.datalists[8] = "01.01.2017"
        self.year = datetime.strptime(self.datalists[8], '%d.%m.%Y').date()
        self.dateEdit_4.setDate(self.year)
        if self.datalists[9] == "":
            self.datalists[9] = "01.01.2017"
        self.year = datetime.strptime(self.datalists[9], '%d.%m.%Y').date()
        self.dateEdit_5.setDate(self.year)
        if self.datalists[10] == "":
            self.datalists[10] = "02.01.2018"
        self.year = datetime.strptime(self.datalists[10], '%d.%m.%Y').date()
        self.dateEdit_6.setDate(self.year)

    def Delers(self):
        self.WrDel = WrData.Datas()
        self.WrDel.Deleter(_prf=self.datalists)
        self.pushButton_10.setEnabled(False)
        self.lineEdit_42.setText("")
        self.lineEdit_43.setText("")
        self.lineEdit_44.setText("")
        self.lineEdit_45.setText("")
        self.comboBox_5.setEditText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/People.png"))
        self.year = datetime.strptime("01.01.2017", '%d.%m.%Y').date()
        self.dateEdit.setDate(self.year)
        self.year = datetime.strptime("01.01.2017", '%d.%m.%Y').date()
        self.dateEdit_2.setDate(self.year)
        self.year = datetime.strptime("01.01.2017", '%d.%m.%Y').date()
        self.dateEdit_3.setDate(self.year)
        self.year = datetime.strptime("01.01.2017", '%d.%m.%Y').date()
        self.dateEdit_4.setDate(self.year)
        self.year = datetime.strptime("01.01.2017", '%d.%m.%Y').date()
        self.dateEdit_5.setDate(self.year)
        self.year = datetime.strptime("01.01.2017", '%d.%m.%Y').date()
        self.dateEdit_6.setDate(self.year)
        self.pushButton_11.setEnabled(False)

    def cengbut(self):
        if self.lineEdit_42.text() == "" or self.lineEdit_43.text() == "" or self.lineEdit_44.text() == "":
            self.pushButton_11.setEnabled(False)
        else:
            self.pushButton_11.setEnabled(True)
