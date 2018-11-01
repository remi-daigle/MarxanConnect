# -*- mode: python -*-

import sys
import os
import re
from PyInstaller.utils.hooks import collect_data_files # this is very helpful

# load VERSION
with open('VERSION') as version_file:
    MarxanConnectVersion = version_file.read().strip()

# Read in the gui.py file to remove deprecated functions
with open('gui.py', 'r', encoding="utf8") as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('wx.HyperlinkCtrl', 'wx.adv.HyperlinkCtrl')
filedata = filedata.replace('wx.HL_DEFAULT_STYLE', 'wx.adv.HL_DEFAULT_STYLE')
filedata = filedata.replace('wx.html.HtmlWindow( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )',
'wx.html2.WebView.New( self.connectivityMetrics)')
filedata = re.sub('Marxan Connect v.....', 'Marxan Connect ' + MarxanConnectVersion, filedata)

# Write the file out again
with open('gui.py', 'w', encoding="utf8") as file:
  file.write(filedata)

# Read in the WindowsSetupBuilder file to edit version
with open('WindowsSetupBuilder.iss', 'r', encoding="utf8") as file :
  filedata = file.read()

# Replace the target string
filedata = re.sub('#define MyAppVersion "v....."', '#define MyAppVersion "' + MarxanConnectVersion + '"',filedata)
filedata = re.sub('OutputBaseFilename=MarxanConnect-v.....-windows-setup', 'OutputBaseFilename=MarxanConnect-' + MarxanConnectVersion.replace(".","-") + '-windows-setup',filedata)

# Write the file out again
with open('WindowsSetupBuilder.iss', 'w', encoding="utf8") as file:
  file.write(filedata)


# Prepare for pyinstaller
env_path = os.environ['CONDA_PREFIX']
dlls = os.path.join(env_path, 'DLLs')
bins = os.path.join(env_path, 'Library', 'bin')

paths = [
    os.getcwd(),
    env_path,
    dlls,
    bins,
]

binaries = [
    (os.path.join(bins,'geos.dll'), ''),
    (os.path.join(bins,'geos_c.dll'), ''),
    (os.path.join(bins,'spatialindex_c-64.dll'), ''),
    (os.path.join(bins,'spatialindex-64.dll'),''),
]

hidden_imports = [
    'igraph',
	'igraph.vendor',
	'igraph.vendor.texttable',
	'wx',
	'wx.adv',
	'wx.html2',
	'matplotlib',
	'matplotlib.pyplot',
	'matplotlib.backends.backend_wxagg',
	'matplotlib.collections',
	'mpl_toolkits.basemap',
	'geopandas',
	'descartes',
	'shapely',
	'os',
	'sys',
	'pandas',
	'numpy',
	'subprocess',
	'json',
]

block_cipher = None

added_files = collect_data_files('geopandas', subdir='datasets')+[('VERSION','.'),
    ('docs','docs')]

a = Analysis(['MarxanConnectGUI.py'],
             pathex=paths,
             binaries=[],
             datas=added_files,
             hiddenimports=hidden_imports,
             hookspath=[],
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
          [],
          exclude_binaries=True,
          name='MarxanConnectGUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='docs\\images\\icon_bundle.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='MarxanConnect')
