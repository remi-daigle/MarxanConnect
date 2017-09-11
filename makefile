MarxanConnectGUImake: gui.py MarxanConnectGUI.py setup.py
	Rscript -e "rmarkdown::render('README.Rmd', output_format='html_document', output_file='index.html')"
	Rscript -e "rmarkdown::render('README.Rmd', output_format='github_document', output_file='README.md')"
	python setup.py build
	cp -r data* build/exe.win-amd64-3.5/
	sed -i -e 's/RmDir "\$INSTDIR"/RmDir \/r \/REBOOTOK "\$INSTDIR"/g' "Marxan with Connectivity.nsi"
	"C:/Program Files (x86)/NSIS/makensis.exe" "Marxan with Connectivity.nsi"