# -*- coding: utf-8 -*-
__author__ = 'Сергі Полунець'
__versions__ = "v.3.7.2.1-32"
import os
names = "Baza"
scripts = "Baza"
icons = "Profico"
num = 2
path = '"C:/Program Files (x86)/Windows Kits/10/Redist/10.0.17763.0/ucrt/DLLs/x86"'
pathQt = 'C:/Python37/Lib/site-packages/PyQt5/Qt/bin'
if str(num) == "1":
    pacs = "--onefile --console"
elif str(num) == "2":
    pacs = "--windowed"
elif str(num) == "3":
    pacs = "--onefile --windowed"
else:
    pacs = "--console"
os.system("pyinstaller.exe {0} --icon={1}.ico  {2}.pyw --name={3} --paths={4} --paths={5} ".format(pacs, icons, scripts, names, path, pathQt))
#os.system("del /a " + "{0}.spec".format(names))
