all: web zip
    # creates the website and builds the executable, creates the Windows installers, and the .zip folder

web: index.Rmd glossary.Rmd tutorial.Rmd CONTRIBUTING.Rmd
    # creates the website
	rm -rf site_libs; \
	Rscript -e "rmarkdown::render_site()"; \
	mv index.md README.md; \
	pandoc --standalone glossary.md -o glossary_webtex.html --webtex --section-divs
	rm README.html; rm ISSUE_TEMPLATE.html; rm PULL_REQUEST_TEMPLATE.html; rm glossary.md \

exe: gui.py MarxanConnectGUI.py setup.py WindowsSetupBuilder.iss
    # builds the executable
	rm -rf build; \
	python setup.py build; \

win: exe
    # creates the Windows installers
	mv build/exe.win-amd64-3.5/ build/MarxanConnect/; \
	"C:\Program Files (x86)\Inno Setup 5\ISCC.exe" WindowsSetupBuilder.iss; \

zip: win
    # creates the .zip folder
	cd build/; \
	zip -r ../MarxanConnect.zip MarxanConnect/* ../data/*