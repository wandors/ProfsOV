# -*- coding: utf-8 -*-
import os
import sys
names = "Профоблік"
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

if sys.platform == 'win32':
    os.system("pyinstaller.exe  {0}  --icon={1}.ico  {2}.pyw --name={3} --paths={4} --paths={5}".format(pacs, icons, scripts, names, path, pathQt))
elif sys.platform == 'linux':
    os.system("pyinstaller  {0}  --icon={1}.ico  {2}.py --name={3}".format(pacs, icons, scripts, names))

# --debug