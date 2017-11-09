# importing wx files
import wx
import wx.lib.agw.aui as aui
import wx.adv

# import gui
import gui

# import matplotlib
import matplotlib

matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap

# import spatial modules
import geopandas as gpd
from descartes import PolygonPatch
import shapely

# import system helper modules
import os
import sys
import pandas
import numpy
# import networkx as nx
import subprocess
import json

# import MarxanConnect python module
import marxanconpy

# define wildcards
wc_MarCon = "Marxan with Connectivity Project (*.MarCon)|*.MarCon|" \
            "All files (*.*)|*.*"


class MarxanConnectGUI(gui.MarxanConnectGUI):
    def __init__(self, parent):
        """
        initialize parent class (the entire GUI)
        """
        gui.MarxanConnectGUI.__init__(self, parent)
        # set the icon
        self.set_icon(frame=self)

        # start up log
        # self.log = LogForm(parent=self)

        # Either load or launch new project
        if len(sys.argv) > 1:
            self.project = {}
            self.project['filepaths'] = {}
            self.project['filepaths']['projfile'] = str(sys.argv[1])
            self.load_project_function()
        else:
            # launch a blank new project
            self.on_new_project(event=None, launch=True)

            # launch Getting started window
            frame = GettingStarted (parent=self)
            frame.Show()

        # set opening tab to Spatial Input (0)
        self.auinotebook.ChangeSelection(0)

        # set tooltips for radioboxes
        self.demo_matrixTypeRadioBox.SetItemToolTip(0, "Settlement Matrix - S [i,j] = dij * μt; where μ = survivorship probability at time t. S is the cumulative or total settlement over an entire dispersal simulation from every patch i to every patch j. Note that a postsettlement mortality could be applied to this matrix to more closely represent recruitment potential (ie realised connectivity). This matrix represents the dispersal connection strengths based on the biophysical dispersal model. A series of S matrices can be aggregated (i.e., different spawning events over many years) for the same life-history characteristics to represent the dispersal potential of a species. The S matrix is used to calculate all other connectivity matrices described below.")
        self.demo_matrixTypeRadioBox.SetItemToolTip(1, "Connectivity Probability Matrix - P [i,j] = (sij / Total Released from i ). Probability of settling on patch j from patch i, representing potential recruitment or surviving larvae. This matrix is often referred to as the discrete dispersal kernel, and the transpose of P, PT, is the population transition matrix (Caswell 1989). Row sums are often << 1 due to larval loss from mortality and larvae never reaching suitable habitat. Each row is a discrete version of the dispersal kernel (Botsford 2009b, also see Werner et al. 2007). Note, when patches are of different sizes, the largest patches will have relatively lower connection probabilities (due to greater denominator). Diag(P) represents percent local-retention at each source patch.")
        self.demo_matrixTypeRadioBox.SetItemToolTip(2, "Migration Matrix - M [i,j] = (sij / Column-sum j), where mij represents the proportion of settlers in patch j that came from patch i. This matrix quantifies the proportion of immigrants (sources) to each destination patch. Diag(M) represents percent self-recruitment. M corresponds to migration matrix models in population genetics (Bodmer and Cavalli-Sforza 1968) and the source distribution matrix (Cowen et al. 2007), and has been used to explore diversity patterns in neutral communities (Ecomonomo and Keitt 2008).")
        self.demo_matrixTypeRadioBox.SetItemToolTip(3, "Local Immigration Matrix - I [i,j] = (sij / Total Released from j). Proportion of the released larvae from destination patch j that settle from source patch i. Values are in terms of the destination patch's size (or dispersal potential) and indicate the potential level of local impact. Can be used to define a demographically relevant settlement rate (e.g., Cowen et al. 2006, Table S1) in terms of the proportion of larvae released from a source population that are required to settle in the focal population to maintain a standard population size (Treml et al. in 2012, Table S4).")
        self.demo_matrixTypeRadioBox.SetItemToolTip(4, "Dispersal Flux Matrix (normalised) - F[i,j] = (Area i / Total Area of habitat in network) * P'ij; where P' is the probability matrix that is row-normalized by i's row-sum, casting probability in terms of successful settlers. F may be a more ecologically meaningful representation of network-wide dispersal, where connectivity is dependent on the source strength of the donor patch and the probability of connection (Urban and Keitt 2001). F is used for exploring patterns in system-wide connectivity using network analysis (Treml et al. in 2012, Treml et al. 2008, Urban and Keitt 2001).")

        self.outline_shapefile_choices()

    def set_icon(self, frame):
        # set the icon
        icons = wx.IconBundle()
        for sz in [16, 32, 48, 96, 256]:
            try:
                icon = wx.Icon(os.path.join(sys.path[0], 'icon_bundle.ico'),
                               wx.BITMAP_TYPE_ICO,
                               desiredWidth=sz,
                               desiredHeight=sz)
                icons.AddIcon(icon)
            except:
                pass
                frame.SetIcons(icons)

# ##########################  project managment functions ##############################################################

    def on_new_project(self, event, launch=False):
        """
        open a new project and name/save a new project file
        """
        # create project list to store project specific data
        self.project = {}
        self.project['workingdirectory'] = os.path.expanduser(os.path.join("~", "Documents"))
        self.project['filepaths'] = {}
        self.project['options'] = {}

        # set default options
        self.project['options']['demo_pu_cm_progress'] = self.demo_PU_CM_progress.GetValue()
        self.project['options']['demo_conmat_units'] = self.demo_matrixUnitsRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_type'] = self.demo_matrixTypeRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_format'] = self.demo_matrixFormatRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_rescale'] = self.demo_rescaleRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_rescale_edge'] = self.demo_rescale_edgeRadioBox.GetStringSelection()
        self.project['options']['gen_pu_cm_progress'] = self.gen_PU_CM_progress.GetValue()
        self.project['options']['gen_conmat_type'] = self.gen_matrixTypeRadioBox.GetStringSelection()
        self.project['options']['gen_conmat_format'] = self.gen_matrixFormatRadioBox.GetStringSelection()
        self.project['options']['gen_conmat_rescale'] = self.gen_rescaleRadioBox.GetStringSelection()
        self.project['options']['gen_conmat_rescale_edge'] = self.gen_rescale_edgeRadioBox.GetStringSelection()
        self.project['options']['land_hab_buff'] = self.land_HAB_buff.GetValue()
        self.project['options']['land_pu_cm_progress'] = self.land_PU_CM_progress.GetValue()
        self.project['options']['land_conmat_type'] = self.land_matrixTypeRadioBox.GetStringSelection()
        self.project['options']['calc_metrics_pu'] = self.calc_metrics_pu.GetValue()
        self.project['options']['calc_metrics_cu'] = self.calc_metrics_cu.GetValue()
        self.project['options']['metricsCalculated'] = False

        # set default file paths
        pfdir = sys.path[0]
        docdir = self.project['workingdirectory']

        # spatial input
        self.project['filepaths']['pu_filepath'] = ""
        self.project['filepaths']['pu_file_pu_id'] = ""
        self.project['filepaths']['fa_filepath'] = ""
        self.project['filepaths']['aa_filepath'] = ""

        # connectivity input
        self.project['filepaths']['demo_cu_filepath'] = ""
        self.project['filepaths']['demo_cu_file_pu_id'] = ""
        self.project['filepaths']['demo_cu_cm_filepath'] = ""
        self.project['filepaths']['demo_pu_cm_filepath'] = ""
        self.project['filepaths']['gen_cu_filepath'] = ""
        self.project['filepaths']['gen_cu_file_pu_id'] = ""
        self.project['filepaths']['gen_cu_cm_filepath'] = ""
        self.project['filepaths']['gen_pu_cm_filepath'] = ""
        self.project['filepaths']['land_cu_filepath'] = ""
        self.project['filepaths']['land_cu_file_pu_id'] = ""
        self.project['filepaths']['land_cu_cm_filepath'] = ""
        self.project['filepaths']['land_pu_cm_filepath'] = ""
        self.project['filepaths']['land_hab_filepath'] = ""
        self.project['filepaths']['land_hab_file_hab_id'] = ""
        self.project['filepaths']['land_res_mat_filepath'] = ""
        self.project['filepaths']['land_res_filepath'] = ""
        self.project['filepaths']['land_res_file_res_id'] = ""

        # Marxan metrics files
        self.project['filepaths']['cf_filepath'] = os.path.join(pfdir, "data", "GBR", "input", "puvspr2.dat")
        self.project['filepaths']['spec_filepath'] = os.path.join(pfdir, "data", "GBR", "input", "spec.dat")
        self.project['filepaths']['bd_filepath'] = os.path.join(pfdir, "data", "GBR", "input", "boundary.dat")

        # Marxan analysis
        self.project['filepaths']['marxan_input'] = os.path.join(pfdir, "data", "GBR", "input.dat")
        self.project['filepaths']['marxan_dir'] = os.path.join(pfdir, "Marxan243")

        # set default file paths in GUI
        self.set_GUI_filepaths()

        # trigger functions which enable/disable options
        self.on_demo_matrixFormatRadioBox(event=None)
        self.on_demo_rescaleRadioBox(event=None)
        self.on_gen_matrixFormatRadioBox(event=None)
        self.on_gen_rescaleRadioBox(event=None)
        self.on_land_matrixTypeRadioBox(event=None)
        self.enable_metrics()
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()
        self.colormap_metric_choices(1)
        self.colormap_metric_choices(2)

        # if called at launch time, no need to ask users to create a new project file right away
        if not launch:
            dlg = wx.FileDialog(self, "Create a new project file:", style=wx.FD_SAVE, wildcard=wc_MarCon)
            if dlg.ShowModal() == wx.ID_OK:
                self.project['filepaths']['projfile'] = dlg.GetPath()
                self.project['filepaths']['projfilename'] = dlg.GetFilename()
                self.project['workingdirectory'] = dlg.GetDirectory()
                with open(self.project['filepaths']['projfile'], 'w') as fp:
                    json.dump(self.project, fp, indent=4, sort_keys=True)
                frame.SetTitle('Marxan with Connectivity (Project: ' + self.project['filepaths']['projfilename'] + ')')
            dlg.Destroy()

    def on_load_project(self, event):
        """
        Create and show the Open FileDialog to load a project
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.project['workingdirectory'],
            defaultFile="",
            wildcard=wc_MarCon,
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.project = {}
            self.project['filepaths'] = {}
            self.project['filepaths']['projfile'] = dlg.GetPath()
        dlg.Destroy()

        self.load_project_function()

    def load_project_function(self):
        with open(self.project['filepaths']['projfile'], 'r') as fp:
            self.project = json.loads(fp.read())

        self.SetTitle('Marxan with Connectivity (Project: ' + self.project['filepaths']['projfilename'] + ')')

        # set default options
        self.demo_PU_CM_progress.SetValue(self.project['options']['demo_pu_cm_progress'])
        self.demo_matrixUnitsRadioBox.SetStringSelection(self.project['options']['demo_conmat_units'])
        self.demo_matrixTypeRadioBox.SetStringSelection(self.project['options']['demo_conmat_type'])
        self.demo_matrixFormatRadioBox.SetStringSelection(self.project['options']['demo_conmat_format'])
        self.demo_rescaleRadioBox.SetStringSelection(self.project['options']['demo_conmat_rescale'])
        self.demo_rescale_edgeRadioBox.SetStringSelection(self.project['options']['demo_conmat_rescale_edge'])

        self.gen_PU_CM_progress.SetValue(self.project['options']['gen_pu_cm_progress'])
        self.gen_matrixTypeRadioBox.SetStringSelection(self.project['options']['gen_conmat_type'])
        self.gen_matrixFormatRadioBox.SetStringSelection(self.project['options']['gen_conmat_format'])
        self.gen_rescaleRadioBox.SetStringSelection(self.project['options']['gen_conmat_rescale'])
        self.gen_rescale_edgeRadioBox.SetStringSelection(self.project['options']['gen_conmat_rescale_edge'])

        self.land_HAB_buff.SetValue(self.project['options']['land_hab_buff'])
        self.land_PU_CM_progress.SetValue(self.project['options']['land_pu_cm_progress'])
        self.land_matrixTypeRadioBox.SetStringSelection(self.project['options']['land_conmat_type'])

        self.calc_metrics_pu.SetValue(self.project['options']['calc_metrics_pu'])
        self.calc_metrics_cu.SetValue(self.project['options']['calc_metrics_cu'])

        # set default file paths in GUI
        self.set_GUI_filepaths()

        # trigger functions which enable/disable options
        self.on_demo_matrixFormatRadioBox(event=None)
        self.on_demo_rescaleRadioBox(event=None)
        if self.project['options']['metricsCalculated']:
            self.customize_spec.Enable(enable=True)
            self.CFT_percent_slider.Enable(enable=True)
            self.export_metrics.Enable(enable=True)
            self.custom_spec_panel.SetToolTip(None)
        self.enable_metrics()
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()
        self.colormap_metric_choices(1)
        self.colormap_metric_choices(2)

    def set_GUI_filepaths(self):
        # set default file paths
        # spatial input
        self.PU_file.SetPath(self.project['filepaths']['pu_filepath'])
        self.set_GUI_id_selection(self.PU_file_pu_id, self.project['filepaths']['pu_filepath'],
                                  self.project['filepaths']['pu_file_pu_id'])
        self.FA_file.SetPath(self.project['filepaths']['fa_filepath'])
        self.AA_file.SetPath(self.project['filepaths']['aa_filepath'])

        # connectivity input
        self.demo_CU_file.SetPath(self.project['filepaths']['demo_cu_filepath'])
        self.set_GUI_id_selection(self.demo_CU_file_pu_id, self.project['filepaths']['demo_cu_filepath'],
                                  self.project['filepaths']['demo_cu_file_pu_id'])
        self.demo_CU_CM_file.SetPath(self.project['filepaths']['demo_cu_cm_filepath'])
        self.demo_PU_CM_file.SetPath(self.project['filepaths']['demo_pu_cm_filepath'])
        self.gen_CU_file.SetPath(self.project['filepaths']['gen_cu_filepath'])
        self.set_GUI_id_selection(self.gen_CU_file_pu_id, self.project['filepaths']['gen_cu_filepath'],
                                  self.project['filepaths']['gen_cu_file_pu_id'])
        self.gen_CU_CM_file.SetPath(self.project['filepaths']['gen_cu_cm_filepath'])
        self.gen_PU_CM_file.SetPath(self.project['filepaths']['gen_pu_cm_filepath'])
        self.land_HAB_file.SetPath(self.project['filepaths']['land_hab_filepath'])
        self.set_GUI_id_selection(self.land_HAB_file_hab_id, self.project['filepaths']['land_hab_filepath'],
                                  self.project['filepaths']['land_hab_file_hab_id'])
        self.land_RES_mat_file.SetPath(self.project['filepaths']['land_res_mat_filepath'])
        self.land_PU_CM_file.SetPath(self.project['filepaths']['land_pu_cm_filepath'])
        self.land_RES_file.SetPath(self.project['filepaths']['land_res_filepath'])
        self.set_GUI_id_selection(self.land_RES_file_res_id, self.project['filepaths']['land_res_filepath'],
                                  self.project['filepaths']['land_res_file_res_id'])

        # Marxan metrics files
        self.CF_file.SetPath(self.project['filepaths']['cf_filepath'])
        self.SPEC_file.SetPath(self.project['filepaths']['spec_filepath'])
        self.BD_file.SetPath(self.project['filepaths']['bd_filepath'])

        # Marxan analysis
        self.inputdat_file.SetPath(self.project['filepaths']['marxan_input'])
        self.marxan_dir.SetPath(self.project['filepaths']['marxan_dir'])

    def set_GUI_id_selection(self,choice,filepath,id):
        if(os.path.isfile(filepath)):
            choice.SetItems(list(gpd.GeoDataFrame.from_file(filepath)))
            choice.SetStringSelection(id)

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
        frame.SetTitle('Marxan with Connectivity (Project: ' + self.project['filepaths']['projfilename'] + ')')

    def on_save_project(self, event):
        """
        save a project, but call 'on_save_project_as' if project file has not previously been defined
        """
        if 'projfile' in self.project['filepaths']:
            with open(self.project['filepaths']['projfile'], 'w') as fp:
                json.dump(self.project, fp, indent=4, sort_keys=True)
        else:
            self.on_save_project_as(event=None)

# ########################## html pop-up functions #####################################################################

    def openhtml(self, html):
        if os.name == 'nt':
            wx.LaunchDefaultBrowser(html)
        else:
            os.system("open " + html)

    def on_glossary(self, event):
        self.openhtml("glossary.html")

    def on_tutorial(self, event):
        self.openhtml("tutorial.html")

    def on_github(self, event):
        self.openhtml("https://github.com/remi-daigle/MarxanConnect/issues")

    def on_contributing(self, event):
        self.openhtml("contributing.html")

    def on_license(self, event):
        with open('LICENSE', 'r', encoding="utf8") as file:
            filedata = file.read()
        dlg = wx.MessageBox(message=filedata,
                            caption="Marxan with Connectivity License",
                            style=wx.OK)
        dlg.Destroy()

    def on_about(self, event):
        dlg = wx.MessageBox(message="Version: v0.0.2\n(C) 2017 Remi Daigle\n",
                            caption="About Marxan with Connectivity",
                            style=wx.OK)
        dlg.Destroy()

    def on_GettingStarted (self, event):
        # insert getting started tab and hyperlinks (wxFormBuilder can't handle hyperlinks)
        frame = GettingStarted (parent=self)
        frame.Show()

# ##########################  warning functions ########################################################################
    def warn_dialog(self, message, caption="Warning!"):
        """
        Warning
        """
        dlg = wx.MessageBox(message, caption, style=wx.OK | wx.ICON_WARNING)

# ##########################  map plotting functions ###################################################################
    def on_plot_map_button(self, event):
        """
        Initiates map plotting. Creates a 'Plot' tab, plots the basemap (if desired) and calls 'draw_shapefiles' to plot
         up to 2 other shapefiles
        """
        # warn if no connectivity metrics
        if not 'connectivityMetrics' in self.project:
            self.warn_dialog(
                message="No connectivity metrics have been calculated yet, please return to the 'Connectivity "
                        "Metrics' tab to calculate metrics before attempting to plot.")
            return  # end plotting

        # prepare plotting window
        if not hasattr(self, 'plot'):
            self.plot = wx.Panel(self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            self.auinotebook.AddPage(self.plot, u"7) Plot", False, wx.NullBitmap)
        self.plot.figure = plt.figure(figsize=self.plot.GetClientSize()/wx.ScreenDC().GetPPI()[0])
        self.plot.axes = self.plot.figure.gca()
        self.plot.canvas = FigureCanvas(self.plot, -1, self.plot.figure)
        self.plot.sizer = wx.BoxSizer(wx.VERTICAL)
        self.plot.sizer.Add(self.plot.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.plot.SetSizer(self.plot.sizer)
        self.plot.Fit()

        # load lyr1 shapefile and data
        sf1, colour1, trans1, metric1, lowcol1, hicol1, legend1 = [None for i in range(7)]
        if self.lyr1_plot_check.GetValue():
            if self.lyr1_choice.GetChoiceCtrl().GetStringSelection() == "Colormap of connectivity metrics":
                lowcol1 = self.metric_lowcol.GetColour()
                hicol1 = self.metric_hicol.GetColour()
                trans1 = self.metric_alpha.GetValue() / 100
                legend1 = self.metric_legend.GetCurrentSelection()
                type1 = self.get_plot_type(selection=self.metric_shp_choice.GetStringSelection())
                metric_type1 = self.get_metric_type(selection=self.metric_choice.GetStringSelection())
                if type1 == "pu":
                    metric1 = self.project['connectivityMetrics'][metric_type1]
                else:
                    metric1 = self.project['connectivityMetrics']['spec_' + type1][metric_type1 + type1]


            elif self.lyr1_choice.GetChoiceCtrl().GetStringSelection() == "Outline of shapefile":
                colour1 = self.poly_col.GetColour()
                trans1 = self.poly_alpha.GetValue() / 100
                type1 = self.get_plot_type(selection=self.poly_shp_choice.GetStringSelection())

            if type1[-2:] == "pu":
                sf1 = gpd.GeoDataFrame.from_file(self.project['filepaths']['pu_filepath']).to_crs({'init': 'epsg:4326'})
            else:
                sf1 = gpd.GeoDataFrame.from_file(self.project['filepaths'][type1 + '_filepath']).to_crs({'init': 'epsg:4326'})

            # warn and break if shapefile not the same size as metrics
            if self.lyr1_choice.GetChoiceCtrl().GetStringSelection() == "Colormap of connectivity metrics":
                if not sf1.shape[0] == len(metric1):
                    self.warn_dialog(message="The selected shapefile does not have the expected number of rows. There "
                                             "are " + str(len(metric1)) + " rows in the selected metric and " + str(
                        sf1.shape[0]) +
                                             " rows in the shapefile")
                    return

        # load lyr2 shapefile and data
        sf2, colour2, trans2, metric2, lowcol2, hicol2, legend2 = [None for i in range(7)]
        if self.lyr2_plot_check.GetValue():
            if self.lyr2_choice.GetChoiceCtrl().GetStringSelection() == "Colormap of connectivity metrics":
                lowcol2 = self.metric_lowcol1.GetColour()
                hicol2 = self.metric_hicol1.GetColour()
                trans2 = self.metric_alpha1.GetValue() / 100
                legend2 = self.metric_legend1.GetCurrentSelection()
                type2 = self.get_plot_type(selection=self.metric_shp_choice1.GetStringSelection())
                metric_type2 = self.get_metric_type(selection=self.metric_choice1.GetStringSelection())
                if type2 == "pu":
                    metric2 = self.project['connectivityMetrics'][metric_type2]
                else:
                    metric2 = self.project['connectivityMetrics']['spec_' + type2][metric_type2 + type2]

            elif self.lyr2_choice.GetChoiceCtrl().GetStringSelection() == "Outline of shapefile":
                colour2 = self.poly_col1.GetColour()
                trans2 = self.poly_alpha1.GetValue() / 100
                type2 = self.get_plot_type(selection=self.poly_shp_choice1.GetStringSelection())

            if type2[-2:] == "pu":
                sf2 = gpd.GeoDataFrame.from_file(self.project['filepaths']['pu_filepath']).to_crs({'init': 'epsg:4326'})
            else:
                sf2 = gpd.GeoDataFrame.from_file(self.project['filepaths'][type2 + '_filepath']).to_crs({'init': 'epsg:4326'})

            # warn and break if shapefile not the same size as metrics
            if self.lyr2_choice.GetChoiceCtrl().GetStringSelection() == "Colormap of connectivity metrics":
                if not sf2.shape[0] == len(metric2):
                    self.warn_dialog(message="The selected shapefile does not have the expected number of rows. There "
                                             "are " + str(len(metric2)) + " rows in the selected metric and " + str(
                        sf2.shape[0]) +
                                             " rows in the shapefile")
                    return

        if self.lyr1_plot_check.GetValue() and self.lyr2_plot_check.GetValue():
            gdf_list = [sf1, sf2]
        elif self.lyr1_plot_check.GetValue():
            gdf_list = [sf1]
        elif self.lyr2_plot_check.GetValue():
            gdf_list = [sf2]
        else:
            self.warn_dialog(message="No data layers were selected")
            lonmin, lonmax, latmin, latmax = -180, 180, -90, -90

        lonmin, lonmax, latmin, latmax = marxanconpy.buffer_shp_corners(gdf_list, float(self.bmap_buffer.GetValue()))


        self.plot.map = Basemap(llcrnrlon=lonmin, llcrnrlat=latmin, urcrnrlon=lonmax, urcrnrlat=latmax,
                                resolution='i', projection='tmerc', lat_0=(latmin + latmax) / 2,
                                lon_0=(lonmin + lonmax) / 2)

        # plot basemap
        if self.bmap_plot_check.GetValue():
            self.plot.map.drawmapboundary(fill_color=tuple(c / 255 for c in self.bmap_oceancol.GetColour()))
            self.plot.map.fillcontinents(color=tuple(c / 255 for c in self.bmap_landcol.GetColour()),
                                         lake_color=tuple(c / 255 for c in self.bmap_lakecol.GetColour()))
            self.plot.map.drawcoastlines()
        else:
            self.plot.map.drawmapboundary(fill_color='white')

        # plot first layer
        if self.lyr1_plot_check.GetValue():
            self.draw_shapefiles(sf=sf1,
                                 colour=colour1,
                                 trans=trans1,
                                 metric=metric1,
                                 lowcol=lowcol1,
                                 hicol=hicol1,
                                 legend=legend1)

        # plot second layer
        if self.lyr2_plot_check.GetValue():
            self.draw_shapefiles(sf=sf2,
                                 colour=colour2,
                                 trans=trans2,
                                 metric=metric2,
                                 lowcol=lowcol2,
                                 hicol=hicol2,
                                 legend=legend2)

        # change selection to plot tab
        for i in range(self.auinotebook.GetPageCount()):
            if self.auinotebook.GetPageText(i) == "7) Plot":
                self.auinotebook.ChangeSelection(i)

    def draw_shapefiles(self, sf, colour=None, trans=None, metric=None, lowcol=None, hicol=None, legend=None):
        """
        Draws the desired shapefile on the plot created by 'on_plot_map_button'
        """
        if metric == None:
            patches = []
            colour = tuple(c / 255 for c in colour)
            for poly in sf.geometry:
                mpoly = shapely.ops.transform(self.plot.map, poly)
                patches.append(PolygonPatch(mpoly))
            self.plot.axes.add_collection(PatchCollection(patches, match_original=True, color=colour, alpha=trans))
        else:
            patches = []
            # define colormap
            c1 = tuple(c / 255 for c in lowcol)
            c2 = tuple(c / 255 for c in hicol)

            seq = [(None,) * 4, 0.0] + list((c1, c2)) + [1.0, (None,) * 4]
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
                patches.append(PolygonPatch(mpoly, color=rgba))

            self.plot.axes.add_collection(PatchCollection(patches, match_original=True, alpha=trans))
            if legend == 0:
                self.plot.ax_legend = self.plot.figure.add_axes([0.415, 0.8, 0.2, 0.04], zorder=3)
                self.plot.cb = matplotlib.colorbar.ColorbarBase(self.plot.ax_legend,
                                                                cmap=cmap,
                                                                ticks=bins,
                                                                boundaries=bins,
                                                                orientation='horizontal')
                self.plot.cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])
            elif legend == 1:
                self.plot.ax_legend = self.plot.figure.add_axes([0.415, 0.15, 0.2, 0.04], zorder=3)
                self.plot.cb = matplotlib.colorbar.ColorbarBase(self.plot.ax_legend,
                                                                cmap=cmap,
                                                                ticks=bins,
                                                                boundaries=bins,
                                                                orientation='horizontal')
                self.plot.cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])

    def outline_shapefile_choices(self):
        choices = []
        if self.project['filepaths']['pu_filepath'] != "":
            choices.append("Planning Units")
        if self.project['filepaths']['fa_filepath'] != "":
            choices.append("Focus Areas")
        if self.project['filepaths']['aa_filepath'] != "":
            choices.append("Avoidance Areas")
        if self.project['filepaths']['demo_cu_filepath'] != "":
            choices.append("Demographic Units")
        if self.project['filepaths']['gen_cu_filepath'] != "":
            choices.append("Genetic Units")
        if self.project['filepaths']['land_cu_filepath'] != "":
            choices.append("Landscape Units")

        self.poly_shp_choice.SetItems(choices)
        self.poly_shp_choice.SetSelection(0)
        self.poly_shp_choice1.SetItems(choices)
        self.poly_shp_choice1.SetSelection(0)

    def colormap_shapefile_choices(self):
        choices = []
        if self.project['filepaths']['demo_cu_filepath'] != "":
            if 'connectivityMetrics' in self.project:
                if 'best_solution' in self.project['connectivityMetrics']:
                    choices.append("Planning Units (Marxan Results)")
            if self.project['filepaths']['demo_cu_filepath'] != "":
                choices.append("Planning Units (Demographic Data)")
            if self.project['filepaths']['gen_cu_filepath'] != "":
                choices.append("Planning Units (Genetic Data)")
            if self.project['filepaths']['land_cu_filepath'] != "":
                choices.append("Planning Units (Landscape Data)")
        if self.project['filepaths']['demo_cu_filepath'] != "":
            choices.append("Demographic Units")
        if self.project['filepaths']['gen_cu_filepath'] != "":
            choices.append("Genetic Units")
        if self.project['filepaths']['land_cu_filepath'] != "":
            choices.append("Landscape Units")

        self.metric_shp_choice.SetItems(choices)
        self.metric_shp_choice.SetSelection(0)
        self.metric_shp_choice1.SetItems(choices)
        self.metric_shp_choice1.SetSelection(0)

    def on_metric_shp_choice(self, event=None):
        self.colormap_metric_choices(1)

    def on_metric_shp_choice1(self, event=None):
        self.colormap_metric_choices(2)

    def colormap_metric_choices(self,lyr):
        choices = []
        if lyr == 1:
            shapefile = self.metric_shp_choice.GetStringSelection()
        else:
            shapefile = self.metric_shp_choice1.GetStringSelection()

        if 'connectivityMetrics' in self.project:
            if shapefile == "Planning Units (Marxan Results)":
                if 'best_solution' in self.project['connectivityMetrics']:
                    choices.append("Selection Frequency")
                    choices.append("Best Solution")
            else:
                plot_type = self.get_plot_type(shapefile)
                print(plot_type)
                if 'spec_' + plot_type in self.project['connectivityMetrics']:
                    if 'vertex_degree_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Vertex Degree")
                    if 'between_cent_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Betweenness Centrality")
                    if 'eig_vect_cent_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Eigen Vector Centrality")
                    if 'self_recruit_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Self Recruitment")
                    if 'outflux_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Outflux")
                    if 'temp_conn_cov_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Temporal Connectivity Covariance")
                    if 'fa_sink_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Focus Area Sink")
                    if 'fa_source_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Focus Area Source")
                    if 'aa_sink_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Avoidance Area Sink")
                    if 'aa_source_' + plot_type in self.project['connectivityMetrics']['spec_' + plot_type].keys():
                        choices.append("Avoidance Area Source")

        if lyr == 1:
            self.metric_choice.SetItems(choices)
            self.metric_choice.SetSelection(0)
        else:
            self.metric_choice1.SetItems(choices)
            self.metric_choice1.SetSelection(0)

    def get_plot_type(self, selection):
        if selection == "Planning Units":
            type = 'pu'
        elif selection == "Planning Units (Marxan Results)":
            type = 'pu'
        elif selection == "Planning Units (Demographic Data)":
            type = 'demo_pu'
        elif selection == "Planning Units (Genetic Data)":
            type = 'gen_pu'
        elif selection == "Planning Units (Landscape Data)":
            type = 'land_pu'
        elif selection == "Demographic Units":
            type = 'demo_cu'
        elif selection == "Genetic Units":
            type = 'gen_cu'
        elif selection == "Landscape Units":
            type = 'land_cu'
        elif selection == "Focus Areas":
            type = 'fa'
        elif selection == "Avoidance Areas":
            type = 'aa'
        return type

    def get_metric_type(self, selection):
        if selection == "Selection Frequency":
            metric_type = 'select_freq'
        elif selection == "Best Solution":
            metric_type = 'best_solution'
        elif selection == "Vertex Degree":
            metric_type = 'vertex_degree_'
        elif selection == "Betweenness Centrality":
            metric_type = 'between_cent_'
        elif selection == "Eigen Vector Centrality":
            metric_type = 'eig_vect_cent_'
        elif selection == "Self Recruitment":
            metric_type = 'self_recruit_'
        elif selection == "Outflux":
            metric_type = 'outflux_'
        elif selection == "Temporal Connectivity Covariance":
            metric_type = 'temp_conn_cov_'
        elif selection == "Focus Area Sink":
            metric_type = 'fa_sink_'
        elif selection == "Focus Area Source":
            metric_type = 'fa_source_'
        elif selection == "Avoidance Area Sink":
            metric_type = 'aa_sink_'
        elif selection == "Avoidance Area Source":
            metric_type = 'aa_source_'
        return metric_type

# ##########################  graph plotting functions #################################################################

    # def on_plot_graph_button(self, event):
    #     """
    #     Initiates graph plotting. Creates a 'Plot' tab, and call 'on_draw_graph' to plot the graph
    #     """
    #     if not hasattr(self, 'plot'):
    #         self.plot = wx.Panel(self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
    #         self.auinotebook.AddPage(self.plot, u"7) Plot", False, wx.NullBitmap)
    #     self.plot.figure = plt.figure()
    #     self.plot.axes = self.plot.figure.gca()
    #     self.plot.canvas = FigureCanvas(self.plot, -1, self.plot.figure)
    #     self.plot.sizer = wx.BoxSizer(wx.VERTICAL)
    #     self.plot.sizer.Add(self.plot.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
    #     self.plot.SetSizer(self.plot.sizer)
    #     self.plot.Fit()
    #     self.on_draw_graph(pucm_filedir=self.project['filepaths']['pucm_filedir'],
    #                        pucm_filename=self.project['filepaths']['pucm_filename'])
    #     for i in range(self.auinotebook.GetPageCount()):
    #         if self.auinotebook.GetPageText(i) == "7) Plot":
    #             self.auinotebook.ChangeSelection(i)
    #
    # def on_draw_graph(self, pucm_filedir, pucm_filename):
    #     """
    #     Draws the desired graph on the plot created by 'on_plot_graph_button'
    #     """
    #     demo_cu_cm_filepath = os.path.join(pucm_filedir, pucm_filename)
    #     conmat = pandas.read_csv(demo_cu_cm_filepath, index_col=0)
    #     g1 = nx.from_numpy_matrix(conmat.as_matrix())
    #     mapping = dict(zip(g1.nodes(), conmat.index))
    #     g1 = nx.relabel_nodes(g1, mapping)
    #     nx.draw_networkx(g1, with_labels=True, edge_color='lightgray')

# ###########################  file management functions ###############################################################
    def on_PU_file(self, event):
        """
        Defines Planning Unit file path
        """
        self.project['filepaths']['pu_filepath'] = self.PU_file.GetPath()
        self.PU_file_pu_id.SetItems(list(gpd.GeoDataFrame.from_file(self.project['filepaths']['pu_filepath'])))
        self.PU_file_pu_id.SetSelection(0)
        self.on_PU_file_pu_id(event=None)
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()

    def on_PU_file_pu_id(self, event):
        """
        Defines ID column label for the Planning Unit file
        """
        self.project['filepaths']['pu_file_pu_id'] = self.PU_file_pu_id.GetStringSelection()

    def on_demo_CU_file(self, event):
        """
        Defines Connectivity Unit file path
        """
        self.project['filepaths']['demo_cu_filepath'] = self.demo_CU_file.GetPath()
        self.demo_CU_file_pu_id.SetItems(list(gpd.GeoDataFrame.from_file(self.project['filepaths']['demo_cu_filepath'])))
        self.demo_CU_file_pu_id.SetSelection(0)
        self.on_demo_CU_file_pu_id(event=None)
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()

    def on_demo_CU_file_pu_id(self, event):
        """
        Defines ID column label for the demographic connectivity unit file
        """
        self.project['filepaths']['demo_cu_file_pu_id'] = self.demo_CU_file_pu_id.GetStringSelection()

    def on_gen_CU_file(self, event):
        """
        Defines genetic Connectivity Unit file path
        """
        self.project['filepaths']['gen_cu_filepath'] = self.gen_CU_file.GetPath()
        self.gen_CU_file_pu_id.SetItems(
            list(gpd.GeoDataFrame.from_file(self.project['filepaths']['gen_cu_filepath'])))
        self.gen_CU_file_pu_id.SetSelection(0)
        self.on_gen_CU_file_pu_id(event=None)
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()

    def on_gen_CU_file_pu_id(self, event):
        """
        Defines ID column label for the genetic connectivity unit file
        """
        self.project['filepaths']['gen_cu_file_pu_id'] = self.gen_CU_file_pu_id.GetStringSelection()

    def on_land_HAB_file(self, event):
        """
        Defines landscape habitat type file path
        """
        self.project['filepaths']['land_hab_filepath'] = self.land_HAB_file.GetPath()
        self.land_HAB_file_hab_id.SetItems(
            list(gpd.GeoDataFrame.from_file(self.project['filepaths']['land_hab_filepath'])))
        self.land_HAB_file_hab_id.SetSelection(0)
        self.on_land_HAB_file_hab_id(event=None)
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()

    def on_land_HAB_file_hab_id(self, event):
        """
        Defines landscape Connectivity Unit file path
        """
        self.project['filepaths']['land_hab_file_hab_id'] = self.land_HAB_file_hab_id.GetStringSelection()

    def on_land_HAB_buff(self, event):
        """
        Defines landscape type connectivity buffer (i.e. the distance between neighbouring planning units at which they
        will be connected for the least cost path analysis.)
        """
        self.project['filepaths']['land_hab_buff'] = self.land_HAB_buff.GetValue()

    def on_land_RES_file(self, event):
        """
        Defines landscape resistance surface file path
        """
        self.project['filepaths']['land_res_filepath'] = self.land_RES_file.GetPath()
        self.land_RES_file_res_id.SetItems(
            list(gpd.GeoDataFrame.from_file(self.project['filepaths']['land_res_filepath'])))
        self.land_RES_file_res_id.SetSelection(0)
        self.on_land_RES_file_hab_id(event=None)
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()

    def on_land_RES_file_hab_id(self, event):
        """
        Defines landscape Connectivity Unit file path
        """
        self.project['filepaths']['land_res_file_hab_id'] = self.land_RES_file_res_id.GetStringSelection()

    def on_demo_CU_CM_file(self, event):
        """
        Defines demographic Connectivity Matrix file path
        """
        self.project['filepaths']['demo_cu_cm_filepath'] = self.demo_CU_CM_file.GetPath()

        # reset filepaths
        self.on_demo_rescaleRadioBox(event=None)

        # check format
        self.check_matrix_list_format(format=self.demo_matrixFormatRadioBox.GetStringSelection(),
                                      filepath=self.demo_CU_CM_file.GetPath())

    def on_demo_PU_CM_file(self, event):
        """
        Defines Planning Unit scaled demographic Connectivity Matrix file path
        """
        self.project['filepaths']['demo_pu_cm_filepath'] = self.demo_PU_CM_file.GetPath()
        # enable metrics
        self.enable_metrics()

    def on_gen_CU_CM_file(self, event):
        """
        Defines genetic Connectivity Matrix file path
        """
        self.project['filepaths']['gen_cu_cm_filepath'] = self.gen_CU_CM_file.GetPath()

        # reset filepaths
        self.on_gen_rescaleRadioBox(event=None)


        # # check format
        # self.check_matrix_list_format(format=self.gen_matrixFormatRadioBox.GetStringSelection(),
        #                               filepath=self.gen_CU_CM_file.GetPath())

    def on_gen_PU_CM_file(self, event):
        """
        Defines Planning Unit scaled genetic Connectivity Matrix file path
        """
        self.project['filepaths']['gen_pu_cm_filepath'] = self.gen_PU_CM_file.GetPath()
        # enable metrics
        self.enable_metrics()

    def on_land_CU_CM_file(self, event):
        """
        Defines landscape Connectivity Matrix file path
        """
        self.project['filepaths']['land_cu_cm_filepath'] = self.land_CU_CM_file.GetPath()

        # reset filepaths
        self.on_land_rescaleRadioBox(event=None)

        # # check format
        # self.check_matrix_list_format(format=self.land_matrixFormatRadioBox.GetStringSelection(),
        #                               filepath=self.land_CU_CM_file.GetPath())

    def on_land_PU_CM_file(self, event):
        """
        Defines landscape Planning Unit scaled Connectivity Matrix file path
        """
        self.project['filepaths']['land_pu_cm_filepath'] = self.land_PU_CM_file.GetPath()
        # enable metrics
        self.enable_metrics()

    def on_FA_file(self, event):
        """
        Defines Focus Areas file path
        """
        self.project['filepaths']['fa_filepath'] = self.FA_file.GetPath()
        # enable metrics
        self.enable_metrics()

    def on_AA_file(self, event):
        """
        Defines Avoidance Areas file path
        """
        self.project['filepaths']['aa_filepath'] = self.AA_file.GetPath()
        # enable metrics
        self.enable_metrics()

    def on_CF_file(self, event):
        """
        Defines conservation features (i.e. puvspr2.dat) file path
        """
        self.project['filepaths']['cf_filepath'] = self.CF_file.GetPath()

    def on_SPEC_file(self, event):
        """
        Defines spec.dat file path
        """
        self.project['filepaths']['spec_filepath'] = self.SPEC_file.GetPath()

    def on_BD_file(self, event):
        """
        Defines Focus Areas file path
        """
        self.project['filepaths']['bd_filepath'] = self.BD_file.GetPath()

    def on_marxan_dir(self, event):
        """
        Defines the directory that contains the Marxan application
        """
        self.project['filepaths']['marxan_dir'] = self.marxan_dir.GetPath()

    def on_inputdat_file(self, event):
        """
        Defines the input file for Marxan
        """
        self.project['filepaths']['marxan_input'] = self.inputdat_file.GetPath()

    def check_matrix_list_format(self, format, filepath):
        # warn if matrix is wrong format
        if format == "Matrix":
            self.conmat = pandas.read_csv(filepath, index_col=0)
        else:
            if format == "List":
                self.ncol = 3
                self.expected = numpy.array(['id1', 'id2', 'value'])
            elif format == "List with Time":
                self.ncol = 4
                self.expected = numpy.array(['time', 'id1', 'id2', 'value'])
            self.conmat = pandas.read_csv(filepath)
            self.message = "See the Glossary for 'Data Formats' under 'Connectivity'."
            self.warn = False
            if not self.conmat.shape[1] == self.ncol:
                self.message = self.message + " The " + format + " Data Format expects exactly " + self.ncol + " columns, not " + \
                               str(self.conmat.shape[1]) + " in the file."
                self.warn = True

            self.missing = [c not in self.conmat.columns for c in self.expected]
            if any(self.missing):
                self.message = self.message + " The " + format + " Data Format expects column header(s) '" + \
                               str(self.expected[self.missing]) + \
                               "' which may be missing in the file."
                self.warn = True
            if self.warn:
                self.warn_dialog(message=self.message)
        return

# ###########################  option setting functions ################################################################
    def on_demo_matrixUnitsRadioBox(self, event):
        self.project['options']['demo_conmat_units'] = self.demo_matrixUnitsRadioBox.GetStringSelection()
        self.enable_metrics()

    def on_demo_matrixTypeRadioBox(self, event):
        self.project['options']['demo_conmat_type'] = self.demo_matrixTypeRadioBox.GetStringSelection()

    def on_demo_matrixFormatRadioBox(self, event):
        self.project['options']['demo_conmat_format'] = self.demo_matrixFormatRadioBox.GetStringSelection()
        self.enable_metrics()

    def on_demo_rescaleRadioBox(self, event):
        """
        Hides unnecessary options if rescaling is not necessary
        """
        # hide or unhide
        self.project['options']['demo_conmat_rescale'] = self.demo_rescaleRadioBox.GetStringSelection()
        if self.demo_rescaleRadioBox.GetStringSelection() == "Identical Grids":
            enable = False
        else:
            enable = True

        self.demo_rescale_edgeRadioBox.Enable(enable)
        self.demo_CU_def.Enable(enable)
        self.demo_CU_filetext.Enable(enable)
        self.demo_CU_file_pu_id.Enable(enable)
        self.demo_CU_file_pu_id_txt.Enable(enable)
        self.demo_CU_file.Enable(enable)
        self.demo_PU_CM_outputtext.Enable(enable)
        self.demo_PU_CM_def.Enable(enable)
        self.demo_PU_CM_progress.Enable(enable)
        self.demo_PU_CM_filetext.Enable(enable)
        self.demo_PU_CM_file.Enable(enable)
        self.demo_rescale_button.Enable(enable)

        # reset filepaths
        # connectivity units planning unit matrix
        if self.demo_rescaleRadioBox.GetStringSelection() == "Identical Grids":
            self.project['filepaths']['demo_pu_cm_filepath'] = self.demo_CU_CM_file.GetPath()
            self.demo_PU_CM_file.SetPath(self.project['filepaths']['demo_pu_cm_filepath'])
            self.project['filepaths']['demo_cu_filepath'] = self.PU_file.GetPath()
            self.demo_CU_file.SetPath(self.project['filepaths']['demo_cu_filepath'])
        else:
            self.project['filepaths']['demo_pu_cm_filepath'] = self.demo_PU_CM_file.GetPath()
            self.project['filepaths']['demo_cu_filepath'] = self.demo_CU_file.GetPath()

        # enable metrics
        self.enable_metrics()

    def on_demo_rescale_edgeRadioBox(self, event):
        self.project['options']['demo_conmat_rescale_edge'] = self.demo_rescale_edgeRadioBox.GetStringSelection()

    def on_gen_rescaleRadioBox(self, event):
        """
        Hides unnecessary options if rescaling is not necessary
        """
        # hide or unhide
        self.project['options']['gen_conmat_rescale'] = self.gen_rescaleRadioBox.GetStringSelection()
        if self.gen_rescaleRadioBox.GetStringSelection() == "Identical Grids":
            enable = False
        else:
            enable = True

        self.gen_CU_def.Enable(enable)
        self.gen_CU_filetext.Enable(enable)
        self.gen_CU_file.Enable(enable)
        self.gen_CU_file_pu_id.Enable(enable)
        self.gen_CU_file_pu_id_txt.Enable(enable)
        self.gen_PU_CM_outputtext.Enable(enable)
        self.gen_PU_CM_def.Enable(enable)
        self.gen_PU_CM_progress.Enable(enable)
        self.gen_PU_CM_filetext.Enable(enable)
        self.gen_PU_CM_file.Enable(enable)
        self.gen_rescale_button.Enable(enable)

        # reset filepaths
        # connectivity units planning unit matrix
        if self.gen_rescaleRadioBox.GetStringSelection() == "Identical Grids":
            self.project['filepaths']['gen_pu_cm_filepath'] = self.gen_CU_CM_file.GetPath()
            self.gen_PU_CM_file.SetPath(self.project['filepaths']['gen_pu_cm_filepath'])
            self.project['filepaths']['gen_cu_filepath'] = self.PU_file.GetPath()
            self.gen_CU_file.SetPath(self.project['filepaths']['gen_cu_filepath'])
        else:
            self.project['filepaths']['gen_pu_cm_filepath'] = self.gen_PU_CM_file.GetPath()
            self.project['filepaths']['gen_cu_filepath'] = self.gen_CU_file.GetPath()

        # enable metrics
        self.enable_metrics()

    def on_gen_matrixTypeRadioBox(self, event):
        self.project['options']['gen_conmat_type'] = self.gen_matrixTypeRadioBox.GetStringSelection()

    def on_gen_matrixFormatRadioBox(self, event):
        self.project['options']['gen_conmat_format'] = self.gen_matrixFormatRadioBox.GetStringSelection()
        self.enable_metrics()

    def on_land_matrixTypeRadioBox(self, event):
        """
        Hides unnecessary options if rescaling is not necessary
        """
        # hide or unhide
        self.project['options']['land_matrixType'] = self.land_matrixTypeRadioBox.GetStringSelection()
        if self.project['options']['land_matrixType'] == "Resistance Surface":
            enable_hab = False
            enable_surface = True
        elif self.project['options']['land_matrixType'] == "Connectivity Matrix":
            enable_hab = False
            enable_surface = False
        else:
            enable_hab = True
            enable_surface = True

        self.land_HAB_filetext.Enable(enable_hab)
        self.land_HAB_file.Enable(enable_hab)
        self.land_HAB_file_hab_id_txt.Enable(enable_hab)
        self.land_HAB_file_hab_id.Enable(enable_hab)
        self.land_RES_mat_filetext.Enable(enable_hab)
        self.land_RES_mat_file.Enable(enable_hab)
        self.resistance_mat_customize.Enable(enable_hab)

        self.land_RES_filetext.Enable(enable_surface)
        self.land_RES_file.Enable(enable_surface)
        self.land_RES_def.Enable(enable_surface)
        self.land_res_file_res_id_txt.Enable(enable_surface)
        self.land_RES_file_res_id.Enable(enable_surface)
        self.land_generate_button.Enable(enable_surface)
        self.land_PU_CM_progress.Enable(enable_surface)

        # enable metrics
        self.enable_metrics()

    def on_demo_PU_CM_progress(self, event):
        """
        Checks if the planning unit connectivity matrix progress bar should be activated. (It freezes up the GUI)
        """
        self.project['options']['demo_pu_cm_progress'] = self.demo_PU_CM_progress.GetValue()

    def on_debug_mode(self, event):
        """
        Shows/Hides the debug window.
        """
        if self.log.IsShown():
            self.log.Hide()
        else:
            self.log.Show()
        return

    def enable_metrics(self):
        if self.project['filepaths']['demo_pu_cm_filepath'] != "":
            demo_enable = True
            if self.project['filepaths']['fa_filepath'] != "":
                demo_fa_enable = True
                if self.demo_matrixFormatRadioBox.GetStringSelection() == "List with Time":
                    demo_fa_time_enable = True
                else:
                    demo_fa_time_enable = False
            else:
                demo_fa_enable = False
                demo_fa_time_enable = False

            if self.demo_matrixUnitsRadioBox.GetStringSelection() == "Individuals":
                demo_ind_enable = True
            else:
                demo_ind_enable = False
            if self.project['filepaths']['aa_filepath'] != "":
                demo_aa_enable = True
            else:
                demo_aa_enable = False

        else:
            demo_enable = False
            demo_fa_enable = False
            demo_fa_time_enable = False
            demo_ind_enable = False
            demo_aa_enable = False

        if self.project['filepaths']['gen_pu_cm_filepath'] != "":
            gen_enable = True
            if self.project['filepaths']['fa_filepath'] != "":
                gen_fa_enable = True
            else:
                gen_fa_enable = False

            if self.project['filepaths']['aa_filepath'] != "":
                gen_aa_enable = True
            else:
                gen_aa_enable = False

        else:
            gen_enable = False
            gen_fa_enable = False
            gen_aa_enable = False

        if self.project['filepaths']['land_pu_cm_filepath'] != "":
            land_enable = True
            if self.project['filepaths']['fa_filepath'] != "":
                land_fa_enable = True
            else:
                land_fa_enable = False

            if self.project['filepaths']['aa_filepath'] != "":
                land_aa_enable = True
            else:
                land_aa_enable = False

        else:
            land_enable = False
            land_fa_enable = False
            land_aa_enable = False

        self.cf_demo_vertex_degree.Enable(enable=demo_enable)
        self.cf_demo_between_cent.Enable(enable=demo_enable)
        self.cf_demo_eig_vect_cent.Enable(enable=demo_enable)
        self.cf_demo_self_recruit.Enable(enable=demo_enable)
        self.cf_demo_outflux.Enable(enable=demo_ind_enable)
        self.cf_demo_stochasticity.Enable(enable=demo_fa_time_enable)
        self.cf_demo_fa_sink.Enable(enable=demo_fa_enable)
        self.cf_demo_fa_source.Enable(enable=demo_fa_enable)
        self.cf_demo_aa_sink.Enable(enable=demo_aa_enable)
        self.cf_demo_aa_source.Enable(enable=demo_aa_enable)

        self.cf_gen_vertex_degree.Enable(enable=gen_enable)
        self.cf_gen_between_cent.Enable(enable=gen_enable)
        self.cf_gen_eig_vect_cent.Enable(enable=gen_enable)
        self.cf_gen_self_recruit.Enable(enable=gen_enable)
        self.cf_gen_fa_sink.Enable(enable=gen_fa_enable)
        self.cf_gen_fa_source.Enable(enable=gen_fa_enable)
        self.cf_gen_aa_sink.Enable(enable=gen_aa_enable)
        self.cf_gen_aa_source.Enable(enable=gen_aa_enable)

        self.cf_land_vertex_degree.Enable(enable=land_enable)
        self.cf_land_between_cent.Enable(enable=land_enable)
        self.cf_land_eig_vect_cent.Enable(enable=land_enable)
        self.cf_land_fa_sink.Enable(enable=land_fa_enable)
        self.cf_land_fa_source.Enable(enable=land_fa_enable)
        self.cf_land_aa_sink.Enable(enable=land_aa_enable)
        self.cf_land_aa_source.Enable(enable=land_aa_enable)

# ########################## rescaling and matrix generation ###########################################################
    def on_demo_rescale_button(self, event):
        """
        Rescales the connectivity matrix to match the scale of the planning units
        """
        self.check_matrix_list_format(format=self.demo_matrixFormatRadioBox.GetStringSelection(),
                                      filepath=self.project['filepaths']['demo_cu_cm_filepath'])
        self.temp = {}
        # create dict entry for connectivityMetrics

        if 'connectivityMetrics' not in self.project:

            self.project['connectivityMetrics'] = {}

        self.temp['demo_pu_conmat'] = marxanconpy.rescale_matrix(
            self.project['filepaths']['pu_filepath'],
            self.project['filepaths']['pu_file_pu_id'],
            self.project['filepaths']['demo_cu_filepath'],
            self.project['filepaths']['demo_cu_file_pu_id'],
            self.project['filepaths']['demo_cu_cm_filepath'],
            matrixformat=self.project['options']['demo_conmat_format'],
            edge=self.project['options']['demo_conmat_rescale_edge'],
            progressbar=self.project['options']['demo_pu_cm_progress'])

        if self.demo_matrixFormatRadioBox.GetStringSelection() == "List with Time":
            self.temp['demo_pu_conmat_time'] = self.temp['demo_pu_conmat'][
                self.temp['demo_pu_conmat']['time'] != 'mean'].copy().melt(id_vars=['time', 'id1'],
                                                                           var_name='id2',
                                                                           value_name='value').to_json(
                orient='split')
            self.temp['demo_pu_conmat'] = self.temp['demo_pu_conmat'][
                self.temp['demo_pu_conmat']['time'] == 'mean'].drop(['id1', 'time'], axis=1).to_json(
                orient='split')
            pandas.read_json(self.temp['demo_pu_conmat_time'],
                             orient='split').to_csv(
                self.project['filepaths']['demo_pu_cm_filepath'],
                index=False, header=True, sep=",")
            pandas.read_json(self.temp['demo_pu_conmat'], orient='split').to_csv(
                str.replace(self.project['filepaths']['demo_pu_cm_filepath'], '.csv',
                            '_mean_of_times.csv'),
                index=True, header=True, sep=",")

        else:
            self.temp['demo_pu_conmat'] = self.temp['demo_pu_conmat'].to_json(orient='split')
            pandas.read_json(self.temp['demo_pu_conmat'],
                             orient='split').to_csv(
                self.project['filepaths']['demo_pu_cm_filepath'], index=True, header=True, sep=",")

    def on_land_generate_button(self, event):
        self.temp = {}
        self.temp['land_pu_conmat'] = marxanconpy.habitatresistance2conmats(
            buff=float(self.project['filepaths']['land_hab_buff']),
            hab_filepath=self.project['filepaths']['land_hab_filepath'],
            pu_filepath=self.project['filepaths']['pu_filepath'],
            hab_id=self.project['filepaths']['land_hab_file_hab_id'])

        self.project['filepaths']['land_pu_cm_filepaths'] = {}
        for hab in self.temp['land_pu_conmat'].keys():
            print(str.replace(
                self.project['filepaths']['land_pu_cm_filepath'],
                ".csv",
                "_"+hab+".csv"))
            self.project['filepaths']['land_pu_cm_filepaths'][hab] = str.replace(
                self.project['filepaths']['land_pu_cm_filepath'],
                ".csv",
                "_"+hab+".csv")
        pandas.read_json(self.temp['land_pu_conmat'][hab], orient='split').to_csv(
            self.project['filepaths']['land_pu_cm_filepaths'][hab], index=True, header=True, sep=",")


# ##########################  metric related functions ################################################################

    def on_calc_metrics(self, event):
        """
        calculates the selected metrics
        """
        # create dict entry for connectivityMetrics
        # if not 'connectivityMetrics' in self.project:
        self.project['connectivityMetrics'] = {}
        self.temp = {}

        self.all_types = []
        if self.calc_metrics_pu.GetValue() and self.calc_metrics_cu.GetValue():
            if os.path.isfile(self.project['filepaths']['demo_pu_cm_filepath']):
                self.all_types += ['demo_pu', 'demo_cu']
            if os.path.isfile(self.project['filepaths']['gen_pu_cm_filepath']):
                self.all_types += ['gen_pu', 'gen_cu']
            if os.path.isfile(self.project['filepaths']['demo_pu_cm_filepath']):
                self.all_types += ['land_pu']
        elif self.calc_metrics_pu.GetValue():
            if os.path.isfile(self.project['filepaths']['demo_pu_cm_filepath']):
                self.all_types += ['demo_pu']
            if os.path.isfile(self.project['filepaths']['gen_pu_cm_filepath']):
                self.all_types += ['gen_pu']
            if os.path.isfile(self.project['filepaths']['land_pu_cm_filepath']):
                self.all_types += ['land_pu']
        elif self.calc_metrics_cu.GetValue():
            if os.path.isfile(self.project['filepaths']['demo_cu_cm_filepath']):
                self.all_types += ['demo_cu']
            if os.path.isfile(self.project['filepaths']['gen_cu_cm_filepath']):
                self.all_types += ['gen_cu']
        else:
            self.warn_dialog(message="No 'Units' selected for metric calculations.")


        for self.type in self.all_types:
            print(self.type)
            # check format
            if self.type[-2:] == 'pu':
                if self.type == 'demo_pu':
                    self.check_matrix_list_format(format=self.demo_matrixFormatRadioBox.GetStringSelection(),
                                                  filepath=self.project['filepaths'][self.type + '_cm_filepath'])
                    self.temp['format'] = self.demo_matrixFormatRadioBox.GetStringSelection()
                if self.type == 'gen_pu':
                    self.check_matrix_list_format(format=self.gen_matrixFormatRadioBox.GetStringSelection(),
                                                  filepath=self.project['filepaths'][self.type + '_cm_filepath'])
                self.temp['format'] = self.gen_matrixFormatRadioBox.GetStringSelection()

            # load correct matrix and transform if necessary
            if os.path.isfile(self.project['filepaths'][self.type + '_cm_filepath']):
                if self.temp['format'] == "Matrix":
                    self.temp[self.type + '_conmat'] = pandas.read_csv(
                        self.project['filepaths'][self.type + '_cm_filepath'], index_col=0)
                    self.project['connectivityMetrics'][self.type + '_conmat'] = self.temp[
                        self.type + '_conmat'].to_json(orient='split')
                elif self.temp['format'] == "List":
                    self.temp[self.type + '_conmat'] = pandas.read_csv(
                        self.project['filepaths'][self.type + '_cm_filepath'])
                    self.temp[self.type + '_conmat'] = self.temp[self.type + '_conmat'].pivot_table(values='value',
                                                                                                    index='id1',
                                                                                                    columns='id2')
                    self.project['connectivityMetrics'][self.type + '_conmat'] = self.temp[
                        self.type + '_conmat'].to_json(orient='split')
                elif self.temp['format'] == "List with Time":
                    self.temp[self.type + '_conmat_time'] = pandas.read_csv(
                        self.project['filepaths'][self.type + '_cm_filepath'])
                    self.temp[self.type + '_conmat'] = self.temp[self.type + '_conmat_time'][
                        ['id1', 'id2', 'value']].groupby(['id1', 'id2']).mean()
                    self.temp[self.type + '_conmat'] = self.temp[self.type + '_conmat'].pivot_table(values='value',
                                                                                                    index='id1',
                                                                                                    columns='id2')
                    self.project['connectivityMetrics'][self.type + '_conmat'] = self.temp[
                        self.type + '_conmat'].to_json(orient='split')
                    self.project['connectivityMetrics'][self.type + '_conmat_time'] = self.temp[
                        self.type + '_conmat_time'].to_json(orient='split')

                    self.warn_dialog(
                        message="A connectivity 'List with Time' was provided; however, all metrics except "
                                "'Temporal Connectivity Correlation' will be calculated from the temporal"
                                "mean of connectivity")
            else:
                self.warn_dialog(message="File not found: " + self.project['filepaths'][self.type + '_cm_filepath'])


            # load correct shapefile path
            if self.type[-2:] == 'pu':
                self.temp['shp_filepath'] = self.project['filepaths']['pu_filepath']
                self.temp['shp_file_pu_id'] = self.project['filepaths']['pu_file_pu_id']
            else:
                self.temp['shp_filepath'] = self.project['filepaths'][self.type + '_filepath']
                self.temp['shp_file_pu_id'] = self.project['filepaths'][self.type + '_file_pu_id']

            # create dict entries for boundary and spec
            self.project['connectivityMetrics']['spec_' + self.type] = {}
            self.project['connectivityMetrics']['boundary'] = {}

            # warn if files not the same length
            self.temp['conmat_len'] = str(len(self.temp[self.type + '_conmat']))
            self.temp['shp_len'] = str(gpd.GeoDataFrame.from_file(self.temp['shp_filepath']).shape[0])
            if self.temp['conmat_len'] != self.temp['shp_len']:
                self.warn_dialog(
                    message="The selected shapefile and connectivity matrix do not have the expected number of rows. "
                            "There are " + self.temp['conmat_len'] + " rows in the selected connectivity matrix and " +
                            self.temp['shp_len'] + " rows in the shapefile")

            # warn and end if pu_id not in shapefile
            # self.temp['shp_file_pu_id']
            # self.temp['shp_filepath']

            # calculate demographic metrics
            if self.type[:4] == 'demo':
                if self.cf_demo_vertex_degree.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['vertex_degree_' + self.type] = \
                        marxanconpy.conmat2vertexdegree(self.temp[self.type + '_conmat'])

                if self.cf_demo_between_cent.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['between_cent_' + self.type] = \
                        marxanconpy.conmat2betweencent(self.temp[self.type + '_conmat'])

                if self.cf_demo_eig_vect_cent.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['eig_vect_cent_' + self.type] = \
                        marxanconpy.conmat2eigvectcent(self.temp[self.type + '_conmat'])

                if self.cf_demo_self_recruit.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['self_recruit_' + self.type] = \
                        marxanconpy.conmat2selfrecruit(self.temp[self.type + '_conmat'])

                if self.cf_demo_outflux.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['outflux_' + self.type] = \
                        marxanconpy.conmat2outflux(self.temp[self.type + '_conmat'])

                if self.demo_matrixUnitsRadioBox.GetStringSelection() != "Individuals":
                    if self.cf_demo_fa_sink.GetValue() or\
                        self.cf_demo_fa_source.GetValue() or\
                        self.cf_demo_aa_sink.GetValue() or\
                        self.cf_demo_aa_source.GetValue():
                        self.warn_dialog(message="Calculating any 'source' or 'sink' metrics using a connectivity"
                                                 " matrix with units other than 'Individuals' assumes outflux from all "
                                                 "planning units is equal.")

                if self.cf_demo_fa_sink.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['fa_sink_' + self.type] = \
                        marxanconpy.conmat2sink(self.temp[self.type + '_conmat'],
                                                self.project['filepaths']['fa_filepath'],
                                                self.temp['shp_filepath'],
                                                self.temp['shp_file_pu_id']
                                                )

                if self.cf_demo_fa_source.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['fa_source_' + self.type] = \
                        marxanconpy.conmat2source(self.temp[self.type + '_conmat'],
                                                self.project['filepaths']['fa_filepath'],
                                                self.temp['shp_filepath'],
                                                self.temp['shp_file_pu_id']
                                                )

                if self.cf_demo_aa_sink.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['aa_sink_' + self.type] = \
                        marxanconpy.conmat2sink(self.temp[self.type + '_conmat'],
                                                self.project['filepaths']['aa_filepath'],
                                                self.temp['shp_filepath'],
                                                self.temp['shp_file_pu_id']
                                                )

                if self.cf_demo_aa_source.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['aa_source_' + self.type] = \
                        marxanconpy.conmat2source(self.temp[self.type + '_conmat'],
                                                self.project['filepaths']['aa_filepath'],
                                                self.temp['shp_filepath'],
                                                self.temp['shp_file_pu_id']
                                                )

                if self.cf_demo_stochasticity.GetValue():
                    if 'fa_filepath' in self.project['filepaths']:
                        self.project['connectivityMetrics']['spec_' + self.type]['temp_conn_cov_' + self.type] = \
                            marxanconpy.conmattime2temp_conn_cov(self.temp[self.type + '_conmat_time'],
                                                                   self.project['filepaths']['fa_filepath'],
                                                                   self.temp['shp_filepath']
                                                                   )
                    else:
                        self.warn_dialog(message="No 'Focus Area' has been specified. Please load a focus area file in "
                                                 "the Spatial Input tab")
                        return


                if self.bd_demo_conn_boundary.GetValue():
                    self.project['connectivityMetrics']['boundary']['conn_boundary_' + self.type] = \
                        marxanconpy.conmat2connboundary(self.temp[self.type + '_conmat'])

                if self.bd_demo_min_plan_graph.GetValue():
                    self.project['connectivityMetrics']['boundary']['min_plan_graph_' + self.type] = \
                        marxanconpy.conmat2minplanarboundary(self.temp[self.type + '_conmat'])

            # calculate genetic metrics ############################################################################
            if self.type[:3] == 'gen':
                print('calc gen')
                if self.cf_gen_vertex_degree.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['vertex_degree_' + self.type] = \
                        marxanconpy.conmat2vertexdegree(self.temp[self.type + '_conmat'])

                if self.cf_gen_between_cent.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['between_cent_' + self.type] = \
                        marxanconpy.conmat2betweencent(self.temp[self.type + '_conmat'])

                if self.cf_gen_eig_vect_cent.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['eig_vect_cent_' + self.type] = \
                        marxanconpy.conmat2eigvectcent(self.temp[self.type + '_conmat'])

                if self.cf_gen_self_recruit.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['self_recruit_' + self.type] = \
                        marxanconpy.conmat2selfrecruit(self.temp[self.type + '_conmat'])

                if self.cf_gen_fa_sink.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['fa_sink_' + self.type] = \
                        marxanconpy.conmat2sink(self.temp[self.type + '_conmat'],
                                                self.project['filepaths']['fa_filepath'],
                                                self.temp['shp_filepath'],
                                                self.temp['shp_file_pu_id']
                                                )

                if self.cf_gen_fa_source.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['fa_source_' + self.type] = \
                        marxanconpy.conmat2source(self.temp[self.type + '_conmat'],
                                                  self.project['filepaths']['fa_filepath'],
                                                  self.temp['shp_filepath'],
                                                  self.temp['shp_file_pu_id']
                                                  )

                if self.cf_gen_aa_sink.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['aa_sink_' + self.type] = \
                        marxanconpy.conmat2sink(self.temp[self.type + '_conmat'],
                                                self.project['filepaths']['aa_filepath'],
                                                self.temp['shp_filepath'],
                                                self.temp['shp_file_pu_id']
                                                )

                if self.cf_gen_aa_source.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['aa_source_' + self.type] = \
                        marxanconpy.conmat2source(self.temp[self.type + '_conmat'],
                                                  self.project['filepaths']['aa_filepath'],
                                                  self.temp['shp_filepath'],
                                                  self.temp['shp_file_pu_id']
                                                  )

                if self.bd_gen_conn_boundary.GetValue():
                    self.project['connectivityMetrics']['boundary']['conn_boundary_' + self.type] = \
                        marxanconpy.conmat2connboundary(self.temp[self.type + '_conmat'])

                if self.bd_gen_min_plan_graph.GetValue():
                    self.project['connectivityMetrics']['boundary']['min_plan_graph_' + self.type] = \
                        marxanconpy.conmat2minplanarboundary(self.temp[self.type + '_conmat'])



                            # create initial spec
        self.on_new_spec()
        self.customize_spec.Enable(enable=True)
        self.CFT_percent_slider.Enable(enable=True)
        self.export_metrics.Enable(enable=True)
        self.custom_spec_panel.SetToolTip(None)
        self.colormap_metric_choices(1)
        self.colormap_metric_choices(2)
        self.project['options']['metricsCalculated'] = True

    def on_export_metrics(self, event):
        if self.calc_metrics_pu.GetValue():
            self.type = 'demo_pu'
        else:
            self.warn_dialog(message="Conservation features can only be exported for planning units.")
            return

        # Export or append feature files
        if self.cf_export_radioBox.GetSelection() == 0:
            # export spec
            spec = pandas.read_json(self.project['spec_' + self.type + '_dat'], orient='split')
            spec.to_csv(self.project['filepaths']['spec_filepath'], index=0)
            # export conservation features
            cf = self.project['connectivityMetrics']['spec_' + self.type].copy()
            cf['pu'] = pandas.read_json(self.project['connectivityMetrics'][self.type + '_conmat'],
                                        orient='split').index
            cf = pandas.DataFrame(cf).melt(id_vars=['pu'], var_name='name', value_name='amount')
            cf = pandas.merge(cf, spec, how='outer', on='name')
            cf = cf.rename(columns={'id': 'species'}).sort_values(['species', 'pu'])
            cf[['species', 'pu', 'amount']].to_csv(self.project['filepaths']['cf_filepath'], index=0)

        elif self.cf_export_radioBox.GetSelection() == 1:
            # append
            old_spec = pandas.read_csv(self.project['filepaths']['spec_filepath'])
            old_cf = pandas.read_csv(self.project['filepaths']['cf_filepath'])

            # append spec
            new_spec = pandas.read_json(self.project['spec_' + self.type + '_dat'], orient='split')
            new_spec['id'] = new_spec['id'] + max(old_spec['id'])

            pandas.concat([old_spec, new_spec]).fillna(0.0).to_csv(
                str.replace(self.project['filepaths']['spec_filepath'],
                            ".dat",
                            "_appended.dat")
                , index=0)
            # append conservation features
            new_cf = self.project['connectivityMetrics']['spec_' + self.type].copy()
            new_cf['pu'] = pandas.read_json(self.project['connectivityMetrics'][self.type + '_conmat'],
                                            orient='split').index
            new_cf = pandas.DataFrame(new_cf).melt(id_vars=['pu'], var_name='name', value_name='amount')
            new_cf = pandas.merge(new_cf, new_spec, how='outer', on='name')
            new_cf = new_cf.rename(columns={'id': 'species'}).sort_values(['species', 'pu'])
            pandas.concat([old_cf, new_cf[['species', 'pu', 'amount']]]).to_csv(
                str.replace(self.project['filepaths']['cf_filepath'], ".dat", "_appended.dat"), index=0)

            if self.BD_filecheck.GetValue():
                self.export_boundary_file(BD_filepath=self.project['filepaths']['bd_filepath'])

    def export_boundary_file(self, BD_filepath):
        if self.calc_metrics_pu.GetValue():
            self.type = 'demo_pu'
        else:
            self.warn_dialog(message="Boundary files can only be exported for planning units.")
            return

        multiple = [self.bd_demo_conn_boundary.GetValue(),
                    self.bd_demo_min_plan_graph.GetValue()].count(True) > 1

        # Export each selected boundary definition            
        if self.bd_demo_conn_boundary.GetValue():
            if multiple:
                pandas.read_json(self.project['connectivityMetrics']['boundary']['conn_boundary_' + self.type],
                                 orient='split').to_csv(str.replace(BD_filepath,
                                                                    ".dat",
                                                                    "_conn_boundary_" + self.type + ".dat"),
                                                        index=False)
            else:
                pandas.read_json(self.project['connectivityMetrics']['boundary']['conn_boundary_' + self.type],
                                 orient='split').to_csv(BD_filepath, index=False)

        if self.bd_demo_min_plan_graph.GetValue():
            if multiple:
                pandas.read_json(self.project['connectivityMetrics']['boundary']['min_plan_graph_' + self.type],
                                 orient='split').to_csv(str.replace(BD_filepath,
                                                                    ".dat",
                                                                    "_min_plan_graph_" + self.type + ".dat"),
                                                        index=False)
            else:
                pandas.read_json(self.project['connectivityMetrics']['boundary']['min_plan_graph_' + self.type],
                                 orient='split').to_csv(BD_filepath, index=False)

        # warn when multiple boundary definitions
        if multiple:
            self.warn_dialog(message="Multiple Boundary Definitions were selected. Boundary file names have been"
                                     " edited to include type.", caption="Warning!")

# ########################## marxan functions ##########################################################################

    def on_inedit(self, event):
        """
        Starts Inedit (will fail to load file if it is not named input.dat)
        """
        if os.path.basename(self.project['filepaths']['marxan_input']) != "input.dat":
            self.warn_dialog("Marxan Inedit will attempt to load 'input.dat' from " + os.path.dirname(
                self.project['filepaths'][
                    'marxan_input']) + "by default. You will have to manually load your file in Inedit")
        subprocess.call(os.path.join(self.project['filepaths']['marxan_dir'], 'Inedit.exe'),
                        cwd=os.path.dirname(self.project['filepaths']['marxan_input']))

    def on_run_marxan(self, event):
        """
        Starts Marxan
        """
        if not 'connectivityMetrics' in self.project:
            self.project['connectivityMetrics'] = {}
        self.temp = {}
        os.system("start /wait cmd /c " +
                  os.path.join(self.project['filepaths']['marxan_dir'], 'Marxan.exe') + ' ' + self.project['filepaths'][
                      'marxan_input'])

        # calculate selection frequency
        for line in open(self.project['filepaths']['marxan_input']):
            if line.startswith('SCENNAME'):
                self.temp['SCENNAME'] = line.replace('SCENNAME ', '').replace('\n', '')
            elif line.startswith('NUMREPS'):
                self.temp['NUMREPS'] = int(line.replace('NUMREPS ', '').replace('\n', ''))
            elif line.startswith('OUTPUTDIR'):
                self.temp['OUTPUTDIR'] = line.replace('OUTPUTDIR ', '').replace('\n', '')

        for self.temp['file'] in range(self.temp['NUMREPS']):
            self.temp['fn'] = os.path.join(self.temp['OUTPUTDIR'],
                                           self.temp['SCENNAME'] + "_r" + "%05d" % (self.temp['file'] + 1) + ".txt")
            if self.temp['file'] == 0:
                self.temp['select_freq'] = pandas.read_csv(self.temp['fn'])
            else:
                self.temp['select_freq']['solution'] = self.temp['select_freq']['solution'] + \
                                                       pandas.read_csv(self.temp['fn'])['solution']

        self.project['connectivityMetrics']['select_freq'] = self.temp['select_freq']['solution'].tolist()

        # load best solution
        self.temp['fn'] = os.path.join(self.temp['OUTPUTDIR'], self.temp['SCENNAME'] + "_best.txt")
        self.project['connectivityMetrics']['best_solution'] = pandas.read_csv(self.temp['fn'])['solution'].tolist()

        # update plotting options
        self.colormap_shapefile_choices()
        self.colormap_metric_choices(1)
        self.colormap_metric_choices(2)



# ###########################  spec grid popup functions ###############################################################
    def on_customize_spec(self, event):
        if self.calc_metrics_pu.GetValue():
            self.type = 'demo_pu'
            self.spec_frame.Show()
        else:
            self.warn_dialog(message="'Planning Units' not selected for metric calculations.")

    def on_new_spec(self):
        self.spec_frame = spec_customizer(parent=self)
        self.all_types = []
        if self.calc_metrics_pu.GetValue():
            if os.path.isfile(self.project['filepaths']['demo_pu_cm_filepath']):
                self.all_types += ['demo_pu']
            if os.path.isfile(self.project['filepaths']['gen_pu_cm_filepath']):
                self.all_types += ['gen_pu']
            if os.path.isfile(self.project['filepaths']['land_pu_cm_filepath']):
                self.all_types += ['land_pu']
        else:
            self.warn_dialog(message="'Planning Units' not selected for metric calculations.")
            return

        for self.type in self.all_types:
            self.spec_frame.keys = list(self.project['connectivityMetrics']['spec_' + self.type])

            for i in range(len(self.spec_frame.keys)):
                self.spec_frame.spec_grid.InsertRows(i)
                self.spec_frame.spec_grid.SetCellValue(i, 0, str(i + 1))
                sum_metric = sum(self.project['connectivityMetrics']['spec_' + self.type][self.spec_frame.keys[i]])
                self.spec_frame.spec_grid.SetCellValue(i, 1, str(sum_metric * self.CFT_percent_slider.GetValue() / 100))
                self.spec_frame.spec_grid.SetCellValue(i, 2, str(1000))
                self.spec_frame.spec_grid.SetCellValue(i, 3, self.spec_frame.keys[i])
                w, h = self.spec_frame.GetClientSize()

                self.spec_frame.SetSize((w + 16, h + 39 + 20))
                self.spec_frame.Layout()

            self.project['spec_' + self.type + '_dat'] = pandas.DataFrame(
                numpy.full((self.spec_frame.spec_grid.GetNumberRows(), self.spec_frame.spec_grid.GetNumberCols()), None))
            self.project['spec_' + self.type + '_dat'].columns = ["id", "target", "spf", "name"]

            for c in range(self.spec_frame.spec_grid.GetNumberCols()):
                for r in range(self.spec_frame.spec_grid.GetNumberRows()):
                    self.project['spec_' + self.type + '_dat'].iloc[r, c] = self.spec_frame.spec_grid.GetCellValue(r, c)

            self.project['spec_' + self.type + '_dat'] = self.project['spec_' + self.type + '_dat'].to_json(orient='split')

    def on_CFT_percent_slider(self, event):
        self.on_new_spec()


class spec_customizer(gui.spec_customizer):
    def __init__(self, parent):
        gui.spec_customizer.__init__(self, parent)
        self.parent = parent

    def on_spec_ok(self, event):
        self.parent.project['spec_' + self.parent.type + '_dat'] = pandas.DataFrame(
            numpy.full((self.spec_grid.GetNumberRows(),
                        self.spec_grid.GetNumberCols()), None))
        self.parent.project['spec_' + self.parent.type + '_dat'].columns = ["id", "target", "spf", "name"]

        for c in range(self.spec_grid.GetNumberCols()):
            for r in range(self.spec_grid.GetNumberRows()):
                self.parent.project['spec_' + self.parent.type + '_dat'].iloc[r, c] = self.spec_grid.GetCellValue(r, c)
        self.parent.project['spec_' + self.parent.type + '_dat'] = self.parent.project[
            'spec_' + self.parent.type + '_dat'].to_json()
        self.Hide()

    def on_spec_cancel(self, event):
        self.Hide()


# ###########################  getting started popup functions #########################################################
class GettingStarted (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Marxan with Connectivity: Getting Started",
                          pos=wx.DefaultPosition,
                          size=wx.Size(900, 700),
                          style=wx.DEFAULT_FRAME_STYLE | wx.FRAME_FLOAT_ON_PARENT)
        self.gettingStarted = wx.Panel(self)
        self.Center()
        # set the icon
        parent.set_icon(frame=self)

        startMainSizer = wx.FlexGridSizer(3, 1, 0, 0)
        startMainSizer.AddGrowableRow(0)
        #        startMainSizer.AddGrowableRow( 1 )
        #        startMainSizer.AddGrowableRow( 2 )
        startMainSizer.SetFlexibleDirection(wx.VERTICAL)
        startMainSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sizer02 = wx.BoxSizer(wx.HORIZONTAL)

        self.gettingstartedtxt = wx.StaticText(self.gettingStarted,
                                               wx.ID_ANY,
                                               u"Welcome to Marxan with Connectivity!\n\nMarxan with Connectivity"
                                               u" (henceforth the \"app\") is a Graphical User Interface (GUI) to help"
                                               u" conservationists include \"connectivity\" in their protected area"
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
                                               wx.DefaultSize, 0)
        self.gettingstartedtxt.Wrap(-1)
        sizer02.Add(self.gettingstartedtxt, 0, wx.ALL | wx.EXPAND, 5)

        startMainSizer.Add(sizer02, 1, wx.EXPAND, 5)

        hyperlinksizer = wx.BoxSizer(wx.VERTICAL)
        self.tutoriallink = wx.adv.HyperlinkCtrl(self.gettingStarted,
                                                 wx.ID_ANY, u"Tutorial",
                                                 u"tutorial.html",
                                                 wx.DefaultPosition,
                                                 wx.DefaultSize)
        hyperlinksizer.Add(self.tutoriallink, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.glossarylink = wx.adv.HyperlinkCtrl(self.gettingStarted,
                                                 wx.ID_ANY,
                                                 u"Glossary",
                                                 u"glossary.html",
                                                 wx.DefaultPosition,
                                                 wx.DefaultSize)
        hyperlinksizer.Add(self.glossarylink, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.githublink = wx.adv.HyperlinkCtrl(self.gettingStarted,
                                               wx.ID_ANY,
                                               u"GitHub Issues",
                                               u"https://github.com/remi-daigle/MarxanConnect/issues",
                                               wx.DefaultPosition,
                                               wx.DefaultSize)
        hyperlinksizer.Add(self.githublink, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        startMainSizer.Add(hyperlinksizer, 1, wx.EXPAND, 5)

        iconsizer = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap1 = wx.StaticBitmap(self.gettingStarted,
                                         wx.ID_ANY, wx.Bitmap(os.path.join(sys.path[0], 'icon_bundle.ico'),
                                                              wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        iconsizer.Add(self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        startMainSizer.Add(iconsizer, 1, wx.EXPAND, 5)

        self.gettingStarted.SetSizer(startMainSizer)
        self.gettingStarted.Layout()
        startMainSizer.Fit(self.gettingStarted)

# ######################################################################################################################

# ########################## debug mode ################################################################################

class RedirectText(object):
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        wx.CallAfter(self.out.WriteText, string)


class LogForm(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, "Debbuging Console")
        self.Bind(wx.EVT_CLOSE, self.__close)
        parent.set_icon(frame=self)

        # Add a panel
        panel = wx.Panel(self, wx.ID_ANY)
        log = wx.TextCtrl(panel, wx.ID_ANY, size=(350, 350), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        # Add widgets to a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(sizer)

        # redirect text here
        redir = RedirectText(log)
        sys.stdout = redir
        sys.stderr = redir

    def __close(self, event):
        self.Hide()


# ##########################  run the GUI ##############################################################################
app = wx.App(False)

# create an object of CalcFrame
frame = MarxanConnectGUI(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()

# stop the app
app.Destroy()
