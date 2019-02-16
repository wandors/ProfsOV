# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fpass.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PasW(object):
    def setupUi(self, PasW):
        PasW.setObjectName("PasW")
        PasW.resize(275, 188)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        PasW.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PasW.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(PasW)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(PasW)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(PasW)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(PasW)
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(PasW)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(PasW)
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(PasW)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(PasW)
        self.pushButton.clicked.connect(self.auts)
        QtCore.QMetaObject.connectSlotsByName(PasW)
        PasW.setTabOrder(self.lineEdit, self.lineEdit_2)
        PasW.setTabOrder(self.lineEdit_2, self.checkBox)
        PasW.setTabOrder(self.checkBox, self.pushButton)

    def retranslateUi(self, PasW):
        _translate = QtCore.QCoreApplication.translate
        PasW.setWindowTitle(_translate("PasW", "Аутентифікація"))
        self.pushButton.setText(_translate("PasW", "УВІЙТИ"))
        self.label_2.setText(_translate("PasW", "Пароль"))
        self.lineEdit_2.setText(_translate("PasW", "1111111111"))
        self.label.setText(_translate("PasW", "Користувач"))
        self.lineEdit.setText(_translate("PasW", "admin"))
        self.checkBox.setText(_translate("PasW", "Автореєстрація"))

    def auts(self):
        # Створюєм файл в каталозі якій відповідає за збереження конфігурації имя та паролю
        self.path = os.environ["APPDATA"] + "\\Microsoft\\Configprof"
        if not os.path.exists(self.path):
            os.mkdir(self.path)


import Profs_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasW = QtWidgets.QWidget()
    ui = Ui_PasW()
    ui.setupUi(PasW)
    PasW.show()
    sys.exit(app.exec_())

