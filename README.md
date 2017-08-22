# MarxanConnectGUI
Marxan with Connectivity (Graphical User Interface)

## Installation
### Windows Installer:
Please download the [MarxanConnectSetupWindows.exe](https://github.com/remi-daigle/MarxanConnectGUI/releases/download/0.0.0/MarxanConnectSetupWindows.exe) file to the desired directory and run it! (**WARNING! MarxanConnectGUI is 'pre-beta' and is not yet fully operational, download at your own risk**)

### Build from source:
Building this repository has only been tested on Python 3.5.2 64-bit on a machine running Windows 10, your mileage may vary! (#Please note, I could not build the repository using Anaconda). It also assumes you have all the pre-requisite python modules installed, i.e.:

```
# for basic GUI
import wxpython
import matplotlib
import matplotlib.basemap
import geopandas
import descartes
import igraph # from 'pip install python-igraph', not just igraph)
import networkx

# for compiling executable
import cx_Freeze
import sys
import os
```
Download this repository, (extract the files if necessary), edit the hard coded file paths open a `cmd` window (or git bash) in the project directory and type:
```
make
```
#### Build notes:
The `gui.py` file was built using the fantastic [wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder).

The windows installer was built using [NSIS](http://nsis.sourceforge.net/Main_Page) and the [NSIS Quick Setup Script Generator](http://nsis.sourceforge.net/NSIS_Quick_Setup_Script_Generator)
