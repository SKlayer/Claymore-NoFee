# -*- mode: python -*-
a = Analysis(['nofee_proxy.py'],
             pathex=['C:\\Users\\ChenHanLin\\Desktop\\pyinstaller-2.0'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'nofee_proxy.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
