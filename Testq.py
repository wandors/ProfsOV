# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Testq.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(374, 170)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(Form)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(Form)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(Form)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(Form)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(Form)
        self.action_6.setObjectName("action_6")
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.pushButton.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Python"))
        self.menu.setTitle(_translate("Form", "Файл"))
        self.menu_2.setTitle(_translate("Form", "Редагувати"))
        self.action_2.setText(_translate("Form", "Створити"))
        self.action_3.setText(_translate("Form", "Выдкрити"))
        self.action_4.setText(_translate("Form", "Закрити"))
        self.action_5.setText(_translate("Form", "Копыювати"))
        self.action_6.setText(_translate("Form", "Вирызати"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
