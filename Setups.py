# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["PyQt5"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Профоблік",
      version="3.8.3.5",
      description="ProfOV",

      options={"build_exe": build_exe_options},
      executables=[Executable("Baza.pyw", base=base, icon="Profico.ico")])