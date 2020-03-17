# -*- coding: utf-8 -*-iltins

__author__ = "Сергій Полунець"
__versions__ = "v.3.5.6.1"

import argparse
import datetime
import os
import pickle
import shutil
import sys
import tempfile
import time
import zlib
import operator
import Profs_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import WrData
from FormNM import Ui_FormN
from zvits import Window


class Ui_Form(object):
    if not os.path.exists(tempfile.gettempdir() + "\Proftemp"):
        os.mkdir(tempfile.gettempdir() + "\Proftemp")
    pathtemp = tempfile.gettempdir() + "\Proftemp"

    def setupUi(self, Form, path):
        self.files = path
        with open(self.pathtemp + "/Profs.dbsp", "w") as f:
            f.write(str(self.files))
            f.close()
        if not os.path.exists(self.files):
            self.f = open(self.files, "wb")
            self.f.close()
        Form.setObjectName("Form")
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        Form.resize(1120, 650)
        Form.move((self.resolution.width() / 2) - (Form.frameSize().width() / 2),
                  (self.resolution.height() / 2) - (Form.frameSize().height() / 2))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 3)
        self.label_13 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 5, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 14, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 18, 0, 1, 10)
        self.label_20 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_20.setLineWidth(2)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(":/image/Books.png"))
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 14, 5, 1, 2)
        self.comboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 6)
        self.label_14 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 10, 5, 1, 2)
        self.line_10 = QtWidgets.QFrame(Form)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 6, 7, 9, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_2.setFont(font)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 10)
        self.label_10 = QtWidgets.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 5, 1, 2)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setMinimumSize(QtCore.QSize(345, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(3)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.showItem)
        self.gridLayout.addWidget(self.listWidget, 4, 0, 12, 2)
        self.line_9 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_9.setFont(font)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(5)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 6, 9, 9, 1)
        self.label_15 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 11, 5, 1, 2)
        self.label_11 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 5, 1, 2)
        self.line_8 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_8.setFont(font)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 6, 4, 9, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 13, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 5, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 12, 3, 1, 1)
        self.line_6 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_6.setFont(font)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(5)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 6, 2, 9, 1)
        self.line_5 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_5.setFont(font)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 5, 2, 1, 8)
        self.line_4 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_4.setFont(font)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 3, 0, 1, 10)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 5, 1, 1)
        self.line_7 = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_7.setFont(font)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(5)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 15, 2, 1, 8)
        self.line = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 16, 0, 1, 10)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 6, 1, 4)
        self.label_16 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 12, 5, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 13, 5, 1, 2)
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 6, 8, 1, 1)
        self.label_23 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_23.setFont(font)
        self.label_23.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 11, 8, 1, 1)
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/image/People.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 7, 8, 4, 1)
        self.label_19 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 1, 1, 9)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 6, 1, 4)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.gridLayout.addWidget(self.pushButton_5, 17, 5, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 17, 6, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 17, 7, 1, 3)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 17, 2, 1, 3)
        self.label_21 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 17, 0, 1, 2)
        self.label_24 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_24.setFont(font)
        self.label_24.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 12, 8, 1, 1)
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 13, 8, 2, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(self.Loadeds)
        self.pushButton.clicked.connect(self.RewProf)
        self.pushButton_2.clicked.connect(self.EditProf)
        self.pushButton_3.clicked.connect(self.SavProfs)
        self.pushButton_5.clicked.connect(self.Exports)
        self.pushButton_6.clicked.connect(self.Zvit)
        self.pushButton_7.clicked.connect(self.Exitss)
        self.pushButton_8.clicked.connect(self.Pilgi)
        self.comboBox.activated.connect(self.combo_chosen)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox, self.pushButton_4)
        Form.setTabOrder(self.pushButton_4, self.listWidget)
        Form.setTabOrder(self.listWidget, self.pushButton)
        Form.setTabOrder(self.pushButton, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton_3)
        Form.setTabOrder(self.pushButton_3, self.pushButton_8)
        Form.setTabOrder(self.pushButton_8, self.pushButton_5)
        Form.setTabOrder(self.pushButton_5, self.pushButton_6)
        Form.setTabOrder(self.pushButton_6, self.pushButton_7)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.clearform()
        Form.setWindowTitle(_translate("Form", "База профілактичного обліку " + __versions__))
        self.label_4.setText(_translate("Form", "Підстава на облік"))
        self.pushButton.setText(_translate("Form", "Створити новий"))
        self.label_3.setText(_translate("Form", "Рік народження"))
        self.label_6.setText(_translate("Form", "ДСР"))
        self.label_2.setText(_translate("Form", "Стаття КК України"))
        self.label_5.setText(_translate("Form", "Початок строку"))
        self.label_9.setText(_translate("Form", "Кінець строку"))
        self.comboBox.setItemText(0, _translate("Form", "Всі підоблікові"))
        self.comboBox.setItemText(1, _translate("Form", "Авторитет"))
        self.comboBox.setItemText(2, _translate("Form", "Бандетизм"))
        self.comboBox.setItemText(3, _translate("Form", "Вбивство на замовлення")) # ч2 cn 115
        self.comboBox.setItemText(4, _translate("Form", "Вживання наркотичних речовин"))
        self.comboBox.setItemText(5, _translate("Form", "Виготовлення зброї, вибухових пристроїв"))
        self.comboBox.setItemText(6, _translate("Form", "Вступили в незаконні бандитські угрупування")) # ст.260
        self.comboBox.setItemText(7, _translate("Form", "Втеча"))
        self.comboBox.setItemText(8, _translate("Form", "Дії що дезорганізують роботу установи"))
        self.comboBox.setItemText(9, _translate("Form", "Захоплення заручників"))
        self.comboBox.setItemText(10, _translate("Form", "Зловживання владою або службовим становищем")) #ч.2 ст. 364
        self.comboBox.setItemText(11, _translate("Form", "Злодіїв в законі"))
        self.comboBox.setItemText(12, _translate("Form", "Лідер ОЗГ"))
        self.comboBox.setItemText(13, _translate("Form", "Масові заворушення")) #ст.330
        self.comboBox.setItemText(14, _translate("Form", "Напад"))
        self.comboBox.setItemText(15, _translate("Form", "Наркоділки з міжрегіональними звязками")) #ст.305
        self.comboBox.setItemText(16, _translate("Form", "Нецільове використання бюджетних коштів"))  # ч.2 ст.210
        self.comboBox.setItemText(17, _translate("Form", "Організація азартних ігор під матеріалну зацікавленість"))
        self.comboBox.setItemText(18, _translate("Form", "Проти основ національної безпеки"))
        self.comboBox.setItemText(19, _translate("Form", "Резонанс в ЗМІ"))
        self.comboBox.setItemText(20, _translate("Form", "Розв'язування війни"))# ст.437
        self.comboBox.setItemText(21, _translate("Form", "Службові злочини"))# ч.5 ст.191
        self.comboBox.setItemText(22, _translate("Form", "Тероризм"))# ст.258-ст.258\5
        self.comboBox.setItemText(23, _translate("Form", "У сфері державної таємниці"))# ч.2 ч.3 ст.368
        self.comboBox.setItemText(24, _translate("Form", "Ухилення від сплати податків")) # ч.2 ч.3 ст.212
        self.comboBox.setItemText(25, _translate("Form", "Шахрайство"))# ч.4 ст.190
        self.label_8.setText(_translate("Form", "УДЗ"))
        self.label_12.setText(_translate("Form", "Зловживання владою або службовим становищем"))
        self.label_7.setText(_translate("Form", "ЗБМ"))
        self.pushButton_2.setText(_translate("Form", "Редагувати"))
        self.pushButton_4.setText(_translate("Form", "Завантажити"))
        self.label.setText(_translate("Form", "П.І.Б."))
        self.label_25.setText(_translate("Form", "ФОТО"))
        self.label_23.setText(_translate("Form", "Відділення"))
        self.label_19.setText(_translate("Form", "Профілактичний облік"))
        self.pushButton_3.setText(_translate("Form", "Зберегти як"))
        self.pushButton_5.setText(_translate("Form", "Список"))
        self.pushButton_6.setText(_translate("Form", "Звіт"))
        self.pushButton_7.setText(_translate("Form", "Контроль"))
        self.label_26.setText(_translate("Form", "Тимчасово вибув з кстанови"))
        if len(self.files) > 45:
            self.files = "{0}...{1}".format(self.files[:25], self.files[len(self.files) - 20:])
        self.label_21.setText("{0}".format(self.files))
        self.pushButton_8.setText(_translate("Form", "Пільги"))
        self.clearform()


    def Loadeds(self):
        self.files = QtWidgets.QFileDialog.getOpenFileName(Form, "Завантажити базу ...", os.environ['USERPROFILE'],
                                                           "dbs (*dbs)")
        self.files = self.files[0]
        if self.files == "":
            self.ff = open(self.pathtemp + "/Profs.dbsp", "r")
            self.files = self.ff.read()
            self.ff.close()
        else:
            self.ff = open(self.pathtemp + "/Profs.dbsp", "w")
            self.ff.write(str(self.files))
            self.ff.close()
            self.listWidget.clear()
            self.clearform()
        self.pushButton_2.setEnabled(False)
        if len(self.files) > 45:
            self.files = "{0}...{1}".format(self.files[:25], self.files[len(self.files) - 20:])
        self.label_21.setText("{0}".format(self.files))

    def SavProfs(self):
        self.files = QtWidgets.QFileDialog.getSaveFileName(Form, "Зберегти дані", os.environ['USERPROFILE'],
                                                           "dbs files (*.dbs)")

        self.files = self.files[0]
        if self.files == "":
            self.ff = open(self.pathtemp + "/Profs.dbsp", "r")
            self.files = self.ff.read()
            self.ff.close()
        else:
            self.ff = open(self.pathtemp + "/Profs.dbsp", "r")
            self.ffpath = self.ff.read()
            self.ff.close()
            shutil.copy(self.ffpath, self.files)
        self.pushButton_2.setEnabled(False)

    def combo_chosen(self):
        self.listWidget.itemClicked.connect(self.showItem)
        self.listsp = []
        self.listWidget.clear()
        self.clearform()
        try:
            self.texts = self.comboBox.currentText()
            self.textsp = self.texts
            self.ff = open(self.pathtemp + "\\Profs.dbsp", "r")
            self.files = self.ff.read()
            self.ff.close()
            WrData.Datas().ClearDB(files=self.files)
            self.dats = WrData.Datas().reddata(files=self.files)
            self.lispr = self.dats
            self.pushButton_2.setEnabled(False)
            self.pushButton_5.setEnabled(True)
            self.pushButton_6.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.pushButton_7.setEnabled(True)
            try:
                self.xPro = True
                self.namepr = self.dats[self.texts]
                for i in self.namepr.keys():
                    self.listsp.append(i)
                    self.iss = self.namepr.keys()
                self.listsp.sort()
                for i in range(len(self.listsp)):
                    item = QtWidgets.QListWidgetItem()
                    self.listWidget.addItem(item)
                    __sortingEnabled = self.listWidget.isSortingEnabled()
                    self.listWidget.setSortingEnabled(False)
                    item = self.listWidget.item(i)
                    item.setText("{0} {1}".format(i + 1, self.listsp[i]))
                    self.listWidget.setSortingEnabled(__sortingEnabled)
            except:
                if self.texts == "Всі підоблікові":
                    self.xPro = False
                    self.proers = self.dats
                    self.lise = []
                    for i in self.proers.values():
                        for ig in i.items():
                            self.lise.append(ig)
                    map(operator.itemgetter(0), self.lise)
                    self.xlis = sorted(self.lise, key=operator.itemgetter(0))
                    for i in self.proers:
                        self.i = self.proers.get(i)
                        for ii in self.i:
                            self.listsp.append(ii)
                    self.listsp.sort()
                    for i in range(len(self.listsp)):
                        item = QtWidgets.QListWidgetItem()
                        self.listWidget.addItem(item)
                        __sortingEnabled = self.listWidget.isSortingEnabled()
                        self.listWidget.setSortingEnabled(False)
                        item = self.listWidget.item(i)
                        item.setText("{0} {1}".format(i + 1, self.listsp[i]))
                        self.listWidget.setSortingEnabled(__sortingEnabled)
        except:
            pass

    def showItem(self, item):
        self.sles = item.isSelected()
        self.item = item.text()
        self.itemin = self.item.find(" ")
        if self.xPro == True:
            self.item = self.item[self.itemin + 1:]
            for ai in self.lispr:
                self.i = self.lispr.get(ai)
                for ip in self.i:
                    if ip == self.item:
                        self.priis = self.i.setdefault(ip)
        if self.xPro == False:
            self.item = self.item[0:self.itemin]
            self.priis = self.xlis[int(self.item) - 1][1]
            self.textsp = str("{0}".format(self.priis['profov']))
        self._soname = str("{0}".format(self.priis['soname']))
        self._name = str("{0}".format(self.priis['name']))
        self._father = str("{0}".format(self.priis['father']))
        self._brsd = str("{0}".format(self.priis['birsdey']))
        self._profer = str(self.textsp)
        self._sttu = str("{0}".format(self.priis['stt']))
        self._begistr = str("{0}".format(self.priis['begin_dey']))
        self._dsr = str("{0}".format(self.priis['DSR']))
        self._zbm = str("{0}".format(self.priis['ZBM']))
        self._udz = str("{0}".format(self.priis['UDZ']))
        self._endstr = str("{0}".format(self.priis['end_dey']))
        try:
            self._outs = str("{0}".format(self.priis['OUTS']))
            if self._outs == "present":
                self.label_26.setText("")
            else:
                self.label_26.setText("Тимчасово вибув з установи")
        except:
            self.label_26.setText("")
        self._vids = str("{0}".format(self.priis['VID']))
        self.label_24.setText(self._vids)
        self.photozl = self.priis['PHOT']
        self._photof = zlib.decompress(self.photozl)
        self.df = open(self.pathtemp + "/_zpn.png", "wb")
        self.df.write(self._photof)
        self.df.close()
        self.fpho = self.pathtemp + "/_zpn.png"
        self.label_10.setText("{0} {1} {2}".format(self._soname, self._name, self._father))
        self.pushButton_2.setEnabled(True)
        self.label_11.setText(self._brsd)
        self.label_12.setText(self._profer)
        self.label_13.setText(self._sttu)
        self.label_14.setText(self._begistr)
        self.label_15.setText(self._dsr)
        self.label_16.setText(self._zbm)
        self.label_17.setText(self._udz)
        self.label_18.setText(self._endstr)
        self.label_22.setPixmap(QtGui.QPixmap(self.fpho))

    def RewProf(self):
        imageFile = QtCore.QFile(":/image/People.png")
        imageFile.open(QtCore.QIODevice.ReadOnly)
        self.imageData = imageFile.readAll()
        imageFile.close()
        self.fp = open(self.pathtemp + "/_zpn.png", "wb")
        self.fp.write(self.imageData)
        self.fp.close()
        self.FormNN = QtWidgets.QDialog()
        self.uiN = Ui_FormN()
        self.FormNN.setWindowModality(QtCore.Qt.ApplicationModal)
        self.uiN.setupUi(self.FormNN)
        self.FormNN.show()

    def EditProf(self):
        self.WrData = WrData.Datas()
        self.fp = open(self.pathtemp + "/_zpn.png", "rb")
        self.fpb = self.fp.read()
        self.fp.close()
        self.filez = zlib.compress(self.fpb)
        try:
            self._vids = self._vids
        except:
            self._vids = ""
        if self.label_26.text() == "Тимчасово вибув з установи":
            self._out = "withdrawn"
        else:
            self._out = "present"
        self.WrData.Editers(_soname=self._soname, _name=self._name, _father=self._father, _birsdey=self._brsd,
                            _profov=self._profer, _stt=self._sttu, _begin_dey=self._begistr, _DSR=self._dsr,
                            _ZBM=self._zbm, _UDZ=self._udz, _end_dey=self._endstr, _VID=self._vids, _PHOT=self.filez,
                            _OUTS=self._out)
        self.FormNN = QtWidgets.QWidget()
        self.FormNN.setWindowModality(QtCore.Qt.ApplicationModal)
        self.uiN = Ui_FormN()
        self.uiN.setupUi(self.FormNN)
        self.uiN.Deletes()
        self.FormNN.show()
        self.pushButton_2.setEnabled(False)
        self.clearform()
        self.listWidget.clear()

    def clearform(self):
        self.label_12.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_15.setText("")
        self.label_14.setText("")
        self.label_13.setText("")
        self.label_17.setText("")
        self.label_16.setText("")
        self.label_18.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/image/People.png"))
        self.label_24.setText("")
        self.label_26.setText("")

    def Exitss(self):
        self._Control()

    def Exports(self):
        self.temfil = self.pathtemp + "/_temp.html"
        self.sefi = open(self.temfil, 'w')
        self.sefi.write("<!DOCTYPE html>")
        self.sefi.write("<html lang=\"en\">")
        self.sefi.write("<head>")
        self.sefi.write("\t<meta charset=\"windows-1251\">")
        self.sefi.write("</head>")
        self.sefi.write("<body>")
        self.sefi.write(
            "\t<h1 align=\"center\"> <font size=\"18\">Список підоблікових осіб станом {0}р.</font> </h1>".format(
                time.strftime("%d.%m.%Y")))
        self.proers = self.dats
        for ai in self.proers:
            self.i = self.lispr.get(ai)
            if ai == self.texts:
                self.sefi.write("\t<p align=\"left\"><font size=\"6\">* {0}</font> </p>".format(str(self.texts)))
                for ip in self.i:
                    self.priis = self.i.setdefault(ip)
                    self._soname = str("{0}".format(self.priis['soname']))
                    self._name = str("{0}".format(self.priis['name']))
                    self._father = str("{0}".format(self.priis['father']))
                    self._endstr = str("{0}".format(self.priis['end_dey']))
                    self._brsd = str("{0}".format(self.priis['birsdey']))
                    try:
                        self._vids = str("{0}".format(self.priis['VID']))
                        try:
                            self._vides = "Відділення № " + str(int(self._vids))
                        except:
                            self._vides = self._vids
                    except:
                        self._vids = ""
                    if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                        self.wisitse = "ТИМЧАСОВО ВИБУВ З УСТАНОВИ"
                    else:
                        self.wisitse = ""
                    self.sefi.write(
                        "\t<p align=\"left\"><font size=\"5\">- {0} {1} {2}, {3} р. н.  {4} {5}</font> </p>".format(
                            self._soname, self._name, self._father, self._brsd, self._vides, self.wisitse))

        for i in self.proers:
            if self.texts == "Всі підоблікові":
                self.i = self.proers.get(i)
                if self.i.__len__() > 0:
                    self.sefi.write("\t<p align=\"left\"><font size=\"6\"><b>* {0}</b></font> </p>".format(str(i)))
                for ia in self.i:
                    self.priis = self.i.setdefault(ia)
                    self._soname = str("{0}".format(self.priis['soname']))
                    self._name = str("{0}".format(self.priis['name']))
                    self._father = str("{0}".format(self.priis['father']))
                    self._endstr = str("{0}".format(self.priis['end_dey']))
                    self._brsd = str("{0}".format(self.priis['birsdey']))
                    try:
                        self._vids = str("{0}".format(self.priis['VID']))
                        try:
                            self._vides = "Відділення № " + str(int(self._vids))
                        except:
                            self._vides = self._vids
                    except:
                        self._vids = ""
                    if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                        self.wisitse = "ТИМЧАСОВО ВИБУВ З УСТАНОВИ"
                    else:
                        self.wisitse = ""
                    self.sefi.write(
                        "\t<p align=\"left\"><font size=\"5\">- {0} {1} {2}, {3} р. н.  {4} "
                        "</font> <font color=\"red\" font size=\"4\" ><b>{5}</b></font></p>".format(
                            self._soname, self._name, self._father, self._brsd, self._vides, self.wisitse))
        self.sefi.close()
        self.uiN = Window("Список підоблікових")
        self.uiN.handleOpen()
        self.uiN.show()

    def Zvit(self):
        self.numint = 0
        self.oth = 0
        self.timuot = 0
        self.ablist = []
        self.band = []
        self.kiler = []
        self.separ = []
        self.lider = []
        self.protiv = []
        self.slugba = []
        self.avtoritet = []
        self.narcdil = []
        self.teror = []
        self.zaruch = []
        self.zlod = []
        self.vlada = []
        self.mzavor = []
        self.kosht = []
        self.zmi = []
        self.wars = []
        self.podat = []
        self.viag = []
        self.temfil = self.pathtemp + "/_temp.html"
        self.sefi = open(self.temfil, 'w')
        self.sefi.write("<!DOCTYPE html>")
        self.sefi.write("<html lang=\"en\">")
        self.sefi.write("<head>")
        self.sefi.write("\t<meta charset=\"windows-1251\">")
        self.sefi.write("</head>")
        self.sefi.write("<body>")
        self.ffs = open(self.pathtemp + "/Profs.dbsp", "r")
        self.filess = self.ffs.read()
        self.ffs.close()
        try:
            self.opfils = open(self.filess, "rb")
            self.datas = pickle.load(self.opfils)
            self.opfils.close()
            self.proerss = self.datas
            for i in self.proerss:
                self.i = self.proerss.get(i)
                for ii in self.i:
                    self.ablist.append(ii)
            self.all = len(self.ablist)
            self.allss = len(list(set(self.ablist)))
            for i in self.proerss:
                self.i = self.proerss.get(i)
                for ip in self.i:
                    self.priis = self.i.setdefault(ip)
                    if str("{0}".format(self.priis['profov'])) == "Втеча" \
                        or str("{0}".format(self.priis['profov'])) == "Напад" \
                        or str("{0}".format(self.priis['profov'])) == "Вживання наркотичних речовин" \
                        or str("{0}".format(self.priis['profov'])) == "Дії що дезорганізують роботу установи" \
                        or str("{0}".format(self.priis['profov'])) == "Виготовлення зброї, вибухових пристроїв" \
                        or str("{0}".format(
                        self.priis['profov'])) == "Організація азартних ігор під матеріалну зацікавленість":
                        self.numint += 1
            for i in self.proerss:
                self.i = self.proerss.get(i)
                for ip in self.i:
                    self.priis = self.i.setdefault(ip)
                    self._soname = str("{0}".format(self.priis['soname']))
                    if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                        self.oth += 1
            for i in self.proerss:
                if i == "Авторитет":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.avtoritet.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Бандетизм":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.band.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Вбивство на замовлення":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.kiler.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Службові злочини":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.slugba.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Вступили в незаконні бандитські угрупування":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.separ.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Лідер ОЗГ":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.lider.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Проти основ національної безпеки":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.protiv.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Наркоділки з міжрегіональними звязками":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.narcdil.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Тероризм":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.teror.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Захоплення заручників":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.zaruch.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Зловживання владою або службовим становищем":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.vlada.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Злодіїв в законі":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.zlod.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Масові заворушення":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.mzavor.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Нецільове використання бюджетних коштів":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.kosht.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Резонанс в ЗМІ":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.zmi.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Розв'язування війни":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.wars.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Ухилення від сплати податків":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.podat.append(self._soname)
                    if len(self.i) == 0:
                        pass
                if i == "Отримання неправомірної винагороди":
                    self.i = self.proerss.get(i)
                    for ip in self.i:
                        self.priis = self.i.setdefault(ip)
                        self._soname = str("{0}".format(self.priis['soname']))
                        if str("{0}".format(self.priis['OUTS'])) == "withdrawn":
                            self.timuot += 1
                        else:
                            self.viag.append(self._soname)
                    if len(self.i) == 0:
                        pass
            self.al = self.all - self.oth
            self.oz = self.numint
            self.avt = len(self.avtoritet)
            self.ban = len(self.band)
            self.kil = len(self.kiler)
            self.sep = len(self.separ)
            self.lid = len(self.lider)
            self.prot = len(self.protiv)
            self.narc = len(self.narcdil)
            self.slu = len(self.slugba)
            self.ter = len(self.teror)
            self.zar = len(self.zaruch)
            self.vlad = len(self.vlada)
            self.zlo = len(self.zlod)
            self.mzav = len(self.mzavor)
            self.kosh = len(self.mzavor)
            self.zmii = len(self.zmi)
            self.war = len(self.wars)
            self.pod = len(self.podat)
            self.vin = len(self.viag)
            self.OSK = (self.avt + self.ban + self.kil + self.sep + self.lid + self.prot +
                        self.narc + self.ter + self.zar + self.vlad + self.zlo + self.mzav +
                        self.kosh + self.zmii + self.war + self.pod + self.vin + self.slu)
            self.sefi.write("\t<h1 align=\"center\"> <font size=\"18\">Звіт ствном на {0}р.</font> </h1>".format(
                time.strftime("%d.%m.%Y")))
            self.sefi.write(
                "\t<p align=\"left\"><font size=\"6\">* Всіх на обліку: {0}</font> </p>".format(
                    str(self.allss - self.oth)))
            self.sefi.write(
                "\t<p align=\"left\"><font size=\"6\">* На обліку ОСК: {0}</font> </p>".format(str(self.OSK)))
            self.sefi.write("\t<p align=\"left\"><font size=\"6\">* Інші підоблікові: {0}</font> </p>".format(
                ((self.allss - self.oth) - self.OSK)))
            self.sefi.close()
            self.uiN = Window("Звіт по підобліовим")
            self.uiN.handleOpen()
            self.uiN.show()
        except:
            self.sefi.write("\t<h1 align=\"center\"> <font size=\"18\">Звіт ствном на {0}р.</font> </h1>".format(
                time.strftime("%d.%m.%Y")))
            self.sefi.close()
            self.uiN = Window("Звіт по підобліовим")
            self.uiN.handleOpen()
            self.ZvN.show()

    def Pilgi(self):
        self.temfil = self.pathtemp + "/_temp.html"
        self.sefi = open(self.temfil, 'w')
        self.sefi.write("<!DOCTYPE html>")
        self.sefi.write("<html lang=\"en\">")
        self.sefi.write("<head>")
        self.sefi.write("\t<meta charset=\"windows-1251\">")
        self.sefi.write("</head>")
        self.sefi.write("<body>")
        self.monslist = ["січень", "лютий", "березень", "квітень",
                         "травень", "червень", "липень", "серпень",
                         "вересень", "жовтень", "листопад", "грудень"]
        self.chemon = int(time.strftime('%m')) % 2
        if self.chemon == 0:
            self.inmon = 31
            if int(time.strftime('%m')) > 9:
                self.inmon = 30
        else:
            self.inmon = 30
            if int(time.strftime('%m')) == 1:
                self.inmon = 28
            if int(time.strftime('%m')) == 7:
                self.inmon = 31
        if 12 == int(time.strftime('%m')):
            self.neztm = int(time.strftime('%m')) + 1
            if self.neztm == 13:
                self.neztm = 1
                self.mone = self.monslist[self.neztm - 1]
                self.years = int(time.strftime('%Y'))
            for self.i in range(0, len(self.monslist)):
                if self.i + 1 == int(time.strftime("%m")):
                    self.mun = self.monslist[self.i]
        else:
            self.mone = int(time.strftime('%m')) + 1
            self.years = int(time.strftime('%Y'))
            for self.i in range(0, len(self.monslist)):
                if self.i + 1 == int(time.strftime("%m")):
                    self.mun = self.monslist[self.i]
        self.sefi.write("\t<h1 align=\"center\"> <font size=\"18\">Матеріали на {0} {1}p.</font> </h1>".format(self.mun,
                                                                                                               str(
                                                                                                                   self.years)))
        self.ff = open(self.pathtemp + "/Profs.dbsp", "r")
        self.files = self.ff.read()
        self.ff.close()
        self.dats = WrData.Datas().reddata(files=self.files)
        self.lispr = self.dats
        for ai in self.lispr:
            self.i = self.lispr.get(ai)
            for ip in self.i:
                self.priis = self.i.setdefault(ip)
                self._dsr = str("{0}".format(self.priis['DSR']))
                if self._dsr == "":
                    self._dsr = "03.01.2016"
                self._zbm = str("{0}".format(self.priis['ZBM']))
                if self._zbm == "":
                    self._zbm = "01.01.2017"
                self._udz = str("{0}".format(self.priis['UDZ']))
                if self._udz == "":
                    self._udz = "01.01.2017"
                self.tdsr = datetime.datetime(int(self._dsr[6:]), int(self._dsr[3:5]), int(self._dsr[:2]), 0, 0)
                self.timuot_dsr = time.mktime(self.tdsr.timetuple())
                self.tzbm = datetime.datetime(int(self._zbm[6:]), int(self._zbm[3:5]), int(self._zbm[:2]), 0, 0)
                self.timuot_zbm = time.mktime(self.tzbm.timetuple())
                self.tudz = datetime.datetime(int(self._udz[6:]), int(self._udz[3:5]), int(self._udz[:2]), 0, 0)
                self.timuot_udz = time.mktime(self.tudz.timetuple())
                if 12 == int(time.strftime('%m')):
                    self.neztm = int(time.strftime('%m')) + 1
                    if self.neztm == 13:
                        self.neztm = 1
                        self.years = int(time.strftime('%Y')) + 1
                        self.dt = datetime.datetime(self.years, self.neztm, 1, 0, 0)
                        self.seconds = self.dt.timestamp()
                        self.dt = datetime.datetime(self.years, self.neztm, self.inmon, 0, 0)
                        self.seconds_next = self.dt.timestamp()
                elif 8 == int(time.strftime('%m')):
                    self.neztm = 9
                    self.inmon = 30
                    self.dt = datetime.datetime(self.years, self.neztm, 1, 0, 0)
                    self.seconds = self.dt.timestamp()
                    self.dt = datetime.datetime(self.years, self.neztm, self.inmon, 0, 0)
                    self.seconds_next = self.dt.timestamp()
                else:
                    self.dt = datetime.datetime(int(time.strftime('%Y')), int(time.strftime('%m')) + 1, 1, 0, 0)
                    self.seconds = self.dt.timestamp()
                    self.years = int(time.strftime('%Y'))
                    self.neztm = int(time.strftime('%m')) + 1
                    self.dt = datetime.datetime(self.years, self.neztm, self.inmon, 0, 0)
                    self.seconds_next = self.dt.timestamp()
                self._soname = str("{0}".format(self.priis['soname']))
                self._name = str("{0}".format(self.priis['name']))
                self._father = str("{0}".format(self.priis['father']))
                if self.seconds <= self.timuot_dsr <= self.seconds_next:
                    self.run_0 = "<b>-</b><b> ДСР</b> {3} {0} {1} {2}\n".format(self._soname, self._name, self._father,
                                                                                self._dsr)
                    self.sefi.write("\t<p align=\"left\"><font size=\"5\"> {0}</font> </p>".format(str(self.run_0)))
                if self.seconds <= self.timuot_zbm <= self.seconds_next:
                    self.run_1 = "<b>-</b><b> ЗБМ</b> {3} {0} {1} {2}\n".format(self._soname, self._name, self._father,
                                                                                self._zbm)
                    self.sefi.write("\t<p align=\"left\"><font size=\"5\"> {0}</font> </p>".format(str(self.run_1)))
                if self.seconds <= self.timuot_udz <= self.seconds_next:
                    self.run_2 = "<b>-</b><b> УДЗ</b> {3} {0} {1} {2}\n".format(self._soname, self._name, self._father,
                                                                                self._udz)
                    self.sefi.write("\t<p align=\"left\"><font size=\"5\"> {0}</font> </p>".format(str(self.run_2)))
        self.sefi.close()
        self.uiN = Window("Пільги по підобліовим")
        self.uiN.handleOpen()
        self.uiN.show()

    def _Control(self):
        self.listprof = {"Злодіїв в законі": "п.1.1", "Авторитет": "п.1.2", "Лідер ОЗГ": "п.1.3", "Резонанс в ЗМІ": "п.1.4",
                         "Проти основ національної безпеки": "п.1.5", "Вбивство на замовлення": "п.1.6", "Створення злочинної організації": "п.1.7",
                         "Бандетизм": "п.1.8", "Наркоділки з міжрегіональними звязками": "п.1.9", "Шахрайство": "п.1.10", "Службові злочини": "п.1.11",
                         "Нецільове використання бюджетних коштів": "п.1.12", "Ухилення від сплати податків": "п.1.13",
                         "Зловживання владою або службовим становищем": "п.1.14", "Тероризм": "п1.15", "Вступили в незаконні бандитські угрупування": "п.1.16",
                         "Масові заворушення": "п.1.17", "Усфері державної таємниці": "п.1.18", "Розв'язування війни": "п.1.19",
                         "Дії що дезорганізують роботу установи": "п.1.20"}
        self.temfil = self.pathtemp + "/_temp.html"
        self.sefi = open(self.temfil, 'w')
        self.sefi.write("<!DOCTYPE html>")
        self.sefi.write("<html lang=\"en\">")
        self.sefi.write("<head>")
        self.sefi.write("\t<meta charset=\"windows-1251\">")
        self.sefi.write("</head>")

        self.sefi.write("\t<h1 align=\"center\"> <font face=\"Times New Roman\" size=\"7\">Державна установа<br>«Полицька виправна колонія (№76)»</font> </h1>")
        self.sefi.write("<style>p {line-height: 2;} p {line-height: 0.5;}</style>")

        self.ffs = open(self.pathtemp + "/Profs.dbsp", "r")
        self.filess = self.ffs.read()
        self.ffs.close()
        try:
            self.opfils = open(self.filess, "rb")
            self.datas = pickle.load(self.opfils)
            self.opfils.close()
            self.proerss = self.datas
            self.plist = []
            for i in self.listprof:
                for ip in self.proerss:
                    self.i = self.proerss.get(i)
                    if str(ip) == str(i):
                        self.sefi.write("\t<p align=\"Center\"><font face=\"Times New Roman\" size=\"5\"><b>{0}</b></font> </p>".format(str(self.listprof.get(ip))))
                        if self.i.__len__() > 0:
                            self.xx = 0
                            for ia in self.i:
                                self.xx += 1
                                self.priis = self.i.setdefault(ia)
                                self._soname = str("{0}".format(self.priis['soname']))
                                self._name = str("{0}".format(self.priis['name']))
                                self._father = str("{0}".format(self.priis['father']))
                                self._brsd = str("{0}".format(self.priis['birsdey']))
                                self.sefi.write(
                                    "\t<p align=\"left\"><font face=\"Times New Roman\" size=\"5\"> {0}. {1} {2} {3} {4}р.н."
                                    "</font></p>".format(self.xx, self._soname, self._name, self._father, self._brsd[6:]))
            self.sefi.write("<style>p {line-height: 2;} p {line-height: 0.5;}</style><br><br>")
            self.sefi.write("\t<p align=\"left\"><font face=\"Times New Roman\" size=\"5\"><b>Оперуповноважений оперативного відділу </b></font></p>")
            self.sefi.write("\t<p align=\"left\"><font face=\"Times New Roman\" size=\"5\"><b>державної установи «Полицька </b></font></p>")
            self.sefi.write("\t<p align=\"left\"><font face=\"Times New Roman\" size=\"5\"><b>виправна колонія (№76)»</b></font></p>")
            self.sefi.write("\t<p align=\"left\"><font face=\"Times New Roman\" size=\"5\"><b>капітан внутрішньої служби &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                            "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Полунець С.В. </b></font></p>")


        except:
            self.sefi.close()
            self.uiN = Window("Контроль що місячний")
            self.uiN.handleOpen()
            self.uiN.show()
        self.sefi.close()
        self.uiN = Window("Контроль що місячний")
        self.uiN.handleOpen()
        self.uiN.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap(":/image/Splash.png")
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    font = splash.font()
    font.setPixelSize(12)
    font.setWeight(QtGui.QFont.Bold)
    splash.setFont(font)
    splash.showMessage("Завантаження...", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.red)
    splash.show()
    app.processEvents()
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()
    if args.filename is not None:
        pethstart = args.filename
    else:
        pethstart = os.environ['USERPROFILE'] + "\Профоблік.dbs"
    time.sleep(3)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form, path=pethstart)
    splash.finish(Form)
    Form.show()
    sys.exit(app.exec_())
