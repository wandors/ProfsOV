# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Baza.pyw'],
             pathex=['C:/Program Files (x86)/Windows Kits/10/Redist/10.0.17763.0/ucrt/DLLs/x86', 'C:/Python37/Lib/site-packages/PyQt5/Qt/bin', 'D:\\Pycharm\\ProfsOV'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [('v', None, 'OPTION')],
          exclude_binaries=True,
          name='Baza',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='Profico.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Baza')
