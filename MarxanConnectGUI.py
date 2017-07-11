#importing wx files
import wx
 
#import the newly created GUI file
import gui
 
#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class MarxanConnectGUI(gui.MarxanConnectGUI):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MarxanConnectGUI.__init__(self,parent)
        icons = wx.IconBundle() 
        for sz in [16, 32, 48, 96, 256]: 
            try: 
                icon = wx.Icon('C:/Users/Remi-Work/Desktop/MarxanConnectGUI/icon_bundle.ico', wx.BITMAP_TYPE_ICO, desiredWidth=sz, desiredHeight=sz) 
                icons.AddIcon(icon) 
            except: 
                pass 
                self.SetIcons(icons) 
#        ico = wx.Icon('favicon.ico', wx.BITMAP_TYPE_ICO)
#        self.SetIcon(ico)
 
#    #what to when 'Solve' is clicked
#    #wx calls this function with and 'event' object
#    def solveFunc(self,event):
#        try:
#            #evaluate the string in 'text' and put the answer back
#            ans = eval(self.text.GetValue())
#            self.text.SetValue (str(ans))
#        except Exception:
#            print 'error'
#    #put a blank string in text when 'Clear' is clicked
#    def clearFunc(self,event):
#        self.text.SetValue(str(''))
 
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = MarxanConnectGUI(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()