#importing wx files
import wx
import wx.lib.agw.aui as aui

#import the newly created GUI file
import gui

#import matplotlib
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap

# import spatial modules
import geopandas as gpd
from descartes import PolygonPatch
import shapely

#import system helper modules
import os
import sys
import pandas
import numpy
import networkx as nx

# import MarxanConnectPy from https://github.com/remi-daigle/MarxanConnectPy
# MarxanConnectPy and MarxanConnectGUI must be in the same folder (i.e. Github/MarxanConnectPy/ and Github/MarxanConnectGUI/)
sys.path.append('../MarxanConnectPy/')
import marxanconpy

# define current working directory
cwd = os.getcwd()


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class MarxanConnectGUI(gui.MarxanConnectGUI):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MarxanConnectGUI.__init__(self,parent)
        icons = wx.IconBundle()
        for sz in [16, 32, 48, 96, 256]: 
            try: 
                icon = wx.Icon(os.path.join(cwd,'icon_bundle.ico'), wx.BITMAP_TYPE_ICO, desiredWidth=sz, desiredHeight=sz)
                icons.AddIcon(icon) 
            except: 
                pass 
                self.SetIcons(icons)

        # set default file paths

        if(os.path.isdir(os.path.join(os.environ['ProgramFiles(x86)'], "MarxanConnect"))):
            pfdir = os.path.join(os.environ['ProgramFiles(x86)'], "MarxanConnect")
        else:
            pfdir = os.path.join(os.environ['ProgramFiles'], "MarxanConnect")

        self.pu_filepath = os.path.join(pfdir,"data","shapefiles","marxan_pu.shp")
        self.cu_filepath = os.path.join(pfdir,"data","shapefiles","connectivity_grid.shp")
        self.cm_filepath = os.path.join(pfdir,"data","grid_connectivity_matrix.csv")
        self.pucm_filename = self.PUCM_filename.GetLabelText()
        self.pucm_filedir = os.path.join(os.environ['USERPROFILE'], "My Documents")



    def on_plot_map_button(self, event):
        if not hasattr(self, 'plot'):
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

    def on_plot_graph_button(self, event):
        if not hasattr(self, 'plot'):
            self.plot = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            self.m_auinotebook1.AddPage(self.plot, u"Plot", False, wx.NullBitmap)
        self.plot.figure = plt.figure()
        self.plot.axes = self.plot.figure.gca()
        self.plot.canvas = FigureCanvas(self.plot, -1, self.plot.figure)
        self.plot.sizer = wx.BoxSizer(wx.VERTICAL)
        self.plot.sizer.Add(self.plot.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.plot.SetSizer(self.plot.sizer)
        self.plot.Fit()
        self.on_draw_graph(pucm_filedir=self.pucm_filedir, pucm_filename=self.pucm_filename)

    def draw_shapefiles(self, pu_filepath, cu_filepath):
        pu = gpd.GeoDataFrame.from_file(pu_filepath)
        cu = gpd.GeoDataFrame.from_file(cu_filepath)

        lonmin, lonmax, latmin, latmax = marxanconpy.buffer_shp_corners([pu,cu],1)

        # bufferwidth = 1
        # lonmin = min([pu.total_bounds[0], cu.total_bounds[0]]) - bufferwidth
        # lonmax = min([pu.total_bounds[2], cu.total_bounds[2]]) + bufferwidth
        # latmin = min([pu.total_bounds[1], cu.total_bounds[1]]) - bufferwidth
        # latmax = min([pu.total_bounds[3], cu.total_bounds[3]]) + bufferwidth

        self.plot.map = Basemap(llcrnrlon=lonmin, llcrnrlat=latmin, urcrnrlon=lonmax, urcrnrlat=latmax,
                                resolution='i', projection='tmerc', lat_0=(latmin+latmax)/2, lon_0=(lonmin+lonmax)/2)


        self.plot.map.drawmapboundary(fill_color='lightskyblue')
        self.plot.map.fillcontinents(color='#ddaa66', lake_color='lightskyblue')
        self.plot.map.drawcoastlines()


        patches = []
        cmap = matplotlib.cm.get_cmap('OrRd')
        norm = matplotlib.colors.Normalize(min(self.connectivityMetrics.eigvectcent), max(self.connectivityMetrics.eigvectcent))
        bins = numpy.linspace(min(self.connectivityMetrics.eigvectcent), max(self.connectivityMetrics.eigvectcent), 10)
        color_producer = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)
        for poly, evc in zip(pu.geometry, self.connectivityMetrics.eigvectcent):
            rgba = color_producer.to_rgba(evc)
            mpoly = shapely.ops.transform(self.plot.map, poly)
            patches.append(PolygonPatch(mpoly,color=rgba))

        # self.plot.axes.add_collection(PatchCollection(patches, match_original=True, color='#f1a340', alpha=0.5))
        self.plot.axes.add_collection(PatchCollection(patches, match_original=True, alpha=0.9))
        self.plot.ax_legend = self.plot.figure.add_axes([0.415, 0.15, 0.2, 0.04], zorder=3)
        self.plot.cb = matplotlib.colorbar.ColorbarBase(self.plot.ax_legend, cmap=cmap, ticks=bins, boundaries=bins, orientation='horizontal')
        self.plot.cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])


        patches = []
        for poly in cu.geometry:
            mpoly = shapely.ops.transform(self.plot.map, poly)
            patches.append(PolygonPatch(mpoly))

        self.plot.axes.add_collection(PatchCollection(patches, match_original=True, color='#998ec3', alpha=0.5))

    def on_draw_graph(self,pucm_filedir, pucm_filename):
        pucm_filepath = os.path.join(pucm_filedir, pucm_filename)
        conmat = pandas.read_csv(pucm_filepath, index_col=0)
        g1 = nx.from_numpy_matrix(conmat.as_matrix())
        mapping = dict(zip(g1.nodes(), conmat.index))
        g1 = nx.relabel_nodes(g1, mapping)
        nx.draw_networkx(g1,with_labels=True,edge_color='lightgray')

        
    def on_PU_file( self, event ):
        self.pu_filepath = self.PU_file.GetPath()
        print(self.pu_filepath)

    def on_rescaleRadioBox(self, event):
        if(self.CU_def.Hide()==True):
            self.CU_def.Hide()
            self.CU_filetext.Hide()
            self.CU_file.Hide()
        else:
            self.CU_def.Show()
            self.CU_filetext.Show()
            self.CU_file.Show()

    def on_CU_file(self, event):
        self.cu_filepath=self.CU_file.GetPath()
        print(self.cu_filepath)

    def on_CM_file( self, event ):
        self.cm_filepath = self.CM_file.GetPath()
        print(self.cm_filepath)

    def on_PUCM_filedir(self, event):
        self.pucm_filedir=self.PUCM_filedir.GetPath()
        print(self.pucm_filedir)

    def on_PUCM_filenameTextEnter(self, event):
        self.pucm_filename = self.PUCM_filenameTextEnter.GetPath()
        print(self.pucm_filename)

    def on_rescale_button(self, event):
        print(self.pu_filepath, self.cu_filepath, self.cm_filepath, self.pucm_filedir, self.pucm_filename)
        marxanconpy.rescale_matrix(self.pu_filepath, self.cu_filepath, self.cm_filepath, self.pucm_filedir, self.pucm_filename)
        print("rescaling!")

    def on_calc_metrics(self, event):
        self.pucm_filepath = os.path.join(self.pucm_filedir, self.pucm_filename)
        if self.ct_demo_vertex_degree.GetValue():
            self.connectivityMetrics.vertexdegree = marxanconpy.conmat2vertexdegree(self.pucm_filepath)

        if self.ct_demo_between_cent.GetValue():
            self.connectivityMetrics.betweencent = marxanconpy.conmat2betweencent(self.pucm_filepath)

        if self.ct_demo_eig_vect_cent.GetValue():
            self.connectivityMetrics.eigvectcent = marxanconpy.conmat2eigvectcent(self.pucm_filepath)

        if self.ct_demo_self_recruit.GetValue():
            self.connectivityMetrics.selfrecruit = marxanconpy.conmat2selfrecruit(self.pucm_filepath)

        if self.bd_demo_conn_boundary.GetValue():
            self.connectivityMetrics.conmat = pandas.read_csv(os.path.join(self.pucm_filedir, self.pucm_filename))
            self.connectivityMetrics.boundary_dat = self.connectivityMetrics.conmat.melt(id_vars=['puID'])
            self.connectivityMetrics.boundary_dat.columns = ['id1', 'id2', 'boundary']

app = wx.App(False)
 
#create an object of CalcFrame
frame = MarxanConnectGUI(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()

#make; echo "testing exemake"; ./dist/MarxanConnectGUI/MarxanConnectGUI.exe