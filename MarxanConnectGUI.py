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
wc_MarCon = "Marxan Connect Project (*.MarCon)|*.MarCon|" \
            "All files (*.*)|*.*"


if len(sys.argv) > 1:
    os.chdir(os.path.dirname(sys.argv[0]))

class MarxanConnectGUI(gui.MarxanConnectGUI):
    def __init__(self, parent):
        """
        initialize parent class (the entire GUI)
        """
        gui.MarxanConnectGUI.__init__(self, parent)
        # set the icon
        self.set_icon(frame=self)

        # start up log
        self.log = LogForm(parent=self)

        # set opening tab to Spatial Input (0)
        self.auinotebook.ChangeSelection(0)

        self.demo_matrixTypeRadioBox.SetItemToolTip(0, "In a probability matrix, each cell represents the probability of movement from site A (row) to site B (column). May or may not account for mortality. If there is no mortality, rows sum to 1")
        self.demo_matrixTypeRadioBox.SetItemToolTip(1, "In a migration matrix, each cell represents the probability of a successful migrant in site B (column) originated in site A (row). Columns sum to 1.")
        self.demo_matrixTypeRadioBox.SetItemToolTip(2, "In a flux matrix, each cell represents the number of elements/individuals moving from site A (row) to site B (column) per unit time.")

        self.demo_matrixFormatRadioBox.SetItemToolTip(0,"Matrix format data has the connectivity values arranged is a square format (i.e.the same number of rows and columns). The row names are the donor sites and the column names are the recipient sites ")
        self.demo_matrixFormatRadioBox.SetItemToolTip(1,"Edge Edge Listwith habi has 3 columns: the donor sites ('id1'), the recipient sites ('id2'), and the connectivity values ('value')")
        self.demo_matrixFormatRadioBox.SetItemToolTip(2,"An Edge List with Time has 4 columns: time ('time'), the donor sites ('id1'), the recipient sites ('id2'), and the connectivity values ('value")

        # Either load or launch new project
        if len(sys.argv) > 1:
            self.spatial = {}
            self.project = {}
            self.project['filepaths'] = {}
            self.project['filepaths']['projfile'] = str(sys.argv[1])
            self.workingdirectory = os.path.dirname(self.project['filepaths']['projfile'])
            self.load_project_function()
        else:
            # launch a blank new project
            self.on_new_project(event=None, launch=True)

            # launch Getting started window
            GettingStartedframe = GettingStarted(parent=self)
            GettingStartedframe.Show()
            # self.project['filepaths'] = {}
            # self.project['filepaths']['projfile'] ="C:\\Users\\Remi-Work\\Documents\\testing.MarCon"
            # self.project['filepaths']['projfile'] ="C:\\Users\\Remi-Work\\Documents\\landscape.MarCon"
            # self.project['filepaths']['projfile'] = "C:\\Users\\Remi-Work\\Desktop\\MarxanConnect\\data\\GBR_demographic_gridded_example\\GBR_demographic_gridded_example.MarCon"
            # self.load_project_function()
            # self.on_land_generate_button(event=None)

    def set_icon(self, frame):
        # set the icon
        icons = wx.IconBundle()
        for sz in [16, 32, 48, 96, 256]:
            try:
                icon = wx.Icon(os.path.join(sys.path[0], 'images\\icon_bundle.ico'),
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
        self.spatial = {}
        self.project = {}
        self.project['filepaths'] = {}
        self.workingdirectory = sys.path[0] #os.path.expanduser(os.path.join("~", "Documents"))
        self.project['options'] = {}

        # set default options
        self.project['options']['fa_status'] = self.fa_status_radioBox.GetStringSelection()
        self.project['options']['aa_status'] = self.aa_status_radioBox.GetStringSelection()
        self.project['options']['demo_pu_cm_progress'] = self.demo_PU_CM_progress.GetValue()
        self.project['options']['demo_conmat_type'] = self.demo_matrixTypeRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_format'] = self.demo_matrixFormatRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_rescale'] = self.demo_rescaleRadioBox.GetStringSelection()
        self.project['options']['demo_conmat_rescale_edge'] = self.demo_rescale_edgeRadioBox.GetStringSelection()
        self.project['options']['land_hab_buff'] = self.land_HAB_buff.GetValue()
        self.project['options']['land_hab_thresh'] = self.land_HAB_thresh.GetValue()
        self.project['options']['land_pu_cm_progress'] = self.land_PU_CM_progress.GetValue()
        self.project['options']['land_conmat_type'] = self.land_type_choice.GetPageText(self.land_type_choice.GetSelection())
        self.project['options']['land_res_matrixType'] = self.land_res_matrixTypeRadioBox.GetStringSelection()
        self.project['options']['calc_metrics_pu'] = self.calc_metrics_pu.GetValue()
        self.project['options']['calc_metrics_cu'] = self.calc_metrics_cu.GetValue()
        self.project['options']['metricsCalculated'] = False
        self.set_metric_options()
        self.project['options']['cf_export'] = self.cf_export_radioBox.GetStringSelection()
        self.project['options']['inputdat_boundary'] = self.inputdat_symmRadio.GetStringSelection()

        # set default file paths
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
        self.project['filepaths']['demo_lp_filepath'] = ""
        self.project['filepaths']['land_cu_filepath'] = ""
        self.project['filepaths']['land_cu_file_hab_id'] = ""
        self.project['filepaths']['land_res_mat_filepath'] = ""
        self.project['filepaths']['land_res_filepath'] = ""
        self.project['filepaths']['land_res_file_hab_id'] = ""
        self.project['filepaths']['land_pu_cm_filepath'] = ""
        self.project['filepaths']['land_lp_filepath'] = ""

        # Marxan metrics files
        self.project['filepaths']['cf_filepath'] = os.path.join("~", "input", "puvspr2.dat")
        self.project['filepaths']['spec_filepath'] = os.path.join("~", "input", "spec.dat")
        self.project['filepaths']['bd_filepath'] = os.path.join("~", "input", "boundary.dat")
        self.project['filepaths']['pudat_filepath'] = os.path.join("~", "input", "pu.dat")

        # Marxan analysis
        self.project['filepaths']['marxan_input'] = os.path.join("~", "input.dat")
        self.project['filepaths']['marxan_dir'] = os.path.join("~", "Marxan243")

        # Export plot data
        self.project['filepaths']['pushp'] = os.path.join("~", "pu.shp")
        self.project['filepaths']['pucsv'] = os.path.join("~", "pu.csv")
        self.project['filepaths']['map'] = os.path.join("~", "map.png")

        # if called at launch time, no need to ask users to create a new project file right away
        if not launch:
            dlg = wx.FileDialog(self, "Create a new project file:", style=wx.FD_SAVE, wildcard=wc_MarCon)
            if dlg.ShowModal() == wx.ID_OK:
                self.project['filepaths']['projfile'] = dlg.GetPath()
                self.project['filepaths']['projfilename'] = dlg.GetFilename()
                self.workingdirectory = dlg.GetDirectory()
                with open(self.project['filepaths']['projfile'], 'w') as fp:
                    json.dump(self.project, fp, indent=4, sort_keys=True)
                frame.SetTitle('Marxan with Connectivity (Project: ' + self.project['filepaths']['projfilename'] + ')')
            dlg.Destroy()

        # set default file paths in GUI
        for p in self.project['filepaths']:
            self.project['filepaths'][p] = self.project['filepaths'][p].replace("~\\",
                                                                                self.workingdirectory + "\\")
        self.set_GUI_filepaths()

        # trigger functions which enable/disable options
        self.on_demo_matrixFormatRadioBox(event=None)
        self.on_demo_rescaleRadioBox(event=None)
        self.on_land_type_choice(event=None)
        self.enable_metrics()
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()
        self.colormap_metric_choices(1)
        self.colormap_metric_choices(2)
        self.colormap_metric_choices("pre-eval")

    def on_load_project(self, event):
        """
        Create and show the Open FileDialog to load a project
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard=wc_MarCon,
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.project = {}
            self.project['filepaths'] = {}
            self.project['filepaths']['projfile'] = dlg.GetPath()
            self.workingdirectory = dlg.GetDirectory()
        dlg.Destroy()

        self.load_project_function()

    def load_project_function(self):
        self.spatial = {}
        with open(self.project['filepaths']['projfile'], 'r') as fp:
            self.project = json.loads(fp.read())

        for p in self.project['filepaths']:
            if p != "working_directory":
                self.project['filepaths'][p] = self.project['filepaths'][p].replace(
                    "~\\",self.workingdirectory + "\\")

        self.SetTitle('Marxan with Connectivity (Project: ' + self.project['filepaths']['projfilename'] + ')')

        # set default options
        self.fa_status_radioBox.SetStringSelection(self.project['options']['fa_status'])
        self.aa_status_radioBox.SetStringSelection(self.project['options']['aa_status'])

        self.demo_PU_CM_progress.SetValue(self.project['options']['demo_pu_cm_progress'])
        self.demo_matrixTypeRadioBox.SetStringSelection(self.project['options']['demo_conmat_type'])
        self.demo_matrixFormatRadioBox.SetStringSelection(self.project['options']['demo_conmat_format'])
        self.demo_rescaleRadioBox.SetStringSelection(self.project['options']['demo_conmat_rescale'])
        self.demo_rescale_edgeRadioBox.SetStringSelection(self.project['options']['demo_conmat_rescale_edge'])

        self.land_HAB_buff.SetValue(self.project['options']['land_hab_buff'])
        self.land_HAB_thresh.SetValue(self.project['options']['land_hab_thresh'])
        self.land_PU_CM_progress.SetValue(self.project['options']['land_pu_cm_progress'])
        for i in range(self.land_type_choice.GetPageCount()):
            if self.land_type_choice.GetPageText(i) == self.project['options']['land_conmat_type']:
                self.land_type_choice.SetSelection(i)
        self.land_res_matrixTypeRadioBox.SetStringSelection(self.project['options']['land_res_matrixType'])

        self.cf_demo_in_degree.SetValue(self.project['options']['demo_metrics']['in_degree'])
        self.cf_demo_out_degree.SetValue(self.project['options']['demo_metrics']['out_degree'])
        self.cf_demo_between_cent.SetValue(self.project['options']['demo_metrics']['between_cent'])
        self.cf_demo_eig_vect_cent.SetValue(self.project['options']['demo_metrics']['eig_vect_cent'])
        self.cf_demo_google.SetValue(self.project['options']['demo_metrics']['google'])
        self.cf_demo_self_recruit.SetValue(self.project['options']['demo_metrics']['self_recruit'])
        self.cf_demo_local_retention.SetValue(self.project['options']['demo_metrics']['local_retention'])
        self.cf_demo_outflux.SetValue(self.project['options']['demo_metrics']['outflux'])
        self.cf_demo_influx.SetValue(self.project['options']['demo_metrics']['influx'])
        self.cf_demo_stochasticity.SetValue(self.project['options']['demo_metrics']['stochasticity'])
        self.cf_demo_fa_recipients.SetValue(self.project['options']['demo_metrics']['fa_recipients'])
        self.cf_demo_fa_donors.SetValue(self.project['options']['demo_metrics']['fa_donors'])
        self.cf_demo_aa_recipients.SetValue(self.project['options']['demo_metrics']['aa_recipients'])
        self.cf_demo_aa_donors.SetValue(self.project['options']['demo_metrics']['aa_donors'])

        self.bd_demo_conn_boundary.SetValue(self.project['options']['demo_metrics']['conn_boundary'])
        self.bd_demo_min_plan_graph.SetValue(self.project['options']['demo_metrics']['min_plan_graph'])

        self.cf_land_in_degree.SetValue(self.project['options']['land_metrics']['in_degree'])
        self.cf_land_out_degree.SetValue(self.project['options']['land_metrics']['out_degree'])
        self.cf_land_between_cent.SetValue(self.project['options']['land_metrics']['between_cent'])
        self.cf_land_eig_vect_cent.SetValue(self.project['options']['land_metrics']['eig_vect_cent'])
        self.cf_land_google.SetValue(self.project['options']['land_metrics']['google'])
        self.cf_land_fa_recipients.SetValue(self.project['options']['land_metrics']['fa_recipients'])
        self.cf_land_fa_donors.SetValue(self.project['options']['land_metrics']['fa_donors'])
        self.cf_land_aa_recipients.SetValue(self.project['options']['land_metrics']['aa_recipients'])
        self.cf_land_aa_donors.SetValue(self.project['options']['land_metrics']['aa_donors'])

        self.bd_land_conn_boundary.SetValue(self.project['options']['land_metrics']['conn_boundary'])
        self.bd_land_min_plan_graph.SetValue(self.project['options']['land_metrics']['min_plan_graph'])

        self.calc_metrics_pu.SetValue(self.project['options']['calc_metrics_pu'])
        self.calc_metrics_cu.SetValue(self.project['options']['calc_metrics_cu'])

        self.inputdat_symmRadio.SetStringSelection(self.project['options']['inputdat_boundary'])
        self.inputdat_symmRadio.SetStringSelection(self.project['options']['inputdat_boundary'])



        # set default file paths in GUI
        self.set_GUI_filepaths()

        # trigger functions which enable/disable options
        self.on_PU_file(event=None)
        self.on_FA_file(event=None)
        self.on_AA_file(event=None)
        self.on_demo_matrixFormatRadioBox(event=None)
        self.on_demo_matrixFormatRadioBox(event=None)
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
        self.colormap_metric_choices("pre-eval")

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
        self.demo_LP_file.SetPath(self.project['filepaths']['demo_lp_filepath'])

        self.land_HAB_file.SetPath(self.project['filepaths']['land_cu_filepath'])
        self.set_GUI_id_selection(self.land_HAB_file_hab_id, self.project['filepaths']['land_cu_filepath'],
                                  self.project['filepaths']['land_cu_file_hab_id'])
        self.land_RES_mat_file.SetPath(self.project['filepaths']['land_res_mat_filepath'])
        self.land_RES_file.SetPath(self.project['filepaths']['land_res_filepath'])
        self.set_GUI_id_selection(self.land_RES_file_res_id, self.project['filepaths']['land_res_filepath'],
                                  self.project['filepaths']['land_res_file_hab_id'])
        self.land_PU_CM_file.SetPath(self.project['filepaths']['land_pu_cm_filepath'])
        self.land_LP_file.SetPath(self.project['filepaths']['land_lp_filepath'])

        # Marxan metrics files
        self.CF_file.SetPath(self.project['filepaths']['cf_filepath'])
        self.SPEC_file.SetPath(self.project['filepaths']['spec_filepath'])
        self.BD_file.SetPath(self.project['filepaths']['bd_filepath'])
        self.PUDAT_file.SetPath(self.project['filepaths']['pudat_filepath'])

        # Marxan analysis
        self.inputdat_file.SetPath(self.project['filepaths']['marxan_input'])
        self.marxan_dir.SetPath(self.project['filepaths']['marxan_dir'])

        # Export plot data
        self.PUSHP_file.SetPath(self.project['filepaths']['pushp'])
        self.PUCSV_file.SetPath(self.project['filepaths']['pucsv'])
        self.MAP_file.SetPath(self.project['filepaths']['map'])

    def set_GUI_id_selection(self,choice,filepath,id):
        if(os.path.isfile(filepath)):
            choice.SetItems(list(gpd.GeoDataFrame.from_file(filepath)))
            choice.SetStringSelection(id)

    def set_metric_options(self):
        self.project['options']['demo_metrics'] = {}
        self.project['options']['demo_metrics']['in_degree'] = self.cf_demo_in_degree.GetValue()
        self.project['options']['demo_metrics']['out_degree'] = self.cf_demo_out_degree.GetValue()
        self.project['options']['demo_metrics']['between_cent'] = self.cf_demo_between_cent.GetValue()
        self.project['options']['demo_metrics']['eig_vect_cent'] = self.cf_demo_eig_vect_cent.GetValue()
        self.project['options']['demo_metrics']['google'] = self.cf_demo_google.GetValue()
        self.project['options']['demo_metrics']['self_recruit'] = self.cf_demo_self_recruit.GetValue()
        self.project['options']['demo_metrics']['local_retention'] = self.cf_demo_local_retention.GetValue()
        self.project['options']['demo_metrics']['outflux'] = self.cf_demo_outflux.GetValue()
        self.project['options']['demo_metrics']['influx'] = self.cf_demo_influx.GetValue()
        self.project['options']['demo_metrics']['stochasticity'] = self.cf_demo_stochasticity.GetValue()
        self.project['options']['demo_metrics']['fa_recipients'] = self.cf_demo_fa_recipients.GetValue()
        self.project['options']['demo_metrics']['fa_donors'] = self.cf_demo_fa_donors.GetValue()
        self.project['options']['demo_metrics']['aa_recipients'] = self.cf_demo_aa_recipients.GetValue()
        self.project['options']['demo_metrics']['aa_donors'] = self.cf_demo_aa_donors.GetValue()

        self.project['options']['demo_metrics']['conn_boundary'] = self.bd_demo_conn_boundary.GetValue()
        self.project['options']['demo_metrics']['min_plan_graph'] = self.bd_demo_min_plan_graph.GetValue()

        self.project['options']['land_metrics'] = {}
        self.project['options']['land_metrics']['in_degree'] = self.cf_land_in_degree.GetValue()
        self.project['options']['land_metrics']['out_degree'] = self.cf_land_out_degree.GetValue()
        self.project['options']['land_metrics']['between_cent'] = self.cf_land_between_cent.GetValue()
        self.project['options']['land_metrics']['eig_vect_cent'] = self.cf_land_eig_vect_cent.GetValue()
        self.project['options']['land_metrics']['google'] = self.cf_land_google.GetValue()
        self.project['options']['land_metrics']['fa_recipients'] = self.cf_land_fa_recipients.GetValue()
        self.project['options']['land_metrics']['fa_donors'] = self.cf_land_fa_donors.GetValue()
        self.project['options']['land_metrics']['aa_recipients'] = self.cf_land_aa_recipients.GetValue()
        self.project['options']['land_metrics']['aa_donors'] = self.cf_land_aa_donors.GetValue()

        self.project['options']['land_metrics']['conn_boundary'] = self.bd_land_conn_boundary.GetValue()
        self.project['options']['land_metrics']['min_plan_graph'] = self.bd_land_min_plan_graph.GetValue()

    def on_save_project(self, event):
        """
        save a project, but call 'on_save_project_as' if project file has not previously been defined
        """
        if 'projfile' in self.project['filepaths']:
            self.set_metric_options()
            self.projfile = self.project['filepaths']['projfile']
            for p in self.project['filepaths']:
                self.project['filepaths'][p] = self.project['filepaths'][p].replace(
                    self.workingdirectory + "\\", "~\\")
            with open(self.projfile, 'w') as fp:
                json.dump(self.project, fp, indent=4, sort_keys=True)
            for p in self.project['filepaths']:
                self.project['filepaths'][p] = self.project['filepaths'][p].replace(
                    "~\\",self.workingdirectory + "\\")
        else:
            self.on_save_project_as(event=None)

    def on_save_project_as(self, event):
        """
        Create and show the Open FileDialog to save a project
        """
        dlg = wx.FileDialog(
            self, message="Save file as ...",
            defaultDir=self.workingdirectory,
            defaultFile="", wildcard=wc_MarCon, style=wx.FD_SAVE
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.project['filepaths']['projfile'] = dlg.GetPath()
            self.project['filepaths']['projfilename'] = dlg.GetFilename()
            self.workingdirectory = dlg.GetDirectory()
            self.set_metric_options()
            self.projfile = self.project['filepaths']['projfile']
            for p in self.project['filepaths']:
                self.project['filepaths'][p] = self.project['filepaths'][p].replace(
                    self.workingdirectory + "\\", "~\\")
            with open(self.projfile, 'w') as fp:
                json.dump(self.project, fp, indent=4, sort_keys=True)
            for p in self.project['filepaths']:
                self.project['filepaths'][p] = self.project['filepaths'][p].replace(
                    "~\\", self.workingdirectory + "\\")
        dlg.Destroy()
        frame.SetTitle('Marxan with Connectivity (Project: ' + self.project['filepaths']['projfilename'] + ')')

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
        dlg = wx.MessageBox(message="Version: v0.0.4\n(C) 2017 Remi Daigle\n",
                            caption="About Marxan with Connectivity",
                            style=wx.OK)
        dlg.Destroy()

    def on_getting_started (self, event):
        # insert getting started tab and hyperlinks (wxFormBuilder can't handle hyperlinks)
        GettingStartedframeframe = GettingStarted (parent=self)
        GettingStartedframeframe.Show()

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
                metric_type1 = self.get_metric_type(selection=self.metric_choice.GetStringSelection(),type=type1)
                if type1 == "pu":
                    metric1 = self.project['connectivityMetrics'][metric_type1]
                else:
                    metric1 = self.project['connectivityMetrics']['spec_' + type1][metric_type1]

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
                metric_type2 = self.get_metric_type(selection=self.metric_choice1.GetStringSelection(),type=type1)
                if type2 == "pu":
                    metric2 = self.project['connectivityMetrics'][metric_type2]
                else:
                    metric2 = self.project['connectivityMetrics']['spec_' + type2][metric_type2]

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
            if self.demo_rescaleRadioBox.GetStringSelection() != "Identical Grids":
                choices.append("Demographic Units")
        if self.project['filepaths']['land_cu_filepath'] != "":
            choices.append("Landscape Units")

        self.poly_shp_choice.SetItems(choices)
        self.poly_shp_choice.SetSelection(0)
        self.poly_shp_choice1.SetItems(choices)
        self.poly_shp_choice1.SetSelection(0)

    def colormap_shapefile_choices(self):
        choices = []
        if 'connectivityMetrics' in self.project:
            if 'best_solution' in self.project['connectivityMetrics'] or 'status' in self.project['connectivityMetrics']:
                choices.append("Planning Units (Marxan Data)")
            if 'spec_demo_pu' in self.project['connectivityMetrics']:
                choices.append("Planning Units (Demographic Data)")
            if 'spec_land_pu' in self.project['connectivityMetrics']:
                choices.append("Planning Units (Landscape Data)")
            if 'spec_demo_cu' in self.project['connectivityMetrics']:
                choices.append("Demographic Units")

        self.metric_shp_choice.SetItems(choices)
        self.metric_shp_choice.SetSelection(0)
        self.metric_shp_choice1.SetItems(choices)
        self.metric_shp_choice1.SetSelection(0)

        choices = []

        if 'connectivityMetrics' in self.project:
            if 'spec_demo_pu' in self.project['connectivityMetrics']:
                choices.append("Planning Units (Demographic Data)")
            if 'spec_land_pu' in self.project['connectivityMetrics']:
                choices.append("Planning Units (Landscape Data)")
        self.preEval_metric_shp_choice.SetItems(choices)
        self.preEval_metric_shp_choice.SetSelection(0)

    def on_metric_shp_choice(self, event=None):
        self.colormap_metric_choices(1)

    def on_metric_shp_choice1(self, event=None):
        self.colormap_metric_choices(2)

    def colormap_metric_choices(self, lyr):
        choices = []
        if lyr == 1:
            shapefile = self.metric_shp_choice.GetStringSelection()
        elif lyr == 2:
            shapefile = self.metric_shp_choice1.GetStringSelection()
        else:
            shapefile = self.preEval_metric_shp_choice.GetStringSelection()

        if 'connectivityMetrics' in self.project:
            if shapefile == "Planning Units (Marxan Data)":
                if 'best_solution' in self.project['connectivityMetrics']:
                    choices.append("Selection Frequency")
                    choices.append("Best Solution")
                if 'status' in self.project['connectivityMetrics']:
                    choices.append("Status")
            else:
                plot_type = self.get_plot_type(shapefile)
                if 'spec_' + plot_type in self.project['connectivityMetrics']:
                    self.spec_resolve_metric_choice('in_degree_', "In Degree", plot_type, choices)
                    self.spec_resolve_metric_choice('out_degree_', "Out Degree", plot_type, choices)
                    self.spec_resolve_metric_choice('between_cent_', "Betweenness Centrality", plot_type, choices)
                    self.spec_resolve_metric_choice('eig_vect_cent_', "Eigen Vector Centrality", plot_type, choices)
                    self.spec_resolve_metric_choice('google_', "Google Page Rank", plot_type, choices)
                    self.spec_resolve_metric_choice('self_recruit_', "Self Recruitment", plot_type, choices)
                    self.spec_resolve_metric_choice('outflux_', "Outflux", plot_type, choices)
                    self.spec_resolve_metric_choice('influx_', "Influx", plot_type, choices)
                    self.spec_resolve_metric_choice('temp_conn_cov_', "Temporal Connectivity Covariance", plot_type, choices)
                    self.spec_resolve_metric_choice('fa_recipients_', "Focus Area Recipients", plot_type, choices)
                    self.spec_resolve_metric_choice('fa_donors_', "Focus Area Donors", plot_type, choices)
                    self.spec_resolve_metric_choice('aa_recipients_', "Avoidance Area Recipients", plot_type, choices)
                    self.spec_resolve_metric_choice('aa_donors_', "Avoidance Area Donors", plot_type, choices)
        if lyr == 1:
            self.metric_choice.SetItems(choices)
            self.metric_choice.SetSelection(0)
        elif lyr == 2:
            self.metric_choice1.SetItems(choices)
            self.metric_choice1.SetSelection(0)
        else:
            self.preEval_metric_choice.SetItems(choices)
            self.preEval_metric_choice.SetSelection(0)
            if 'connectivityMetrics' in self.project:
                self.on_preEval_metric_choice(event=None)

    def spec_resolve_metric_choice(self, prefix, text = None, type = None, choices=None, gettext = True):
        if gettext:
            for k in self.project['connectivityMetrics']['spec_' + type].keys():
                if k.startswith(prefix+type):
                    if len(k)==len(prefix+type):
                        choices.append(text)
                    else:
                        choices.append(text+' ('+k.replace(prefix+type+'_','')+')')
        else:
            if text.startswith(type):
                if len(type) == len(text):
                    return str(prefix)
                else:
                    return str(prefix+'_'+str.replace(text,type+' (','')[:-1])

    def on_plot_export_button( self, event ):
        self.temp = {}
        self.temp['pu'] = self.spatial['pu_shp'].to_crs("+proj=longlat +datum=WGS84")
        if 'spec_demo_pu' in self.project['connectivityMetrics']:
            self.temp['pu'] = pandas.concat(
                [self.temp['pu'], pandas.DataFrame.from_dict(self.project['connectivityMetrics']['spec_demo_pu'])],
                axis=1)
        if 'spec_land_pu' in self.project['connectivityMetrics']:
            self.temp['pu'] = pandas.concat(
                [self.temp['pu'], pandas.DataFrame.from_dict(self.project['connectivityMetrics']['spec_land_pu'])],
                axis=1)
        if 'best_solution' in self.project['connectivityMetrics']:
            self.temp['pu'] = pandas.concat([self.temp['pu'], pandas.DataFrame.from_dict(
                {'best_solution': self.project['connectivityMetrics']['best_solution'],
                 'select_freq': self.project['connectivityMetrics']['select_freq']})],
                                            axis=1)
        if 'status' in self.project['connectivityMetrics']:
            self.temp['pu'] = pandas.concat([self.temp['pu'], pandas.DataFrame.from_dict(
                {'status': self.project['connectivityMetrics']['status']})],
                                            axis=1)

        if self.PUSHP_filecheck.GetValue():
            self.temp['pu'].to_file(self.project['filepaths']['pushp'])
        if self.PUCSV_filecheck.GetValue():
            self.temp['pu'].to_csv(self.project['filepaths']['pucsv'])
        if self.MAP_filecheck.GetValue():
            self.plot.figure.savefig(self.project['filepaths']['map'])

    def get_plot_type(self, selection):
        if selection == "Planning Units":
            type = 'pu'
        elif selection == "Planning Units (Marxan Results)":
            type = 'pu'
        elif selection == "Planning Units (Demographic Data)":
            type = 'demo_pu'
        elif selection == "Planning Units (Landscape Data)":
            type = 'land_pu'
        elif selection == "Demographic Units":
            type = 'demo_cu'
        elif selection == "Landscape Units":
            type = 'land_cu'
        elif selection == "Focus Areas":
            type = 'fa'
        elif selection == "Avoidance Areas":
            type = 'aa'
        else:
            type = 'pu'
        return type

    def get_metric_type(self, selection, type):
        metric_type = self.spec_resolve_metric_choice('select_freq', selection, "Selection Frequency", type,
                                                      gettext=False)
        metric_type = self.spec_resolve_metric_choice('best_solution', selection, "Best Solution", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('status', selection, "Status", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('in_degree_' + type, selection, "In Degree", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('out_degree_' + type, selection, "Out Degree", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('between_cent_' + type, selection, "Betweenness Centrality", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('eig_vect_cent_' + type, selection, "Eigen Vector Centrality", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('google_' + type, selection, "Google Page Rank", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('self_recruit_' + type, selection, "Self Recruitment", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('local_retention_' + type, selection, "Local Retention", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('outflux_' + type, selection, "Outflux", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('influx_' + type, selection, "Influx", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('temp_conn_cov_' + type, selection, "Temporal Connectivity Covariance", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('fa_recipients_' + type, selection, "Focus Area Recipients", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('fa_donors_' + type, selection, "Focus Area Donors", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('aa_recipients_' + type, selection, "Avoidance Area Recipients", type,
                                                      gettext=False) or metric_type
        metric_type = self.spec_resolve_metric_choice('aa_donors_' + type, selection, "Avoidance Area Donors", type,
                                                      gettext=False) or metric_type
        return metric_type

# ###########################  file management functions ###############################################################
    def on_PU_file(self, event):
        """
        Defines Planning Unit file path
        """
        self.temp = {}
        self.project['filepaths']['pu_filepath'] = self.PU_file.GetPath()
        if os.path.isfile(self.project['filepaths']['pu_filepath']):
            self.spatial['pu_shp'] = gpd.GeoDataFrame.from_file(self.project['filepaths']['pu_filepath']).to_crs('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
            self.spatial['pu_proj'] = marxanconpy.get_appropriate_projection(self.spatial['pu_shp'], 'area')
            self.spatial['pu_shp'] = self.spatial['pu_shp'].to_crs(self.spatial['pu_proj'])
            self.temp['items'] = list(gpd.GeoDataFrame.from_file(self.project['filepaths']['pu_filepath']))
            self.PU_file_pu_id.SetItems(self.temp['items'])
            if self.project['filepaths']['pu_file_pu_id'] in self.temp['items']:
                self.PU_file_pu_id.SetStringSelection(self.project['filepaths']['pu_file_pu_id'])
            else:
                self.PU_file_pu_id.SetSelection(0)
        self.on_PU_file_pu_id(event=None)
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()
        self.on_FA_file(event=None)
        self.on_AA_file(event=None)

    def on_PU_file_pu_id(self, event):
        """
        Defines ID column label for the Planning Unit file
        """
        self.project['filepaths']['pu_file_pu_id'] = self.PU_file_pu_id.GetStringSelection()

    def on_demo_CU_file(self, event):
        """
        Defines Connectivity Unit file path
        """
        self.temp = {}
        self.project['filepaths']['demo_cu_filepath'] = self.demo_CU_file.GetPath()
        self.temp['items'] = list(gpd.GeoDataFrame.from_file(self.project['filepaths']['demo_cu_filepath']))
        self.demo_CU_file_pu_id.SetItems(self.temp['items'])
        if self.project['filepaths']['demo_cu_file_pu_id'] in self.temp['items']:
            self.demo_CU_file_pu_id.SetStringSelection(self.project['filepaths']['demo_cu_file_pu_id'])
        else:
            self.demo_CU_file_pu_id.SetSelection(0)
        self.on_demo_CU_file_pu_id(event=None)
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()

    def on_demo_CU_file_pu_id(self, event):
        """
        Defines ID column label for the demographic connectivity unit file
        """
        self.project['filepaths']['demo_cu_file_pu_id'] = self.demo_CU_file_pu_id.GetStringSelection()

    def on_land_HAB_file(self, event):
        """
        Defines landscape habitat type file path
        """
        self.temp = {}
        self.project['filepaths']['land_cu_filepath'] = self.land_HAB_file.GetPath()
        self.temp['items'] = list(gpd.GeoDataFrame.from_file(self.project['filepaths']['land_cu_filepath']))
        self.land_HAB_file_hab_id.SetItems(self.temp['items'])
        if self.project['filepaths']['land_cu_file_hab_id'] in self.temp['items']:
            self.land_HAB_file_hab_id.SetStringSelection(self.project['filepaths']['land_cu_file_hab_id'])
        else:
            self.land_HAB_file_hab_id.SetSelection(0)
        self.on_land_HAB_file_hab_id(event=None)
        self.outline_shapefile_choices()
        self.colormap_shapefile_choices()

    def on_land_HAB_file_hab_id(self, event):
        """
        Defines landscape Connectivity Unit file path
        """
        self.project['filepaths']['land_cu_file_hab_id'] = self.land_HAB_file_hab_id.GetStringSelection()

    def on_land_RES_mat_file(self, event):
        """
        Defines landscape habitat resistance matrix file path
        """
        self.project['filepaths']['land_res_mat_filepath'] = self.land_RES_mat_file.GetPath()

    def on_land_RES_file(self, event):
        """
        Defines landscape resistance surface file path
        """
        self.temp = {}
        self.project['filepaths']['land_res_filepath'] = self.land_RES_file.GetPath()
        self.temp['items'] = list(gpd.GeoDataFrame.from_file(self.project['filepaths']['land_res_file_hab_id']))
        self.land_RES_file_res_id.SetItems(self.temp['items'])
        if self.project['filepaths']['land_res_file_hab_id'] in self.temp['items']:
            self.land_RES_file_res_id.SetStringSelection(self.project['filepaths']['land_res_file_hab_id'])
        else:
            self.land_RES_file_res_id.SetSelection(0)

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
        if os.path.isfile(self.project['filepaths']['fa_filepath']):
            if 'pu_shp' in self.spatial:
                self.spatial['fa_shp'] = gpd.GeoDataFrame.from_file(self.project['filepaths']['fa_filepath']).to_crs(self.spatial['pu_proj'])
                self.spatial['fa_shp']['diss'] = 1
                self.spatial['fa_shp'] = self.spatial['fa_shp'].dissolve(by='diss')
                self.spatial['pu_shp']['fa_included'] = 0
                for index, purow in self.spatial['pu_shp'].iterrows():
                    self.spatial['pu_shp'].loc[index,'fa_included'] = self.spatial[
                        'fa_shp'].geometry.intersects(purow.geometry).bool()
        # enable metrics
        self.lock_pudat(self.project['filepaths']['pudat_filepath'])
        self.enable_metrics()

    def on_AA_file(self, event):
        """
        Defines Avoidance Areas file path
        """
        self.project['filepaths']['aa_filepath'] = self.AA_file.GetPath()
        if os.path.isfile(self.project['filepaths']['aa_filepath']):
            if 'pu_shp' in self.spatial:
                self.spatial['aa_shp'] = gpd.GeoDataFrame.from_file(self.project['filepaths']['aa_filepath']).to_crs(self.spatial['pu_proj'])
                self.spatial['aa_shp']['diss'] = 1
                self.spatial['aa_shp'] = self.spatial['aa_shp'].dissolve(by='diss')
                self.spatial['pu_shp']['aa_included'] = 0
                for index, purow in self.spatial['pu_shp'].iterrows():
                    self.spatial['pu_shp'].loc[index,'aa_included'] = self.spatial['aa_shp'].geometry.intersects(purow.geometry).bool()
        # enable metrics
        self.lock_pudat(self.project['filepaths']['pudat_filepath'])
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

    def on_PUDAT_file(self, event):
        """
        Defines planning unit data file path
        """
        self.project['filepaths']['pudat_filepath'] = self.PUDAT_file.GetPath()
        self.lock_pudat(self.project['filepaths']['pudat_filepath'])

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
            if format == "Edge List":
                self.ncol = 3
                self.expected = numpy.array(['id1', 'id2', 'value'])
            elif format == "Edge List with Time":
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

    def on_PUSHP_file( self, event ):
        """
        Defines planning unit (with metrics) export shapefile file path
        """
        self.project['filepaths']['pushp'] = self.PUSHP_file.GetPath()

    def on_PUCSV_file( self, event ):
        """
        Defines planning unit (with metrics) export csv file path
        """
        self.project['filepaths']['pucsv'] = self.PUCSV_file.GetPath()

    def on_MAP_file( self, event ):
        """
        Defines map image file path
        """
        self.project['filepaths']['map'] = self.MAP_file.GetPath()

# ###########################  option setting functions ################################################################

    def on_fa_status_radioBox(self, event):
        self.project['options']['fa_status'] = self.fa_status_radioBox.GetStringSelection()
        self.lock_pudat(self.project['filepaths']['pudat_filepath'])

    def on_aa_status_radioBox(self, event):
        self.project['options']['aa_status'] = self.aa_status_radioBox.GetStringSelection()
        self.lock_pudat(self.project['filepaths']['pudat_filepath'])

    def on_demo_matrixTypeRadioBox(self, event):
        self.project['options']['demo_conmat_type'] = self.demo_matrixTypeRadioBox.GetStringSelection()
        self.enable_metrics()

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

    def on_land_type_choice(self, event):
        """
        Hides unnecessary options if rescaling is not necessary
        """
        # hide or unhide
        self.project['options']['land_conmat_type'] = self.land_type_choice.GetPageText(self.land_type_choice.GetSelection())
        if self.project['options']['land_conmat_type'] == "Resistance Surface":
            enable_hab = False
            enable_surface = True
            self.warn_dialog("This feature is not yet operational, please check back in the next version!")
        elif self.project['options']['land_conmat_type'] == "Connectivity Matrix":
            enable_hab = False
            enable_surface = False
        elif self.project['options']['land_conmat_type'] == "Habitat Type + Resistance":
            enable_hab = True
            enable_surface = False

        self.land_HAB_filetext.Enable(enable_hab)
        self.land_HAB_file.Enable(enable_hab)
        self.land_HAB_file_hab_id_txt.Enable(enable_hab)
        self.land_HAB_file_hab_id.Enable(enable_hab)
        self.land_RES_mat_filetext.Enable(enable_hab)
        self.land_RES_mat_file.Enable(enable_hab)
        self.resistance_mat_customize.Enable(enable_hab)
        self.land_HAB_buff.Enable(enable_hab)
        self.land_HAB_buff_txt.Enable(enable_hab)
        self.land_HAB_thresh.Enable(enable_hab)
        self.land_HAB_thresh_txt.Enable(enable_hab)
        self.land_res_matrixTypeRadioBox.Enable(enable_hab)

        self.land_RES_filetext.Enable(enable_surface)
        self.land_RES_file.Enable(enable_surface)
        self.land_RES_def.Enable(enable_surface)
        self.land_res_file_res_id_txt.Enable(enable_surface)
        self.land_RES_file_res_id.Enable(enable_surface)
        self.land_generate_button.Enable(enable_surface or enable_hab)
        self.land_PU_CM_progress.Enable(enable_surface or enable_hab)

        # enable metrics
        self.enable_metrics()

    def on_land_res_matrixTypeRadioBox(self, event):
        self.project['options']['land_res_matrixType'] = self.land_res_matrixTypeRadioBox.GetStringSelection()
        if self.project['options']['land_res_matrixType'] == "Least-Cost Path":
            enable_hab = False
        elif self.project['options']['land_res_matrixType'] == "Euclidean Distance":
            enable_hab = False
        self.land_RES_mat_filetext.Enable(enable_hab)
        self.land_RES_mat_file.Enable(enable_hab)
        self.resistance_mat_customize.Enable(enable_hab)

    def on_land_HAB_buff(self, event):
        """
        Defines landscape type connectivity buffer (i.e. the distance between neighbouring planning units at which they
        will be connected for the least cost path analysis.)
        """
        self.project['options']['land_hab_buff'] = self.land_HAB_buff.GetValue()

    def on_land_HAB_thresh(self, event):
        """
        Threshold under which habitat connectivity values is considered null. Ranges from 0 to 1. Without a threshold,
         values for in/out degrees, and betweenness centrality will be homogeneous throughout each habitat type.
        """
        self.project['options']['land_hab_thresh'] = self.land_HAB_thresh.GetValue()

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
                if self.demo_matrixFormatRadioBox.GetStringSelection() == "Edge List with Time":
                    demo_fa_time_enable = True
                else:
                    demo_fa_time_enable = False
            else:
                demo_fa_enable = False
                demo_fa_time_enable = False

            if self.demo_matrixTypeRadioBox.GetStringSelection() == "Probability":
                demo_prob_enable = True
            else:
                demo_prob_enable = False
            if self.demo_matrixTypeRadioBox.GetStringSelection() == "Migration":
                demo_mig_enable = True
            else:
                demo_mig_enable = False
            if self.demo_matrixTypeRadioBox.GetStringSelection() == "Flux":
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
            demo_prob_enable = False
            demo_mig_enable = False
            demo_ind_enable = False
            demo_aa_enable = False

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

        self.cf_demo_in_degree.Enable(enable=demo_enable)
        self.cf_demo_out_degree.Enable(enable=demo_enable)
        self.cf_demo_between_cent.Enable(enable=demo_enable)
        self.cf_demo_eig_vect_cent.Enable(enable=demo_enable)
        self.cf_demo_google.Enable(enable=demo_enable)
        self.cf_demo_self_recruit.Enable(enable=demo_mig_enable)
        self.cf_demo_local_retention.Enable(enable=demo_prob_enable)
        self.cf_demo_outflux.Enable(enable=demo_ind_enable)
        self.cf_demo_influx.Enable(enable=demo_ind_enable)
        self.cf_demo_stochasticity.Enable(enable=demo_fa_time_enable)
        self.cf_demo_fa_recipients.Enable(enable=demo_fa_enable)
        self.cf_demo_fa_donors.Enable(enable=demo_fa_enable)
        self.cf_demo_aa_recipients.Enable(enable=demo_aa_enable)
        self.cf_demo_aa_donors.Enable(enable=demo_aa_enable)


        self.bd_demo_conn_boundary.Enable(enable=demo_enable)
        self.bd_demo_min_plan_graph.Enable(enable=demo_enable)

        self.cf_land_in_degree.Enable(enable=land_enable)
        self.cf_land_out_degree.Enable(enable=land_enable)
        self.cf_land_between_cent.Enable(enable=land_enable)
        self.cf_land_eig_vect_cent.Enable(enable=land_enable)
        self.cf_land_google.Enable(enable=land_enable)
        self.cf_land_fa_recipients.Enable(enable=land_fa_enable)
        self.cf_land_fa_donors.Enable(enable=land_fa_enable)
        self.cf_land_aa_recipients.Enable(enable=land_aa_enable)
        self.cf_land_aa_donors.Enable(enable=land_aa_enable)

        self.bd_land_conn_boundary.Enable(enable=land_enable)
        self.bd_land_min_plan_graph.Enable(enable=land_enable)

    def on_inputdat_symmRadio(self, event):
        self.project['options']['inputdat_boundary'] = self.inputdat_symmRadio.GetStringSelection()

    def on_cf_export_radioBox( self, event ):
        self.project['options']['cf_export'] = self.cf_export_radioBox.GetStringSelection()

# ########################## rescaling and matrix generation ###########################################################
    def on_demo_rescale_button(self, event):
        """
        Rescales the connectivity matrix to match the scale of the planning units
        """
        self.warn_dialog("Rescaling of matrices is offered as a convenience function. It it up to the user to determine"
                         " if the rescaling is ecologically valid. We recommend acquiring connectivity data at the same"
                         " scale as the planning unit")

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

        if self.demo_matrixFormatRadioBox.GetStringSelection() == "Edge List with Time":
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
            buff=float(self.project['options']['land_hab_buff']),
            hab_filepath=self.project['filepaths']['land_cu_filepath'],
            hab_id=self.project['filepaths']['land_cu_file_hab_id'],
            res_mat_filepath=self.project['filepaths']['land_res_mat_filepath'],
            pu_filepath=self.project['filepaths']['pu_filepath'],
            pu_id=self.project['filepaths']['pu_file_pu_id'],
            res_type=self.project['options']['land_res_matrixType'],
            progressbar=self.land_PU_CM_progress.GetValue())

        pandas.read_json(self.temp['land_pu_conmat'], orient='split').to_csv(
            self.project['filepaths']['land_pu_cm_filepath'], index=0, header=True, sep=",")

    def on_resistance_mat_customize(self,event):
        file_viewer(parent=self, file=self.project['filepaths']['land_res_mat_filepath'],
                    title='Resistance Matrix - WARNING CHANGES WILL NOT BE SAVED, check back in the next version!')

# ##########################  metric related functions ################################################################

    def on_calc_metrics(self, event):
        """
        calculates the selected metrics
        """
        # create dict entry for connectivityMetrics
        self.project['connectivityMetrics'] = {}
        self.temp = {}

        self.all_types = []
        if self.calc_metrics_pu.GetValue() and self.calc_metrics_cu.GetValue():
            if os.path.isfile(self.project['filepaths']['demo_pu_cm_filepath']):
                self.all_types += ['demo_pu', 'demo_cu']
            if os.path.isfile(self.project['filepaths']['land_pu_cm_filepath']):
                self.all_types += ['land_pu']
        elif self.calc_metrics_pu.GetValue():
            if os.path.isfile(self.project['filepaths']['demo_pu_cm_filepath']):
                self.all_types += ['demo_pu']
            if os.path.isfile(self.project['filepaths']['land_pu_cm_filepath']):
                self.all_types += ['land_pu']
        elif self.calc_metrics_cu.GetValue():
            if os.path.isfile(self.project['filepaths']['demo_cu_cm_filepath']):
                self.all_types += ['demo_cu']
        else:
            self.warn_dialog(message="No 'Units' selected for metric calculations.")

        # create dict entries for boundary
        self.project['connectivityMetrics']['boundary'] = {}

        for self.type in self.all_types:

            # check format
            if self.type[-2:] == 'pu':
                if self.type == 'demo_pu':
                    self.check_matrix_list_format(format=self.demo_matrixFormatRadioBox.GetStringSelection(),
                                                  filepath=self.project['filepaths'][self.type + '_cm_filepath'])
                    self.temp['format'] = self.demo_matrixFormatRadioBox.GetStringSelection()
                if self.type == 'land_pu':
                    self.temp['format'] = "Edge List with Habitat"

            # load correct matrix and transform if necessary
            if os.path.isfile(self.project['filepaths'][self.type + '_cm_filepath']):
                if self.temp['format'] == "Matrix":
                    self.temp[self.type + '_conmat'] = pandas.read_csv(
                        self.project['filepaths'][self.type + '_cm_filepath'], index_col=0)
                elif self.temp['format'] == "Edge List":
                    self.temp[self.type + '_conmat'] = pandas.read_csv(
                        self.project['filepaths'][self.type + '_cm_filepath'])
                    self.temp[self.type + '_conmat'] = self.temp[self.type + '_conmat'].pivot_table(values='value',
                                                                                                    index='id1',
                                                                                                    columns='id2')
                elif self.temp['format'] == "Edge List with Time":
                    self.temp[self.type + '_conmat_time'] = pandas.read_csv(
                        self.project['filepaths'][self.type + '_cm_filepath'])
                    self.temp[self.type + '_conmat'] = self.temp[self.type + '_conmat_time'][
                        ['id1', 'id2', 'value']].groupby(['id1', 'id2']).mean()
                    self.temp[self.type + '_conmat'] = self.temp[self.type + '_conmat'].pivot_table(values='value',
                                                                                                    index='id1',
                                                                                                    columns='id2')

                    self.warn_dialog(
                        message="A connectivity 'Edge List with Time' was provided; however, all metrics except "
                                "'Temporal Connectivity Correlation' will be calculated from the temporal"
                                "mean of connectivity")
                elif self.temp['format'] == "Edge List with Habitat":
                    self.temp[self.type + '_conmat_hab'] = pandas.read_csv(
                        self.project['filepaths'][self.type + '_cm_filepath'])
                    self.temp[self.type + '_conmat_hab'].loc[self.temp[self.type + '_conmat_hab']['value'] < float(
                        self.project['options']['land_hab_thresh']),'value'] = 0

                    self.temp[self.type + '_conmat'] = {}
                    for h in self.temp[self.type + '_conmat_hab']['habitat'].unique():
                        self.temp[self.type + '_conmat'][h] = self.temp[self.type + '_conmat_hab'][
                            self.temp[self.type + '_conmat_hab']['habitat'] == h].pivot_table(values='value', index='id1',
                                                                                          columns='id2')
                        if not self.temp[self.type + '_conmat'][h].values.sum()>0:
                            del self.temp[self.type + '_conmat'][h]
                            self.warn_dialog("All connectivity values for habitat '"+str(h)+"' are below the Habitat Connectivity Lower Threshold, excluding from further analyses")

            else:
                self.warn_dialog(message="File not found: " + self.project['filepaths'][self.type + '_cm_filepath'])


            # load correct shapefile path
            if self.type[-2:] == 'pu':
                self.temp['shp_filepath'] = self.project['filepaths']['pu_filepath']
                self.temp['shp_file_pu_id'] = self.project['filepaths']['pu_file_pu_id']
            else:
                self.temp['shp_filepath'] = self.project['filepaths'][self.type + '_filepath']
                self.temp['shp_file_pu_id'] = self.project['filepaths'][self.type + '_file_pu_id']

            # create dict entries for spec
            self.project['connectivityMetrics']['spec_' + self.type] = {}

            # warn if files not the same length
            if self.temp['format'] == "Edge List with Habitat":
                self.temp['conmat_len'] = str(len(next(iter(self.temp[self.type + '_conmat'].values()))))
            else:
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
                if not os.path.isfile(self.project['filepaths']['demo_lp_filepath']):
                    self.warn_dialog("No Local Production input. Marxan Connect will assume equal production in each planning unit.")

                if self.cf_demo_in_degree.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['in_degree_' + self.type] = \
                        marxanconpy.conmat2vertexdegree(self.temp[self.type + '_conmat'],mode='IN')

                if self.cf_demo_out_degree.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['out_degree_' + self.type] = \
                        marxanconpy.conmat2vertexdegree(self.temp[self.type + '_conmat'],mode='OUT')

                if self.cf_demo_between_cent.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['between_cent_' + self.type] = \
                        marxanconpy.conmat2betweencent(self.temp[self.type + '_conmat'])

                if self.cf_demo_eig_vect_cent.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['eig_vect_cent_' + self.type] = \
                        marxanconpy.conmat2eigvectcent(self.temp[self.type + '_conmat'])

                if self.cf_demo_google.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['google_' + self.type] = \
                        marxanconpy.conmat2google(self.temp[self.type + '_conmat'])

                if self.cf_demo_self_recruit.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['self_recruit_' + self.type] = \
                        marxanconpy.conmat2selfrecruit(self.temp[self.type + '_conmat'])

                if self.cf_demo_local_retention.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['local_retention_' + self.type] = \
                        marxanconpy.conmat2selfrecruit(self.temp[self.type + '_conmat'])

                if self.cf_demo_outflux.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['outflux_' + self.type] = \
                        marxanconpy.conmat2outflux(self.temp[self.type + '_conmat'])

                if self.cf_demo_influx.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['influx_' + self.type] = \
                        marxanconpy.conmat2influx(self.temp[self.type + '_conmat'])

                if self.demo_matrixTypeRadioBox.GetStringSelection() != "Flux":
                    if self.cf_demo_fa_recipients.GetValue() or\
                        self.cf_demo_fa_donors.GetValue() or\
                        self.cf_demo_aa_recipients.GetValue() or\
                        self.cf_demo_aa_donors.GetValue():
                        self.warn_dialog(message="Calculating any 'donors' or 'recipients' metrics using a connectivity"
                                                 " matrix with units other than 'Individuals' assumes outflux from all "
                                                 "planning units is equal.")

                if self.cf_demo_fa_recipients.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['fa_recipients_' + self.type] = \
                        marxanconpy.conmat2recipients(self.temp[self.type + '_conmat'],
                                                self.project['filepaths']['fa_filepath'],
                                                self.temp['shp_filepath'],
                                                self.temp['shp_file_pu_id']
                                                )

                if self.cf_demo_fa_donors.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['fa_donors_' + self.type] = \
                        marxanconpy.conmat2donors(self.temp[self.type + '_conmat'],
                                                self.project['filepaths']['fa_filepath'],
                                                self.temp['shp_filepath'],
                                                self.temp['shp_file_pu_id']
                                                )

                if self.cf_demo_aa_recipients.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['aa_recipients_' + self.type] = \
                        marxanconpy.conmat2recipients(self.temp[self.type + '_conmat'],
                                                      self.project['filepaths']['aa_filepath'],
                                                      self.temp['shp_filepath'],
                                                      self.temp['shp_file_pu_id'],
                                                      True
                                                      )

                if self.cf_demo_aa_donors.GetValue():
                    self.project['connectivityMetrics']['spec_' + self.type]['aa_donors_' + self.type] = \
                        marxanconpy.conmat2donors(self.temp[self.type + '_conmat'],
                                                  self.project['filepaths']['aa_filepath'],
                                                  self.temp['shp_filepath'],
                                                  self.temp['shp_file_pu_id'],
                                                  True
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

            # calculate landscape metrics ############################################################################
            if self.type[-7:] == 'land_pu':
                for h in self.temp[self.type + '_conmat'].keys():
                    if self.cf_land_in_degree.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type][
                            'in_degree_' + self.type + "_" + str(h)] = marxanconpy.conmat2vertexdegree(
                            self.temp[self.type + '_conmat'][h], mode='IN')

                    if self.cf_land_out_degree.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type][
                            'out_degree_' + self.type + "_" + str(h)] = marxanconpy.conmat2vertexdegree(
                            self.temp[self.type + '_conmat'][h], mode='OUT')

                    if self.cf_land_between_cent.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type]['between_cent_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2betweencent(self.temp[self.type + '_conmat'][h])

                    if self.cf_land_eig_vect_cent.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type]['eig_vect_cent_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2eigvectcent(self.temp[self.type + '_conmat'][h])

                    if self.cf_land_google.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type]['google_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2google(self.temp[self.type + '_conmat'][h])

                    if self.cf_land_fa_recipients.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type]['fa_recipients_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2recipients(self.temp[self.type + '_conmat'][h],
                                                    self.project['filepaths']['fa_filepath'],
                                                    self.temp['shp_filepath'],
                                                    self.temp['shp_file_pu_id']
                                                    )

                    if self.cf_land_fa_donors.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type]['fa_donors_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2donors(self.temp[self.type + '_conmat'][h],
                                                      self.project['filepaths']['fa_filepath'],
                                                      self.temp['shp_filepath'],
                                                      self.temp['shp_file_pu_id']
                                                      )

                    if self.cf_land_aa_recipients.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type][
                            'aa_recipients_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2recipients(self.temp[self.type + '_conmat'][h],
                                                          self.project['filepaths']['aa_filepath'],
                                                          self.temp['shp_filepath'],
                                                          self.temp['shp_file_pu_id'],
                                                          True
                                                          )

                    if self.cf_land_aa_donors.GetValue():
                        self.project['connectivityMetrics']['spec_' + self.type][
                            'aa_donors_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2donors(self.temp[self.type + '_conmat'][h],
                                                      self.project['filepaths']['aa_filepath'],
                                                      self.temp['shp_filepath'],
                                                      self.temp['shp_file_pu_id'],
                                                      True
                                                      )

                    if self.bd_land_conn_boundary.GetValue():
                        self.project['connectivityMetrics']['boundary']['conn_boundary_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2connboundary(self.temp[self.type + '_conmat'][h])

                    if self.bd_land_min_plan_graph.GetValue():
                        self.project['connectivityMetrics']['boundary']['min_plan_graph_' + self.type + "_" + str(h)] = \
                            marxanconpy.conmat2minplanarboundary(self.temp[self.type + '_conmat'][h])


        # create initial spec
        self.project['options']['metricsCalculated'] = True
        self.on_new_spec()
        self.customize_spec.Enable(enable=True)
        self.CFT_percent_slider.Enable(enable=True)
        self.export_metrics.Enable(enable=True)
        self.custom_spec_panel.SetToolTip(None)
        self.colormap_shapefile_choices()
        self.colormap_metric_choices(1)
        self.colormap_metric_choices(2)
        self.colormap_metric_choices("pre-eval")

    def on_export_metrics(self, event):
        cf = {}
        spec = {}
        for type in ['spec_demo_pu','spec_land_pu']:
            if type in self.project['connectivityMetrics']:
                for k in self.project['connectivityMetrics'][type].keys():
                    cf[k] = self.project['connectivityMetrics'][type].copy().pop(k)

        spec = pandas.read_json(self.project['spec_dat'], orient='split')
        if len(cf) == 0:
            self.warn_dialog(message="Conservation features can only be exported for planning units.")
            return

        # Export or append feature files
        if self.cf_export_radioBox.GetSelection() == 0:
            # export spec

            spec.to_csv(self.project['filepaths']['spec_filepath'], index=0)
            # export conservation features
            cf['pu'] = gpd.GeoDataFrame.from_file(self.project['filepaths']['pu_filepath'])[self.project['filepaths']['pu_file_pu_id']]
            cf = pandas.DataFrame(cf).melt(id_vars=['pu'], var_name='name', value_name='amount')
            cf = pandas.merge(cf, spec, how='outer', on='name')
            cf = cf.rename(columns={'id': 'species'}).sort_values(['pu', 'species'])
            cf = cf[cf['amount'] > 0]
            cf[['species', 'pu', 'amount']].to_csv(self.project['filepaths']['cf_filepath'], index=0)

        elif self.cf_export_radioBox.GetSelection() == 1:
            # append
            old_spec = pandas.read_csv(self.project['filepaths']['spec_filepath'])
            old_cf = pandas.read_csv(self.project['filepaths']['cf_filepath'])

            # append spec
            new_spec = spec.copy()
            new_spec['id'] = new_spec['id'] + max(old_spec['id'])
            pandas.concat([old_spec, new_spec]).fillna(0.0).to_csv(
                str.replace(self.project['filepaths']['spec_filepath'],
                            ".dat",
                            "_appended.dat")
                , index=0)
            # append conservation features
            new_cf = cf.copy()
            new_cf['pu'] = gpd.GeoDataFrame.from_file(self.project['filepaths']['pu_filepath'])[self.project['filepaths']['pu_file_pu_id']]
            new_cf = pandas.DataFrame(new_cf).melt(id_vars=['pu'], var_name='name', value_name='amount')
            new_cf = pandas.merge(new_cf, new_spec, how='outer', on='name')
            new_cf = new_cf.rename(columns={'id': 'species'})
            new_cf = new_cf[new_cf['amount']>0]
            pandas.concat([old_cf, new_cf[['species', 'pu', 'amount']]]).sort_values(['pu','species']).to_csv(
                str.replace(self.project['filepaths']['cf_filepath'], ".dat", "_appended.dat"), index=0)

        if self.BD_filecheck.GetValue():
            self.export_boundary_file(BD_filepath=self.project['filepaths']['bd_filepath'])
        if self.PUDAT_filecheck.GetValue():
            self.export_pudat_file(pudat_filepath=self.project['filepaths']['pudat_filepath'])

    def export_boundary_file(self, BD_filepath):
        self.all_types = []
        for type in ['demo_pu', 'land_pu']:
            if 'spec_'+type in self.project['connectivityMetrics']:
                self.all_types += [type]
        if len(self.all_types)==0:
            self.warn_dialog(message="Boundary files can only be exported for planning units.")
            return
        multiple = len(self.project['connectivityMetrics']['boundary'].keys()) > 1

        for k in self.project['connectivityMetrics']['boundary']:
            # Export each selected boundary definition
            if multiple:
                pandas.read_json(self.project['connectivityMetrics']['boundary'][k],
                                 orient='split').to_csv(str.replace(BD_filepath,
                                                                    ".dat",
                                                                    "_" + k + ".dat"),
                                                        index=False)
            else:
                pandas.read_json(self.project['connectivityMetrics']['boundary'][k],
                                 orient='split').to_csv(BD_filepath, index=False)

        # warn when multiple boundary definitions
        if multiple:
            self.warn_dialog(message="Multiple Boundary Definitions were selected. Boundary file names have been"
                                     " edited to include type.", caption="Warning!")

    def lock_pudat(self, pudat_filepath):
        if os.path.isfile(self.project['filepaths']['pudat_filepath']):
            self.temp = {}
            self.temp['pudat'] = pandas.read_csv(pudat_filepath)
            if os.path.isfile(self.project['filepaths']['fa_filepath']):
                if self.fa_status_radioBox.GetStringSelection() == "Locked out":
                    self.temp['pudat'].loc[numpy.array(self.spatial['pu_shp']['fa_included']), 'status'] = 3
                if self.fa_status_radioBox.GetStringSelection() == "Locked in":
                    self.temp['pudat'].loc[numpy.array(self.spatial['pu_shp']['fa_included']), 'status'] = 2

            if os.path.isfile(self.project['filepaths']['aa_filepath']):
                if self.aa_status_radioBox.GetStringSelection() == "Locked out":
                    self.temp['pudat'].loc[numpy.array(self.spatial['pu_shp']['aa_included']), 'status'] = 3
                if self.aa_status_radioBox.GetStringSelection() == "Locked in":
                    self.temp['pudat'].loc[numpy.array(self.spatial['pu_shp']['aa_included']), 'status'] = 2

            self.temp['all_metrics'] = []
            if 'connectivityMetrics' in self.project:
                if 'spec_demo_pu' in self.project['connectivityMetrics']:
                    self.temp['all_metrics'] += self.project['connectivityMetrics']['spec_demo_pu']
                if 'spec_land_pu' in self.project['connectivityMetrics']:
                    self.temp['all_metrics'] += self.project['connectivityMetrics']['spec_land_pu']

            for self.temp['metric'] in self.temp['all_metrics']:
                if 'demo_pu' in self.temp['metric']:
                    self.temp['metric_values'] = self.project['connectivityMetrics']['spec_demo_pu'][self.temp['metric']]
                if 'land_pu' in self.temp['metric']:
                    self.temp['metric_values'] = self.project['connectivityMetrics']['spec_land_pu'][self.temp['metric']]

                if self.temp['metric'].endswith('lockout'):
                    self.temp['pudat'].loc[numpy.array(self.temp['metric_values']) != 0, 'status'] = 3
                if self.temp['metric'].endswith('lockin'):
                    self.temp['pudat'].loc[numpy.array(self.temp['metric_values']) != 0, 'status'] = 2

                self.project['connectivityMetrics']['status'] = self.temp['pudat']['status'].tolist()
                self.colormap_shapefile_choices()
                self.colormap_metric_choices(1)
                self.colormap_metric_choices(2)

    def export_pudat_file(self, pudat_filepath):
        self.lock_pudat(pudat_filepath)
        self.temp['pudat'].to_csv(self.project['filepaths']['pudat_filepath'],index=0)
        # self.temp['pudat'].to_csv(str.replace(self.project['filepaths']['pudat_filepath'], ".dat", "_lock.dat"), index=0)

# ########################## pre-evaluation functions ##################################################################
    def on_preEval_metric_shp_choice(self,event):
        self.colormap_metric_choices("pre-eval")
        self.on_preEval_metric_choice(event=None)

    def on_preEval_metric_choice(self, event):
        self.temp = {}
        type = self.get_plot_type(selection=self.preEval_metric_shp_choice.GetStringSelection())
        metric_type = self.get_metric_type(selection=self.preEval_metric_choice.GetStringSelection(),
                                                     type=self.get_plot_type(
                                                         selection=self.preEval_metric_shp_choice.GetStringSelection()))

        if 'spec_' + type in self.project['connectivityMetrics']:
            self.temp['metric'] = self.project['connectivityMetrics']['spec_' + type][metric_type]

            self.preEval_grid.SetCellValue(0, 0, str(sum(self.temp['metric'])))
            self.preEval_grid.SetCellValue(1, 0, str(numpy.mean(self.temp['metric'])))
            self.preEval_grid.SetCellValue(2, 0, str(numpy.std(self.temp['metric'])))
            self.preEval_grid.SetCellValue(3, 0, str(min(self.temp['metric'])))
            self.preEval_grid.SetCellValue(4, 0, str(numpy.percentile(self.temp['metric'], 25)))
            self.preEval_grid.SetCellValue(5, 0, str(numpy.percentile(self.temp['metric'], 50)))
            self.preEval_grid.SetCellValue(6, 0, str(numpy.percentile(self.temp['metric'], 75)))
            self.preEval_grid.SetCellValue(7, 0, str(max(self.temp['metric'])))
            if 'aa_included' in self.spatial:
                self.preEval_grid.SetCellValue(8, 0, str((sum(
                    self.spatial['pu_shp']['aa_included'].multiply(self.temp['metric'])) / sum(
                    self.temp['metric']) * 100)))
            else:
                self.preEval_grid.SetCellValue(8, 0, 'NA')
            if 'fa_included' in self.spatial:
                self.preEval_grid.SetCellValue(9, 0, str((sum(
                    self.spatial['pu_shp']['fa_included'].multiply(self.temp['metric'])) / sum(
                    self.temp['metric']) * 100)))
            else:
                self.preEval_grid.SetCellValue(9, 0, 'NA')

    def on_plot_freq_metric( self, event ):
        self.temp = {}
        type = self.get_plot_type(selection=self.preEval_metric_shp_choice.GetStringSelection())
        metric_type = self.get_metric_type(selection=self.preEval_metric_choice.GetStringSelection(),
                                           type=self.get_plot_type(
                                               selection=self.preEval_metric_shp_choice.GetStringSelection()))

        # get the 'from' for discretization
        if 'spec_' + type in self.project['connectivityMetrics']:
            self.temp['metric'] = numpy.array(self.project['connectivityMetrics']['spec_' + type][metric_type])

        # prepare plotting window
        if not hasattr(self, 'plot'):
            self.plot = wx.Panel(self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            self.auinotebook.AddPage(self.plot, u"7) Plot", False, wx.NullBitmap)
        self.plot.figure = plt.figure(figsize=self.plot.GetClientSize() / wx.ScreenDC().GetPPI()[0])
        self.plot.axes = self.plot.figure.gca()
        self.plot.canvas = FigureCanvas(self.plot, -1, self.plot.figure)
        self.plot.sizer = wx.BoxSizer(wx.VERTICAL)
        self.plot.sizer.Add(self.plot.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.plot.SetSizer(self.plot.sizer)
        self.plot.Fit()

        self.plot.hist = plt.hist(self.temp['metric'],bins=int(len(self.temp['metric'])/15))
        self.plot.xlabel = plt.xlabel(metric_type)
        self.plot.ylabel = plt.ylabel("Frequency")
        self.plot.axvline = plt.axvline(numpy.percentile(self.temp['metric'], 25), label='test',color='k',linestyle='--')
        self.plot.text = plt.text(numpy.percentile(self.temp['metric'], 20),sum(self.plot.axes.get_ylim())/2,'Lower Quartile',rotation=90,verticalalignment='center')
        self.plot.axvline = plt.axvline(numpy.percentile(self.temp['metric'], 50), label='test',color='k',linestyle='--')
        self.plot.text = plt.text(numpy.percentile(self.temp['metric'], 45), sum(self.plot.axes.get_ylim()) / 2, 'Median', rotation=90,verticalalignment='center')
        self.plot.axvline = plt.axvline(numpy.percentile(self.temp['metric'], 75), label='test',color='k',linestyle='--')
        self.plot.text = plt.text(numpy.percentile(self.temp['metric'], 70), sum(self.plot.axes.get_ylim()) / 2, 'Upper Quartile', rotation=90,verticalalignment='center')
        # change selection to plot tab
        for i in range(self.auinotebook.GetPageCount()):
            if self.auinotebook.GetPageText(i) == "7) Plot":
                self.auinotebook.ChangeSelection(i)

    def on_remove_metric(self,event):
        type = self.get_plot_type(selection=self.preEval_metric_shp_choice.GetStringSelection())
        metric_type = self.get_metric_type(selection=self.preEval_metric_choice.GetStringSelection(),
                                           type=self.get_plot_type(
                                               selection=self.preEval_metric_shp_choice.GetStringSelection()))
        if 'spec_' + type in self.project['connectivityMetrics']:
            del self.project['connectivityMetrics']['spec_' + type][metric_type]
            if len(self.project['connectivityMetrics']['spec_' + type])==0:
                del self.project['connectivityMetrics']['spec_' + type]
        self.colormap_shapefile_choices()
        self.colormap_metric_choices("pre-eval")
        self.on_preEval_metric_choice(event=None)
        self.on_new_spec()

    def on_preEval_create_new(self, event):
        self.temp = {}
        type = self.get_plot_type(selection=self.preEval_metric_shp_choice.GetStringSelection())
        metric_type = self.get_metric_type(selection=self.preEval_metric_choice.GetStringSelection(),
                                           type=self.get_plot_type(
                                               selection=self.preEval_metric_shp_choice.GetStringSelection()))
        
        # get the 'from' for discretization
        if 'spec_' + type in self.project['connectivityMetrics']:
            self.temp['metric'] = numpy.array(self.project['connectivityMetrics']['spec_' + type][metric_type])

        if self.preEval_discrete_from_quartile.GetValue():
            if self.preEval_discrete_from_quartile_radio.GetStringSelection()== "Minimum":
                self.temp['from_type'] = 'minimum'
                self.temp['from'] = min(self.temp['metric'])
            if self.preEval_discrete_from_quartile_radio.GetStringSelection()== "Lower Quartile":
                self.temp['from_type'] = 'lower_quartile'
                self.temp['from'] = numpy.percentile(self.temp['metric'], 25)
            if self.preEval_discrete_from_quartile_radio.GetStringSelection()== "Median":
                self.temp['from_type'] = 'median'
                self.temp['from'] = numpy.percentile(self.temp['metric'], 50)
            if self.preEval_discrete_from_quartile_radio.GetStringSelection()== "Upper Quartile":
                self.temp['from_type'] = 'upper_quartile'
                self.temp['from'] = numpy.percentile(self.temp['metric'], 75)
            if self.preEval_discrete_from_quartile_radio.GetStringSelection()== "Maximum":
                self.temp['from_type'] = 'maximum'
                self.temp['from'] = max(self.temp['metric'])

        if self.preEval_discrete_from_percentile.GetValue():
            self.temp['from'] = numpy.percentile(self.temp['metric'],
                                                 self.preEval_discrete_from_percentile_slider.GetValue())
            self.temp['from_type'] = str(self.temp['from']) + 'th_percentile'

        if self.preEval_discrete_from_value.GetValue():
            self.temp['from'] = float(self.preEval_discrete_from_value_txtctrl.GetValue())
            self.temp['from_type'] = str(self.temp['from']) + 'th_percentile'

        # get the 'to' for discretization
        if self.preEval_discrete_to_quartile.GetValue():
            if self.preEval_discrete_to_quartile_radio.GetStringSelection() == "Minimum":
                self.temp['to_type'] = 'minimum'
                self.temp['to'] = min(self.temp['metric'])
            if self.preEval_discrete_to_quartile_radio.GetStringSelection() == "Lower Quartile":
                self.temp['to_type'] = 'lower_quartile'
                self.temp['to'] = numpy.percentile(self.temp['metric'], 25)
            if self.preEval_discrete_to_quartile_radio.GetStringSelection() == "Median":
                self.temp['to_type'] = 'median'
                self.temp['to'] = numpy.percentile(self.temp['metric'], 50)
            if self.preEval_discrete_to_quartile_radio.GetStringSelection() == "Upper Quartile":
                self.temp['to_type'] = 'upper_quartile'
                self.temp['to'] = numpy.percentile(self.temp['metric'], 75)
            if self.preEval_discrete_to_quartile_radio.GetStringSelection() == "Maximum":
                self.temp['to_type'] = 'maximum'
                self.temp['to'] = max(self.temp['metric'])

        if self.preEval_discrete_to_percentile.GetValue():
            self.temp['to'] = numpy.percentile(self.temp['metric'],
                                                 self.preEval_discrete_to_percentile_slider.GetValue())
            self.temp['to_type'] = str(self.temp['to']) + 'th_percentile'

        if self.preEval_discrete_to_value.GetValue():
            self.temp['to'] = float(self.preEval_discrete_to_value_txtctrl.GetValue())
            self.temp['to_type'] = str(self.temp['to']) + 'th_percentile'

        
        # create new metric
        self.temp['new_metric'] = (self.temp['metric']>=self.temp['from']) & (self.temp['metric']<=self.temp['to']).astype(int)
        if self.preEval_status_radio.GetStringSelection() == "Status-quo":
            self.project['connectivityMetrics']['spec_' + type][
            metric_type + '_' + self.temp['from_type'] + '_to_' + self.temp['to_type']] = self.temp[
            'new_metric'].tolist()
        if self.preEval_status_radio.GetStringSelection() == "Locked out":
            self.project['connectivityMetrics']['spec_' + type][
            metric_type + '_' + self.temp['from_type'] + '_to_' + self.temp['to_type'] + '_lockout'] = self.temp[
            'new_metric'].tolist()
        if self.preEval_status_radio.GetStringSelection() == "Locked in":
            self.project['connectivityMetrics']['spec_' + type][
            metric_type + '_' + self.temp['from_type'] + '_to_' + self.temp['to_type'] + '_lockin'] = self.temp[
            'new_metric'].tolist()
        
        # reset choices
        self.lock_pudat(self.project['filepaths']['pudat_filepath'])
        self.colormap_shapefile_choices()
        self.colormap_metric_choices("pre-eval")
        self.on_preEval_metric_choice(event=None)
        self.on_new_spec()

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

        # edit input file
        # Read in the file
        with open(self.project['filepaths']['marxan_input'], 'r', encoding="utf8") as file:
            filedata = file.readlines()

        if self.project['options']['inputdat_boundary'] == 'Asymetric':
            if not 'ASYMMETRICCONNECTIVITY  1\n' in filedata:
                filedata.insert([index for index, line in enumerate(filedata) if line.startswith('NUMREPS')][0] + 1,
                            'ASYMMETRICCONNECTIVITY  1\n')
        else:
            if 'ASYMMETRICCONNECTIVITY  1\n' in filedata:
                filedata.remove('ASYMMETRICCONNECTIVITY  1\n')

        # Write the file out again
        with open(self.project['filepaths']['marxan_input'], 'w', encoding="utf8") as file:
            file.write("".join(filedata))



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

    def on_view_mvbest(self,event):
        self.temp = {}
        for line in open(self.project['filepaths']['marxan_input']):
            if line.startswith('SCENNAME'):
                self.temp['SCENNAME'] = line.replace('SCENNAME ', '').replace('\n', '')
            elif line.startswith('OUTPUTDIR'):
                self.temp['OUTPUTDIR'] = line.replace('OUTPUTDIR ', '').replace('\n', '')
        file_viewer(parent=self, file=os.path.join(self.temp['OUTPUTDIR'],self.temp['SCENNAME']+'_mvbest.txt'),
                    title='mvbest')

    def on_view_sum(self,event):
        self.temp = {}
        for line in open(self.project['filepaths']['marxan_input']):
            if line.startswith('SCENNAME'):
                self.temp['SCENNAME'] = line.replace('SCENNAME ', '').replace('\n', '')
            elif line.startswith('OUTPUTDIR'):
                self.temp['OUTPUTDIR'] = line.replace('OUTPUTDIR ', '').replace('\n', '')
        file_viewer(parent=self, file=os.path.join(self.temp['OUTPUTDIR'],self.temp['SCENNAME']+'_sum.txt'),
                    title='sum')

# ###########################  spec grid popup functions ###############################################################
    def on_customize_spec(self, event):
        if self.calc_metrics_pu.GetValue() & self.project['options']['metricsCalculated']:
            if hasattr(self,'spec_frame'):
                self.spec_frame.Show()
            else:
                self.on_new_spec()
                self.spec_frame.Show()
        else:
            self.warn_dialog(message="'Planning Units' not selected for metric calculations.")

    def on_new_spec(self):
        self.spec_frame = spec_customizer(parent=self)
        self.all_types = []
        if self.calc_metrics_pu.GetValue():
            if os.path.isfile(self.project['filepaths']['demo_pu_cm_filepath']):
                self.all_types += ['demo_pu']
            if os.path.isfile(self.project['filepaths']['land_pu_cm_filepath']):
                self.all_types += ['land_pu']
        else:
            self.warn_dialog(message="'Planning Units' not selected for metric calculations.")
            return

        for self.type in self.all_types:
            self.spec_frame.keys = list(self.project['connectivityMetrics']['spec_' + self.type])

            for j in range(len(self.spec_frame.keys)):
                if j != self.spec_frame.spec_grid.GetNumberRows():
                    i = self.spec_frame.spec_grid.GetNumberRows()
                else:
                    i=j
                self.spec_frame.spec_grid.InsertRows(i)
                self.spec_frame.spec_grid.SetCellValue(i, 0, str(i + 1))
                sum_metric = sum(self.project['connectivityMetrics']['spec_' + self.type][self.spec_frame.keys[j]])
                self.spec_frame.spec_grid.SetCellValue(i, 1, str(sum_metric * self.CFT_percent_slider.GetValue() / 100))
                self.spec_frame.spec_grid.SetCellValue(i, 2, str(1000))
                self.spec_frame.spec_grid.SetCellValue(i, 3, self.spec_frame.keys[j])
                w, h = self.spec_frame.GetClientSize()

                self.spec_frame.SetSize((w + 16, h + 39 + 20))
                self.spec_frame.Layout()
                self.spec_frame.spec_grid.AutoSize()
        self.project['spec_dat'] = pandas.DataFrame(
            numpy.full((self.spec_frame.spec_grid.GetNumberRows(), self.spec_frame.spec_grid.GetNumberCols()), None))
        self.project['spec_dat'].columns = ["id", "target", "spf", "name"]

        for c in range(self.spec_frame.spec_grid.GetNumberCols()):
            for r in range(self.spec_frame.spec_grid.GetNumberRows()):
                self.project['spec_dat'].iloc[r, c] = self.spec_frame.spec_grid.GetCellValue(r, c)

        self.project['spec_dat'] = self.project['spec_dat'].to_json(orient='split')

    def on_CFT_percent_slider(self, event):
        self.on_new_spec()

class spec_customizer(gui.spec_customizer):
    def __init__(self, parent):
        gui.spec_customizer.__init__(self, parent)
        self.parent = parent

    def on_spec_ok(self, event):
        self.parent.project['spec_dat'] = pandas.DataFrame(
            numpy.full((self.spec_grid.GetNumberRows(),
                        self.spec_grid.GetNumberCols()), None))
        self.parent.project['spec_dat'].columns = ["id", "target", "spf", "name"]

        for c in range(self.spec_grid.GetNumberCols()):
            for r in range(self.spec_grid.GetNumberRows()):
                self.parent.project['spec_dat'].iloc[r, c] = self.spec_grid.GetCellValue(r, c)
        self.parent.project['spec_dat'] = self.parent.project[
            'spec_dat'].to_json(orient='split')
        self.Hide()

    def on_spec_cancel(self, event):
        self.Hide()

# ###########################  getting started popup functions #########################################################
class GettingStarted (wx.Frame):
    def __init__(self, parent):
        gui.GettingStarted.__init__(self, parent)
        # set the icon
        parent.set_icon(frame=self)

# ########################### file popup viewer #####################################################################

class file_viewer(wx.Dialog):
    def __init__(self, parent, file, title):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=wx.Size(-1, -1), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        file_mainsizer = wx.FlexGridSizer(0, 1, 0, 0)
        file_mainsizer.SetFlexibleDirection(wx.BOTH)
        file_mainsizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.file_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Load file
        df = pandas.read_csv(file)

        # Grid
        self.file_grid.CreateGrid(df.shape[0], df.shape[1])
        self.file_grid.EnableEditing(False)
        self.file_grid.EnableGridLines(True)
        self.file_grid.EnableDragGridSize(False)
        self.file_grid.SetMargins(0, 0)

        # Columns
        self.file_grid.EnableDragColMove(False)
        self.file_grid.EnableDragColSize(True)
        self.file_grid.SetColLabelSize(30)
        for col, label in enumerate(df.columns):
            self.file_grid.SetColLabelValue(col,label)
            for index in df.index:
                self.file_grid.SetCellValue(index, col, str(df.iloc[index, col]))
        self.file_grid.AutoSizeColumns()
        self.file_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.file_grid.EnableDragRowSize(True)
        self.file_grid.SetRowLabelSize(80)
        self.file_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Cell Defaults
        self.file_grid.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        file_mainsizer.Add(self.file_grid, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        file_button_sizer = wx.FlexGridSizer(0, 3, 0, 0)
        file_button_sizer.AddGrowableCol(0)
        file_button_sizer.SetFlexibleDirection(wx.BOTH)
        file_button_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.spacer_text = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer_text.Wrap(-1)
        file_button_sizer.Add(self.spacer_text, 0, wx.ALL, 5)

        self.file_ok = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        file_button_sizer.Add(self.file_ok, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        file_mainsizer.Add(file_button_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(file_mainsizer)
        self.Layout()
        file_mainsizer.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.file_ok.Bind(wx.EVT_BUTTON, self.on_file_ok)

        self.Show()

    def on_file_ok(self,event):
        self.Hide()

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
