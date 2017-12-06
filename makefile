MarxanConnectGUImake: gui.py MarxanConnectGUI.py setup.py WindowsSetupBuilder.iss index.Rmd glossary.Rmd tutorial.Rmd tutorial.Rmd
	rm -rf build; \
	Rscript -e "rmarkdown::render_site()"; \
	Rscript -e "rmarkdown::render('index.Rmd', output_format='github_document', output_file='README.md')"; \
	rm README.html; \
	python setup.py build; \
	mv build/exe.win-amd64-3.5/ build/MarxanConnect/; \
	"C:\Program Files (x86)\Inno Setup 5\ISCC.exe" WindowsSetupBuilder.iss; \
	cd build/; \
	zip -r ../MarxanConnect.zip MarxanConnect/* ../data/*