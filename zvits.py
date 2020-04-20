# -*- coding: utf-8 -*-

import os
import sys
import tempfile
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import Profs_rc

class Window(QtWidgets.QWidget):
    if sys.platform == 'win32':
        pathtemp = tempfile.gettempdir() + "/Proftemp"
    if sys.platform == 'linux':
        pathtemp = os.environ['HOME'] + "/Proftemp"
    titles = ""
    def __init__(self, titles):
        QtWidgets.QDialog.__init__(self)
        self.setFixedSize(960, 600)
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((self.resolution.width() / 2) - (self.frameSize().width() / 2),
                  (self.resolution.height() / 2) - (self.frameSize().height() / 2))
        self.activateWindow()
        self.setWindowTitle(self.tr(titles))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowIcon(icon)
        self.editor = QtWidgets.QTextEdit(self)
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonOpen = QtWidgets.QPushButton('В pdf', self)
        self.buttonOpen.clicked.connect(self.topdf)
        self.buttonPrint = QtWidgets.QPushButton('Друкувати', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtWidgets.QPushButton('Переглянути', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        layout.addWidget(self.buttonOpen, 1, 0)
        layout.addWidget(self.buttonPrint, 1, 1)
        layout.addWidget(self.buttonPreview, 1, 2)
        self.handleTextChanged()

    def handleOpen(self):
        path = self.pathtemp + "/_temp.html"
        info = QtCore.QFileInfo(path)
        f = open(path, "r")
        text = f.read()
        f.close()
        if info.completeSuffix() == 'html':
            self.editor.setHtml(text)
        else:
            self.editor.setPlainText(text)

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        icon = QtGui.QIcon()
        dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        dialog.paintRequested.connect(self.editor.print_)
        dialog.exec_()

    def handleTextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)
        self.buttonPreview.setEnabled(enable)

    def topdf(self):
        self.files = QtWidgets.QFileDialog.getSaveFileName(self, "Зберегти дані", os.environ['USERPROFILE'] + "/Documents", "PDF (*.pdf)")
        self.files = self.files[0]
        if self.files != "":
            doc = QtGui.QTextDocument()
            location = self.pathtemp + "/_temp.html"
            html = open(location).read()
            doc.setHtml(html)
            printer = QtPrintSupport.QPrinter()
            printer.setOutputFileName(self.files)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPageSize(QtPrintSupport.QPrinter.A4)
            printer.setPageMargins(0, 0, 0, 0, QtPrintSupport.QPrinter.Millimeter)
            doc.print_(printer)
