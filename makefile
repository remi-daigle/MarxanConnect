MarxanConnectGUImake: gui.py MarxanConnectGUI.py setup.py
	python setup.py build
	cp -r ../MarxanConnectPy/data* build/
	"C:/Program Files (x86)/NSIS/makensis.exe" "Marxan with Connectivity.nsi"