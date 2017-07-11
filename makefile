MarxanConnectGUImake: gui.py MarxanConnectGUI.py
	pyinstaller --onefile --windowed --icon=icon_bundle.ico --hidden-import wx --hidden-import wx._xml -y MarxanConnectGUI.py