#importing wx files
import wx

#import the newly created GUI file
import gui

#import matplotlib
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



import geopandas as gpd
from descartes import PolygonPatch
import shapely




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
        pu = gpd.GeoDataFrame.from_file(pu_filepath)
        cu = gpd.GeoDataFrame.from_file(cu_filepath)

        bufferwidth = 1
        lonmin = min([pu.total_bounds[0], cu.total_bounds[0]]) - bufferwidth
        lonmax = min([pu.total_bounds[2], cu.total_bounds[2]]) + bufferwidth
        latmin = min([pu.total_bounds[1], cu.total_bounds[1]]) - bufferwidth
        latmax = min([pu.total_bounds[3], cu.total_bounds[3]]) + bufferwidth

        self.plot.map = Basemap(llcrnrlon=lonmin, llcrnrlat=latmin, urcrnrlon=lonmax, urcrnrlat=latmax,
                                resolution='i', projection='tmerc', lat_0=(latmin+latmax)/2, lon_0=(lonmin+lonmax)/2)


        self.plot.map.drawmapboundary(fill_color='lightskyblue')
        self.plot.map.fillcontinents(color='#ddaa66', lake_color='lightskyblue')
        self.plot.map.drawcoastlines()

        patches = []
        for poly in pu.geometry:
            mpoly = shapely.ops.transform(self.plot.map, poly)
            patches.append(PolygonPatch(mpoly))

        self.plot.axes.add_collection(PatchCollection(patches, match_original=True, color='#f1a340', alpha=0.5))

        patches = []
        for poly in cu.geometry:
            mpoly = shapely.ops.transform(self.plot.map, poly)
            patches.append(PolygonPatch(mpoly))

        self.plot.axes.add_collection(PatchCollection(patches, match_original=True, color='#998ec3', alpha=0.5))


        
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