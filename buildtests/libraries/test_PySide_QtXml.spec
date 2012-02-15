# -*- mode: python -*-

__testname__ = 'test_PySide_QtXml'

a = Analysis([__testname__ + '.py'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build',
                            'pyi.' + sys.platform,
                            __testname__,
                            __testname__ + '.exe'),
          debug=True,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', __testname__))
