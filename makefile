# trim release candidate daily version if necessary
v=`cat VERSION`
V=`cat VERSION | cut -d "-" -f1`
ifeq (${V},)
  version=${v}
else
  version=${V}
endif
rc:=`date +%Y.%m.%d.%H`

all: web win zip
    # creates the website and builds the executable, creates the Windows installers, and the .zip folder
	
web: docs/index.Rmd docs/glossary.Rmd docs/tutorial.Rmd docs/CONTRIBUTING.Rmd
    # creates the website
	# rm -rf docs/site_libs; \
	Rscript -e "rmarkdown::render_site('docs')"; \
	# move .md to root for github
	mv docs/index.md README.md; \
	mv docs/CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md; \
	mv docs/CONTRIBUTING.md CONTRIBUTING.md; \
	# create webtex version of glossary for gui
	sed -i -e 's/](glossary.html/](glossary_webtex.html/g' docs/glossary.md; \
	pandoc docs/glossary.md -o docs/glossary_webtex.html --section-divs --standalone --bibliography='docs/references.bib' --webtex; \
	rm docs/glossary.md

exe: gui.py MarxanConnectGUI.py
	# builds the executable
	# if you add the 'daily=1' argument to make, then it appends date/time 
ifeq (${daily},1)
	echo ${version}-rc${rc} > VERSION
else
	echo ${version} > VERSION
endif
	# remove old builds
	rm -rf build
	rm -rf dist
	# build gui
	pyinstaller setup.spec -y --clean --windowed --icon=docs/images/icon_bundle.ico;\

win: exe WindowsSetupBuilder.iss
    # creates the Windows installers
	"C:\Program Files (x86)\Inno Setup 5\ISCC.exe" WindowsSetupBuilder.iss

zip: exe
	rm -rf MarxanConnect.zip; \
    # creates the Marxan Connect .zip folder
	cd dist/MarxanConnect/; \
	zip -r ../../MarxanConnect.zip *; \
	cd ../..