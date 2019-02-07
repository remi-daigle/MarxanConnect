# -*- mode: python -*-

import sys
import os
import re
from PyInstaller.utils.hooks import collect_data_files
import platform

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
filedata = re.sub(r'Marxan Connect v.*\. https', 'Marxan Connect ' + MarxanConnectVersion +'. https', filedata)
filedata = filedata.replace('wx.HyperlinkCtrl', 'wx.adv.HyperlinkCtrl')
if platform.system() == 'Darwin':
    filedata = filedata.replace('|All files (*.*)|*.*"', '"')

# Write the file out again
with open('gui.py', 'w', encoding="utf8") as file:
  file.write(filedata)

block_cipher = None

if platform.system() == 'Windows':
    # Read in the WindowsSetupBuilder file to edit version
    with open('WindowsSetupBuilder.iss', 'r', encoding="utf8") as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub(r'#define MyAppVersion "v.*"', '#define MyAppVersion "' + MarxanConnectVersion + '"', filedata)
    filedata = re.sub(r'OutputBaseFilename=MarxanConnect-v.*-windows-setup',
                      'OutputBaseFilename=MarxanConnect-' + MarxanConnectVersion.replace(".", "-") + '-windows-setup',
                      filedata)

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

    added_files = collect_data_files('geopandas', subdir='datasets')+[('VERSION','.'),
        ('docs','docs'),('Marxan243','Marxan243')]

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
              upx=False,
              console=False,
              icon='docs\\images\\icon_bundle.ico')
    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   strip=False,
                   upx=False,
                   name='MarxanConnect')

if platform.system() == 'Darwin':
    # Prepare for pyinstaller
    env_path = os.environ['CONDA_PREFIX']
    # dlls = os.path.join(env_path, 'DLLs')
    # bins = os.path.join(env_path, 'Library', 'bin')
    libs = os.path.join(env_path, 'lib')

    _osgeo_pyds = collect_data_files('osgeo', include_py_files=True)

    osgeo_pyds = []
    for p, lib in _osgeo_pyds:
        if '.pyd' in p:
            osgeo_pyds.append((p, '.'))

    # paths = [
    #     os.getcwd(),
    #     env_path,
    #     dlls,
    #     bins,
    # ]

    binaries = osgeo_pyds + [
        (os.path.join(libs, 'libspatialindex.dylib'), '.'),
        (os.path.join(libs, 'libspatialindex_c.dylib'), '.'),
        (os.path.join(libs, 'libspatialindex.4.dylib'), '.'),
        (os.path.join(libs, 'libspatialindex_c.4.dylib'), '.'),
    ]

    hidden_imports = [
        'igraph',
        'igraph.vendor',
        'igraph.vendor.texttable',
        'fiona._shim',
        'fiona.schema',
        'geopandas',
        'ctypes',
        'ctypes.util',
        'fiona',
        'gdal',
        'geos',
        'shapely',
        'shapely.geometry',
        'pyproj',
        'rtree',
        'geopandas.datasets',
        'pytest',
        'pandas._libs.tslibs.timedeltas',
    ]

    added_files = collect_data_files('geopandas', subdir='datasets') + [
        ('VERSION', '.'),
        ('docs', 'docs'),
        ('Marxan243', 'Marxan243'),
    ]


    a = Analysis(['MarxanConnectGUI.py'],
                 pathex=['/Users/remidaigle/Documents/GitHub/MarxanConnect'],
                 binaries=binaries,
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
              console=False)
    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   strip=False,
                   upx=True,
                   name='MarxanConnectGUI')
    app = BUNDLE(coll,
                 name='MarxanConnectGUI.app',
                 icon='docs/images/icon_mac.icns',
                 bundle_identifier=None)
