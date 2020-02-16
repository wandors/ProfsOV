# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BazaUSxIuy.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import Profs_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 586)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icon/Profico.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"Book Antiqua")
        font1.setPointSize(10)
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 8, 3, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton.setFont(font2)

        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 3)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 9, 5, 1, 2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 7, 3, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 11, 3, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 9, 3, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 10, 3, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 14, 3, 1, 1)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFont(font2)
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_3, 18, 0, 1, 10)

        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setFrameShape(QFrame.NoFrame)
        self.label_20.setLineWidth(2)
        self.label_20.setPixmap(QPixmap(u":/image/Books.png"))
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 14, 5, 1, 2)

        self.comboBox = QComboBox(Form)
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
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font2)
        self.comboBox.setEditable(False)

        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 6)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 10, 5, 1, 2)

        self.line_10 = QFrame(Form)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_10, 6, 7, 9, 1)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font2)
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 10)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_10.setPalette(palette)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 6, 5, 1, 2)

        self.listWidget = QListWidget(Form)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setText(u"\u041c\u0435\u0442\u0435\u043b\u044c\u0441\u044c\u043a\u0456\u0439 \u041e\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0422\u0430\u0440\u0430\u0441\u043e\u0432\u0438\u0447");
        __qlistwidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(345, 0))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.listWidget.setFont(font4)
        self.listWidget.setFrameShape(QFrame.Box)
        self.listWidget.setFrameShadow(QFrame.Plain)
        self.listWidget.setLineWidth(3)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setWordWrap(True)

        self.gridLayout.addWidget(self.listWidget, 4, 0, 12, 2)

        self.line_9 = QFrame(Form)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFont(font2)
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(5)
        self.line_9.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_9, 6, 9, 9, 1)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 11, 5, 1, 2)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 7, 5, 1, 2)

        self.line_8 = QFrame(Form)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFont(font2)
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_8, 6, 4, 9, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 13, 3, 1, 1)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 8, 5, 1, 2)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 12, 3, 1, 1)

        self.line_6 = QFrame(Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFont(font2)
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(5)
        self.line_6.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_6, 6, 2, 9, 1)

        self.line_5 = QFrame(Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFont(font2)
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_5, 5, 2, 1, 8)

        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFont(font2)
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_4, 3, 0, 1, 10)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_2, 4, 5, 1, 1)

        self.line_7 = QFrame(Form)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFont(font2)
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(5)
        self.line_7.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_7, 15, 2, 1, 8)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFont(font2)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 16, 0, 1, 10)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_4, 2, 6, 1, 4)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 12, 5, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.label, 6, 3, 1, 1)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 13, 5, 1, 2)

        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFrameShape(QFrame.WinPanel)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_25, 6, 8, 1, 1)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setUnderline(True)
        self.label_23.setFont(font5)
        self.label_23.setFrameShape(QFrame.WinPanel)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_23, 11, 8, 1, 1)

        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFrameShape(QFrame.StyledPanel)
        self.label_22.setPixmap(QPixmap(u":/image/People.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 7, 8, 4, 1)

        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")
        font6 = QFont()
        font6.setPointSize(35)
        self.label_19.setFont(font6)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)

        self.gridLayout.addWidget(self.label_19, 0, 1, 1, 9)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_3, 4, 6, 1, 4)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 17, 5, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 17, 6, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 17, 7, 1, 3)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 17, 2, 1, 3)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_21.setFont(font7)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_21, 17, 0, 1, 2)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")
        font8 = QFont()
        font8.setPointSize(15)
        self.label_24.setFont(font8)
        self.label_24.setFrameShape(QFrame.Panel)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 12, 8, 1, 1)

        self.label_26 = QLabel(Form)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(True)

        self.gridLayout.addWidget(self.label_26, 13, 8, 2, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        QWidget.setTabOrder(self.comboBox, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.listWidget)
        QWidget.setTabOrder(self.listWidget, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_7)

        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(self.pushButton_4.click)
        self.pushButton.clicked.connect(self.pushButton.click)
        self.pushButton_2.clicked.connect(self.pushButton_2.click)
        self.pushButton_3.clicked.connect(self.pushButton_3.click)
        self.pushButton_5.clicked.connect(self.pushButton_5.click)
        self.pushButton_6.clicked.connect(self.pushButton_6.click)
        self.pushButton_7.clicked.connect(self.pushButton_7.click)
        self.pushButton_8.clicked.connect(self.pushButton_8.click)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0411\u0430\u0437\u0430 \u043f\u0440\u043e\u0444\u0456\u043b\u0430\u043a\u0442\u0438\u0447\u043d\u043e\u0433\u043e \u043e\u0431\u043b\u0456\u043a\u0443 \u041f\u0412\u041a - 76", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u0456\u0434\u0441\u0442\u0430\u0432\u0430 \u043d\u0430 \u043e\u0431\u043b\u0456\u043a", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u043d\u043e\u0432\u0438\u0439", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0441\u0442.115 \u0447.2", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u0456\u043a \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0414\u0421\u0420", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0442\u044f \u041a\u041a \u0423\u043a\u0440\u0430\u0457\u043d\u0438", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0447\u0430\u0442\u043e\u043a \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041a\u0456\u043d\u0435\u0446\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.label_20.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"08.04.2020", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u0412\u0441\u0456 \u043f\u0456\u0434\u043e\u0431\u043b\u0456\u043a\u043e\u0432\u0456", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u0411\u0430\u043d\u0434\u0438\u0442\u0438\u0437\u043c", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u0412\u0431\u0438\u0432\u0441\u0442\u0432\u043e \u043d\u0430 \u0437\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u043d\u044f", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\u0412\u0436\u0438\u0432\u0430\u043d\u043d\u044f \u043d\u0430\u0440\u043e\u043a\u043e\u0442\u0438\u0447\u043d\u0438\u0445 \u0437\u0430\u0441\u043e\u0431\u0456\u0432", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"\u0412\u0438\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u043d\u044f \u0437\u0431\u0440\u043e\u0457, \u0432\u0438\u0431\u0443\u0445\u043e\u0432\u0438\u0445 \u043f\u0440\u0438\u0441\u0442\u0440\u043e\u0457\u0432", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"\u0412\u0442\u0435\u0447\u0430", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"\u0412\u0441\u0442\u0443\u043f\u0438\u043b\u0438 \u0432 \u043d\u0435\u0437\u0430\u043a\u043e\u043d\u043d\u0456 \u0431\u0430\u043d\u0434\u0438\u0442\u0441\u044c\u043a\u0456 \u0443\u0433\u0440\u0443\u043f\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Form", u"\u0414\u0456\u0457 \u0449\u043e \u0434\u0435\u0437\u043e\u0440\u0433\u0430\u043d\u0456\u0437\u0443\u044e\u0442\u044c \u0440\u043e\u0431\u043e\u0442\u0443 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Form", u"\u0417\u0430\u0445\u043e\u043f\u043b\u0435\u043d\u043d\u044f \u0437\u0430\u0440\u0443\u0447\u043d\u0438\u043a\u0456\u0432", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Form", u"\u0417\u043b\u043e\u0432\u0436\u0438\u0432\u0430\u043d\u043d\u044f \u0432\u043b\u0430\u0434\u043e\u044e \u0430\u0431\u043e \u0441\u043b\u0443\u0436\u0431\u043e\u0432\u0438\u043c \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0449\u0435\u043c", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Form", u"\u0417\u043b\u043e\u0434\u0456\u0457\u0432 \u0432 \u0437\u0430\u043a\u043e\u043d\u0456", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("Form", u"\u041b\u0456\u0434\u0435\u0440 \u041e\u0417\u0413", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0430\u0434", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("Form", u"\u041d\u0430\u0440\u043a\u043e\u0434\u0456\u043b\u043a\u0438 \u0437 \u043c\u0456\u0436\u0440\u0435\u0433\u0456\u043e\u043d\u0430\u043b\u044c\u043d\u0438\u043c\u0438 \u0437\u0432\u044f\u0437\u043a\u0430\u043c\u0438", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("Form", u"\u041d\u0435\u0446\u0456\u043b\u044c\u043e\u0432\u0435 \u0432\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u0430\u043d\u043d\u044f \u0431\u044e\u0434\u0436\u0435\u0442\u043d\u0438\u0445 \u043a\u043e\u0448\u0442\u0456\u0432", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0442\u0438 \u043e\u0441\u043d\u043e\u0432 \u043d\u0430\u0446\u0456\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0457 \u0431\u0435\u0437\u043f\u0435\u043a\u0438", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("Form", u"\u0421\u043b\u0443\u0436\u0431\u043e\u0432\u0456 \u0437\u043b\u043e\u0447\u0438\u043d\u0438", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("Form", u"\u0423\u0445\u0438\u043b\u0435\u043d\u043d\u044f \u0432\u0456\u0434 \u0441\u043f\u043b\u0430\u0442\u0438 \u043f\u043e\u0434\u0430\u0442\u043a\u0456\u0432", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("Form", u"\u0425\u0430\u0431\u0430\u0440", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("Form", u"\u0428\u0430\u0445\u0440\u0430\u0439\u0441\u0442\u0432\u043e", None))

        self.label_14.setText(QCoreApplication.translate("Form", u"08.04.2011", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0421\u0430\u043a\u0432\u0430\u0440\u0430\u043b\u0456\u0434\u0437\u0435 \u041c\u0438\u0445\u0430\u0439\u043b\u043e \u0412\u043e\u043b\u043e\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_15.setText(QCoreApplication.translate("Form", u"08.04.2015", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"25.06.1980", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0423\u0414\u0417", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0417\u043b\u043e\u0432\u0436\u0438\u0432\u0430\u043d\u043d\u044f \u0432\u043b\u0430\u0434\u043e\u044e \u0430\u0431\u043e \u0441\u043b\u0443\u0436\u0431\u043e\u0432\u0438\u043c \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0449\u0435\u043c", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0417\u0411\u041c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"08.04.2017", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041f.\u0406.\u0411.", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"07.04.2018", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u0424\u041e\u0422\u041e", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u0412\u0456\u0434\u0434\u0456\u043b\u0435\u043d\u043d\u044f", None))
        self.label_22.setText("")
        self.label_19.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0444\u0456\u043b\u0430\u043a\u0442\u0438\u0447\u043d\u0438\u0439 \u043e\u0431\u043b\u0456\u043a", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u044f\u043a", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u0417\u0432\u0456\u0442", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u0438\u0442\u0438", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u041f\u0456\u043b\u044c\u0433\u0438", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u0428\u043b\u044f\u0445 \u0434\u043e \u0431\u0430\u0437\u0438:", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"4", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043c\u0447\u0430\u0441\u043e\u0432\u043e \u0432\u0438\u0431\u0443\u0432 \u0437 \u043a\u0441\u0442\u0430\u043d\u043e\u0432\u0438", None))
    # retranslateUi
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
