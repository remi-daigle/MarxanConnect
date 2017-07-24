MarxanConnectGUImake: gui.py MarxanConnectGUI.py setup.py
	python setup.py build
	cp -r ../MarxanConnectPy/data* build/exe.win-amd64-3.5/
	"C:/Program Files (x86)/NSIS/makensis.exe" "Marxan with Connectivity.nsi"