MarxanConnectGUImake: gui.py MarxanConnectGUI.py setup.py WindowsSetupBuilder.iss README.Rmd glossary.Rmd tutorial.Rmd tutorial.Rmd
	Rscript -e "rmarkdown::render('README.Rmd', output_format='html_document', output_file='index.html')"
	Rscript -e "rmarkdown::render('README.Rmd', output_format='github_document', output_file='README.md')"
	Rscript -e "rmarkdown::render('glossary.Rmd')"
	Rscript -e "rmarkdown::render('tutorial.Rmd')"
	Rscript -e "rmarkdown::render('contributing.Rmd')"
	rm README.html
	python setup.py build
	#zip -r MarxanConnect.zip build\exe.win-amd64-3.5\*
	"C:\Program Files (x86)\Inno Setup 5\ISCC.exe" WindowsSetupBuilder.iss