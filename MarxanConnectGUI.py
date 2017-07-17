#importing wx files
import wx
 
#import the newly created GUI file
import gui

#import matplotlib
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.pyplot as plt


import geopandas as gpd
from descartes import PolygonPatch


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

 
    def on_plot_button_click(self,event):
        print("plot button works")
        plotwindow = wx.App()
        fr = wx.Frame(None, title='test')
        panel = popupplot(fr)
        panel.draw_shapefiles(pu_filepath=self.pu_filepath,cu_filepath=self.cu_filepath)
        fr.Show()
        plotwindow.MainLoop()

    def on_pu_file_pick( self, event ):
        self.pu_filepath = self.pu_filePicker.GetPath()
        print(self.pu_filepath)

    def on_cu_file_pick(self, event):
        self.cu_filepath=self.cu_filePicker.GetPath()
        print(self.cu_filepath)

class popupplot(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = plt.figure()
        self.axes = self.figure.gca()
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw_shapefiles(self,pu_filepath,cu_filepath):
        print("drawing: "+pu_filepath+" and ",cu_filepath)
        pu = gpd.GeoDataFrame.from_file(pu_filepath)
        for i in range(len(pu)):
            poly = pu.geometry[i]
            self.axes.add_patch(PolygonPatch(poly, color='#f1a340',alpha=0.5))

        cu = gpd.GeoDataFrame.from_file(cu_filepath)
        for i in range(len(cu)):
            poly = cu.geometry[i]
            self.axes.add_patch(PolygonPatch(poly, color='#998ec3',alpha=0.5,label='Connectivity Shapefile'))

        self.axes.axis('scaled')
        self.axes.plot()

app = wx.App(False)
 
#create an object of CalcFrame
frame = MarxanConnectGUI(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()

#make; echo "testing exemake"; ./dist/MarxanConnectGUI/MarxanConnectGUI.exe