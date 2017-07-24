#import modules
import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\Remi-Work\AppData\Local\Programs\Python\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Remi-Work\AppData\Local\Programs\Python\Python35\tcl\tk8.6'

# define additional modules (those not automatically found)
build_exe_options = {"includes": ['numpy.core._methods', 'numpy.lib.format','matplotlib.backends.backend_qt5agg','matplotlib.backends.backend_tkagg','tkinter','tkinter.filedialog'],"include_files": [r"C:\Users\Remi-Work\AppData\Local\Programs\Python\Python35\DLLs\tcl86t.dll", r"C:\Users\Remi-Work\AppData\Local\Programs\Python\Python35\DLLs\tk86t.dll"], 'namespace_packages': ['mpl_toolkits'] }

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "MarxanConnectGUI" ,
      version = "0.1" ,
      description = "" ,
      options = {'build_exe': build_exe_options},
      executables = [Executable("MarxanConnectGUI.py", base=base, icon='icon_bundle.ico')])