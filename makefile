MarxanConnectGUImake: gui.py MarxanConnectGUI.py setup.py
	Rscript -e "rmarkdown::render('README.Rmd', output_format=c('html_document','github_document'), output_file=c('index.html','README.md'))"
	python setup.py build
	cp -r data* build/exe.win-amd64-3.5/
	sed -i -e 's/RmDir "\$INSTDIR"/RmDir \/r \/REBOOTOK "\$INSTDIR"/g' "Marxan with Connectivity.nsi"
	"C:/Program Files (x86)/NSIS/makensis.exe" "Marxan with Connectivity.nsi"