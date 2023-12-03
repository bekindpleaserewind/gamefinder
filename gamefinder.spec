# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

added_files =[
    ('icons/*.png', '.'),
    ('alerts/*.mp3', 'alerts'),
    ('aspectfilters.yaml', '.'),
    ('itemfilters.yaml', '.'),
]

a = Analysis(
    ['gamefinder.py'],
    pathex=['.'],
    binaries=[],
    datas=added_files,
    hiddenimports=['signals', 'appinfo', 'businesslogic'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='gamefinder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
