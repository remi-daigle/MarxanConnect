#importing wx files
import wx

#import the newly created GUI file
import gui

#import matplotlib
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



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
        self.pu_filepath = "C:\Program Files (x86)\MarxanConnect\data\shapefiles\marxan_pu.shp"
        self.cu_filepath = "C:\Program Files (x86)\MarxanConnect\data\shapefiles\connectivity_grid.shp"

    def on_plot_button(self, event):
        print("plot button works")
        self.plot = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_auinotebook1.AddPage(self.plot, u"Plot", False, wx.NullBitmap)
        self.plot.figure = plt.figure()
        self.plot.axes = self.plot.figure.gca()
        self.plot.canvas = FigureCanvas(self.plot, -1, self.plot.figure)
        self.plot.sizer = wx.BoxSizer(wx.VERTICAL)
        self.plot.sizer.Add(self.plot.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.plot.SetSizer(self.plot.sizer)
        self.plot.Fit()
        self.draw_shapefiles(pu_filepath=self.pu_filepath, cu_filepath=self.cu_filepath)


    def draw_shapefiles(self, pu_filepath, cu_filepath):
        print("drawing: " + pu_filepath + " and ", cu_filepath)
        pu = gpd.GeoDataFrame.from_file(pu_filepath)
        for i in range(len(pu)):
            poly = pu.geometry[i]
            self.plot.axes.add_patch(PolygonPatch(poly, color='#f1a340', alpha=0.5))

        cu = gpd.GeoDataFrame.from_file(cu_filepath)
        for i in range(len(cu)):
            poly = cu.geometry[i]
            self.plot.axes.add_patch(PolygonPatch(poly, color='#998ec3', alpha=0.5, label='Connectivity Shapefile'))

        self.plot.axes.axis('scaled')
        self.plot.axes.plot()


    def on_PU_file( self, event ):
        self.pu_filepath = self.PU_file.GetPath()
        print(self.pu_filepath)

    def on_CU_file(self, event):
        self.cu_filepath=self.CU_file.GetPath()
        print(self.cu_filepath)

app = wx.App(False)
 
#create an object of CalcFrame
frame = MarxanConnectGUI(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()

#make; echo "testing exemake"; ./dist/MarxanConnectGUI/MarxanConnectGUI.exe