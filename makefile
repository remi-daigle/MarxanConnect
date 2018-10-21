all: web win zip
    # creates the website and builds the executable, creates the Windows installers, and the .zip folder

web: docs/index.Rmd docs/glossary.Rmd docs/tutorial.Rmd docs/CONTRIBUTING.Rmd
    # creates the website
	rm -rf docs/site_libs; \
	Rscript -e "rmarkdown::render_site('docs')"; \
	mv docs/index.md README.md; \
	mv docs/CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md; \
	mv docs/CONTRIBUTING.md CONTRIBUTING.md; \
	sed -i -e 's/](glossary.html/](glossary_webtex.html/g' docs/glossary.md; \
	pandoc docs/glossary.md -o docs/glossary_webtex.html --section-divs --standalone --bibliography='docs/references.bib' --webtex; \
	rm docs/glossary.md

exe: gui.py MarxanConnectGUI.py setup.py
    # builds the executable
	rm -rf MarxanConnect/; \
	python setup.py build; 

win: exe WindowsSetupBuilder.iss
    # creates the Windows installers
	"C:\Program Files (x86)\Inno Setup 5\ISCC.exe" WindowsSetupBuilder.iss

zip: exe
	rm -rf MarxanConnect.zip; \
    # creates the Marxan Connect .zip folder
	cd MarxanConnect/; \
	zip -r ../MarxanConnect.zip *; \
	cd ..