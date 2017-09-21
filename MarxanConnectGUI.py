#importing wx files
import wx
import wx.lib.agw.aui as aui
import wx.adv

# import gui
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
import threading
import json

# import MarxanConnect python module
import marxanconpy


# define wildcards
wc_MarCon = "Marxan with Connectivity Project (*.MarCon)|*.MarCon|" \
            "All files (*.*)|*.*"

class MarxanConnectGUI(gui.MarxanConnectGUI):
    
    def __init__(self,parent):
        """
        initialize parent class (the entire GUI)
        """
        gui.MarxanConnectGUI.__init__(self,parent)
        # set the icon
        icons = wx.IconBundle()
        for sz in [16, 32, 48, 96, 256]: 
            try: 
                icon = wx.Icon(os.path.join(sys.path[0],'icon_bundle.ico'),
                               wx.BITMAP_TYPE_ICO,
                               desiredWidth=sz,
                               desiredHeight=sz)
                icons.AddIcon(icon) 
            except: 
                pass 
                self.SetIcons(icons)
        
        # launch a blank new project
        self.on_new_project(event=None, launch = True)
        print("This is the name of the script: ", sys.argv[0])
        print("Number of arguments: ", len(sys.argv))
        print("The arguments are: ", str(sys.argv))
        # launch Getting started window
        frame = getting_started(parent=self)
        # frame.Show()
        
        # set opening tab to Spatial Input (0)
        self.auinotebook.ChangeSelection(2)
    
###########################  project managment functions ######################        
    def on_new_project( self, event, launch = False):
        """
        open a new project and name/save a new project file
        """
        # create project list to store project specific data
        self.project = {}
        self.project['workingdirectory'] = os.path.join(os.environ['USERPROFILE'], "Documents")
        self.project['filepaths'] = {}
        self.project['options'] = {}

        # set default options
        self.project['options']['demo_pu_cm_export'] = self.demo_PU_CM_export.GetValue()
        self.project['options']['demo_pu_cm_progress'] = self.demo_PU_CM_progress.GetValue()
        self.project['options']['demo_conmat_units'] = self.demo_matrixUnitsRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_type'] = self.demo_matrixTypeRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_format'] = self.demo_matrixFormatRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_rescale'] = self.demo_rescaleRadioBox.GetStringSelection()
        self.project['options']['calc_metrics_type'] = self.calc_metrics_type.GetStringSelection()

        # trigger functions which enable/disable options
        self.on_calc_metrics_type(event = None)
        self.on_demo_matrixFormatRadioBox(event = None)
        self.on_demo_rescaleRadioBox(event = None)

        # set default file paths
        pfdir = sys.path[0]
        self.project['filepaths']['pu_filepath'] = os.path.join(pfdir,"data","shapefiles","marxan_pu.shp")
        self.project['filepaths']['demo_cu_filepath'] = os.path.join(pfdir,"data","shapefiles","connectivity_grid.shp")
        self.project['filepaths']['demo_cu_cm_filepath'] = os.path.join(pfdir,"data","grid_connectivity_matrix.csv")
        self.project['filepaths']['demo_pu_cm_filepath'] = self.project['filepaths']['demo_cu_cm_filepath']
        self.project['filepaths']['cf_filepath'] = os.path.join(os.environ['USERPROFILE'], "Documents","puvspr.dat")
        self.project['filepaths']['spec_filepath'] = os.path.join(os.environ['USERPROFILE'], "Documents","spec.dat")
        self.project['filepaths']['bd_filepath'] = os.path.join(os.environ['USERPROFILE'], "Documents","boundary.dat")

        # set default file paths in the GUI
        self.PU_file.SetPath(self.project['filepaths']['pu_filepath'])
        self.demo_CU_file.SetPath(self.project['filepaths']['demo_cu_filepath'])
        self.demo_CU_CM_file.SetPath(self.project['filepaths']['demo_cu_cm_filepath'])
        self.demo_PU_CM_file.SetPath(self.project['filepaths']['demo_pu_cm_filepath'])
        self.CF_file.SetPath(self.project['filepaths']['cf_filepath'])
        self.SPEC_file.SetPath(self.project['filepaths']['spec_filepath'])
        self.BD_file.SetPath(self.project['filepaths']['bd_filepath'])

        # if called at launch time, no need to ask users to create a new project file right away
        if(not launch):
            dlg = wx.FileDialog(self, "Create a new project file:",style=wx.FD_SAVE,wildcard=wc_MarCon)
            if dlg.ShowModal() == wx.ID_OK:
                self.project['filepaths']['projfile'] = dlg.GetPath()
                self.project['filepaths']['projfilename'] = dlg.GetFilename()
                self.project['workingdirectory'] = dlg.GetDirectory() 
                with open(self.project['filepaths']['projfile'], 'w') as fp:
                    json.dump(self.project, fp, indent=4, sort_keys=True)
                frame.SetTitle('Marxan with Connectivity (Project: '+self.project['filepaths']['projfilename']+')')
            dlg.Destroy()       
        
    def on_load_project(self, event):
        """
        Create and show the Open FileDialog to load a project
        """
        self.project = {}
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.project['workingdirectory'], 
            defaultFile="",
            wildcard=wc_MarCon,
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            self.project['filepaths']['projfile'] = dlg.GetPath()
            with open(self.project['filepaths']['projfile'], 'r') as fp:
                self.project=json.loads(fp.read())
        dlg.Destroy()
        frame.SetTitle('Marxan with Connectivity (Project: '+self.project['filepaths']['projfilename']+')')

        # set default options
        self.demo_PU_CM_export.SetValue(self.project['options']['demo_pu_cm_export'])
        self.demo_PU_CM_progress.SetValue(self.project['options']['demo_pu_cm_progress'])
        self.demo_matrixUnitsRadioBox.SetStringSelection(self.project['options']['demo_conmat_units'])
        self.demo_matrixTypeRadioBox.SetStringSelection(self.project['options']['demo_conmat_type'])
        self.demo_matrixFormatRadioBox.SetStringSelection(self.project['options']['demo_conmat_format'])
        self.demo_rescaleRadioBox.SetStringSelection(self.project['options']['demo_conmat_rescale'])
        self.calc_metrics_type.SetStringSelection(self.project['options']['calc_metrics_type'])

        # trigger functions which enable/disable options
        self.on_calc_metrics_type(event = None)
        self.on_demo_matrixFormatRadioBox(event = None)
        self.on_demo_rescaleRadioBox(event = None)

        # set default file paths
        self.PU_file.SetPath(self.project['filepaths']['pu_filepath'])
        self.demo_CU_file.SetPath(self.project['filepaths']['demo_cu_filepath'])
        self.demo_CU_CM_file.SetPath(self.project['filepaths']['demo_cu_cm_filepath'])
        self.demo_PU_CM_file.SetPath(self.project['filepaths']['demo_pu_cm_filepath'])
        self.CF_file.SetPath(self.project['filepaths']['cf_filepath'])
        self.SPEC_file.SetPath(self.project['filepaths']['spec_filepath'])
        self.BD_file.SetPath(self.project['filepaths']['bd_filepath'])

    def on_save_project_as(self, event):
        """
        Create and show the Open FileDialog to save a project
        """
        dlg = wx.FileDialog(
            self, message="Save file as ...", 
            defaultDir=self.project['workingdirectory'], 
            defaultFile="", wildcard=wc_MarCon, style=wx.FD_SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            self.project['filepaths']['projfile'] = dlg.GetPath()
            self.project['filepaths']['projfilename'] = dlg.GetFilename()
            self.project['workingdirectory'] = dlg.GetDirectory()
            with open(self.project['filepaths']['projfile'], 'w') as fp:
                json.dump(self.project, fp, indent=4, sort_keys=True)
        dlg.Destroy()
        frame.SetTitle('Marxan with Connectivity (Project: '+self.project['filepaths']['projfilename']+')')
	
    def on_save_project( self, event ):
        """
        save a project, but call 'on_save_project_as' if project file has not previously been defined
        """
        if 'projfile' in self.project['filepaths']:
            with open(self.project['filepaths']['projfile'], 'w') as fp:
                json.dump(self.project, fp, indent=4, sort_keys=True)
        else:
            self.on_save_project_as(event=None)

########################### html pop-up functions ################################

    def on_glossary( self, event ):
        wx.LaunchDefaultBrowser("glossary.html")
	
    def on_tutorial( self, event ):
        wx.LaunchDefaultBrowser("tutorial.html")
	
    def on_github( self, event ):
        wx.LaunchDefaultBrowser("https://github.com/remi-daigle/MarxanConnect/issues")
	
    def on_contributing( self, event ):
        wx.LaunchDefaultBrowser("contributing.html")

    def on_license( self, event ):
        with open('LICENSE', 'r', encoding="utf8") as file :
            filedata = file.read()
        dlg = wx.MessageBox(message = filedata,
                            caption = "Marxan with Connectivity License",
                            style=wx.OK)
        dlg.Destroy()
    
    def on_about( self, event ):
        dlg = wx.MessageBox(message = "Version: v0.0.2\n(C) 2017 Remi Daigle\n",
                            caption = "About Marxan with Connectivity",
                            style=wx.OK)
        dlg.Destroy()

    def on_getting_started( self, event ):
        # insert getting started tab and hyperlinks (wxFormBuilder can't handle hyperlinks)
        frame = getting_started(parent = self)
        frame.Show()
     
###########################  warning functions ################################
    def warn_dialog(self, message, caption = "Warning!"):
        """
        Warning
        """
        dlg = wx.MessageBox(message, caption, style=wx.OK | wx.ICON_WARNING)

###########################  map plotting functions ###########################
    def on_plot_map_button(self, event):
        """
        Initiates map plotting. Creates a 'Plot' tab, plots the basemap (if desired) and calls 'draw_shapefiles' to plot
         up to 2 other shapefiles
        """
        if not hasattr(self, 'plot'):
            self.plot = wx.Panel(self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            self.auinotebook.AddPage(self.plot, u"7) Plot", False, wx.NullBitmap)
        self.plot.figure = plt.figure()
        self.plot.axes = self.plot.figure.gca()
        self.plot.canvas = FigureCanvas(self.plot, -1, self.plot.figure)
        self.plot.sizer = wx.BoxSizer(wx.VERTICAL)
        self.plot.sizer.Add(self.plot.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.plot.SetSizer(self.plot.sizer)
        self.plot.Fit()
        
        pu = gpd.GeoDataFrame.from_file(self.project['filepaths']['pu_filepath'])
        cu = gpd.GeoDataFrame.from_file(self.project['filepaths']['demo_cu_filepath'])
        
        lonmin, lonmax, latmin, latmax = marxanconpy.buffer_shp_corners([pu,cu],float(self.bmap_buffer.GetValue()))


        self.plot.map = Basemap(llcrnrlon=lonmin, llcrnrlat=latmin, urcrnrlon=lonmax, urcrnrlat=latmax,
                                resolution='i', projection='tmerc', lat_0=(latmin+latmax)/2, lon_0=(lonmin+lonmax)/2)

        #plot basemap
        if(self.bmap_plot_check.GetValue()):
            self.plot.map.drawmapboundary(fill_color=tuple(c/255 for c in self.bmap_oceancol.GetColour()))
            self.plot.map.fillcontinents(color=tuple(c/255 for c in self.bmap_landcol.GetColour()),
                                         lake_color=tuple(c/255 for c in self.bmap_lakecol.GetColour()))
            self.plot.map.drawcoastlines()
        else:
            self.plot.map.drawmapboundary(fill_color='white')
        
        #plot first layer
        if(self.lyr1_plot_check.GetValue()):
            if(self.lyr1_choice.GetChoiceCtrl().GetCurrentSelection()==0):
                metric = self.get_con_feature_data()
                self.draw_shapefiles(sf = pu, metric = metric, lowcol = self.pu_metric_lowcol.GetColour(),
                                     hicol = self.pu_metric_hicol.GetColour(),
                                     trans = self.pu_metric_alpha.GetValue()/100,
                                     legend = self.pu_metric_legend.GetCurrentSelection())
            elif(self.lyr1_choice.GetChoiceCtrl().GetCurrentSelection()==1):
                metric = self.get_con_feature_data()
                self.draw_shapefiles(sf = cu, metric = metric, lowcol = self.cu_metric_lowcol.GetColour(),
                                     hicol = self.cu_metric_hicol.GetColour(),
                                     trans = self.cu_metric_alpha.GetValue()/100,
                                     legend = self.cu_metric_legend.GetCurrentSelection())
            elif(self.lyr1_choice.GetChoiceCtrl().GetCurrentSelection()==2):
                self.draw_shapefiles(sf = pu, colour = self.pu_poly_col.GetColour(),
                                     trans = self.pu_poly_alpha.GetValue()/100)
            else:
                self.draw_shapefiles(sf = cu, colour = self.cu_poly_col.GetColour(),
                                     trans = self.cu_poly_alpha.GetValue()/100)
        
        #plot second layer
        if(self.lyr2_plot_check.GetValue()):
            if(self.lyr2_choice.GetChoiceCtrl().GetCurrentSelection()==0):
                metric = self.get_con_feature_data()
                self.draw_shapefiles(sf = pu, metric = metric, lowcol = self.pu_metric_lowcol1.GetColour(),
                                     hicol = self.pu_metric_hicol1.GetColour(),
                                     trans = self.pu_metric_alpha1.GetValue()/100,
                                     legend = self.pu_metric_legend1.GetCurrentSelection())
            elif(self.lyr2_choice.GetChoiceCtrl().GetCurrentSelection()==1):
                metric = self.get_con_feature_data()
                self.draw_shapefiles(sf = cu, metric = metric, lowcol = self.cu_metric_lowcol1.GetColour(),
                                     hicol = self.cu_metric_hicol1.GetColour(),
                                     trans = self.cu_metric_alpha1.GetValue()/100,
                                     legend = self.cu_metric_legend1.GetCurrentSelection())
            elif(self.lyr2_choice.GetChoiceCtrl().GetCurrentSelection()==2):
                self.draw_shapefiles(sf = pu,
                                     colour = self.pu_poly_col1.GetColour(),
                                     trans = self.pu_poly_alpha1.GetValue()/100)
            else:
                self.draw_shapefiles(sf = cu,
                                     colour = self.cu_poly_col1.GetColour(),
                                     trans = self.cu_poly_alpha1.GetValue()/100)
        
        #change selection to plot tab
        for i in range(self.auinotebook.GetPageCount()):
            if self.auinotebook.GetPageText(i) == "7) Plot":
                self.auinotebook.ChangeSelection(i)

    def draw_shapefiles(self, sf, colour=None, trans=None, metric=None, lowcol=None, hicol=None, legend=None):
        """
        Draws the desired shapefile on the plot created by 'on_plot_map_button'
        """
        if(metric==None):
            patches = []
            colour=tuple(c/255 for c in tuple(c/255 for c in colour))
            for poly in sf.geometry:
                mpoly = shapely.ops.transform(self.plot.map, poly)
                patches.append(PolygonPatch(mpoly))
            self.plot.axes.add_collection(PatchCollection(patches, match_original=True, color=colour, alpha=trans))
        else:
            patches = []
            #define colormap
            c1=tuple(c/255 for c in lowcol)
            c2=tuple(c/255 for c in hicol)
            
            seq = [(None,) * 4, 0.0] + list((c1,c2)) + [1.0, (None,) * 4]
            cdict = {'red': [], 'green': [], 'blue': []}
            for i, item in enumerate(seq):
                if isinstance(item, float):
                    r1, g1, b1, a = seq[i - 1]
                    r2, g2, b2, a = seq[i + 1]
                    cdict['red'].append([item, r1, r2])
                    cdict['green'].append([item, g1, g2])
                    cdict['blue'].append([item, b1, b2])
            cmap = matplotlib.colors.LinearSegmentedColormap('CustomMap', cdict)
                    
            norm = matplotlib.colors.Normalize(min(metric), max(metric))
            bins = numpy.linspace(min(metric), max(metric), 10)
            color_producer = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)
            for poly, evc in zip(sf.geometry, metric):
                rgba = color_producer.to_rgba(evc)
                mpoly = shapely.ops.transform(self.plot.map, poly)
                patches.append(PolygonPatch(mpoly,color=rgba))
    
            self.plot.axes.add_collection(PatchCollection(patches, match_original=True, alpha=trans))
            if(legend==0):
                self.plot.ax_legend = self.plot.figure.add_axes([0.415, 0.8, 0.2, 0.04], zorder=3)
                self.plot.cb = matplotlib.colorbar.ColorbarBase(self.plot.ax_legend,
                                                                cmap=cmap,
                                                                ticks=bins,
                                                                boundaries=bins,
                                                                orientation='horizontal')
                self.plot.cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])
            elif(legend==1):
                self.plot.ax_legend = self.plot.figure.add_axes([0.415, 0.15, 0.2, 0.04], zorder=3)
                self.plot.cb = matplotlib.colorbar.ColorbarBase(self.plot.ax_legend,
                                                                cmap=cmap,
                                                                ticks=bins,
                                                                boundaries=bins,
                                                                orientation='horizontal')
                self.plot.cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])
                

###########################  graph plotting functions #########################

    def on_plot_graph_button(self, event):
        """
        Initiates graph plotting. Creates a 'Plot' tab, and call 'on_draw_graph' to plot the graph
        """
        if not hasattr(self, 'plot'):
            self.plot = wx.Panel(self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            self.auinotebook.AddPage(self.plot, u"7) Plot", False, wx.NullBitmap)
        self.plot.figure = plt.figure()
        self.plot.axes = self.plot.figure.gca()
        self.plot.canvas = FigureCanvas(self.plot, -1, self.plot.figure)
        self.plot.sizer = wx.BoxSizer(wx.VERTICAL)
        self.plot.sizer.Add(self.plot.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.plot.SetSizer(self.plot.sizer)
        self.plot.Fit()
        self.on_draw_graph(pucm_filedir=self.project['filepaths']['pucm_filedir'],
                           pucm_filename=self.project['filepaths']['pucm_filename'])
        for i in range(self.auinotebook.GetPageCount()):
            if self.auinotebook.GetPageText(i) == "7) Plot":
                self.auinotebook.ChangeSelection(i)

    def on_draw_graph(self,pucm_filedir, pucm_filename):
        """
        Draws the desired graph on the plot created by 'on_plot_graph_button'
        """
        demo_cu_cm_filepath = os.path.join(pucm_filedir, pucm_filename)
        conmat = pandas.read_csv(demo_cu_cm_filepath, index_col=0)
        g1 = nx.from_numpy_matrix(conmat.as_matrix())
        mapping = dict(zip(g1.nodes(), conmat.index))
        g1 = nx.relabel_nodes(g1, mapping)
        nx.draw_networkx(g1,with_labels=True,edge_color='lightgray')

###########################  file management functions ########################
    def on_PU_file(self, event):
        """
        Defines Planning Unit file path
        """
        self.project['filepaths']['pu_filepath'] = self.PU_file.GetPath()

    def on_demo_CU_file(self, event):
        """
        Defines Connectivity Unit file path
        """
        self.project['filepaths']['demo_cu_filepath']=self.demo_CU_file.GetPath()

    def on_demo_CU_CM_file(self, event ):
        """
        Defines Connectivity Matrix file path
        """
        self.project['filepaths']['demo_cu_cm_filepath'] = self.demo_CU_CM_file.GetPath()

        # reset filepaths
        if self.demo_rescaleRadioBox.GetStringSelection() == "Identical Grids":
            self.project['filepaths']['demo_pu_cm_filepath'] = self.demo_CU_CM_file.GetPath()
            self.demo_PU_CM_file.SetPath(self.project['filepaths']['demo_pu_cm_filepath'])

        # check format
        self.check_matrix_list_format(format = self.demo_matrixFormatRadioBox.GetStringSelection(),
                                      filepath = self.demo_CU_CM_file.GetPath())

    def on_demo_PU_CM_file(self, event):
        """
        Defines Planning Unit scaled Connectivity Matrix file path
        """
        self.project['filepaths']['demo_pu_cm_filepath'] = self.demo_PU_CM_file.GetPath()
        
    def on_FA_file(self, event):
        """
        Defines Focus Areas file path
        """
        self.project['filepaths']['fa_filepath'] = self.FA_file.GetPath()
        
    def on_CF_file(self, event):
        """
        Defines Focus Areas file path
        """
        self.project['filepaths']['cf_filepath'] = self.CF_file.GetPath()
        
    def on_SPEC_file(self, event):
        """
        Defines Focus Areas file path
        """
        self.project['filepaths']['spec_filepath'] = self.SPEC_file.GetPath()
        
    def on_BD_file(self, event):
        """
        Defines Focus Areas file path
        """
        self.project['filepaths']['bd_filepath'] = self.BD_file.GetPath()

    def check_matrix_list_format(self, format, filepath):
        print('checking')
        # warn if matrix is wrong format
        if format == "Matrix":
            print('matrix')
            self.conmat = pandas.read_csv(filepath, index_col=0)
        else:
            if format == "List":
                self.ncol = 3
                self.expected = numpy.array(['id1', 'id2', 'value'])
            elif format == "List with Time":
                self.ncol = 3
                self.expected = numpy.array(['time','id1', 'id2', 'value'])
            self.conmat = pandas.read_csv(filepath)
            self.message = "See the Glossary for 'Data Formats' under 'Connectivity'."
            self.warn = False
            if not self.conmat.shape[1]==self.ncol:
                self.message=self.message+" The "+format+" Data Format expects exactly "+self.ncol+" columns, not "+\
                             str(self.conmat.shape[1])+" in the file."
                self.warn = True

            self.missing = [c not in self.conmat.columns for c in self.expected]
            if any(self.missing):
                self.message = self.message + " The "+format+" Data Format expects column header(s) '"+\
                               str(self.expected[self.missing]) +\
                               "' which may be missing in the file."
                self.warn = True
            if self.warn:
                self.warn_dialog(message = self.message)


    ###########################  option setting functions ###########################
    def on_demo_matrixUnitsRadioBox(self, event):
        self.project['options']['demo_conmat_units'] = self.demo_matrixUnitsRadioBox.GetStringSelection()

    def on_demo_matrixTypeRadioBox(self, event):
        self.project['options']['demo_conmat_type'] = self.demo_matrixTypeRadioBox.GetStringSelection()

    def on_demo_matrixFormatRadioBox(self, event):
        self.project['options']['demo_conmat_format'] =self.demo_matrixFormatRadioBox.GetStringSelection()
        if self.demo_matrixFormatRadioBox.GetStringSelection() == "List with Time":
            self.cf_demo_stochasticity.Enable(enable=True)
        else:
            self.cf_demo_stochasticity.Enable(enable=False)

    def on_demo_rescaleRadioBox(self, event):
        """
        Hides unnecessary options if rescaling is not necessary
        """
        # hide or unhide
        self.project['options']['demo_conmat_rescale'] = self.demo_rescaleRadioBox.GetStringSelection()
        if(self.demo_rescaleRadioBox.GetStringSelection()=="Identical Grids"):
            self.demo_CU_def.Enable(enable = False)
            self.demo_CU_filetext.Enable(enable = False)
            self.demo_CU_file.Enable(enable = False)
            self.demo_PU_CM_outputtext.Enable(enable = False)
            self.demo_PU_CM_def.Enable(enable = False)
            self.demo_PU_CM_export.Enable(enable=False)
            self.demo_PU_CM_progress.Enable(enable=False)
            self.demo_PU_CM_filetext.Enable(enable = False)
            self.demo_PU_CM_file.Enable(enable = False)
            self.demo_rescale_button.Enable(enable = False)
        else:
            self.demo_CU_def.Enable(enable = True)
            self.demo_CU_filetext.Enable(enable = True)
            self.demo_CU_file.Enable(enable = True)
            self.demo_PU_CM_outputtext.Enable(enable = True)
            self.demo_PU_CM_def.Enable(enable = True)
            self.demo_PU_CM_export.Enable(enable=True)
            self.demo_PU_CM_progress.Enable(enable=True)
            if self.demo_PU_CM_export.GetValue():
                self.demo_PU_CM_filetext.Enable(enable = True)
                self.demo_PU_CM_file.Enable(enable = True)
            self.demo_rescale_button.Enable(enable = True)

        # reset filepaths
        if self.demo_rescaleRadioBox.GetStringSelection()=="Identical Grids":
            self.project['filepaths']['demo_pu_cm_filepath'] = self.demo_CU_CM_file.GetPath()
            self.demo_PU_CM_file.SetPath(self.project['filepaths']['demo_pu_cm_filepath'])
        else:
            self.project['filepaths']['demo_pu_cm_filepath'] = self.demo_PU_CM_file.GetPath()

    def on_demo_rescale_button(self, event):
        """
        Rescales the connectivity matrix to match the scale of the planning units
        """
        ProcessThreading(parent=self, rescale_matrix = True)

    def on_demo_PU_CM_export(self, event):
        """
        Checks if the planning unit connectivity matrix should be exported when rescaling
        """
        self.project['options']['demo_pu_cm_export'] = self.demo_PU_CM_export.GetValue()
        if self.demo_PU_CM_export.GetValue():
            self.demo_PU_CM_filetext.Enable(enable=True)
            self.demo_PU_CM_file.Enable(enable=True)
        else:
            self.demo_PU_CM_filetext.Enable(enable = False)
            self.demo_PU_CM_file.Enable(enable = False)

    def on_demo_PU_CM_progress(self, event):
        """
        Checks if the planning unit connectivity matrix progress bar should be activated. (It freezes up the GUI)
        """
        self.project['options']['demo_pu_cm_progress'] = self.demo_PU_CM_progress.GetValue()

    def on_calc_metrics_type(self, event):
        """
        Choose correct matrix for demographic metrics
        """
        if(self.calc_metrics_type.GetCurrentSelection()==0):
            self.type = 'pu'
        elif (self.calc_metrics_type.GetCurrentSelection() == 1):
            self.type = 'cu'

###########################  metric related functions #########################
    def on_calc_metrics(self, event):
        """
        calculates the selected metrics
        """
        # create dict entry for connectivityMetrics
        if not 'connectivityMetrics' in self.project:
            self.project['connectivityMetrics']={}

        # check format
        self.check_matrix_list_format(format=self.demo_matrixFormatRadioBox.GetStringSelection(),
                                          filepath=self.project['filepaths']['demo_'+self.type+'_cm_filepath'])

        # load correct matrix and transform if necessary
        if os.path.isfile(self.project['filepaths']['demo_'+self.type+'_cm_filepath']):
            if self.demo_matrixFormatRadioBox.GetStringSelection()=="Matrix":
                self.conmat = pandas.read_csv(self.project['filepaths']['demo_'+self.type+'_cm_filepath'],index_col= 0)
                self.project['connectivityMetrics']['demo_'+self.type+'_cm_conmat'] = self.conmat.to_json(orient='split')
            elif self.demo_matrixFormatRadioBox.GetStringSelection()=="List":
                self.conmat = pandas.read_csv(self.project['filepaths']['demo_'+self.type+'_cm_filepath'])
                self.conmat = self.conmat.pivot_table(values = 'value', index = 'id1', columns = 'id2')
                self.project['connectivityMetrics']['demo_'+self.type+'_cm_conmat'] = self.conmat.to_json(orient='split')
            elif self.demo_matrixFormatRadioBox.GetStringSelection()=="List with Time":
                self.conmat_time = pandas.read_csv(self.project['filepaths']['demo_' + self.type + '_cm_filepath'])
                self.conmat = self.conmat_time[['id1', 'id2', 'value']].groupby(['id1', 'id2']).mean()
                self.conmat = self.conmat.pivot_table(values='value', index='id1', columns='id2')
                self.project['connectivityMetrics']['demo_' + self.type + '_cm_conmat'] = self.conmat.to_json(
                    orient='split')
                self.project['connectivityMetrics']['demo_' + self.type + '_cm_conmat_time'] = self.conmat_time.to_json(
                    orient='split')

                self.warn_dialog(message = "A connectivity 'List with Time' was provided; however, all metrics except "
                                           "'Temporal Connectivity Correlation' will be calculated from the temporal"
                                           "mean of connectivity")
        else:
            self.warn_dialog(message="File not found: "+self.project['filepaths']['demo_'+self.type+'_cm_filepath'])
            

        # create dict entries for boundary and spec, also enable customize spec
        if not 'spec_'+self.type in self.project['connectivityMetrics']:
            self.project['connectivityMetrics']['spec_'+self.type]={}
            self.customize_spec.Enable(enable=True)
            self.CFT_percent_slider.Enable(enable=True)
            self.export_metrics.Enable(enable=True)
            self.custom_spec_panel.SetToolTip(None)
        if not 'boundary' in self.project['connectivityMetrics']:
            self.project['connectivityMetrics']['boundary']={}

        # calculate demographic metrics
        if(self.cf_demo_vertex_degree.GetValue()):
            self.project['connectivityMetrics']['spec_'+self.type]['demo_vertex_degree_'+self.type] = \
                marxanconpy.conmat2vertexdegree(self.conmat)

        if(self.cf_demo_between_cent.GetValue()):
            self.project['connectivityMetrics']['spec_'+self.type]['demo_between_cent_'+self.type] = \
                marxanconpy.conmat2betweencent(self.conmat)

        if(self.cf_demo_eig_vect_cent.GetValue()):
            self.project['connectivityMetrics']['spec_'+self.type]['demo_eig_vect_cent_'+self.type] = \
                marxanconpy.conmat2eigvectcent(self.conmat)

        if(self.cf_demo_self_recruit.GetValue()):
            self.project['connectivityMetrics']['spec_'+self.type]['demo_self_recruit_'+self.type] = \
                marxanconpy.conmat2selfrecruit(self.conmat)

        if(self.bd_demo_conn_boundary.GetValue()):
            self.project['connectivityMetrics']['boundary']['demo_conn_boundary_'+self.type] = \
                marxanconpy.conmat2connboundary(self.conmat)

        if(self.bd_demo_min_plan_graph.GetValue()):
           self.project['connectivityMetrics']['boundary']['demo_min_plan_graph_'+self.type] = \
               marxanconpy.conmat2minplanarboundary(self.conmat)

        # choose correct matrix for genetic metrics
        # insert stuff here!
        # calculate genetic metrics
        # insert stuff here!
        
        # choose correct matrix for landscape metrics
        # insert stuff here!
        # calculate landscape metrics
        # insert stuff here!

        # create initial spec
        self.on_new_spec()

    def on_export_metrics(self, event):
        # Export or append feature files
        if self.cf_export_radioBox.GetSelection()==0:
            # export spec
            spec = pandas.read_json(self.project['spec_'+self.type+'_dat'], orient = 'split')
            spec.to_csv(self.project['filepaths']['spec_filepath'], index=0)
            # export conservation features
            cf = self.project['connectivityMetrics']['spec_'+self.type].copy()
            cf['pu'] = pandas.read_json(self.project['connectivityMetrics']['demo_'+self.type+'_cm_conmat'],
                                        orient = 'split').index
            cf = pandas.DataFrame(cf).melt(id_vars=['pu'], var_name='name', value_name='amount')
            cf = pandas.merge(cf,spec,how='outer',on='name')
            cf = cf.rename(columns = {'id':'species'}).sort_values(['species','pu'])
            cf[['species','pu','amount']].to_csv(self.project['filepaths']['cf_filepath'], index=0)

        elif self.cf_export_radioBox.GetSelection()==1:
            # append
            old_spec = pandas.read_csv(self.project['filepaths']['spec_filepath'])
            old_cf = pandas.read_csv(self.project['filepaths']['cf_filepath'])

            # append spec
            new_spec = pandas.read_json(self.project['spec_'+self.type+'_dat'], orient='split')
            new_spec['id'] = new_spec['id']+max(old_spec['id'])

            pandas.concat([old_spec,new_spec]).to_csv(str.replace(self.project['filepaths']['spec_filepath'],
                                                                    ".dat",
                                                                    "_appended.dat")
                                                      , index=0)
            # append conservation features
            new_cf = self.project['connectivityMetrics']['spec_'+self.type].copy()
            new_cf['pu'] = pandas.read_json(self.project['connectivityMetrics']['demo_'+self.type+'_cm_conmat'],
                                            orient = 'split').index
            new_cf = pandas.DataFrame(new_cf).melt(id_vars=['pu'], var_name='name', value_name='amount')
            new_cf = pandas.merge(new_cf, new_spec, how='outer', on='name')
            new_cf = new_cf.rename(columns={'id': 'species'}).sort_values(['species', 'pu'])
            pandas.concat([old_cf,new_cf[['species', 'pu', 'amount']]]).to_csv(
                str.replace(self.project['filepaths']['cf_filepath'], ".dat", "_appended.dat"), index=0)

        if self.BD_filecheck.GetValue():
            self.export_boundary_file(BD_filepath = self.project['filepaths']['bd_filepath'])

    def export_boundary_file(self, BD_filepath):

        multiple = [self.bd_demo_conn_boundary.GetValue(),
                    self.bd_demo_min_plan_graph.GetValue()].count(True)>1
        
        # Export each selected boundary definition            
        if self.bd_demo_conn_boundary.GetValue():
            if multiple:
                pandas.read_json(self.project['connectivityMetrics']['boundary']['demo_conn_boundary_'+self.type],
                                 orient='split').to_csv(str.replace(BD_filepath,
                                                                    ".dat",
                                                                    "_demo_conn_boundary_"+self.type+".dat"),
                                                        index = False)
            else:
                pandas.read_json(self.project['connectivityMetrics']['boundary']['demo_conn_boundary_'+self.type],
                                 orient='split').to_csv(BD_filepath, index = False)
        
        if self.bd_demo_min_plan_graph.GetValue():
            if multiple:
                pandas.read_json(self.project['connectivityMetrics']['boundary']['demo_min_plan_graph_'+self.type],
                                 orient='split').to_csv(str.replace(BD_filepath,
                                                                    ".dat",
                                                                    "_demo_min_plan_graph_"+self.type+".dat"),
                                                        index = False)
            else:
                pandas.read_json(self.project['connectivityMetrics']['boundary']['demo_min_plan_graph_'+self.type],
                                 orient='split').to_csv(BD_filepath, index = False)
        
        # warn when multiple boundary definitions
        if multiple:
            self.warn_dialog(message = "Multiple Boundary Definitions were selected. Boundary file names have been"
                                       " edited to include type.", caption = "Warning!")
        
    def get_con_feature_data(self):
        """
        returns the pre-calculated metric for plotting
        """
        #choose metric
        if(self.type=='pu'):
            metricindex = self.pu_metric_choice.GetCurrentSelection()
        elif(self.type=='cu'):
            metricindex = self.cu_metric_choice.GetCurrentSelection()

        #get metric
        if(metricindex==0):
            metric = self.project['connectivityMetrics']['spec_'+self.type]['demo_vertex_degree_'+self.type]
        elif(metricindex==1):
            metric = self.project['connectivityMetrics']['spec_'+self.type]['demo_between_cent_'+self.type]
        elif(metricindex==2):
            metric = self.project['connectivityMetrics']['spec_'+self.type]['demo_eig_vect_cent_'+self.type]
        elif(metricindex==3):
            metric = self.project['connectivityMetrics']['spec_'+self.type]['demo_self_recruit_'+self.type]
            
        return(metric)

###########################  spec grid popup functions #########################
    def on_customize_spec(self, event):
        self.spec_frame.Show()

    def on_new_spec(self):
        self.spec_frame=spec_customizer(parent=self)
        self.spec_frame.keys = list(self.project['connectivityMetrics']['spec_'+self.type])
        
        for i in range(len(self.spec_frame.keys)):
            self.spec_frame.spec_grid.InsertRows(i)
            self.spec_frame.spec_grid.SetCellValue(i,0,str(i+1))
            sum_metric = sum(self.project['connectivityMetrics']['spec_'+self.type][self.spec_frame.keys[i]])
            self.spec_frame.spec_grid.SetCellValue(i,1,str(sum_metric*self.CFT_percent_slider.GetValue()/100))
            self.spec_frame.spec_grid.SetCellValue(i,2,str(1000))
            self.spec_frame.spec_grid.SetCellValue(i,3,self.spec_frame.keys[i])
            w,h = self.spec_frame.GetClientSize()

            self.spec_frame.SetSize((w+16, h+39+20))
            self.spec_frame.Layout()

        self.project['spec_'+self.type+'_dat'] = pandas.DataFrame(
            numpy.full((self.spec_frame.spec_grid.GetNumberCols(), self.spec_frame.spec_grid.GetNumberRows()), None))
        self.project['spec_'+self.type+'_dat'].columns = ["id", "target", "spf", "name"]

        for c in range(self.spec_frame.spec_grid.GetNumberCols()):
            for r in range(self.spec_frame.spec_grid.GetNumberRows()):
                self.project['spec_'+self.type+'_dat'].iloc[r, c] = self.spec_frame.spec_grid.GetCellValue(r, c)
        self.project['spec_'+self.type+'_dat'] = self.project['spec_'+self.type+'_dat'].to_json(orient = 'split')

    def on_CFT_percent_slider(self, event):
        self.on_new_spec()

class spec_customizer (gui.spec_customizer):
    def __init__( self, parent ):
        gui.spec_customizer.__init__(self,parent)
        self.parent = parent
        
    def on_spec_ok( self, event ):
        self.parent.project['spec_'+self.parent.type+'_dat'] = pandas.DataFrame(numpy.full((self.spec_grid.GetNumberCols(),
                                                                                self.spec_grid.GetNumberRows()),None))
        self.parent.project['spec_'+self.parent.type+'_dat'].columns = ["id","target","spf","name"]

        for c in range(self.spec_grid.GetNumberCols()):
            for r in range(self.spec_grid.GetNumberRows()):
                self.parent.project['spec_'+self.parent.type+'_dat'].iloc[r,c] = self.spec_grid.GetCellValue(r,c)
        self.parent.project['spec_'+self.parent.type+'_dat'] = self.parent.project['spec_'+self.parent.type+'_dat'].to_json()
        self.Hide()
	
    def on_spec_cancel( self, event ):
        self.Hide()

###########################  getting started popup functions #########################
class getting_started(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Marxan with Connectivity: Getting Started",
                          pos = wx.DefaultPosition,
                          size = wx.Size( 900,700 ),
                          style=wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT)
        self.gettingStarted = wx.Panel(self)
        self.Center()
        # set the icon
        icons = wx.IconBundle()
        for sz in [16, 32, 48, 96, 256]: 
            try: 
                icon = wx.Icon(os.path.join(sys.path[0],'icon_bundle.ico'),
                               wx.BITMAP_TYPE_ICO,
                               desiredWidth=sz,
                               desiredHeight=sz)
                icons.AddIcon(icon) 
            except: 
                pass 
                self.SetIcons(icons)
        
        startMainSizer = wx.FlexGridSizer( 3, 1, 0, 0 )
        startMainSizer.AddGrowableRow( 0 )
#        startMainSizer.AddGrowableRow( 1 )
#        startMainSizer.AddGrowableRow( 2 )
        startMainSizer.SetFlexibleDirection( wx.VERTICAL )
        startMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
        sizer02 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.gettingstartedtxt = wx.StaticText( self.gettingStarted,
                                                wx.ID_ANY,
                                                u"Welcome to Marxan with Connectivity!\n\nMarxan with Connectivity"
                                                u" (henceforth the \"app\") is a Graphical User Interface (GUI) to help"
                                                u" conservationists include “connectivity” in their protected area"
                                                u" network planning.\n\nThe term \"connectivity\" has a variety of"
                                                u" definitions (i.e. larval connectivity, genetic connectivity, "
                                                u"landscape connectivity, etc) and protected area networks can be "
                                                u"optimized for various connectivity objectives. The app is intended to"
                                                u" guide conservationists through the process of identifying important"
                                                u" aspects of connectivity for their conservation scenarios as well as"
                                                u" highlighting the necessary data.\n\nThe app also includes be a fully"
                                                u" functional python module (in progress) that is operated via command"
                                                u" line that can be used to reproduce an analysis using the project"
                                                u" file generated by the GUI.\n\nTo use this software, please visit the"
                                                u" Tutorial and the Glossary which can be accessed under the help menu,"
                                                u" or the links below (in progress). Otherwise, if you would just like "
                                                u"to get started, please proceed through all the tabs from left to "
                                                u"right starting the \"Spatial Input\". After calculating the"
                                                u" \"Connectivity Metrics\", you can choose to conduct a Marxan"
                                                u" analysis in the app (maybe), export the connectivity metrics for use"
                                                u" in a standalone custom Marxan analysis, or you can visualize the"
                                                u" Connectivity Metrics using the \"Plotting Options\" tab\n\nIf you"
                                                u" would like to report any bugs or request a missing feature, please"
                                                u" post an issue on the GitHub repository which is available in the"
                                                u" help menu, or the link below.",
                                                wx.DefaultPosition,
                                                wx.DefaultSize, 0 )
        self.gettingstartedtxt.Wrap( -1 )
        sizer02.Add( self.gettingstartedtxt, 0, wx.ALL|wx.EXPAND, 5 )
		
        startMainSizer.Add( sizer02, 1, wx.EXPAND, 5 )
		
        hyperlinksizer = wx.BoxSizer( wx.VERTICAL )
        self.tutoriallink = wx.adv.HyperlinkCtrl( self.gettingStarted,
                                                  wx.ID_ANY, u"Tutorial",
                                                  u"tutorial.html",
                                                  wx.DefaultPosition,
                                                  wx.DefaultSize)
        hyperlinksizer.Add( self.tutoriallink, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
    		
        self.glossarylink = wx.adv.HyperlinkCtrl( self.gettingStarted,
                                                  wx.ID_ANY,
                                                  u"Glossary",
                                                  u"glossary.html",
                                                  wx.DefaultPosition,
                                                  wx.DefaultSize)
        hyperlinksizer.Add( self.glossarylink, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
    		
        self.githublink = wx.adv.HyperlinkCtrl( self.gettingStarted,
                                                wx.ID_ANY,
                                                u"GitHub Issues",
                                                u"https://github.com/remi-daigle/MarxanConnect/issues",
                                                wx.DefaultPosition,
                                                wx.DefaultSize)
        hyperlinksizer.Add( self.githublink, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
        
        startMainSizer.Add( hyperlinksizer, 1, wx.EXPAND, 5 )
        
        iconsizer = wx.BoxSizer( wx.VERTICAL )
		
        self.m_bitmap1 = wx.StaticBitmap( self.gettingStarted,
                                          wx.ID_ANY, wx.Bitmap(os.path.join(sys.path[0],'icon_bundle.ico'),
                                                                wx.BITMAP_TYPE_ANY ),
                                          wx.DefaultPosition, wx.DefaultSize, 0 )
        iconsizer.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        startMainSizer.Add( iconsizer, 1, wx.EXPAND, 5 )
        
        self.gettingStarted.SetSizer( startMainSizer )
        self.gettingStarted.Layout()
        startMainSizer.Fit( self.gettingStarted )        



########################################################################################################################

###########################  threading #########################
class ProcessThreading(object):
    """
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, parent, rescale_matrix = False):
        self.parent = parent
        self.rescale_matrix = rescale_matrix

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution

    def run(self):
        if self.rescale_matrix:
            # create dict entry for connectivityMetrics
            if not 'connectivityMetrics' in self.parent.project:
                self.parent.project['connectivityMetrics'] = {}
            print('rescaling')
            self.parent.project['connectivityMetrics']['demo_pu_cm_conmat'] = marxanconpy.rescale_matrix(
                self.parent.project['filepaths']['pu_filepath'],
                self.parent.project['filepaths']['demo_cu_filepath'],
                self.parent.project['filepaths']['demo_cu_cm_filepath'],
                progressbar=self.parent.project['options']['demo_pu_cm_progress']).to_json(orient='split')

            if self.parent.demo_PU_CM_export.GetValue():
                pandas.read_json(self.parent.project['connectivityMetrics']['demo_pu_cm_conmat'],orient='split').to_csv(
                    self.parent.project['filepaths']['demo_pu_cm_filepath'], index=True, header=True, sep=",")
            print("done!")
###########################  run the GUI ######################################
app = wx.App(False)
 
#create an object of CalcFrame
frame = MarxanConnectGUI(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()

#stop the app
app.Destroy()
