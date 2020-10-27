---
title: "Marxan Connect"
output:
  html_document:
    keep_md: yes
    toc: yes
    toc_float: yes
---

Marxan Connect (henceforth the "app") is a Graphical User Interface (GUI) to help conservationists include "connectivity" in their protected area network planning. The app has now been described in a peer-reviewed publication in [Methods in Ecology and Evolution](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13349).

The term "connectivity" has a variety of definitions (i.e. larval connectivity, genetic connectivity, landscape connectivity, etc) and protected area networks can be optimized for various connectivity objectives. The app is intended to guide conservationists through the process of identifying important aspects of connectivity for their conservation scenarios as well as highlighting the necessary data.

The app also includes a fully functional Python package that is operated via command line. The Python package, [`marxanconpy`](https://remi-daigle.github.io/marxanconpy/), can be used to reproduce an analysis using the project file (`.MarCon`) generated by the GUI.

To use this software, please visit the [Tutorial](https://marxanconnect.ca/tutorial.html) and the [Glossary](https://marxanconnect.ca/glossary.html). Otherwise, if you would just like to get started, please [install](#installing) the app and proceed through all the tabs from left to right starting with "Spatial Input". After calculating the "Connectivity Metrics", you can choose to conduct a Marxan or (experimentally) Marxan with Zones analysis in the app, export the connectivity metrics for use in a standalone custom Marxan analysis, or you can visualize the Connectivity Metrics using the "Plotting Options" tab

If you would like to report any bugs or request a missing feature, please post an [issue](https://github.com/remi-daigle/MarxanConnect/issues) on the GitHub repository. Please provide as much information as possible, such as: detailed description, app version, operating system, even a link to your data if relevant (also, see [Contributing](#contributing)). 

In terms of using the software for conservation planning, 'best practices' (*i.e. detailed documentation, case studies) are currently under development. 

# Authors

* **Remi Daigle** - *App design, programming, development, maintenance* - [remi-daigle](https://github.com/remi-daigle)
* **Anna Metaxas** - *Initial conception, Acquisition of funding, App improvements and development*
* **Arieanna Balbar** - *App improvements, testing, and development* - [abalbar](https://github.com/abalbar)
* **Jennifer McGowan** - *App improvements, design for discrete conservation features*
* **Eric Anton Treml** - *App improvements, input to connectivity definitions and metrics*
* **Caitie Kuempel** - *App improvements* - [cdkuempel](https://github.com/cdkuempel)
* **Hugh Possingham** - *App improvements*
* **Maria Beger** - *Initial conception, Acquisition of funding, App improvements and development*

See also the list of [contributors](https://github.com/remi-daigle/MarxanConnect/contributors) who participated in this project on Github and the [Acknowledgments](#acknowledgments) section.

# Installing Marxan Connect

Marxan Connect was built for Windows or macOS. The app is currently not compatible with Linux although the python processing script ([`marxanconpy`](https://github.com/remi-daigle/MarxanConnect/blob/master/marxanconpy.py)) and GUI scripts ([`gui`](https://github.com/remi-daigle/MarxanConnect/blob/master/gui.py) and [`MarxanConnectGUI`](https://github.com/remi-daigle/MarxanConnect/blob/master/MarxanConnectGUI.py)) were designed with interoperability in mind. 

## Windows (7/8/10)

### Windows Installer

(**WARNING! Marxan Connect is in 'beta' release**)

Please download the latest [MarxanConnect-vX-Y-Z-windows-setup.exe](https://github.com/remi-daigle/MarxanConnect/releases) installer file, run it, and follow the instructions. You may get a 'Windows protected your PC' security warning since we are not a large software company. Assuming you trust the contents of the app, click on `More info`, then `Run anyway` to install. Alternatively (for advanced users only), follow the [Building from source](#building-from-source) instructions to use the latest bleeding edge version of the app.

### Windows Zipped Bundle

If you cannot use the installer because you do not have administrative privileges, we've provided a zipped bundle of the app to allow users to bypass that problem. To use, download the latest [MarxanConnect.zip](https://github.com/remi-daigle/MarxanConnect/releases), unzip it to your preferred destination (e.g. `~/Desktop`), and double-click `MarxanConnectGUI.exe`. In this case you will have to generate any start menu shortcuts, or file associations (i.e. `.MarCon`) manually.

## macOS (>Yosemite 10.10.5)

Please download the latest [MarxanConnect-vX-Y-Z.dmg](https://github.com/remi-daigle/MarxanConnect/releases) file, double-click the downloaded file and a Finder window wil appear, and click-and-drag into the Applications folder. You may get a 'This is an application downloaded from the Internet' security warning since we are not a large software company. Assuming you trust the contents of the app, in the Finder, locate Marxan Connect. Press the Control key and click the app icon, then choose Open from the shortcut menu. Click Open. Marxan Connect is saved as an exception to your security settings, and you can open it in the future by double-clicking it just as you can any registered app. This was built and tested in macOS Mojave (10.14), but testing indicates it is compatible with older operating systems (>Yosemite 10.10.5). Alternatively (for advanced users only), follow the [Building from source](#building-from-source) instructions to use the latest bleeding edge version of the app.

## Linux 

There is no prebuilt version of Marxan Connect for Linux, see [this issue](https://github.com/remi-daigle/MarxanConnect/issues/57) for more information. If you know how to resolve this issue, please submit a pull request or comment on the issue page. Alternatively (for advanced users only), follow the [Building from source](#building-from-source) instructions to use the latest bleeding edge version of the app.

# Installing the command line interface

For users who prefer the command line, please visit the [`marxanconpy` website](https://remi-daigle.github.io/marxanconpy/)

# Building from source

Not for the typical user. Building from source is only necessary if you plan to contribute to the project (see [Contributing](#contributing) section below) or if you want to use the bleeding edge version of the app. 

* Download this repository
* If necessary, edit the hard coded file paths in [setup.py](https://github.com/remi-daigle/MarxanConnect/blob/master/setup.py) and [WindowsSetupBuilder.iss](https://github.com/remi-daigle/MarxanConnect/blob/master/WindowsSetupBuilder.iss)
* If necessary, edit the version number (see the [Versioning](#versioning) section)
* On Windows, open a terminal or `cmd` window (or git bash) in the project directory and type:

```
make
```

The default `make` will try to compile the windows version, so on macOS a full build would be `make web mac` or `make web mac daily=1` for a release candidate. Alternatively, you can compile the website with `make web`, the Marxan Connect Windows executable with `make exe`, the windows installer `make win`, the Windows zip with `make zip`, and the macOS image with `make mac`. During development, if you don't want to build an 'official _version_', then use the `daily=1` argument for the makefile (*e.g.* `make exe daily=1`) to create an automaticaly named release candidate. 

## Prerequisites (for building from source)

* [Python 3 64-bit](https://www.python.org/downloads) or [Anaconda](https://www.anaconda.com/distribution/)
* [wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder)
* [Inno Setup](http://www.jrsoftware.org/isinfo.php)
* [R](https://www.r-project.org/) and the [`rmarkdown`](http://rmarkdown.rstudio.com/) package
* [Pandoc](https://pandoc.org/installing.html) and pandoc-citeproc

It also assumes you have all the pre-requisite python modules installed to build the app itself, *i.e.*:


```bash
#!/bin/bash

conda create --name marcon wxpython matplotlib geopandas descartes shapely pandas numpy cartopy

source activate marcon # for windows
conda activate marcon # for mac/linux

pip install python-igraph # on windows you may need to install via wheel https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-igraph
pip install PyInstaller marxanconpy bs4
pip install dmgbuild pexpect # for mac only
```

As well as pre-requesite R packages to build the website, *i.e.*:


```r
if(!require("rmarkdown")) install.packages("rmarkdown")
```

```
## Loading required package: rmarkdown
```

```r
if(!require("sf")) install.packages("sf")
if(!require("leaflet")) install.packages("leaflet")
if(!require("tmap")) install.packages("tmap")
if(!require("tidyverse")) install.packages("tidyverse")
if(!require("DT")) install.packages("DT")
if(!require("igraph")) install.packages("igraph")
if(!require("ggraph")) install.packages("ggraph")
if(!require("gganimate")) devtools::install_github('thomasp85/gganimate')
if(!require("tidygraph")) install.packages("tidygraph")
if(!require("RColorBrewer")) install.packages("RColorBrewer")
```

# Built With

The `gui.py` file was built using the fantastic [wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder).

The windows installer was built using [Inno Setup](http://www.jrsoftware.org/isinfo.php).

THe documentation and website was built with [R](https://www.r-project.org/) and the [`rmarkdown`](http://rmarkdown.rstudio.com/) package

# Contributing

Please read [CONTRIBUTING.md](https://marxanconnect.ca/CONTRIBUTING.html) for details on our code of conduct, and the process for submitting pull requests or issues to us.

# Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/remi-daigle/MarxanConnect/tags). 

# License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/remi-daigle/MarxanConnect/blob/master/LICENSE) file for details

# Acknowledgments

* Funding for the development of this software was provided Canadian Healthy Oceans Network [(CHONe)](https://chone2.ca/) a Natural Sciences and Engineering Research Council of Canada [(NSERC)](http://www.nserc-crsng.gc.ca/index_eng.asp) Strategic Network and the [University of Queensland](https://www.uq.edu.au/).
* Additional contributions by the [University of Leeds](https://www.leeds.ac.uk/), [The Nature Conservancy](https://www.nature.org/), [Dalhousie University](https://www.dal.ca/), [The University of Melbourne](https://www.unimelb.edu.au/), and the Australian Research Council - Centre of Excellence for Environmental Decisions [(CEED)](http://ceed.edu.au/)
* This project builds on the existing [Marxan](http://marxan.net/) (Ball et al. 2009) software and would not be possible without the hard work of Ian Ball, Hugh Possingham, and Matt Watts.

# References

Ball, I.R., H.P. Possingham, and M. Watts. 2009. Marxan and relatives: Software for spatial conservation prioritisation. Chapter 14: Pages 185-195 in Spatial conservation prioritisation: Quantitative methods and computational tools. Eds Moilanen, A., K.A. Wilson, and H.P. Possingham. Oxford University Press, Oxford, UK.
