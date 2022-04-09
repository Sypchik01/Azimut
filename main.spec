# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


exe = EXE(pyz,
          a.scripts,
          a.binaries +  [('oci.dll',r'.\oracle_dll\oci.dll', 'BINARY')] + 
                        [('ocijdbc21.dll',r'.\oracle_dll\ocijdbc21.dll','BINARY')] +
                        [('ociw32.dll',r'.\oracle_dll\ociw32.dll','BINARY')] +
                        [('oramysql.dll',r'.\oracle_dll\oramysql.dll','BINARY')] +
                        [('orannzsbb.dll',r'.\oracle_dll\orannzsbb.dll','BINARY')] +
                        [('oraocci21.dll',r'.\oracle_dll\oraocci21.dll','BINARY')] +
                        [('oraocci21d.dll',r'.\oracle_dll\oraocci21d.dll','BINARY')] +
                        [('oraociei.dll',r'.\oracle_dll\oraociei.dll','BINARY')] +
                        [('orasql.dll',r'.\oracle_dll\orasql.dll','BINARY')],
          a.zipfiles,
          a.datas,
          name='Азимут',
          debug=False,
          strip=False,
          upx=True,
          console=False )