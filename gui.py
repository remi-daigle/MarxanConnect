# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.html
import wx.grid
import wx.adv

###########################################################################
## Class MarxanConnectGUI
###########################################################################

class MarxanConnectGUI ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marxan Connect", pos = wx.DefaultPosition, size = wx.Size( 1200,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.menu = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.new_project = wx.MenuItem( self.file, wx.ID_ANY, u"New Project"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.new_project )

		self.save_project = wx.MenuItem( self.file, wx.ID_ANY, u"Save Project"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.save_project )

		self.save_project_as = wx.MenuItem( self.file, wx.ID_ANY, u"Save Project As..."+ u"\t" + u"Ctrl+Shift+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.save_project_as )

		self.load_project = wx.MenuItem( self.file, wx.ID_ANY, u"Load Project"+ u"\t" + u"Ctrl+L", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.load_project )

		self.menu.Append( self.file, u"File" )

		self.debug = wx.Menu()
		self.github = wx.MenuItem( self.debug, wx.ID_ANY, u"GitHub issues", wx.EmptyString, wx.ITEM_NORMAL )
		self.debug.Append( self.github )

		self.debug_mode = wx.MenuItem( self.debug, wx.ID_ANY, u"Debug Mode"+ u"\t" + u"Ctrl+D", wx.EmptyString, wx.ITEM_NORMAL )
		self.debug.Append( self.debug_mode )

		self.menu.Append( self.debug, u"Debug" )

		self.help = wx.Menu()
		self.glossary = wx.MenuItem( self.help, wx.ID_ANY, u"Glossary", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.glossary )

		self.tutorial = wx.MenuItem( self.help, wx.ID_ANY, u"Tutorial", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.tutorial )

		self.contributing = wx.MenuItem( self.help, wx.ID_ANY, u"Contributing", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.contributing )

		self.license = wx.MenuItem( self.help, wx.ID_ANY, u"License", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.license )

		self.about = wx.MenuItem( self.help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.about )

		self.start = wx.MenuItem( self.help, wx.ID_ANY, u"Getting Started", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.start )

		self.experimental = wx.Menu()
		self.mwz = wx.MenuItem( self.experimental, wx.ID_ANY, u"Marxan with Zones", wx.EmptyString, wx.ITEM_NORMAL )
		self.experimental.Append( self.mwz )

		self.posthoc = wx.MenuItem( self.experimental, wx.ID_ANY, u"Posthoc Tab", wx.EmptyString, wx.ITEM_NORMAL )
		self.experimental.Append( self.posthoc )

		self.help.AppendSubMenu( self.experimental, u"Experimental Features" )

		self.menu.Append( self.help, u"Help" )

		self.SetMenuBar( self.menu )

		aui_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.auinotebook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_TAB_EXTERNAL_MOVE|wx.aui.AUI_NB_TAB_MOVE|wx.aui.AUI_NB_TAB_SPLIT|wx.aui.AUI_NB_TOP|wx.aui.AUI_NB_WINDOWLIST_BUTTON )
		self.spatialInput = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spatialMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		spatialMainSizer.AddGrowableCol( 0 )
		spatialMainSizer.AddGrowableRow( 1 )
		spatialMainSizer.AddGrowableRow( 2 )
		spatialMainSizer.AddGrowableRow( 4 )
		spatialMainSizer.AddGrowableRow( 6 )
		spatialMainSizer.AddGrowableRow( 8 )
		spatialMainSizer.AddGrowableRow( 10 )
		spatialMainSizer.SetFlexibleDirection( wx.VERTICAL )
		spatialMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

		self.pu_title = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Planning Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_title.Wrap( -1 )

		self.pu_title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		spatialMainSizer.Add( self.pu_title, 0, wx.ALL, 5 )

		pu_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.PU_def = wx.StaticText( self.spatialInput, wx.ID_ANY, u"The planning unit is the fundamental spatial polygon on which Marxan analyses are based. The units can be any shape. Often square or hexagonal regular grids, or based on habitat features (e.g. reefs, kelp beds, rivers, forests). All futher analyses will be based on whether a feature is present or absent in the planning unit.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_def.Wrap( -1 )

		pu_def_sizer.Add( self.PU_def, 0, wx.ALL|wx.EXPAND, 5 )


		spatialMainSizer.Add( pu_def_sizer, 1, wx.EXPAND, 5 )

		pu_file_sizer1 = wx.FlexGridSizer( 0, 4, 0, 0 )
		pu_file_sizer1.AddGrowableCol( 1 )
		pu_file_sizer1.SetFlexibleDirection( wx.HORIZONTAL )
		pu_file_sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.PU_filetext = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Planning Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_filetext.Wrap( -1 )

		self.PU_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		pu_file_sizer1.Add( self.PU_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.PU_file = wx.FilePickerCtrl( self.spatialInput, wx.ID_ANY, u"~\\data\\shapefiles\\marxan_pu.shp", u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		pu_file_sizer1.Add( self.PU_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

		self.PU_file_pu_id_txt = wx.StaticText( self.spatialInput, wx.ID_ANY, u"ID Column Label", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_file_pu_id_txt.Wrap( -1 )

		self.PU_file_pu_id_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		pu_file_sizer1.Add( self.PU_file_pu_id_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		PU_file_pu_idChoices = []
		self.PU_file_pu_id = wx.Choice( self.spatialInput, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PU_file_pu_idChoices, 0 )
		self.PU_file_pu_id.SetSelection( 0 )
		pu_file_sizer1.Add( self.PU_file_pu_id, 0, wx.ALL, 5 )


		spatialMainSizer.Add( pu_file_sizer1, 1, wx.EXPAND, 5 )

		self.fa_title = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Focus Areas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fa_title.Wrap( -1 )

		self.fa_title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		spatialMainSizer.Add( self.fa_title, 0, wx.ALL, 5 )

		fa_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.FA_def = wx.StaticText( self.spatialInput, wx.ID_ANY, u"For some of the connectivity metrics, it is important to consider 'focus areas' for which connectivity should be optimised. Such focus areas could include existing protected areas, important habitat for endangered species, and/or otherwise important habitats for connectivity (e.g. nursery grounds, genetically unique and potentially adaptively advantageous populations).", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FA_def.Wrap( -1 )

		fa_def_sizer.Add( self.FA_def, 0, wx.ALL|wx.EXPAND, 5 )


		spatialMainSizer.Add( fa_def_sizer, 1, wx.EXPAND, 5 )

		fa_file_sizer = wx.FlexGridSizer( 1, 2, 0, 0 )
		fa_file_sizer.AddGrowableCol( 1 )
		fa_file_sizer.SetFlexibleDirection( wx.BOTH )
		fa_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.FA_filetext = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Focus Areas Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FA_filetext.Wrap( -1 )

		self.FA_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		fa_file_sizer.Add( self.FA_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.FA_file = wx.FilePickerCtrl( self.spatialInput, wx.ID_ANY, wx.EmptyString, u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fa_file_sizer.Add( self.FA_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )


		spatialMainSizer.Add( fa_file_sizer, 1, wx.EXPAND, 5 )

		fa_status_sizer = wx.FlexGridSizer( 1, 1, 0, 0 )
		fa_status_sizer.AddGrowableCol( 0 )
		fa_status_sizer.SetFlexibleDirection( wx.BOTH )
		fa_status_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fa_status_radioBoxChoices = [ u"Locked in", u"Locked out", u"Status-quo" ]
		self.fa_status_radioBox = wx.RadioBox( self.spatialInput, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, fa_status_radioBoxChoices, 3, wx.RA_SPECIFY_COLS )
		self.fa_status_radioBox.SetSelection( 2 )
		self.fa_status_radioBox.SetToolTip( u"For the planning units which overlap with the Focus Area, you can choose to overwrite the status of the original planning unit (i.e. pu.dat) to lock the planning units in out. Alternatively, select 'Status-quo' to keep the status of the original planning unit (i.e. pu.dat)." )

		fa_status_sizer.Add( self.fa_status_radioBox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		spatialMainSizer.Add( fa_status_sizer, 1, wx.EXPAND, 5 )

		self.aa_title = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Avoidance Areas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.aa_title.Wrap( -1 )

		self.aa_title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		spatialMainSizer.Add( self.aa_title, 0, wx.ALL, 5 )

		aa_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.AA_def = wx.StaticText( self.spatialInput, wx.ID_ANY, u"For some of the connectivity metrics, it is important to consider 'avoidance areas' for which connectivity should be avoided. Such avoidance areas could include areas heavily infested by invasive species or are more likely to be invaded (e.g. international shipping ports), or areas that are potential sources of pollutants (e.g. oil extraction, river outflows).", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AA_def.Wrap( -1 )

		aa_def_sizer.Add( self.AA_def, 0, wx.ALL|wx.EXPAND, 5 )


		spatialMainSizer.Add( aa_def_sizer, 1, wx.EXPAND, 5 )

		aa_file_sizer = wx.FlexGridSizer( 1, 2, 0, 0 )
		aa_file_sizer.AddGrowableCol( 1 )
		aa_file_sizer.SetFlexibleDirection( wx.BOTH )
		aa_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.AA_filetext = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Avoidance Areas Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AA_filetext.Wrap( -1 )

		self.AA_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		aa_file_sizer.Add( self.AA_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.AA_file = wx.FilePickerCtrl( self.spatialInput, wx.ID_ANY, wx.EmptyString, u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		aa_file_sizer.Add( self.AA_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )


		spatialMainSizer.Add( aa_file_sizer, 1, wx.EXPAND, 5 )

		aa_status_sizer = wx.FlexGridSizer( 1, 1, 0, 0 )
		aa_status_sizer.AddGrowableCol( 0 )
		aa_status_sizer.AddGrowableRow( 0 )
		aa_status_sizer.SetFlexibleDirection( wx.BOTH )
		aa_status_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		aa_status_radioBoxChoices = [ u"Locked in", u"Locked out", u"Status-quo" ]
		self.aa_status_radioBox = wx.RadioBox( self.spatialInput, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, aa_status_radioBoxChoices, 3, wx.RA_SPECIFY_COLS )
		self.aa_status_radioBox.SetSelection( 2 )
		self.aa_status_radioBox.SetToolTip( u"For the planning units which overlap with the Avoidance Area, you can choose to overwrite the status of the original planning unit (i.e. pu.dat) to lock the planning units in out. Alternatively, select 'Status-quo' to keep the status of the original planning unit (i.e. pu.dat)." )

		aa_status_sizer.Add( self.aa_status_radioBox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		spatialMainSizer.Add( aa_status_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.spatialInput.SetSizer( spatialMainSizer )
		self.spatialInput.Layout()
		spatialMainSizer.Fit( self.spatialInput )
		self.auinotebook.AddPage( self.spatialInput, u"1) Spatial Input", True, wx.NullBitmap )
		self.connectivityInput = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		conn_input_mainsizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		conn_input_mainsizer.AddGrowableCol( 0 )
		conn_input_mainsizer.AddGrowableRow( 3 )
		conn_input_mainsizer.SetFlexibleDirection( wx.BOTH )
		conn_input_mainsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		con_input_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.con_input_def_txt = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Connectivity data originate from many sources and to simplify the input procedure has been divided into two main categories: demographic connectivity and landscape connectivity.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.con_input_def_txt.Wrap( -1 )

		con_input_def_sizer.Add( self.con_input_def_txt, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )


		conn_input_mainsizer.Add( con_input_def_sizer, 1, wx.EXPAND, 5 )

		con_input_def_sizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.con_input_def_txt1 = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Choosing a different category will not erase any input and input from multiple categories can be used simultaneously in the analyses in the next steps", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.con_input_def_txt1.Wrap( -1 )

		con_input_def_sizer1.Add( self.con_input_def_txt1, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )


		conn_input_mainsizer.Add( con_input_def_sizer1, 1, wx.EXPAND, 5 )

		con_input_choice_sizer = wx.BoxSizer( wx.VERTICAL )

		self.con_input_choice_txt = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Choose Connectivity Input Category:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.con_input_choice_txt.Wrap( -1 )

		self.con_input_choice_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		con_input_choice_sizer.Add( self.con_input_choice_txt, 0, wx.ALL, 5 )


		conn_input_mainsizer.Add( con_input_choice_sizer, 1, wx.EXPAND, 5 )

		self.conn_category_choicebook = wx.Choicebook( self.connectivityInput, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.conn_category_choicebook.SetToolTip( u"Choosing a different category will not erase any input and input from multiple categories can be used simultaneously in the analyses in the next steps" )

		self.demographic = wx.Panel( self.conn_category_choicebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		demoMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		demoMainSizer.AddGrowableCol( 0 )
		demoMainSizer.AddGrowableRow( 0 )
		demoMainSizer.SetFlexibleDirection( wx.VERTICAL )
		demoMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

		demo_cm_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.demo_CM_def = wx.StaticText( self.demographic, wx.ID_ANY, u"The connectivity matrix (or list) is the fundamental input format for demographic data. It describes the movement from donor sites to recipient sites. It can be obtained by directly quantifying the movement of individual organisms (e.g. tagging) or  by modelling the dispersal of individual organisms (e.g. biophysical modelling of larval dispersal). Please indicate your connectivity data units, type, and format in the boxes below, and if necessary use the rescaling tools if the data were not gathered at the same spatial scale as the planning units. The demographic connectivity data does not need to be at the same spatial scale as the Marxan planning units. If there is a mismatch, rescale the connectivity data below. If the connectivity data were collected at a scale different than that of the planning units, you will need to supply a Connectivity Matrix Shapefile which describes the spatial polygons for which the data were gathered.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_CM_def.Wrap( -1 )

		demo_cm_def_sizer.Add( self.demo_CM_def, 0, wx.ALL|wx.EXPAND, 5 )


		demoMainSizer.Add( demo_cm_def_sizer, 1, wx.EXPAND, 5 )

		demo_radio_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		demo_radio_sizer.AddGrowableCol( 1 )
		demo_radio_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		demo_radio_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		demo_matrixTypeRadioBoxChoices = [ u"Probability", u"Migration", u"Flow" ]
		self.demo_matrixTypeRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Connectivity Matrix Type", wx.DefaultPosition, wx.DefaultSize, demo_matrixTypeRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.demo_matrixTypeRadioBox.SetSelection( 0 )
		demo_radio_sizer.Add( self.demo_matrixTypeRadioBox, 0, wx.ALL|wx.EXPAND, 5 )

		demo_matrixFormatRadioBoxChoices = [ u"Matrix", u"Edge List", u"Edge List with Time", u"Edge List with Type" ]
		self.demo_matrixFormatRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Format", wx.DefaultPosition, wx.DefaultSize, demo_matrixFormatRadioBoxChoices, 2, wx.RA_SPECIFY_COLS )
		self.demo_matrixFormatRadioBox.SetSelection( 1 )
		demo_radio_sizer.Add( self.demo_matrixFormatRadioBox, 0, wx.ALL, 5 )

		demo_rescaleRadioBoxChoices = [ u"Identical Grids", u"Rescale Connectivity Matrix" ]
		self.demo_rescaleRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Rescale Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, demo_rescaleRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.demo_rescaleRadioBox.SetSelection( 0 )
		demo_radio_sizer.Add( self.demo_rescaleRadioBox, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		demo_rescale_edgeRadioBoxChoices = [ u"Proportional to overlap", u"Assume homogeneous connectivity" ]
		self.demo_rescale_edgeRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Rescaling edge handling", wx.DefaultPosition, wx.DefaultSize, demo_rescale_edgeRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.demo_rescale_edgeRadioBox.SetSelection( 0 )
		demo_radio_sizer.Add( self.demo_rescale_edgeRadioBox, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


		demoMainSizer.Add( demo_radio_sizer, 1, wx.ALIGN_CENTER, 5 )

		demo_cu_cm_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		demo_cu_cm_file_sizer.AddGrowableCol( 1 )
		demo_cu_cm_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		demo_cu_cm_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.demo_CU_CM_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Connectivity Matrix:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_CU_CM_filetext.Wrap( -1 )

		self.demo_CU_CM_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		demo_cu_cm_file_sizer.Add( self.demo_CU_CM_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.demo_CU_CM_file = wx.FilePickerCtrl( self.demographic, wx.ID_ANY, u"~\\data\\grid_connectivity_matrix.csv", u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		demo_cu_cm_file_sizer.Add( self.demo_CU_CM_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )


		demoMainSizer.Add( demo_cu_cm_file_sizer, 1, wx.EXPAND, 5 )

		demo_rescale_sizer = wx.FlexGridSizer( 1, 2, 0, 0 )
		demo_rescale_sizer.AddGrowableCol( 0 )
		demo_rescale_sizer.AddGrowableCol( 1 )
		demo_rescale_sizer.SetFlexibleDirection( wx.BOTH )
		demo_rescale_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		demoMainSizer.Add( demo_rescale_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		demo_pucm_output_txt_sizer = wx.BoxSizer( wx.VERTICAL )

		self.demo_pucm_seperator = wx.StaticLine( self.demographic, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		demo_pucm_output_txt_sizer.Add( self.demo_pucm_seperator, 0, wx.EXPAND |wx.ALL, 5 )

		self.demo_PU_CM_outputtext = wx.StaticText( self.demographic, wx.ID_ANY, u"Rescaling:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_PU_CM_outputtext.Wrap( -1 )

		self.demo_PU_CM_outputtext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		self.demo_PU_CM_outputtext.Enable( False )

		demo_pucm_output_txt_sizer.Add( self.demo_PU_CM_outputtext, 0, wx.ALL, 5 )


		demoMainSizer.Add( demo_pucm_output_txt_sizer, 1, wx.EXPAND, 5 )

		demo_cu_file_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		demo_cu_file_sizer.AddGrowableCol( 1 )
		demo_cu_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		demo_cu_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.demo_CU_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Connectivity Unit Shapefile:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_CU_filetext.Wrap( -1 )

		self.demo_CU_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		self.demo_CU_filetext.Enable( False )

		demo_cu_file_sizer.Add( self.demo_CU_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.demo_CU_file = wx.FilePickerCtrl( self.demographic, wx.ID_ANY, u"~\\data\\shapefiles\\connectivity_grid.shp", u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.demo_CU_file.Enable( False )

		demo_cu_file_sizer.Add( self.demo_CU_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

		self.demo_CU_file_pu_id_txt = wx.StaticText( self.demographic, wx.ID_ANY, u"ID Column Label", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_CU_file_pu_id_txt.Wrap( -1 )

		self.demo_CU_file_pu_id_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		self.demo_CU_file_pu_id_txt.Enable( False )

		demo_cu_file_sizer.Add( self.demo_CU_file_pu_id_txt, 0, wx.ALL, 5 )

		demo_CU_file_pu_idChoices = []
		self.demo_CU_file_pu_id = wx.Choice( self.demographic, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, demo_CU_file_pu_idChoices, 0 )
		self.demo_CU_file_pu_id.SetSelection( 0 )
		self.demo_CU_file_pu_id.Enable( False )

		demo_cu_file_sizer.Add( self.demo_CU_file_pu_id, 0, wx.ALL, 5 )


		demoMainSizer.Add( demo_cu_file_sizer, 1, wx.EXPAND, 5 )

		demo_pucm_output_txt_sizer = wx.BoxSizer( wx.VERTICAL )


		demoMainSizer.Add( demo_pucm_output_txt_sizer, 1, wx.EXPAND, 5 )

		demo_pucm_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.demo_PU_CM_def = wx.StaticText( self.demographic, wx.ID_ANY, u"The Planning Unit Connectivity Matrix is the output of the rescaling process. It is scaled to the planning units and will be used to calcuate the Connectivity Metrics for the planning units.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_PU_CM_def.Wrap( -1 )

		self.demo_PU_CM_def.Enable( False )

		demo_pucm_def_sizer.Add( self.demo_PU_CM_def, 0, wx.ALL|wx.EXPAND, 5 )


		demoMainSizer.Add( demo_pucm_def_sizer, 1, wx.EXPAND, 5 )

		demo_pucm_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		demo_pucm_sizer.AddGrowableCol( 2 )
		demo_pucm_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		demo_pucm_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.demo_PU_CM_progress = wx.CheckBox( self.demographic, wx.ID_ANY, u"Progress Bar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_PU_CM_progress.SetValue(True)
		self.demo_PU_CM_progress.Enable( False )

		demo_pucm_sizer.Add( self.demo_PU_CM_progress, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.demo_PU_CM_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Output Matrix:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_PU_CM_filetext.Wrap( -1 )

		self.demo_PU_CM_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		self.demo_PU_CM_filetext.Enable( False )

		demo_pucm_sizer.Add( self.demo_PU_CM_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.demo_PU_CM_file = wx.FilePickerCtrl( self.demographic, wx.ID_ANY, u"~\\Documents\\PU_connectivity_matrix.csv", u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		self.demo_PU_CM_file.Enable( False )

		demo_pucm_sizer.Add( self.demo_PU_CM_file, 0, wx.ALL|wx.EXPAND, 5 )


		demoMainSizer.Add( demo_pucm_sizer, 1, wx.EXPAND, 5 )

		self.demo_rescale_button = wx.Button( self.demographic, wx.ID_ANY, u"Rescale Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_rescale_button.Enable( False )

		demoMainSizer.Add( self.demo_rescale_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.demographic.SetSizer( demoMainSizer )
		self.demographic.Layout()
		demoMainSizer.Fit( self.demographic )
		self.conn_category_choicebook.AddPage( self.demographic, u"Demographic Input", True )
		self.landscape = wx.Panel( self.conn_category_choicebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		landMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		landMainSizer.AddGrowableCol( 0 )
		landMainSizer.AddGrowableRow( 0 )
		landMainSizer.SetFlexibleDirection( wx.VERTICAL )
		landMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

		land_cm_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.land_CM_def = wx.StaticText( self.landscape, wx.ID_ANY, u"The connectivity matrix (or list) is the ultimate input format for landscape data, but there are multiple input types that can be used to calculate connectivity matrices. Users can:  1) load a habitat type shapefile and an optional resistance matrix, which can be used to calculate the connectivity matrix via least-cost path or Euclidean distance analysis, 2) load a resistance surface that can be used to calculate the connectivity matrix via least-cost path analysis, or  3) load a connectivity matrix directly", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_CM_def.Wrap( -1 )

		land_cm_def_sizer.Add( self.land_CM_def, 0, wx.ALL|wx.EXPAND, 5 )


		landMainSizer.Add( land_cm_def_sizer, 1, wx.EXPAND, 5 )

		self.land_type_choice = wx.Choicebook( self.landscape, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.hab_res = wx.Panel( self.land_type_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		hab_res_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		hab_res_sizer.AddGrowableCol( 0 )
		hab_res_sizer.SetFlexibleDirection( wx.BOTH )
		hab_res_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		land_radio_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		land_radio_sizer.AddGrowableCol( 1 )
		land_radio_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_radio_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		land_res_matrixTypeRadioBoxChoices = [ u"Least-Cost Path", u"Euclidean Distance" ]
		self.land_res_matrixTypeRadioBox = wx.RadioBox( self.hab_res, wx.ID_ANY, u"Distance Calculation Type", wx.DefaultPosition, wx.DefaultSize, land_res_matrixTypeRadioBoxChoices, 2, wx.RA_SPECIFY_COLS )
		self.land_res_matrixTypeRadioBox.SetSelection( 0 )
		land_radio_sizer.Add( self.land_res_matrixTypeRadioBox, 0, wx.ALL, 5 )


		hab_res_sizer.Add( land_radio_sizer, 1, wx.ALIGN_CENTER, 5 )

		land_cu_file_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		land_cu_file_sizer.AddGrowableCol( 1 )
		land_cu_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_cu_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.land_HAB_filetext = wx.StaticText( self.hab_res, wx.ID_ANY, u"Habitat Type Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_filetext.Wrap( -1 )

		self.land_HAB_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_cu_file_sizer.Add( self.land_HAB_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.land_HAB_file = wx.FilePickerCtrl( self.hab_res, wx.ID_ANY, wx.EmptyString, u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		land_cu_file_sizer.Add( self.land_HAB_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

		self.land_HAB_file_hab_id_txt = wx.StaticText( self.hab_res, wx.ID_ANY, u"Habitat ID Column Label", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_file_hab_id_txt.Wrap( -1 )

		self.land_HAB_file_hab_id_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_cu_file_sizer.Add( self.land_HAB_file_hab_id_txt, 0, wx.ALL, 5 )

		land_HAB_file_hab_idChoices = []
		self.land_HAB_file_hab_id = wx.Choice( self.hab_res, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, land_HAB_file_hab_idChoices, 0 )
		self.land_HAB_file_hab_id.SetSelection( 0 )
		self.land_HAB_file_hab_id.SetToolTip( u"The column which contains the habitat names or ID's." )

		land_cu_file_sizer.Add( self.land_HAB_file_hab_id, 0, wx.ALL, 5 )


		hab_res_sizer.Add( land_cu_file_sizer, 1, wx.EXPAND, 5 )

		land_cu_limits_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		land_cu_limits_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_cu_limits_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.land_HAB_buff_txt = wx.StaticText( self.hab_res, wx.ID_ANY, u"Habitat Neighour Buffer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_buff_txt.Wrap( -1 )

		self.land_HAB_buff_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_cu_limits_sizer.Add( self.land_HAB_buff_txt, 0, wx.ALL, 5 )

		self.land_HAB_buff = wx.TextCtrl( self.hab_res, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_buff.SetToolTip( u"Buffer distance (m) under which planning units will be considered connected neighbours in the distance calculations. All distance calculations assume travel in straight lines between the centers of neighbouring planning units." )

		land_cu_limits_sizer.Add( self.land_HAB_buff, 0, wx.ALL, 5 )

		self.land_HAB_thresh_txt = wx.StaticText( self.hab_res, wx.ID_ANY, u"Habitat Connectivity Lower Threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_thresh_txt.Wrap( -1 )

		self.land_HAB_thresh_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_cu_limits_sizer.Add( self.land_HAB_thresh_txt, 0, wx.ALL, 5 )

		self.land_HAB_thresh = wx.TextCtrl( self.hab_res, wx.ID_ANY, u"0.001", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_thresh.SetToolTip( u"Threshold under which habitat connectivity values is considered null. Ranges from 0 to 1. Without a threshold, values for in/out degrees, and betweenness centrality will be homogeneous throughout each habitat type." )

		land_cu_limits_sizer.Add( self.land_HAB_thresh, 0, wx.ALL, 5 )


		hab_res_sizer.Add( land_cu_limits_sizer, 1, wx.EXPAND, 5 )

		land_cu_cm_file_sizer = wx.FlexGridSizer( 0, 6, 0, 0 )
		land_cu_cm_file_sizer.AddGrowableCol( 1 )
		land_cu_cm_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_cu_cm_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.land_RES_mat_filetext = wx.StaticText( self.hab_res, wx.ID_ANY, u"Resistance Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_RES_mat_filetext.Wrap( -1 )

		self.land_RES_mat_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_cu_cm_file_sizer.Add( self.land_RES_mat_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.land_RES_mat_file = wx.FilePickerCtrl( self.hab_res, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		land_cu_cm_file_sizer.Add( self.land_RES_mat_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

		self.resistance_mat_customize = wx.Button( self.hab_res, wx.ID_ANY, u"Customize", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cu_cm_file_sizer.Add( self.resistance_mat_customize, 0, wx.ALL, 5 )


		hab_res_sizer.Add( land_cu_cm_file_sizer, 1, wx.EXPAND, 5 )


		self.hab_res.SetSizer( hab_res_sizer )
		self.hab_res.Layout()
		hab_res_sizer.Fit( self.hab_res )
		self.land_type_choice.AddPage( self.hab_res, u"Habitat Type + Isolation", True )
		self.res_suf = wx.Panel( self.land_type_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		land_res_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		land_res_sizer.AddGrowableCol( 0 )
		land_res_sizer.SetFlexibleDirection( wx.BOTH )
		land_res_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		land_res_txt_sizer = wx.BoxSizer( wx.VERTICAL )

		self.land_res_seperator = wx.StaticLine( self.res_suf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		land_res_txt_sizer.Add( self.land_res_seperator, 0, wx.EXPAND |wx.ALL, 5 )

		self.land_res_text = wx.StaticText( self.res_suf, wx.ID_ANY, u"Resistance Surface:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_res_text.Wrap( -1 )

		self.land_res_text.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )

		land_res_txt_sizer.Add( self.land_res_text, 0, wx.ALL, 5 )


		land_res_sizer.Add( land_res_txt_sizer, 1, wx.EXPAND, 5 )

		land_res_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.land_RES_def = wx.StaticText( self.res_suf, wx.ID_ANY, u"This feature is not yet operational, please check again in the next version.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_RES_def.Wrap( -1 )

		land_res_def_sizer.Add( self.land_RES_def, 0, wx.ALL|wx.EXPAND, 5 )


		land_res_sizer.Add( land_res_def_sizer, 1, wx.EXPAND, 5 )

		land_res_file_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		land_res_file_sizer.AddGrowableCol( 1 )
		land_res_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_res_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.land_RES_filetext = wx.StaticText( self.res_suf, wx.ID_ANY, u"Resistance Surface Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_RES_filetext.Wrap( -1 )

		self.land_RES_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )

		land_res_file_sizer.Add( self.land_RES_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.land_RES_file = wx.FilePickerCtrl( self.res_suf, wx.ID_ANY, wx.EmptyString, u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		land_res_file_sizer.Add( self.land_RES_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

		self.land_res_file_res_id_txt = wx.StaticText( self.res_suf, wx.ID_ANY, u"Resistance Column Label", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_res_file_res_id_txt.Wrap( -1 )

		self.land_res_file_res_id_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_res_file_sizer.Add( self.land_res_file_res_id_txt, 0, wx.ALL, 5 )

		land_RES_file_res_idChoices = []
		self.land_RES_file_res_id = wx.Choice( self.res_suf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, land_RES_file_res_idChoices, 0 )
		self.land_RES_file_res_id.SetSelection( 0 )
		land_res_file_sizer.Add( self.land_RES_file_res_id, 0, wx.ALL, 5 )


		land_res_sizer.Add( land_res_file_sizer, 1, wx.EXPAND, 5 )


		self.res_suf.SetSizer( land_res_sizer )
		self.res_suf.Layout()
		land_res_sizer.Fit( self.res_suf )
		self.land_type_choice.AddPage( self.res_suf, u"Resistance Surface", False )
		self.con_mat = wx.Panel( self.land_type_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.land_type_choice.AddPage( self.con_mat, u"Connectivity Edge List with Habitat", False )
		landMainSizer.Add( self.land_type_choice, 1, wx.EXPAND, 5 )

		land_pucm_output_txt_sizer = wx.BoxSizer( wx.VERTICAL )

		self.land_pucm_seperator = wx.StaticLine( self.landscape, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		land_pucm_output_txt_sizer.Add( self.land_pucm_seperator, 0, wx.EXPAND |wx.ALL, 5 )

		self.demo_PUCM_text = wx.StaticText( self.landscape, wx.ID_ANY, u"Connectivity Edge List:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_PUCM_text.Wrap( -1 )

		self.demo_PUCM_text.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		land_pucm_output_txt_sizer.Add( self.demo_PUCM_text, 0, wx.ALL, 5 )


		landMainSizer.Add( land_pucm_output_txt_sizer, 1, wx.EXPAND, 5 )

		land_pucm_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.land_PU_CM_def = wx.StaticText( self.landscape, wx.ID_ANY, u"The connectivity \"edge list with habitat\" is either the only user input for the landscape category, or the output of the least-cost path analysis. It will be used to calcuate the Connectivity Metrics for the planning units.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_PU_CM_def.Wrap( -1 )

		land_pucm_def_sizer.Add( self.land_PU_CM_def, 0, wx.ALL|wx.EXPAND, 5 )


		landMainSizer.Add( land_pucm_def_sizer, 1, wx.EXPAND, 5 )

		land_pucm_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		land_pucm_sizer.AddGrowableCol( 2 )
		land_pucm_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_pucm_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.land_PU_CM_progress = wx.CheckBox( self.landscape, wx.ID_ANY, u"Progress Bar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_PU_CM_progress.SetValue(True)
		land_pucm_sizer.Add( self.land_PU_CM_progress, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.land_PU_CM_filetext = wx.StaticText( self.landscape, wx.ID_ANY, u"Landscape Connectivity Edge List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_PU_CM_filetext.Wrap( -1 )

		self.land_PU_CM_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_pucm_sizer.Add( self.land_PU_CM_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.land_PU_CM_file = wx.FilePickerCtrl( self.landscape, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		land_pucm_sizer.Add( self.land_PU_CM_file, 0, wx.ALL|wx.EXPAND, 5 )


		landMainSizer.Add( land_pucm_sizer, 1, wx.EXPAND, 5 )

		self.land_generate_button = wx.Button( self.landscape, wx.ID_ANY, u"Generate Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		landMainSizer.Add( self.land_generate_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.landscape.SetSizer( landMainSizer )
		self.landscape.Layout()
		landMainSizer.Fit( self.landscape )
		self.conn_category_choicebook.AddPage( self.landscape, u"Landscape Input", False )
		conn_input_mainsizer.Add( self.conn_category_choicebook, 1, wx.ALL|wx.EXPAND, 5 )

		LP_txt_sizer = wx.BoxSizer( wx.VERTICAL )

		self.demo_LP_seperator = wx.StaticLine( self.connectivityInput, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		LP_txt_sizer.Add( self.demo_LP_seperator, 0, wx.EXPAND |wx.ALL, 5 )

		self.demo_LP_text = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Local Production:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_LP_text.Wrap( -1 )

		self.demo_LP_text.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		LP_txt_sizer.Add( self.demo_LP_text, 0, wx.ALL, 5 )


		conn_input_mainsizer.Add( LP_txt_sizer, 1, wx.EXPAND, 5 )

		LP_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.demo_LP_def = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Local production is the number of elements/individuals produced by each planning unit.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_LP_def.Wrap( -1 )

		LP_def_sizer.Add( self.demo_LP_def, 0, wx.ALL|wx.EXPAND, 5 )


		conn_input_mainsizer.Add( LP_def_sizer, 1, wx.EXPAND, 5 )

		LP_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		LP_sizer.AddGrowableCol( 1 )
		LP_sizer.SetFlexibleDirection( wx.BOTH )
		LP_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LP_def = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Local Production:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LP_def.Wrap( -1 )

		self.LP_def.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		LP_sizer.Add( self.LP_def, 0, wx.ALL|wx.EXPAND, 5 )

		self.LP_file = wx.FilePickerCtrl( self.connectivityInput, wx.ID_ANY, u"~\\data\\grid_connectivity_matrix.csv", u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		LP_sizer.Add( self.LP_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )


		conn_input_mainsizer.Add( LP_sizer, 1, wx.EXPAND, 5 )


		self.connectivityInput.SetSizer( conn_input_mainsizer )
		self.connectivityInput.Layout()
		conn_input_mainsizer.Fit( self.connectivityInput )
		self.auinotebook.AddPage( self.connectivityInput, u"2) Connectivity Input", False, wx.NullBitmap )
		self.connectivityMetrics = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		metricsMainSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		metricsMainSizer.AddGrowableCol( 1 )
		metricsMainSizer.AddGrowableRow( 0 )
		metricsMainSizer.SetFlexibleDirection( wx.BOTH )
		metricsMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		metric_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		metric_sizer.SetFlexibleDirection( wx.BOTH )
		metric_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.cf_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Conservation Features", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_txt.Wrap( -1 )

		self.cf_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		metric_sizer.Add( self.cf_txt, 0, wx.ALL, 5 )

		cf_sizer = wx.FlexGridSizer( 4, 3, 0, 0 )
		cf_sizer.AddGrowableCol( 0 )
		cf_sizer.AddGrowableCol( 1 )
		cf_sizer.AddGrowableCol( 2 )
		cf_sizer.SetFlexibleDirection( wx.BOTH )
		cf_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		demo_cf_sizer = wx.BoxSizer( wx.VERTICAL )

		self.demo_cf_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Demographic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_cf_txt.Wrap( -1 )

		self.demo_cf_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		demo_cf_sizer.Add( self.demo_cf_txt, 0, wx.ALL, 5 )

		self.cf_demo_in_degree = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"In Degree", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_in_degree, 0, wx.ALL, 5 )

		self.cf_demo_out_degree = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Out Degree", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_out_degree, 0, wx.ALL, 5 )

		self.cf_demo_between_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Betweenness Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_between_cent, 0, wx.ALL, 5 )

		self.cf_demo_eig_vect_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Eigenvector Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_eig_vect_cent, 0, wx.ALL, 5 )

		self.cf_demo_google = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Google PageRank", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_google, 0, wx.ALL, 5 )

		self.cf_demo_self_recruit = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Self Recruitment", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_self_recruit, 0, wx.ALL, 5 )

		self.cf_demo_local_retention = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Local Retention", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_local_retention, 0, wx.ALL, 5 )

		self.cf_demo_inflow = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"In-Flow", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_inflow, 0, wx.ALL, 5 )

		self.cf_demo_outflow = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Out-Flow", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_outflow, 0, wx.ALL, 5 )

		self.cf_demo_stochasticity = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Temporal Connectivity Covariance", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_stochasticity, 0, wx.ALL, 5 )

		self.cf_demo_fa_recipients = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Focus Area Recipients", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_fa_recipients, 0, wx.ALL, 5 )

		self.cf_demo_fa_donors = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Focus Area Donors", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_fa_donors, 0, wx.ALL, 5 )

		self.cf_demo_aa_recipients = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Avoidance Area Recipients", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_aa_recipients, 0, wx.ALL, 5 )

		self.cf_demo_aa_donors = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Avoidance Area Donors", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_cf_sizer.Add( self.cf_demo_aa_donors, 0, wx.ALL, 5 )


		cf_sizer.Add( demo_cf_sizer, 1, wx.EXPAND, 5 )

		land_cf_sizer = wx.BoxSizer( wx.VERTICAL )

		self.land_cf_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_cf_txt.Wrap( -1 )

		self.land_cf_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_cf_sizer.Add( self.land_cf_txt, 0, wx.ALL, 5 )

		self.cf_land_in_degree = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"In Degree", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_in_degree, 0, wx.ALL, 5 )

		self.cf_land_out_degree = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Out Degree", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_out_degree, 0, wx.ALL, 5 )

		self.cf_land_between_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Betweenness Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_between_cent, 0, wx.ALL, 5 )

		self.cf_land_eig_vect_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Eigenvector Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_eig_vect_cent, 0, wx.ALL, 5 )

		self.cf_land_google = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Google PageRank", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_google, 0, wx.ALL, 5 )

		self.cf_land_self_recruit = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Self Recruitment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_self_recruit.SetValue(True)
		self.cf_land_self_recruit.Hide()

		land_cf_sizer.Add( self.cf_land_self_recruit, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		self.cf_land_retention = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Local Retention", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_retention.Hide()

		land_cf_sizer.Add( self.cf_land_retention, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		self.cf_land_import = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_import.Hide()

		land_cf_sizer.Add( self.cf_land_import, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		self.cf_land_outflux = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Outflux", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_outflux.SetValue(True)
		self.cf_land_outflux.Hide()

		land_cf_sizer.Add( self.cf_land_outflux, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		self.cf_land_stochasticity = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Temporal Connectivity Covariance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_stochasticity.Hide()

		land_cf_sizer.Add( self.cf_land_stochasticity, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )

		self.cf_land_fa_recipients = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Focus Area Recipients", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_fa_recipients, 0, wx.ALL, 5 )

		self.cf_land_fa_donors = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Focus Area Donors", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_fa_donors, 0, wx.ALL, 5 )

		self.cf_land_aa_recipients = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Avoidance Area Recipients", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_aa_recipients, 0, wx.ALL, 5 )

		self.cf_land_aa_donors = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Avoidance Area Donors", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cf_sizer.Add( self.cf_land_aa_donors, 0, wx.ALL, 5 )


		cf_sizer.Add( land_cf_sizer, 1, wx.EXPAND, 5 )


		metric_sizer.Add( cf_sizer, 1, wx.EXPAND, 5 )

		self.metrics_seperator = wx.StaticLine( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		metric_sizer.Add( self.metrics_seperator, 0, wx.EXPAND |wx.ALL, 5 )

		self.bd_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Planning Unit Dependency as Boundary Definition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_txt.Wrap( -1 )

		self.bd_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		metric_sizer.Add( self.bd_txt, 0, wx.ALL, 5 )

		bd_sizer = wx.FlexGridSizer( 4, 3, 0, 0 )
		bd_sizer.AddGrowableCol( 0 )
		bd_sizer.AddGrowableCol( 1 )
		bd_sizer.AddGrowableCol( 2 )
		bd_sizer.SetFlexibleDirection( wx.BOTH )
		bd_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		demo_bd_sizer = wx.BoxSizer( wx.VERTICAL )

		self.demo_bd_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Demographic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_bd_txt.Wrap( -1 )

		self.demo_bd_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		demo_bd_sizer.Add( self.demo_bd_txt, 0, wx.ALL, 5 )

		self.bd_demo_conn_boundary = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Connectivity as spatial dependency", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_bd_sizer.Add( self.bd_demo_conn_boundary, 0, wx.ALL, 5 )

		self.bd_demo_min_plan_graph = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Minimum Planar Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_demo_min_plan_graph.Hide()

		demo_bd_sizer.Add( self.bd_demo_min_plan_graph, 0, wx.ALL, 5 )


		bd_sizer.Add( demo_bd_sizer, 1, wx.EXPAND, 5 )

		land_bd_sizer = wx.BoxSizer( wx.VERTICAL )

		self.land_bd_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_bd_txt.Wrap( -1 )

		self.land_bd_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		land_bd_sizer.Add( self.land_bd_txt, 0, wx.ALL, 5 )

		self.bd_land_conn_boundary = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Connectivity as spatial dependency", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_bd_sizer.Add( self.bd_land_conn_boundary, 0, wx.ALL, 5 )

		self.bd_land_min_plan_graph = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Minimum Planar Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_land_min_plan_graph.Hide()

		land_bd_sizer.Add( self.bd_land_min_plan_graph, 0, wx.ALL, 5 )


		bd_sizer.Add( land_bd_sizer, 1, wx.EXPAND, 5 )


		metric_sizer.Add( bd_sizer, 1, wx.EXPAND, 5 )


		metricsMainSizer.Add( metric_sizer, 1, wx.EXPAND, 5 )

		metric_help_sizer = wx.FlexGridSizer( 6, 1, 0, 0 )
		metric_help_sizer.AddGrowableCol( 0 )
		metric_help_sizer.AddGrowableRow( 1 )
		metric_help_sizer.SetFlexibleDirection( wx.BOTH )
		metric_help_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		metric_definition_choiceChoices = [ u"In Degree", u"Out Degree", u"Betweenness Centrality", u"Eigenvector Centrality", u"Google PageRank", u"Self Recruitment", u"Local Retention", u"Out-Flow", u"In-Flow", u"Temporal Connectivity Covariance", u"Focus Area Recipients", u"Focus Area Donors", u"Avoidance Area Recipients", u"Avoidance Area Donors", u"Connectivity as spatial dependency" ]
		self.metric_definition_choice = wx.Choice( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, metric_definition_choiceChoices, 0 )
		self.metric_definition_choice.SetSelection( 0 )
		metric_help_sizer.Add( self.metric_definition_choice, 0, wx.ALL|wx.EXPAND, 5 )

		self.metric_definition_html = wx.html2.WebView.New( self.connectivityMetrics)
		metric_help_sizer.Add( self.metric_definition_html, 0, wx.ALL|wx.EXPAND, 5 )


		metricsMainSizer.Add( metric_help_sizer, 1, wx.EXPAND, 5 )

		self.m_staticText118 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText118.Wrap( -1 )

		metricsMainSizer.Add( self.m_staticText118, 0, wx.ALL, 5 )

		metrics_buttons_sizer1 = wx.FlexGridSizer( 0, 6, 0, 0 )
		metrics_buttons_sizer1.AddGrowableCol( 0 )
		metrics_buttons_sizer1.SetFlexibleDirection( wx.BOTH )
		metrics_buttons_sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.spacertext1 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertext1.Wrap( -1 )

		metrics_buttons_sizer1.Add( self.spacertext1, 0, wx.ALL, 5 )

		self.calc_metrics = wx.Button( self.connectivityMetrics, wx.ID_ANY, u"Calculate Metrics", wx.DefaultPosition, wx.DefaultSize, 0 )
		metrics_buttons_sizer1.Add( self.calc_metrics, 0, wx.ALL, 5 )

		self.metrics_for_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"For:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metrics_for_txt.Wrap( -1 )

		metrics_buttons_sizer1.Add( self.metrics_for_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.calc_metrics_pu = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Planning Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.calc_metrics_pu.SetValue(True)
		metrics_buttons_sizer1.Add( self.calc_metrics_pu, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.calc_metrics_cu = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Connectivity Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.calc_metrics_cu.SetToolTip( u"Calculating Connectivity Metrics is for plotting purposes only. These metrics will not be exported or appended to the Marxan input files." )

		metrics_buttons_sizer1.Add( self.calc_metrics_cu, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		metricsMainSizer.Add( metrics_buttons_sizer1, 1, wx.EXPAND, 5 )


		self.connectivityMetrics.SetSizer( metricsMainSizer )
		self.connectivityMetrics.Layout()
		metricsMainSizer.Fit( self.connectivityMetrics )
		self.auinotebook.AddPage( self.connectivityMetrics, u"3) Connectivity Metrics", False, wx.NullBitmap )
		self.preEvaluation = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		preEvalMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		preEvalMainSizer.AddGrowableCol( 0 )
		preEvalMainSizer.AddGrowableRow( 0 )
		preEvalMainSizer.AddGrowableRow( 6 )
		preEvalMainSizer.SetFlexibleDirection( wx.BOTH )
		preEvalMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		preEval_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.preEval_def_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"This tab will allow you to evaluate the metrics created on the previous tab and discretize the metrics to create connectivity-based conservation features by choosing a minimum and maximum threshold. These thresholds can be chosen from the quartiles, a percentile, or a custom numeric value. These discrete features can optionally be locked in or out when they are created. Selected metrics or discrete features can be removed if they are not appropriate for the Marxan analysis.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_def_txt.Wrap( -1 )

		preEval_def_sizer.Add( self.preEval_def_txt, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )


		preEvalMainSizer.Add( preEval_def_sizer, 1, wx.EXPAND, 5 )

		preEval_choice_sizer = wx.BoxSizer( wx.VERTICAL )

		self.preEval_choice_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Choose Available Connectivity Metric to Discretize:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_choice_txt.Wrap( -1 )

		self.preEval_choice_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		preEval_choice_sizer.Add( self.preEval_choice_txt, 0, wx.ALL, 5 )

		fgSizer68 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer68.AddGrowableCol( 0 )
		fgSizer68.SetFlexibleDirection( wx.BOTH )
		fgSizer68.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		preEval_metrics_opt_sizer = wx.FlexGridSizer( 2, 2, 0, 0 )
		preEval_metrics_opt_sizer.AddGrowableCol( 1 )
		preEval_metrics_opt_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_metrics_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_metric_shp_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_metric_shp_txt.Wrap( -1 )

		preEval_metrics_opt_sizer.Add( self.preEval_metric_shp_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

		self.preEval_metric_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_metric_txt.Wrap( -1 )

		preEval_metrics_opt_sizer.Add( self.preEval_metric_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

		preEval_metric_shp_choiceChoices = [ u"Planning Units (Demographic Data)", u"Planning Units (Landscape Data)" ]
		self.preEval_metric_shp_choice = wx.Choice( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, preEval_metric_shp_choiceChoices, 0 )
		self.preEval_metric_shp_choice.SetSelection( 0 )
		preEval_metrics_opt_sizer.Add( self.preEval_metric_shp_choice, 0, wx.ALL, 5 )

		preEval_metric_choiceChoices = [ u"Selection Frequency", u"Best Solution", u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment", u"Outflux", u"Temporal Connectivity Covariance", u"Focus Area Sink", u"Focus Area Source", u"Avoidance Area Sink", u"Avoidance Area Source" ]
		self.preEval_metric_choice = wx.Choice( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, preEval_metric_choiceChoices, 0 )
		self.preEval_metric_choice.SetSelection( 0 )
		preEval_metrics_opt_sizer.Add( self.preEval_metric_choice, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer68.Add( preEval_metrics_opt_sizer, 1, wx.EXPAND, 5 )

		bSizer56 = wx.BoxSizer( wx.HORIZONTAL )

		self.plot_freq_metric = wx.Button( self.preEvaluation, wx.ID_ANY, u"Plot Frequency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.plot_freq_metric.SetToolTip( u"Plot frequency histogram for selected metric" )

		bSizer56.Add( self.plot_freq_metric, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.remove_metric = wx.Button( self.preEvaluation, wx.ID_ANY, u"Remove Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.remove_metric, 0, wx.ALIGN_BOTTOM|wx.ALL, 4 )

		preEval_status_radioChoices = [ u"Locked in", u"Locked out", u"Status-quo" ]
		self.preEval_status_radio = wx.RadioBox( self.preEvaluation, wx.ID_ANY, u"New Metric Status", wx.DefaultPosition, wx.DefaultSize, preEval_status_radioChoices, 3, wx.RA_SPECIFY_COLS )
		self.preEval_status_radio.SetSelection( 2 )
		self.preEval_status_radio.SetToolTip( u"For the planning units which contain the discrete metric (to be created), you can choose to overwrite the status of the original planning unit (i.e. pu.dat) to lock the planning units in out. Alternatively, select 'Status-quo' to keep the status of the original planning unit (i.e. pu.dat)." )

		bSizer56.Add( self.preEval_status_radio, 0, 0, 5 )


		fgSizer68.Add( bSizer56, 1, wx.EXPAND, 5 )


		preEval_choice_sizer.Add( fgSizer68, 1, wx.EXPAND, 5 )


		preEvalMainSizer.Add( preEval_choice_sizer, 1, wx.EXPAND, 5 )

		preEval_table_discrete_sizer = wx.FlexGridSizer( 1, 5, 0, 0 )
		preEval_table_discrete_sizer.AddGrowableCol( 2 )
		preEval_table_discrete_sizer.AddGrowableCol( 4 )
		preEval_table_discrete_sizer.AddGrowableRow( 0 )
		preEval_table_discrete_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_table_discrete_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		preEval_table_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		preEval_table_sizer.AddGrowableCol( 0 )
		preEval_table_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_table_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_table_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Selected Metric Summary", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_table_txt.Wrap( -1 )

		self.preEval_table_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		preEval_table_sizer.Add( self.preEval_table_txt, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.preEval_grid = wx.grid.Grid( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.preEval_grid.CreateGrid( 10, 1 )
		self.preEval_grid.EnableEditing( False )
		self.preEval_grid.EnableGridLines( True )
		self.preEval_grid.EnableDragGridSize( False )
		self.preEval_grid.SetMargins( 0, 0 )

		# Columns
		self.preEval_grid.SetColSize( 0, 150 )
		self.preEval_grid.EnableDragColMove( False )
		self.preEval_grid.EnableDragColSize( True )
		self.preEval_grid.SetColLabelSize( 30 )
		self.preEval_grid.SetColLabelValue( 0, u"Value" )
		self.preEval_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.preEval_grid.EnableDragRowSize( True )
		self.preEval_grid.SetRowLabelSize( 150 )
		self.preEval_grid.SetRowLabelValue( 0, u"Sum" )
		self.preEval_grid.SetRowLabelValue( 1, u"Mean" )
		self.preEval_grid.SetRowLabelValue( 2, u"Standard Deviation" )
		self.preEval_grid.SetRowLabelValue( 3, u"Minimum" )
		self.preEval_grid.SetRowLabelValue( 4, u"Lower Quartile" )
		self.preEval_grid.SetRowLabelValue( 5, u"Median" )
		self.preEval_grid.SetRowLabelValue( 6, u"Upper Quartile" )
		self.preEval_grid.SetRowLabelValue( 7, u"Maximum" )
		self.preEval_grid.SetRowLabelValue( 8, u"% in Avoidance Area" )
		self.preEval_grid.SetRowLabelValue( 9, u"% in Focus Area" )
		self.preEval_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.preEval_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		preEval_table_sizer.Add( self.preEval_grid, 0, wx.ALL, 5 )


		preEval_table_discrete_sizer.Add( preEval_table_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline12 = wx.StaticLine( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		preEval_table_discrete_sizer.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

		preEval_discrete_from_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		preEval_discrete_from_sizer.AddGrowableCol( 0 )
		preEval_discrete_from_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_from_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_discrete_from_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Make discrete feature from minimum threshold:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_discrete_from_txt.Wrap( -1 )

		self.preEval_discrete_from_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		preEval_discrete_from_sizer.Add( self.preEval_discrete_from_txt, 0, 0, 5 )

		preEval_discrete_from_quartile_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		preEval_discrete_from_quartile_sizer.AddGrowableCol( 1 )
		preEval_discrete_from_quartile_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_from_quartile_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_discrete_from_quartile = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Quartile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_discrete_from_quartile.SetValue(True)
		preEval_discrete_from_quartile_sizer.Add( self.preEval_discrete_from_quartile, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		preEval_discrete_from_quartile_radioChoices = [ u"Minimum", u"Lower Quartile", u"Median", u"Upper Quartile", u"Maximum" ]
		self.preEval_discrete_from_quartile_radio = wx.RadioBox( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, preEval_discrete_from_quartile_radioChoices, 1, wx.RA_SPECIFY_COLS )
		self.preEval_discrete_from_quartile_radio.SetSelection( 2 )
		preEval_discrete_from_quartile_sizer.Add( self.preEval_discrete_from_quartile_radio, 0, wx.ALL, 5 )


		preEval_discrete_from_sizer.Add( preEval_discrete_from_quartile_sizer, 1, wx.EXPAND, 5 )

		preEval_discrete_from_percentile_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		preEval_discrete_from_percentile_sizer.AddGrowableCol( 1 )
		preEval_discrete_from_percentile_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_from_percentile_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_discrete_from_percentile = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Percentile", wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_discrete_from_percentile_sizer.Add( self.preEval_discrete_from_percentile, 0, wx.ALL, 5 )

		self.preEval_discrete_from_percentile_slider = wx.Slider( self.preEvaluation, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		preEval_discrete_from_percentile_sizer.Add( self.preEval_discrete_from_percentile_slider, 0, wx.EXPAND|wx.RIGHT, 30 )


		preEval_discrete_from_sizer.Add( preEval_discrete_from_percentile_sizer, 1, wx.EXPAND, 5 )

		preEval_discrete_from_value_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		preEval_discrete_from_value_sizer.AddGrowableCol( 1 )
		preEval_discrete_from_value_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_from_value_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_discrete_from_value = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_discrete_from_value_sizer.Add( self.preEval_discrete_from_value, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.preEval_discrete_from_value_txtctrl = wx.TextCtrl( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_discrete_from_value_sizer.Add( self.preEval_discrete_from_value_txtctrl, 0, wx.ALL, 5 )


		preEval_discrete_from_sizer.Add( preEval_discrete_from_value_sizer, 1, wx.EXPAND, 5 )


		preEval_table_discrete_sizer.Add( preEval_discrete_from_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline13 = wx.StaticLine( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		preEval_table_discrete_sizer.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		preEval_discrete_to_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		preEval_discrete_to_sizer.AddGrowableCol( 0 )
		preEval_discrete_to_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_to_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_discrete_to_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Make discrete feature to maximum threshold:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_discrete_to_txt.Wrap( -1 )

		self.preEval_discrete_to_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		preEval_discrete_to_sizer.Add( self.preEval_discrete_to_txt, 0, 0, 5 )

		preEval_discrete_to_quartile_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		preEval_discrete_to_quartile_sizer.AddGrowableCol( 1 )
		preEval_discrete_to_quartile_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_to_quartile_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_discrete_to_quartile = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Quartile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_discrete_to_quartile.SetValue(True)
		preEval_discrete_to_quartile_sizer.Add( self.preEval_discrete_to_quartile, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		preEval_discrete_to_quartile_radioChoices = [ u"Minimum", u"Lower Quartile", u"Median", u"Upper Quartile", u"Maximum" ]
		self.preEval_discrete_to_quartile_radio = wx.RadioBox( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, preEval_discrete_to_quartile_radioChoices, 1, wx.RA_SPECIFY_COLS )
		self.preEval_discrete_to_quartile_radio.SetSelection( 4 )
		preEval_discrete_to_quartile_sizer.Add( self.preEval_discrete_to_quartile_radio, 0, wx.ALL, 5 )


		preEval_discrete_to_sizer.Add( preEval_discrete_to_quartile_sizer, 1, wx.EXPAND, 5 )

		preEval_discrete_to_percentile_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		preEval_discrete_to_percentile_sizer.AddGrowableCol( 1 )
		preEval_discrete_to_percentile_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_to_percentile_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_discrete_to_percentile = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Percentile", wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_discrete_to_percentile_sizer.Add( self.preEval_discrete_to_percentile, 0, wx.ALL, 5 )

		self.preEval_discrete_to_percentile_slider = wx.Slider( self.preEvaluation, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		preEval_discrete_to_percentile_sizer.Add( self.preEval_discrete_to_percentile_slider, 0, wx.EXPAND|wx.RIGHT, 30 )


		preEval_discrete_to_sizer.Add( preEval_discrete_to_percentile_sizer, 1, wx.EXPAND, 5 )

		preEval_discrete_to_value_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		preEval_discrete_to_value_sizer.AddGrowableCol( 1 )
		preEval_discrete_to_value_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_to_value_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.preEval_discrete_to_value = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_discrete_to_value_sizer.Add( self.preEval_discrete_to_value, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.preEval_discrete_to_value_txtctrl = wx.TextCtrl( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_discrete_to_value_sizer.Add( self.preEval_discrete_to_value_txtctrl, 0, wx.ALL, 5 )


		preEval_discrete_to_sizer.Add( preEval_discrete_to_value_sizer, 1, wx.EXPAND, 5 )


		preEval_table_discrete_sizer.Add( preEval_discrete_to_sizer, 1, wx.EXPAND, 5 )


		preEvalMainSizer.Add( preEval_table_discrete_sizer, 1, wx.EXPAND, 5 )

		self.preEval_create_new = wx.Button( self.preEvaluation, wx.ID_ANY, u"Create New Feature", wx.DefaultPosition, wx.DefaultSize, 0 )
		preEvalMainSizer.Add( self.preEval_create_new, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticline8 = wx.StaticLine( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		preEvalMainSizer.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		self.preEval_choice_txt2 = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Connectivity-Based Conservation Feature Available for Export:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_choice_txt2.Wrap( -1 )

		self.preEval_choice_txt2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		preEvalMainSizer.Add( self.preEval_choice_txt2, 0, wx.ALL, 5 )

		self.discrete_grid = wx.grid.Grid( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.discrete_grid.CreateGrid( 0, 2 )
		self.discrete_grid.EnableEditing( True )
		self.discrete_grid.EnableGridLines( True )
		self.discrete_grid.EnableDragGridSize( False )
		self.discrete_grid.SetMargins( 0, 0 )

		# Columns
		self.discrete_grid.SetColSize( 0, 600 )
		self.discrete_grid.SetColSize( 1, 50 )
		self.discrete_grid.EnableDragColMove( False )
		self.discrete_grid.EnableDragColSize( True )
		self.discrete_grid.SetColLabelSize( 30 )
		self.discrete_grid.SetColLabelValue( 0, u"New Conservation Feature" )
		self.discrete_grid.SetColLabelValue( 1, u"Status" )
		self.discrete_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.discrete_grid.EnableDragRowSize( True )
		self.discrete_grid.SetRowLabelSize( 80 )
		self.discrete_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.discrete_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		preEvalMainSizer.Add( self.discrete_grid, 0, wx.ALL, 5 )


		self.preEvaluation.SetSizer( preEvalMainSizer )
		self.preEvaluation.Layout()
		preEvalMainSizer.Fit( self.preEvaluation )
		self.auinotebook.AddPage( self.preEvaluation, u"4) Pre-Evaluation", False, wx.NullBitmap )
		self.exportMarxan = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		exportMarxanMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		exportMarxanMainSizer.AddGrowableCol( 0 )
		exportMarxanMainSizer.AddGrowableRow( 0 )
		exportMarxanMainSizer.AddGrowableRow( 3 )
		exportMarxanMainSizer.AddGrowableRow( 6 )
		exportMarxanMainSizer.AddGrowableRow( 9 )
		exportMarxanMainSizer.SetFlexibleDirection( wx.BOTH )
		exportMarxanMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		exportMarxan_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.exportMarxan_def_txt = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"This tab will allow you to export the discrete connectivity metrics, the spatial dependencies, and the planning unit status to Marxan formatted files. \"Original\" files refer to pre-existing Marxan files that do not include connectivity while \"New\" files are the ones that will be written upon export. All \"Original\" files are optional, but including them here allows you to append connectivity conservation features to an existing analysis.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exportMarxan_def_txt.Wrap( -1 )

		exportMarxan_def_sizer.Add( self.exportMarxan_def_txt, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )


		exportMarxanMainSizer.Add( exportMarxan_def_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline82 = wx.StaticLine( self.exportMarxan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		exportMarxanMainSizer.Add( self.m_staticline82, 0, wx.EXPAND |wx.ALL, 5 )

		self.preEval_choice_txt1 = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"Planning Unit versus Conservation Feature (puvspr.dat) and Conservation Feature (spec.dat) Files:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_choice_txt1.Wrap( -1 )

		self.preEval_choice_txt1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		exportMarxanMainSizer.Add( self.preEval_choice_txt1, 0, wx.ALL, 5 )

		cf_export_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		cf_export_sizer.AddGrowableCol( 1 )
		cf_export_sizer.SetFlexibleDirection( wx.BOTH )
		cf_export_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer79 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer79.SetFlexibleDirection( wx.BOTH )
		fgSizer79.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		cf_export_radioBoxChoices = [ u"Append", u"Export", u"Ignore" ]
		self.cf_export_radioBox = wx.RadioBox( self.exportMarxan, wx.ID_ANY, u"Metrics", wx.DefaultPosition, wx.DefaultSize, cf_export_radioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.cf_export_radioBox.SetSelection( 0 )
		self.cf_export_radioBox.SetToolTip( u"To add the new connectivity-based conservation features to existing Marxan files, select \"Append\". To export only the new connectivity-based conservation features  to new Marxan files, select \"Export\". Otherwise select \"ignore\" to avoid exporting connectivity-based conservation features ." )

		fgSizer79.Add( self.cf_export_radioBox, 0, wx.ALL, 5 )

		spec_radioChoices = [ u"Proportion", u"Target" ]
		self.spec_radio = wx.RadioBox( self.exportMarxan, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, spec_radioChoices, 1, wx.RA_SPECIFY_COLS )
		self.spec_radio.SetSelection( 0 )
		self.spec_radio.SetToolTip( u"Do you want to set targets or proportions in your conservation feature file (i.e. spec.dat)?" )

		fgSizer79.Add( self.spec_radio, 0, wx.ALL, 5 )


		cf_export_sizer.Add( fgSizer79, 1, wx.EXPAND, 5 )

		cf_file_export_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		cf_file_export_sizer.AddGrowableCol( 1 )
		cf_file_export_sizer.SetFlexibleDirection( wx.BOTH )
		cf_file_export_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.cf_export_txt = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"Original Planning Unit versus Conservation Feature File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_export_txt.Wrap( -1 )

		cf_file_export_sizer.Add( self.cf_export_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.orig_CF_file = wx.FilePickerCtrl( self.exportMarxan, wx.ID_ANY, u"~\\puvspr.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		cf_file_export_sizer.Add( self.orig_CF_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.cf_export_txt1 = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"New Planning Unit versus Conservation Feature File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_export_txt1.Wrap( -1 )

		cf_file_export_sizer.Add( self.cf_export_txt1, 0, wx.ALL, 5 )

		self.CF_file = wx.FilePickerCtrl( self.exportMarxan, wx.ID_ANY, u"~\\puvspr_connect.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		cf_file_export_sizer.Add( self.CF_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.SPEC_filetxt = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"Original Conservation Feature File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SPEC_filetxt.Wrap( -1 )

		cf_file_export_sizer.Add( self.SPEC_filetxt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.orig_SPEC_file = wx.FilePickerCtrl( self.exportMarxan, wx.ID_ANY, u"~\\spec.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		cf_file_export_sizer.Add( self.orig_SPEC_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.SPEC_filetxt1 = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"New Conservation Feature File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SPEC_filetxt1.Wrap( -1 )

		cf_file_export_sizer.Add( self.SPEC_filetxt1, 0, wx.ALL, 5 )

		self.SPEC_file = wx.FilePickerCtrl( self.exportMarxan, wx.ID_ANY, u"~\\spec_connect.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		cf_file_export_sizer.Add( self.SPEC_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.custom_spec_panel = wx.Panel( self.exportMarxan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.custom_spec_panel.SetToolTip( u"To enable, please calculate  any Conservation Feature metrics" )

		custom_spec_panel_sizer = wx.FlexGridSizer( 1, 1, 0, 0 )
		custom_spec_panel_sizer.SetFlexibleDirection( wx.BOTH )
		custom_spec_panel_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.customize_spec = wx.Button( self.custom_spec_panel, wx.ID_ANY, u"Customize Conservation Feature File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.customize_spec.Enable( False )

		custom_spec_panel_sizer.Add( self.customize_spec, 0, wx.ALL, 5 )


		self.custom_spec_panel.SetSizer( custom_spec_panel_sizer )
		self.custom_spec_panel.Layout()
		custom_spec_panel_sizer.Fit( self.custom_spec_panel )
		cf_file_export_sizer.Add( self.custom_spec_panel, 1, 0, 5 )

		target_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		target_sizer.AddGrowableCol( 1 )
		target_sizer.SetFlexibleDirection( wx.BOTH )
		target_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.targets_txt = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"Proportions", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.targets_txt.Wrap( -1 )

		target_sizer.Add( self.targets_txt, 0, wx.ALL, 5 )

		self.targets = wx.TextCtrl( self.exportMarxan, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.targets.SetToolTip( u"Target(s) or Proportion(s) for each connectivity based conservation feature. Either a single default value for all features, or a comma seperated string of values of the same length as there are conservation features." )

		target_sizer.Add( self.targets, 0, wx.ALL|wx.EXPAND, 5 )

		self.export_CF_files = wx.Button( self.exportMarxan, wx.ID_ANY, u"Export Both Conservation Feature Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.export_CF_files.Enable( False )

		target_sizer.Add( self.export_CF_files, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		cf_file_export_sizer.Add( target_sizer, 1, wx.EXPAND, 5 )


		cf_export_sizer.Add( cf_file_export_sizer, 1, wx.EXPAND, 5 )


		exportMarxanMainSizer.Add( cf_export_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline811 = wx.StaticLine( self.exportMarxan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		exportMarxanMainSizer.Add( self.m_staticline811, 0, wx.EXPAND |wx.ALL, 5 )

		self.preEval_choice_txt11 = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"Spatial Dependencies (boundary.dat) File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_choice_txt11.Wrap( -1 )

		self.preEval_choice_txt11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		exportMarxanMainSizer.Add( self.preEval_choice_txt11, 0, wx.ALL, 5 )

		bd_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		bd_file_sizer.AddGrowableCol( 1 )
		bd_file_sizer.SetFlexibleDirection( wx.BOTH )
		bd_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText142 = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"Original Spatial Dependencies File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText142.Wrap( -1 )

		bd_file_sizer.Add( self.m_staticText142, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.orig_BD_file = wx.FilePickerCtrl( self.exportMarxan, wx.ID_ANY, u"~\\bound.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		bd_file_sizer.Add( self.orig_BD_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.BD_filecheck = wx.CheckBox( self.exportMarxan, wx.ID_ANY, u"Export New Spatial Dependencies to: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BD_filecheck.SetValue(True)
		bd_file_sizer.Add( self.BD_filecheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		BD_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		BD_sizer.AddGrowableCol( 0 )
		BD_sizer.SetFlexibleDirection( wx.BOTH )
		BD_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.BD_file = wx.FilePickerCtrl( self.exportMarxan, wx.ID_ANY, u"~\\bound_connect.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		BD_sizer.Add( self.BD_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.export_BD_file = wx.Button( self.exportMarxan, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.export_BD_file.Enable( False )

		BD_sizer.Add( self.export_BD_file, 0, wx.ALL, 5 )


		bd_file_sizer.Add( BD_sizer, 1, wx.EXPAND, 5 )


		exportMarxanMainSizer.Add( bd_file_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline8111 = wx.StaticLine( self.exportMarxan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		exportMarxanMainSizer.Add( self.m_staticline8111, 0, wx.EXPAND |wx.ALL, 5 )

		self.preEval_choice_txt111 = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"Planning Unit (pu.dat) File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_choice_txt111.Wrap( -1 )

		self.preEval_choice_txt111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		exportMarxanMainSizer.Add( self.preEval_choice_txt111, 0, wx.ALL, 5 )

		pudat_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		pudat_file_sizer.AddGrowableCol( 1 )
		pudat_file_sizer.SetFlexibleDirection( wx.BOTH )
		pudat_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.orig_PUDAT_file_txt = wx.StaticText( self.exportMarxan, wx.ID_ANY, u"Original Planning Unit File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.orig_PUDAT_file_txt.Wrap( -1 )

		pudat_file_sizer.Add( self.orig_PUDAT_file_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.orig_PUDAT_file = wx.FilePickerCtrl( self.exportMarxan, wx.ID_ANY, u"~\\pu.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		pudat_file_sizer.Add( self.orig_PUDAT_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.PUDAT_filecheck = wx.CheckBox( self.exportMarxan, wx.ID_ANY, u"Export New Planning Unit File to: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUDAT_filecheck.SetValue(True)
		pudat_file_sizer.Add( self.PUDAT_filecheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		PUDAT_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		PUDAT_sizer.AddGrowableCol( 0 )
		PUDAT_sizer.SetFlexibleDirection( wx.BOTH )
		PUDAT_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.PUDAT_file = wx.FilePickerCtrl( self.exportMarxan, wx.ID_ANY, u"~\\pu_connect.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		PUDAT_sizer.Add( self.PUDAT_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.export_pudat = wx.Button( self.exportMarxan, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.export_pudat.Enable( False )

		PUDAT_sizer.Add( self.export_pudat, 0, wx.ALL, 5 )


		pudat_file_sizer.Add( PUDAT_sizer, 1, wx.EXPAND, 5 )


		exportMarxanMainSizer.Add( pudat_file_sizer, 1, wx.EXPAND, 5 )

		self.m_staticline16 = wx.StaticLine( self.exportMarxan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		exportMarxanMainSizer.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )

		self.export_metrics = wx.Button( self.exportMarxan, wx.ID_ANY, u"Export All Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.export_metrics.Enable( False )

		exportMarxanMainSizer.Add( self.export_metrics, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.exportMarxan.SetSizer( exportMarxanMainSizer )
		self.exportMarxan.Layout()
		exportMarxanMainSizer.Fit( self.exportMarxan )
		self.auinotebook.AddPage( self.exportMarxan, u"5) Marxan Files", False, wx.NullBitmap )
		self.marxanAnalysis = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		marxanMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		marxanMainSizer.AddGrowableCol( 0 )
		marxanMainSizer.AddGrowableRow( 0 )
		marxanMainSizer.AddGrowableRow( 1 )
		marxanMainSizer.AddGrowableRow( 2 )
		marxanMainSizer.AddGrowableRow( 3 )
		marxanMainSizer.AddGrowableRow( 4 )
		marxanMainSizer.SetFlexibleDirection( wx.VERTICAL )
		marxanMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

		marxan_logotxt_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		marxan_logotxt_sizer.SetFlexibleDirection( wx.BOTH )
		marxan_logotxt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.marxan_logo_bitmap = wx.StaticBitmap( self.marxanAnalysis, wx.ID_ANY, wx.Bitmap( u"docs/images/marxanlogo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		marxan_logotxt_sizer.Add( self.marxan_logo_bitmap, 0, wx.ALL, 5 )

		marxan_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.marxan_def = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"This tab allows you to choose Marxan input files (i.e. with or without connectivity) generated on the previous tab. After creating the input file (input.dat), you can run Marxan from here or you can run it manually.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.marxan_def.Wrap( -1 )

		marxan_def_sizer.Add( self.marxan_def, 0, wx.ALL|wx.EXPAND, 5 )


		marxan_logotxt_sizer.Add( marxan_def_sizer, 1, wx.EXPAND, 5 )


		marxanMainSizer.Add( marxan_logotxt_sizer, 1, wx.EXPAND, 5 )

		inputdat_file_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		inputdat_file_sizer.AddGrowableCol( 1 )
		inputdat_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		inputdat_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputdat_filetext = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Template Marxan Input File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputdat_filetext.Wrap( -1 )

		self.inputdat_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		inputdat_file_sizer.Add( self.inputdat_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.inputdat_template_file = wx.FilePickerCtrl( self.marxanAnalysis, wx.ID_ANY, u"C:\\Users\\daigl\\Documents\\GitHub\\MarxanConnect\\Marxan243\\input_template.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		inputdat_file_sizer.Add( self.inputdat_template_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

		self.default_input_template = wx.Button( self.marxanAnalysis, wx.ID_ANY, u"Reset to Default", wx.DefaultPosition, wx.DefaultSize, 0 )
		inputdat_file_sizer.Add( self.default_input_template, 0, wx.ALL, 5 )


		marxanMainSizer.Add( inputdat_file_sizer, 1, wx.EXPAND, 5 )

		marxan_misc = wx.FlexGridSizer( 2, 0, 0, 0 )
		marxan_misc.SetFlexibleDirection( wx.BOTH )
		marxan_misc.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.NUMREPS_txt = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Repeat Runs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NUMREPS_txt.Wrap( -1 )

		self.NUMREPS_txt.SetToolTip( u"The number of repeated runs, also known as \"NUMREPS\"." )

		marxan_misc.Add( self.NUMREPS_txt, 0, wx.ALL, 5 )

		self.SCENNAME_txt = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Scenario Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SCENNAME_txt.Wrap( -1 )

		self.SCENNAME_txt.SetToolTip( u"The scenario name which gets included in the output filenames, also known as \"SCENNAME\"." )

		marxan_misc.Add( self.SCENNAME_txt, 0, wx.ALL, 5 )

		self.NUMREPS = wx.TextCtrl( self.marxanAnalysis, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
		marxan_misc.Add( self.NUMREPS, 0, wx.ALL|wx.EXPAND, 5 )

		self.SCENNAME = wx.TextCtrl( self.marxanAnalysis, wx.ID_ANY, u"connect", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		marxan_misc.Add( self.SCENNAME, 0, wx.ALL, 5 )


		marxanMainSizer.Add( marxan_misc, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		marxan_input_Radio_Sizer = wx.FlexGridSizer( 1, 5, 0, 0 )
		marxan_input_Radio_Sizer.SetFlexibleDirection( wx.HORIZONTAL )
		marxan_input_Radio_Sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		marxan_CFChoices = [ u"Original", u"New" ]
		self.marxan_CF = wx.RadioBox( self.marxanAnalysis, wx.ID_ANY, u"Conservation Features", wx.DefaultPosition, wx.DefaultSize, marxan_CFChoices, 2, wx.RA_SPECIFY_COLS )
		self.marxan_CF.SetSelection( 1 )
		self.marxan_CF.SetToolTip( u"Use the the 'Original' (probably without connectivity) or 'New' (probably with connectivity) files for conservation features (e.g. spec.dat and puvspr.dat)?" )

		marxan_input_Radio_Sizer.Add( self.marxan_CF, 0, wx.ALL|wx.EXPAND, 5 )

		marxan_boundChoices = [ u"Original", u"New", u"None" ]
		self.marxan_bound = wx.RadioBox( self.marxanAnalysis, wx.ID_ANY, u"Spatial Dependencies", wx.DefaultPosition, wx.DefaultSize, marxan_boundChoices, 3, wx.RA_SPECIFY_COLS )
		self.marxan_bound.SetSelection( 1 )
		self.marxan_bound.SetToolTip( u"Use the the 'Original' (probably without connectivity) or 'New' (probably with connectivity) files for spatial dependencies (e.g. bound.dat)? Or none at all." )

		marxan_input_Radio_Sizer.Add( self.marxan_bound, 0, wx.ALL, 5 )

		inputdat_symmRadioChoices = [ u"Asymmetric", u"Symmetric" ]
		self.inputdat_symmRadio = wx.RadioBox( self.marxanAnalysis, wx.ID_ANY, u"Spatial Dependencies Type", wx.DefaultPosition, wx.DefaultSize, inputdat_symmRadioChoices, 2, wx.RA_SPECIFY_COLS )
		self.inputdat_symmRadio.SetSelection( 1 )
		marxan_input_Radio_Sizer.Add( self.inputdat_symmRadio, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.csm_txt = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Connectivity Strength Modifier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.csm_txt.Wrap( -1 )

		self.csm_txt.SetToolTip( u"The Connectivity Strength Modifier is also known as the Boundary Length Modifier." )

		bSizer44.Add( self.csm_txt, 0, wx.ALL, 5 )

		self.CSM = wx.TextCtrl( self.marxanAnalysis, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.CSM, 0, wx.ALL|wx.EXPAND, 5 )


		marxan_input_Radio_Sizer.Add( bSizer44, 1, wx.EXPAND, 5 )

		marxan_PUChoices = [ u"Original", u"New" ]
		self.marxan_PU = wx.RadioBox( self.marxanAnalysis, wx.ID_ANY, u"Planning Units", wx.DefaultPosition, wx.DefaultSize, marxan_PUChoices, 2, wx.RA_SPECIFY_COLS )
		self.marxan_PU.SetSelection( 1 )
		self.marxan_PU.SetToolTip( u"Use the the 'Original' (probably without connectivity) or 'New' (probably with connectivity) files for planning units (e.g. pu.dat)?" )

		marxan_input_Radio_Sizer.Add( self.marxan_PU, 0, wx.ALL, 5 )


		marxanMainSizer.Add( marxan_input_Radio_Sizer, 1, wx.ALIGN_CENTER, 5 )

		marxan_Radio_sizer = wx.FlexGridSizer( 1, 2, 0, 0 )
		marxan_Radio_sizer.AddGrowableCol( 0 )
		marxan_Radio_sizer.AddGrowableCol( 1 )
		marxan_Radio_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		marxan_Radio_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		marxan_RadioChoices = [ u"Marxan", u"Marxan with Zones" ]
		self.marxan_Radio = wx.RadioBox( self.marxanAnalysis, wx.ID_ANY, u"Marxan Version", wx.DefaultPosition, wx.DefaultSize, marxan_RadioChoices, 2, wx.RA_SPECIFY_COLS )
		self.marxan_Radio.SetSelection( 1 )
		marxan_Radio_sizer.Add( self.marxan_Radio, 0, wx.ALL|wx.EXPAND, 5 )

		marxanBit_RadioChoices = [ u"32-bit", u"64-bit" ]
		self.marxanBit_Radio = wx.RadioBox( self.marxanAnalysis, wx.ID_ANY, u"Bit Version", wx.DefaultPosition, wx.DefaultSize, marxanBit_RadioChoices, 2, wx.RA_SPECIFY_COLS )
		self.marxanBit_Radio.SetSelection( 1 )
		self.marxanBit_Radio.SetToolTip( u"Processing speed is typically higher with the 64-bit version of Marxan, but this is only compatible with 64-bit computers. Asymmetric linkage definitions may not be compatible with 32-bit Marxan." )

		marxan_Radio_sizer.Add( self.marxanBit_Radio, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )


		marxanMainSizer.Add( marxan_Radio_sizer, 1, wx.ALIGN_CENTER, 5 )

		self.generate_inputdat = wx.Button( self.marxanAnalysis, wx.ID_ANY, u"Generate New Input File From Template", wx.DefaultPosition, wx.DefaultSize, 0 )
		marxanMainSizer.Add( self.generate_inputdat, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticline11 = wx.StaticLine( self.marxanAnalysis, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		marxanMainSizer.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		inputdat_file_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		inputdat_file_sizer.AddGrowableCol( 1 )
		inputdat_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		inputdat_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputdat_filetext = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Marxan Input File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputdat_filetext.Wrap( -1 )

		self.inputdat_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		inputdat_file_sizer.Add( self.inputdat_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.inputdat_file = wx.FilePickerCtrl( self.marxanAnalysis, wx.ID_ANY, u"C:\\Users\\Remi-Work\\Desktop\\MarxanConnectGUI\\data\\GBR\\input.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		inputdat_file_sizer.Add( self.inputdat_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

		self.customize_inpudat = wx.Button( self.marxanAnalysis, wx.ID_ANY, u"Customize", wx.DefaultPosition, wx.DefaultSize, 0 )
		inputdat_file_sizer.Add( self.customize_inpudat, 0, wx.ALL, 5 )


		marxanMainSizer.Add( inputdat_file_sizer, 1, wx.EXPAND, 5 )

		run_marxan_sizer = wx.FlexGridSizer( 1, 4, 0, 0 )
		run_marxan_sizer.AddGrowableCol( 0 )
		run_marxan_sizer.SetFlexibleDirection( wx.BOTH )
		run_marxan_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.spacertextrunmarxan = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertextrunmarxan.Wrap( -1 )

		run_marxan_sizer.Add( self.spacertextrunmarxan, 0, wx.ALL, 5 )

		self.run_marxan_button = wx.Button( self.marxanAnalysis, wx.ID_ANY, u"Run Marxan", wx.DefaultPosition, wx.DefaultSize, 0 )
		run_marxan_sizer.Add( self.run_marxan_button, 0, wx.ALL, 5 )

		self.view_sum = wx.Button( self.marxanAnalysis, wx.ID_ANY, u"View sum", wx.DefaultPosition, wx.DefaultSize, 0 )
		run_marxan_sizer.Add( self.view_sum, 0, wx.ALL, 5 )

		self.view_mvbest = wx.Button( self.marxanAnalysis, wx.ID_ANY, u"View mvbest", wx.DefaultPosition, wx.DefaultSize, 0 )
		run_marxan_sizer.Add( self.view_mvbest, 0, wx.ALL, 5 )


		marxanMainSizer.Add( run_marxan_sizer, 1, wx.EXPAND, 5 )


		self.marxanAnalysis.SetSizer( marxanMainSizer )
		self.marxanAnalysis.Layout()
		marxanMainSizer.Fit( self.marxanAnalysis )
		self.auinotebook.AddPage( self.marxanAnalysis, u"6) Run Marxan", False, wx.NullBitmap )
		self.postHocEvaluation = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		postHocMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		postHocMainSizer.AddGrowableCol( 0 )
		postHocMainSizer.AddGrowableRow( 2 )
		postHocMainSizer.SetFlexibleDirection( wx.BOTH )
		postHocMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		postHoc_def_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.postHoc_def_txt = wx.StaticText( self.postHocEvaluation, wx.ID_ANY, u"This tab will allow you to evaluate the Marxan output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.postHoc_def_txt.Wrap( -1 )

		postHoc_def_sizer.Add( self.postHoc_def_txt, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )


		postHocMainSizer.Add( postHoc_def_sizer, 1, wx.EXPAND, 5 )

		postHoc_choice_sizer = wx.BoxSizer( wx.VERTICAL )

		self.postHoc_choice_txt = wx.StaticText( self.postHocEvaluation, wx.ID_ANY, u"Choose Available Marxan output to evaluate.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.postHoc_choice_txt.Wrap( -1 )

		self.postHoc_choice_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		postHoc_choice_sizer.Add( self.postHoc_choice_txt, 0, wx.ALL, 5 )

		postHoc_choice_opt_sizer = wx.FlexGridSizer( 2, 2, 0, 0 )
		postHoc_choice_opt_sizer.AddGrowableCol( 1 )
		postHoc_choice_opt_sizer.SetFlexibleDirection( wx.BOTH )
		postHoc_choice_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.postHoc_category_choice_txt = wx.StaticText( self.postHocEvaluation, wx.ID_ANY, u"Connectivity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.postHoc_category_choice_txt.Wrap( -1 )

		postHoc_choice_opt_sizer.Add( self.postHoc_category_choice_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

		self.postHoc_output_choice_txt = wx.StaticText( self.postHocEvaluation, wx.ID_ANY, u"Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.postHoc_output_choice_txt.Wrap( -1 )

		postHoc_choice_opt_sizer.Add( self.postHoc_output_choice_txt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		postHoc_category_choiceChoices = [ u"Demographic Data", u"Landscape Data" ]
		self.postHoc_category_choice = wx.Choice( self.postHocEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, postHoc_category_choiceChoices, 0 )
		self.postHoc_category_choice.SetSelection( 0 )
		postHoc_choice_opt_sizer.Add( self.postHoc_category_choice, 0, wx.ALL, 5 )

		postHoc_output_choiceChoices = []
		self.postHoc_output_choice = wx.Choice( self.postHocEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, postHoc_output_choiceChoices, 0 )
		self.postHoc_output_choice.SetSelection( 0 )
		postHoc_choice_opt_sizer.Add( self.postHoc_output_choice, 0, wx.ALL|wx.EXPAND, 5 )


		postHoc_choice_sizer.Add( postHoc_choice_opt_sizer, 1, wx.EXPAND, 5 )


		postHocMainSizer.Add( postHoc_choice_sizer, 1, wx.EXPAND, 5 )

		postHoc_grid_sizer = wx.BoxSizer( wx.VERTICAL )

		self.postHoc_grid = wx.grid.Grid( self.postHocEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.postHoc_grid.CreateGrid( 0, 0 )
		self.postHoc_grid.EnableEditing( True )
		self.postHoc_grid.EnableGridLines( True )
		self.postHoc_grid.EnableDragGridSize( True )
		self.postHoc_grid.SetMargins( 0, 0 )

		# Columns
		self.postHoc_grid.AutoSizeColumns()
		self.postHoc_grid.EnableDragColMove( False )
		self.postHoc_grid.EnableDragColSize( True )
		self.postHoc_grid.SetColLabelSize( 30 )
		self.postHoc_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.postHoc_grid.AutoSizeRows()
		self.postHoc_grid.EnableDragRowSize( False )
		self.postHoc_grid.SetRowLabelSize( 80 )
		self.postHoc_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.postHoc_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		postHoc_grid_sizer.Add( self.postHoc_grid, 0, wx.ALL|wx.EXPAND, 5 )


		postHocMainSizer.Add( postHoc_grid_sizer, 1, wx.EXPAND, 5 )

		pudat_file_sizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		pudat_file_sizer1.AddGrowableCol( 1 )
		pudat_file_sizer1.SetFlexibleDirection( wx.BOTH )
		pudat_file_sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.postHoc_export_txt = wx.StaticText( self.postHocEvaluation, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.postHoc_export_txt.Wrap( -1 )

		pudat_file_sizer1.Add( self.postHoc_export_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

		self.postHoc_file = wx.FilePickerCtrl( self.postHocEvaluation, wx.ID_ANY, u"~\\postHoc.csv", u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		pudat_file_sizer1.Add( self.postHoc_file, 0, wx.ALL|wx.EXPAND, 5 )


		postHocMainSizer.Add( pudat_file_sizer1, 1, wx.EXPAND, 5 )

		metrics_buttons_sizer2 = wx.FlexGridSizer( 0, 6, 0, 0 )
		metrics_buttons_sizer2.AddGrowableCol( 0 )
		metrics_buttons_sizer2.SetFlexibleDirection( wx.BOTH )
		metrics_buttons_sizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.spacertext2 = wx.StaticText( self.postHocEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertext2.Wrap( -1 )

		metrics_buttons_sizer2.Add( self.spacertext2, 0, wx.ALL, 5 )

		self.export_postHoc = wx.Button( self.postHocEvaluation, wx.ID_ANY, u"Export File", wx.DefaultPosition, wx.DefaultSize, 0 )
		metrics_buttons_sizer2.Add( self.export_postHoc, 0, wx.ALL, 5 )

		self.calc_postHoc = wx.Button( self.postHocEvaluation, wx.ID_ANY, u"Calculate Post-Hoc", wx.DefaultPosition, wx.DefaultSize, 0 )
		metrics_buttons_sizer2.Add( self.calc_postHoc, 0, wx.ALL, 5 )


		postHocMainSizer.Add( metrics_buttons_sizer2, 1, wx.EXPAND, 5 )


		self.postHocEvaluation.SetSizer( postHocMainSizer )
		self.postHocEvaluation.Layout()
		postHocMainSizer.Fit( self.postHocEvaluation )
		self.auinotebook.AddPage( self.postHocEvaluation, u"7) Post-Hoc Evaluation", False, wx.NullBitmap )
		self.plottingOptions = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		plottingMainSizer = wx.FlexGridSizer( 15, 0, 0, 0 )
		plottingMainSizer.AddGrowableCol( 0 )
		plottingMainSizer.AddGrowableRow( 1 )
		plottingMainSizer.AddGrowableRow( 2 )
		plottingMainSizer.AddGrowableRow( 3 )
		plottingMainSizer.SetFlexibleDirection( wx.BOTH )
		plottingMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

		self.mapoptions_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Map Plotting Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mapoptions_txt.Wrap( -1 )

		self.mapoptions_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		plottingMainSizer.Add( self.mapoptions_txt, 0, wx.ALL, 5 )

		bmap_txt_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.bmap_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot Basemap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_plot_check.SetValue(True)
		bmap_txt_sizer.Add( self.bmap_plot_check, 0, wx.ALL, 5 )

		bmap_sizer = wx.BoxSizer( wx.HORIZONTAL )

		bmap_options_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		bmap_options_sizer.SetFlexibleDirection( wx.BOTH )
		bmap_options_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.bmap_landcol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Land Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_landcol_txt.Wrap( -1 )

		bmap_options_sizer.Add( self.bmap_landcol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bmap_lakecol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Lake Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_lakecol_txt.Wrap( -1 )

		bmap_options_sizer.Add( self.bmap_lakecol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bmap_oceancol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Ocean Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_oceancol_txt.Wrap( -1 )

		bmap_options_sizer.Add( self.bmap_oceancol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bmap_buffer_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Buffer (degrees)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_buffer_txt.Wrap( -1 )

		bmap_options_sizer.Add( self.bmap_buffer_txt, 0, 0, 5 )

		self.bmap_landcol = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.Colour( 221, 170, 102 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.bmap_landcol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		bmap_options_sizer.Add( self.bmap_landcol, 0, wx.ALL, 5 )

		self.bmap_lakecol = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.Colour( 176, 196, 222 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.bmap_lakecol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		bmap_options_sizer.Add( self.bmap_lakecol, 0, wx.ALL, 5 )

		self.bmap_oceancol = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.Colour( 135, 206, 250 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.bmap_oceancol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		bmap_options_sizer.Add( self.bmap_oceancol, 0, wx.ALL, 5 )

		self.bmap_buffer = wx.TextCtrl( self.plottingOptions, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_buffer.SetToolTip( u"Spatial Buffer around the shapefiles measured in decimal degrees" )

		bmap_options_sizer.Add( self.bmap_buffer, 0, wx.ALL, 5 )


		bmap_sizer.Add( bmap_options_sizer, 1, wx.EXPAND, 5 )


		bmap_txt_sizer.Add( bmap_sizer, 1, wx.EXPAND, 5 )


		plottingMainSizer.Add( bmap_txt_sizer, 1, wx.EXPAND, 5 )

		lyr1_txt_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.lyr1_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot 1st Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr1_plot_check.SetValue(True)
		lyr1_txt_sizer.Add( self.lyr1_plot_check, 0, wx.ALL, 5 )

		lyr1_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.lyr1_choice = wx.Choicebook( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_TOP )
		self.metrics_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		metrics_opt_sizer = wx.FlexGridSizer( 4, 3, 0, 0 )
		metrics_opt_sizer.SetFlexibleDirection( wx.BOTH )
		metrics_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.metric_shp_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_shp_txt.Wrap( -1 )

		metrics_opt_sizer.Add( self.metric_shp_txt, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.metric_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_txt.Wrap( -1 )

		metrics_opt_sizer.Add( self.metric_txt, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.metric_lowcol_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_lowcol_txt.Wrap( -1 )

		metrics_opt_sizer.Add( self.metric_lowcol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )

		metric_shp_choiceChoices = [ u"Planning Units (Marxan Results)", u"Planning Units (Demographic Data)", u"Planning Units (Genetic Data)", u"Planning Units (Landscape Data)", u"Demographic Units", u"Genetic Units", u"Landscape Units" ]
		self.metric_shp_choice = wx.Choice( self.metrics_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, metric_shp_choiceChoices, 0 )
		self.metric_shp_choice.SetSelection( 0 )
		metrics_opt_sizer.Add( self.metric_shp_choice, 0, wx.ALL, 5 )

		metric_choiceChoices = [ u"Selection Frequency", u"Best Solution", u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment", u"Outflux", u"Temporal Connectivity Covariance", u"Focus Area Sink", u"Focus Area Source", u"Avoidance Area Sink", u"Avoidance Area Source" ]
		self.metric_choice = wx.Choice( self.metrics_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, metric_choiceChoices, 0 )
		self.metric_choice.SetSelection( 0 )
		metrics_opt_sizer.Add( self.metric_choice, 0, wx.ALL, 5 )

		self.metric_lowcol = wx.ColourPickerCtrl( self.metrics_opt, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.metric_lowcol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		metrics_opt_sizer.Add( self.metric_lowcol, 0, wx.ALL, 5 )

		self.metric_alpha_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_alpha_txt.Wrap( -1 )

		metrics_opt_sizer.Add( self.metric_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )

		self.metric_legend_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_legend_txt.Wrap( -1 )

		metrics_opt_sizer.Add( self.metric_legend_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )

		self.metric_hicol_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_hicol_txt.Wrap( -1 )

		metrics_opt_sizer.Add( self.metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )

		self.metric_alpha = wx.Slider( self.metrics_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		metrics_opt_sizer.Add( self.metric_alpha, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		metric_legendChoices = [ u"Top", u"Bottom", u"None" ]
		self.metric_legend = wx.Choice( self.metrics_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, metric_legendChoices, 0 )
		self.metric_legend.SetSelection( 1 )
		metrics_opt_sizer.Add( self.metric_legend, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.metric_hicol = wx.ColourPickerCtrl( self.metrics_opt, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.metric_hicol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		metrics_opt_sizer.Add( self.metric_hicol, 0, wx.ALL, 5 )


		self.metrics_opt.SetSizer( metrics_opt_sizer )
		self.metrics_opt.Layout()
		metrics_opt_sizer.Fit( self.metrics_opt )
		self.lyr1_choice.AddPage( self.metrics_opt, u"Colormap of connectivity metrics", True )
		self.poly_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		poly_plot_opt_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		poly_plot_opt_sizer.SetFlexibleDirection( wx.BOTH )
		poly_plot_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.poly_shp_txt = wx.StaticText( self.poly_plot_opt, wx.ID_ANY, u"Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.poly_shp_txt.Wrap( -1 )

		poly_plot_opt_sizer.Add( self.poly_shp_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.poly_col_txt = wx.StaticText( self.poly_plot_opt, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.poly_col_txt.Wrap( -1 )

		poly_plot_opt_sizer.Add( self.poly_col_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.poly_alpha_txt = wx.StaticText( self.poly_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.poly_alpha_txt.Wrap( -1 )

		poly_plot_opt_sizer.Add( self.poly_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		poly_shp_choiceChoices = [ u"Planning Units", u"Focus Areas", u"Avoidance Areas", u"Demographic Units", u"Genetic Units", u"Landscape Units" ]
		self.poly_shp_choice = wx.Choice( self.poly_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, poly_shp_choiceChoices, 0 )
		self.poly_shp_choice.SetSelection( 3 )
		poly_plot_opt_sizer.Add( self.poly_shp_choice, 0, wx.ALL, 5 )

		self.poly_col = wx.ColourPickerCtrl( self.poly_plot_opt, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.poly_col.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		poly_plot_opt_sizer.Add( self.poly_col, 0, wx.ALL, 5 )

		self.poly_alpha = wx.Slider( self.poly_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		poly_plot_opt_sizer.Add( self.poly_alpha, 0, wx.ALL, 5 )


		self.poly_plot_opt.SetSizer( poly_plot_opt_sizer )
		self.poly_plot_opt.Layout()
		poly_plot_opt_sizer.Fit( self.poly_plot_opt )
		self.lyr1_choice.AddPage( self.poly_plot_opt, u"Outline of shapefile", False )
		lyr1_sizer.Add( self.lyr1_choice, 1, wx.EXPAND |wx.ALL, 5 )


		lyr1_txt_sizer.Add( lyr1_sizer, 1, wx.EXPAND, 5 )


		plottingMainSizer.Add( lyr1_txt_sizer, 1, wx.EXPAND, 5 )

		lyr2_txt_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.lyr2_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot 2nd Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
		lyr2_txt_sizer.Add( self.lyr2_plot_check, 0, wx.ALL, 5 )

		lyr2_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.lyr2_choice = wx.Choicebook( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_TOP )
		self.metrics_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		metrics_opt_sizer1 = wx.FlexGridSizer( 4, 3, 0, 0 )
		metrics_opt_sizer1.SetFlexibleDirection( wx.BOTH )
		metrics_opt_sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.metric_shp_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_shp_txt1.Wrap( -1 )

		metrics_opt_sizer1.Add( self.metric_shp_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.metric_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_txt1.Wrap( -1 )

		metrics_opt_sizer1.Add( self.metric_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.metric_lowcol_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_lowcol_txt1.Wrap( -1 )

		metrics_opt_sizer1.Add( self.metric_lowcol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )

		metric_shp_choice1Choices = [ u"Planning Units (Marxan Results)", u"Planning Units (Demographic Data)", u"Planning Units (Genetic Data)", u"Planning Units (Landscape Data)", u"Demographic Units", u"Genetic Units", u"Landscape Units" ]
		self.metric_shp_choice1 = wx.Choice( self.metrics_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, metric_shp_choice1Choices, 0 )
		self.metric_shp_choice1.SetSelection( 0 )
		metrics_opt_sizer1.Add( self.metric_shp_choice1, 0, wx.ALL, 5 )

		metric_choice1Choices = [ u"Selection Frequency", u"Best Solution", u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment", u"Outflux", u"Temporal Connectivity Covariance", u"Focus Area Sink", u"Focus Area Source", u"Avoidance Area Sink", u"Avoidance Area Source" ]
		self.metric_choice1 = wx.Choice( self.metrics_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, metric_choice1Choices, 0 )
		self.metric_choice1.SetSelection( 1 )
		metrics_opt_sizer1.Add( self.metric_choice1, 0, wx.ALL, 5 )

		self.metric_lowcol1 = wx.ColourPickerCtrl( self.metrics_opt1, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.metric_lowcol1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		metrics_opt_sizer1.Add( self.metric_lowcol1, 0, wx.ALL, 5 )

		self.metric_alpha_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_alpha_txt1.Wrap( -1 )

		metrics_opt_sizer1.Add( self.metric_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )

		self.metric_legend_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_legend_txt1.Wrap( -1 )

		metrics_opt_sizer1.Add( self.metric_legend_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )

		self.metric_hicol_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_hicol_txt1.Wrap( -1 )

		metrics_opt_sizer1.Add( self.metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )

		self.metric_alpha1 = wx.Slider( self.metrics_opt1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		metrics_opt_sizer1.Add( self.metric_alpha1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		metric_legend1Choices = [ u"Top", u"Bottom", u"None" ]
		self.metric_legend1 = wx.Choice( self.metrics_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, metric_legend1Choices, 0 )
		self.metric_legend1.SetSelection( 1 )
		metrics_opt_sizer1.Add( self.metric_legend1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.metric_hicol1 = wx.ColourPickerCtrl( self.metrics_opt1, wx.ID_ANY, wx.Colour( 0, 128, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.metric_hicol1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		metrics_opt_sizer1.Add( self.metric_hicol1, 0, wx.ALL, 5 )


		self.metrics_opt1.SetSizer( metrics_opt_sizer1 )
		self.metrics_opt1.Layout()
		metrics_opt_sizer1.Fit( self.metrics_opt1 )
		self.lyr2_choice.AddPage( self.metrics_opt1, u"Colormap of connectivity metrics", False )
		self.poly_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		poly_plot_opt_sizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		poly_plot_opt_sizer1.SetFlexibleDirection( wx.BOTH )
		poly_plot_opt_sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.poly_shp_txt1 = wx.StaticText( self.poly_plot_opt1, wx.ID_ANY, u"Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.poly_shp_txt1.Wrap( -1 )

		poly_plot_opt_sizer1.Add( self.poly_shp_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.poly_col_txt1 = wx.StaticText( self.poly_plot_opt1, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.poly_col_txt1.Wrap( -1 )

		poly_plot_opt_sizer1.Add( self.poly_col_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.poly_alpha_txt1 = wx.StaticText( self.poly_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.poly_alpha_txt1.Wrap( -1 )

		poly_plot_opt_sizer1.Add( self.poly_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		poly_shp_choice1Choices = [ u"Planning Units", u"Focus Areas", u"Avoidance Areas", u"Demographic Units", u"Genetic Units", u"Landscape Units" ]
		self.poly_shp_choice1 = wx.Choice( self.poly_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, poly_shp_choice1Choices, 0 )
		self.poly_shp_choice1.SetSelection( 0 )
		poly_plot_opt_sizer1.Add( self.poly_shp_choice1, 0, wx.ALL, 5 )

		self.poly_col1 = wx.ColourPickerCtrl( self.poly_plot_opt1, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.poly_col1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )

		poly_plot_opt_sizer1.Add( self.poly_col1, 0, wx.ALL, 5 )

		self.poly_alpha1 = wx.Slider( self.poly_plot_opt1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		poly_plot_opt_sizer1.Add( self.poly_alpha1, 0, wx.ALL, 5 )


		self.poly_plot_opt1.SetSizer( poly_plot_opt_sizer1 )
		self.poly_plot_opt1.Layout()
		poly_plot_opt_sizer1.Fit( self.poly_plot_opt1 )
		self.lyr2_choice.AddPage( self.poly_plot_opt1, u"Outline of shapefile", True )
		lyr2_sizer.Add( self.lyr2_choice, 1, wx.EXPAND |wx.ALL, 5 )


		lyr2_txt_sizer.Add( lyr2_sizer, 1, wx.EXPAND, 5 )


		plottingMainSizer.Add( lyr2_txt_sizer, 1, wx.EXPAND, 5 )

		self.plot_map_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Plot Map", wx.DefaultPosition, wx.DefaultSize, 0 )
		plottingMainSizer.Add( self.plot_map_button, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.plot_opt_seperator = wx.StaticLine( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		plottingMainSizer.Add( self.plot_opt_seperator, 0, wx.EXPAND |wx.ALL, 5 )

		self.Export = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Export Spatial Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Export.Wrap( -1 )

		self.Export.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		plottingMainSizer.Add( self.Export, 0, wx.ALL, 5 )

		pushp_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		pushp_file_sizer.AddGrowableCol( 1 )
		pushp_file_sizer.SetFlexibleDirection( wx.BOTH )
		pushp_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.PUSHP_filecheck = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Export data to shapefile: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUSHP_filecheck.SetValue(True)
		pushp_file_sizer.Add( self.PUSHP_filecheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.PUSHP_file = wx.FilePickerCtrl( self.plottingOptions, wx.ID_ANY, u"~\\pu.shp", u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		pushp_file_sizer.Add( self.PUSHP_file, 0, wx.ALL|wx.EXPAND, 5 )


		plottingMainSizer.Add( pushp_file_sizer, 1, wx.EXPAND, 5 )

		pucsv_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		pucsv_file_sizer.AddGrowableCol( 1 )
		pucsv_file_sizer.SetFlexibleDirection( wx.BOTH )
		pucsv_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.PUCSV_filecheck = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Export data to file: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCSV_filecheck.SetValue(True)
		pucsv_file_sizer.Add( self.PUCSV_filecheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.PUCSV_file = wx.FilePickerCtrl( self.plottingOptions, wx.ID_ANY, u"~\\pu.csv", u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		pucsv_file_sizer.Add( self.PUCSV_file, 0, wx.ALL|wx.EXPAND, 5 )


		plottingMainSizer.Add( pucsv_file_sizer, 1, wx.EXPAND, 5 )

		map_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		map_file_sizer.AddGrowableCol( 1 )
		map_file_sizer.SetFlexibleDirection( wx.BOTH )
		map_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.MAP_filecheck = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Export map to: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MAP_filecheck.SetValue(True)
		map_file_sizer.Add( self.MAP_filecheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.MAP_file = wx.FilePickerCtrl( self.plottingOptions, wx.ID_ANY, u"~\\map.png", u"Select a file", u"Portable Network Graphics (*.png)|*.png|Joint Photographic Experts Group (*.jpg)|*.jpg|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		map_file_sizer.Add( self.MAP_file, 0, wx.ALL|wx.EXPAND, 5 )


		plottingMainSizer.Add( map_file_sizer, 1, wx.EXPAND, 5 )

		self.plot_export_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		plottingMainSizer.Add( self.plot_export_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.plottingOptions.SetSizer( plottingMainSizer )
		self.plottingOptions.Layout()
		plottingMainSizer.Fit( self.plottingOptions )
		self.auinotebook.AddPage( self.plottingOptions, u"8) Plotting Options", False, wx.NullBitmap )

		aui_sizer.Add( self.auinotebook, 1, wx.EXPAND, 5 )


		self.SetSizer( aui_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_new_project, id = self.new_project.GetId() )
		self.Bind( wx.EVT_MENU, self.on_save_project, id = self.save_project.GetId() )
		self.Bind( wx.EVT_MENU, self.on_save_project_as, id = self.save_project_as.GetId() )
		self.Bind( wx.EVT_MENU, self.on_load_project, id = self.load_project.GetId() )
		self.Bind( wx.EVT_MENU, self.on_github, id = self.github.GetId() )
		self.Bind( wx.EVT_MENU, self.on_debug_mode, id = self.debug_mode.GetId() )
		self.Bind( wx.EVT_MENU, self.on_glossary, id = self.glossary.GetId() )
		self.Bind( wx.EVT_MENU, self.on_tutorial, id = self.tutorial.GetId() )
		self.Bind( wx.EVT_MENU, self.on_contributing, id = self.contributing.GetId() )
		self.Bind( wx.EVT_MENU, self.on_license, id = self.license.GetId() )
		self.Bind( wx.EVT_MENU, self.on_about, id = self.about.GetId() )
		self.Bind( wx.EVT_MENU, self.on_getting_started, id = self.start.GetId() )
		self.Bind( wx.EVT_MENU, self.on_mwz, id = self.mwz.GetId() )
		self.Bind( wx.EVT_MENU, self.on_posthoc, id = self.posthoc.GetId() )
		self.PU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PU_file )
		self.PU_file_pu_id.Bind( wx.EVT_CHOICE, self.on_PU_file_pu_id )
		self.FA_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_FA_file )
		self.fa_status_radioBox.Bind( wx.EVT_RADIOBOX, self.on_fa_status_radioBox )
		self.AA_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_AA_file )
		self.aa_status_radioBox.Bind( wx.EVT_RADIOBOX, self.on_aa_status_radioBox )
		self.conn_category_choicebook.Bind( wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.on_conn_category_choice )
		self.demo_matrixTypeRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_matrixTypeRadioBox )
		self.demo_matrixFormatRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_matrixFormatRadioBox )
		self.demo_rescaleRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_rescaleRadioBox )
		self.demo_rescale_edgeRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_rescale_edgeRadioBox )
		self.demo_CU_CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_demo_CU_CM_file )
		self.demo_CU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_demo_CU_file )
		self.demo_CU_file_pu_id.Bind( wx.EVT_CHOICE, self.on_demo_CU_file_pu_id )
		self.demo_PU_CM_progress.Bind( wx.EVT_CHECKBOX, self.on_demo_PU_CM_progress )
		self.demo_PU_CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_demo_PU_CM_file )
		self.demo_rescale_button.Bind( wx.EVT_BUTTON, self.on_demo_rescale_button )
		self.land_type_choice.Bind( wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.on_land_type_choice )
		self.land_res_matrixTypeRadioBox.Bind( wx.EVT_RADIOBOX, self.on_land_res_matrixTypeRadioBox )
		self.land_HAB_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_land_HAB_file )
		self.land_HAB_file_hab_id.Bind( wx.EVT_CHOICE, self.on_land_HAB_file_hab_id )
		self.land_HAB_buff.Bind( wx.EVT_TEXT, self.on_land_HAB_buff )
		self.land_HAB_thresh.Bind( wx.EVT_TEXT, self.on_land_HAB_thresh )
		self.land_RES_mat_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_land_RES_mat_file )
		self.resistance_mat_customize.Bind( wx.EVT_BUTTON, self.on_resistance_mat_customize )
		self.land_RES_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_land_RES_file )
		self.land_RES_file_res_id.Bind( wx.EVT_CHOICE, self.on_land_RES_file_hab_id )
		self.land_PU_CM_progress.Bind( wx.EVT_CHECKBOX, self.on_land_PU_CM_progress )
		self.land_PU_CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_land_PU_CM_file )
		self.land_generate_button.Bind( wx.EVT_BUTTON, self.on_land_generate_button )
		self.LP_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_LP_file )
		self.cf_demo_in_degree.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_out_degree.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_between_cent.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_eig_vect_cent.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_google.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_self_recruit.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_local_retention.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_inflow.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_outflow.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_stochasticity.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_fa_recipients.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_fa_donors.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_aa_recipients.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_demo_aa_donors.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_in_degree.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_out_degree.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_between_cent.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_eig_vect_cent.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_google.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_fa_recipients.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_fa_donors.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_aa_recipients.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.cf_land_aa_donors.Bind( wx.EVT_CHECKBOX, self.enable_calc_metrics )
		self.bd_demo_conn_boundary.Bind( wx.EVT_CHECKBOX, self.on_bd_demo_conn_boundary )
		self.bd_demo_min_plan_graph.Bind( wx.EVT_CHECKBOX, self.on_bd_demo_min_plan_graph )
		self.bd_land_conn_boundary.Bind( wx.EVT_CHECKBOX, self.on_bd_land_conn_boundary )
		self.bd_land_min_plan_graph.Bind( wx.EVT_CHECKBOX, self.on_bd_land_min_plan_graph )
		self.metric_definition_choice.Bind( wx.EVT_CHOICE, self.on_metric_definition_choice )
		self.calc_metrics.Bind( wx.EVT_BUTTON, self.on_calc_metrics )
		self.preEval_metric_shp_choice.Bind( wx.EVT_CHOICE, self.on_preEval_metric_shp_choice )
		self.preEval_metric_choice.Bind( wx.EVT_CHOICE, self.on_preEval_metric_choice )
		self.plot_freq_metric.Bind( wx.EVT_BUTTON, self.on_plot_freq_metric )
		self.remove_metric.Bind( wx.EVT_BUTTON, self.on_remove_metric )
		self.preEval_discrete_from_quartile.Bind( wx.EVT_CHECKBOX, self.on_from_check )
		self.preEval_discrete_from_percentile.Bind( wx.EVT_CHECKBOX, self.on_from_check )
		self.preEval_discrete_from_value.Bind( wx.EVT_CHECKBOX, self.on_from_check )
		self.preEval_discrete_to_quartile.Bind( wx.EVT_CHECKBOX, self.on_to_check )
		self.preEval_discrete_to_percentile.Bind( wx.EVT_CHECKBOX, self.on_to_check )
		self.preEval_discrete_to_value.Bind( wx.EVT_CHECKBOX, self.on_to_check )
		self.preEval_create_new.Bind( wx.EVT_BUTTON, self.on_preEval_create_new )
		self.cf_export_radioBox.Bind( wx.EVT_RADIOBOX, self.on_cf_export_radioBox )
		self.spec_radio.Bind( wx.EVT_RADIOBOX, self.on_spec_radio )
		self.orig_CF_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_orig_CF_file )
		self.CF_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CF_file )
		self.orig_SPEC_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_orig_SPEC_file )
		self.SPEC_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_SPEC_file )
		self.customize_spec.Bind( wx.EVT_BUTTON, self.on_customize_spec )
		self.targets.Bind( wx.EVT_TEXT, self.on_targets )
		self.export_CF_files.Bind( wx.EVT_BUTTON, self.on_export_CF_files )
		self.orig_BD_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_orig_BD_file )
		self.BD_filecheck.Bind( wx.EVT_CHECKBOX, self.on_BD_filecheck )
		self.BD_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_BD_file )
		self.export_BD_file.Bind( wx.EVT_BUTTON, self.on_export_BD_file )
		self.orig_PUDAT_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_orig_PUDAT_file )
		self.PUDAT_filecheck.Bind( wx.EVT_CHECKBOX, self.on_PUDAT_filecheck )
		self.PUDAT_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PUDAT_file )
		self.export_pudat.Bind( wx.EVT_BUTTON, self.on_export_PUDAT )
		self.export_metrics.Bind( wx.EVT_BUTTON, self.on_export_metrics )
		self.inputdat_template_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_inputdat_template_file )
		self.default_input_template.Bind( wx.EVT_BUTTON, self.on_default_input_template )
		self.NUMREPS.Bind( wx.EVT_TEXT, self.on_NUMREPS )
		self.SCENNAME.Bind( wx.EVT_TEXT, self.on_SCENNAME )
		self.marxan_CF.Bind( wx.EVT_RADIOBOX, self.on_marxan_CF )
		self.marxan_bound.Bind( wx.EVT_RADIOBOX, self.on_marxan_bound )
		self.inputdat_symmRadio.Bind( wx.EVT_RADIOBOX, self.on_inputdat_symmRadio )
		self.CSM.Bind( wx.EVT_TEXT, self.on_CSM )
		self.marxan_PU.Bind( wx.EVT_RADIOBOX, self.on_marxan_PU )
		self.marxan_Radio.Bind( wx.EVT_RADIOBOX, self.on_marxan_Radio )
		self.marxanBit_Radio.Bind( wx.EVT_RADIOBOX, self.on_marxanBit_Radio )
		self.generate_inputdat.Bind( wx.EVT_BUTTON, self.on_generate_inputdat )
		self.inputdat_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_inputdat_file )
		self.customize_inpudat.Bind( wx.EVT_BUTTON, self.on_customize_inpudat )
		self.run_marxan_button.Bind( wx.EVT_BUTTON, self.on_run_marxan )
		self.view_sum.Bind( wx.EVT_BUTTON, self.on_view_sum )
		self.view_mvbest.Bind( wx.EVT_BUTTON, self.on_view_mvbest )
		self.postHoc_category_choice.Bind( wx.EVT_CHOICE, self.on_postHoc_category_choice )
		self.postHoc_output_choice.Bind( wx.EVT_CHOICE, self.on_postHoc_output_choice )
		self.postHoc_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_postHoc_file )
		self.export_postHoc.Bind( wx.EVT_BUTTON, self.on_export_postHoc )
		self.calc_postHoc.Bind( wx.EVT_BUTTON, self.on_calc_postHoc )
		self.metric_shp_choice.Bind( wx.EVT_CHOICE, self.on_metric_shp_choice )
		self.metric_shp_choice1.Bind( wx.EVT_CHOICE, self.on_metric_shp_choice1 )
		self.plot_map_button.Bind( wx.EVT_BUTTON, self.on_plot_map_button )
		self.PUSHP_filecheck.Bind( wx.EVT_CHECKBOX, self.on_PUSHP_filecheck )
		self.PUSHP_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PUSHP_file )
		self.PUCSV_filecheck.Bind( wx.EVT_CHECKBOX, self.on_PUCSV_filecheck )
		self.PUCSV_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PUCSV_file )
		self.MAP_filecheck.Bind( wx.EVT_CHECKBOX, self.on_MAP_filecheck )
		self.MAP_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_MAP_file )
		self.plot_export_button.Bind( wx.EVT_BUTTON, self.on_plot_export_button )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_new_project( self, event ):
		event.Skip()

	def on_save_project( self, event ):
		event.Skip()

	def on_save_project_as( self, event ):
		event.Skip()

	def on_load_project( self, event ):
		event.Skip()

	def on_github( self, event ):
		event.Skip()

	def on_debug_mode( self, event ):
		event.Skip()

	def on_glossary( self, event ):
		event.Skip()

	def on_tutorial( self, event ):
		event.Skip()

	def on_contributing( self, event ):
		event.Skip()

	def on_license( self, event ):
		event.Skip()

	def on_about( self, event ):
		event.Skip()

	def on_getting_started( self, event ):
		event.Skip()

	def on_mwz( self, event ):
		event.Skip()

	def on_posthoc( self, event ):
		event.Skip()

	def on_PU_file( self, event ):
		event.Skip()

	def on_PU_file_pu_id( self, event ):
		event.Skip()

	def on_FA_file( self, event ):
		event.Skip()

	def on_fa_status_radioBox( self, event ):
		event.Skip()

	def on_AA_file( self, event ):
		event.Skip()

	def on_aa_status_radioBox( self, event ):
		event.Skip()

	def on_conn_category_choice( self, event ):
		event.Skip()

	def on_demo_matrixTypeRadioBox( self, event ):
		event.Skip()

	def on_demo_matrixFormatRadioBox( self, event ):
		event.Skip()

	def on_demo_rescaleRadioBox( self, event ):
		event.Skip()

	def on_demo_rescale_edgeRadioBox( self, event ):
		event.Skip()

	def on_demo_CU_CM_file( self, event ):
		event.Skip()

	def on_demo_CU_file( self, event ):
		event.Skip()

	def on_demo_CU_file_pu_id( self, event ):
		event.Skip()

	def on_demo_PU_CM_progress( self, event ):
		event.Skip()

	def on_demo_PU_CM_file( self, event ):
		event.Skip()

	def on_demo_rescale_button( self, event ):
		event.Skip()

	def on_land_type_choice( self, event ):
		event.Skip()

	def on_land_res_matrixTypeRadioBox( self, event ):
		event.Skip()

	def on_land_HAB_file( self, event ):
		event.Skip()

	def on_land_HAB_file_hab_id( self, event ):
		event.Skip()

	def on_land_HAB_buff( self, event ):
		event.Skip()

	def on_land_HAB_thresh( self, event ):
		event.Skip()

	def on_land_RES_mat_file( self, event ):
		event.Skip()

	def on_resistance_mat_customize( self, event ):
		event.Skip()

	def on_land_RES_file( self, event ):
		event.Skip()

	def on_land_RES_file_hab_id( self, event ):
		event.Skip()

	def on_land_PU_CM_progress( self, event ):
		event.Skip()

	def on_land_PU_CM_file( self, event ):
		event.Skip()

	def on_land_generate_button( self, event ):
		event.Skip()

	def on_LP_file( self, event ):
		event.Skip()

	def enable_calc_metrics( self, event ):
		event.Skip()























	def on_bd_demo_conn_boundary( self, event ):
		event.Skip()

	def on_bd_demo_min_plan_graph( self, event ):
		event.Skip()

	def on_bd_land_conn_boundary( self, event ):
		event.Skip()

	def on_bd_land_min_plan_graph( self, event ):
		event.Skip()

	def on_metric_definition_choice( self, event ):
		event.Skip()

	def on_calc_metrics( self, event ):
		event.Skip()

	def on_preEval_metric_shp_choice( self, event ):
		event.Skip()

	def on_preEval_metric_choice( self, event ):
		event.Skip()

	def on_plot_freq_metric( self, event ):
		event.Skip()

	def on_remove_metric( self, event ):
		event.Skip()

	def on_from_check( self, event ):
		event.Skip()



	def on_to_check( self, event ):
		event.Skip()



	def on_preEval_create_new( self, event ):
		event.Skip()

	def on_cf_export_radioBox( self, event ):
		event.Skip()

	def on_spec_radio( self, event ):
		event.Skip()

	def on_orig_CF_file( self, event ):
		event.Skip()

	def on_CF_file( self, event ):
		event.Skip()

	def on_orig_SPEC_file( self, event ):
		event.Skip()

	def on_SPEC_file( self, event ):
		event.Skip()

	def on_customize_spec( self, event ):
		event.Skip()

	def on_targets( self, event ):
		event.Skip()

	def on_export_CF_files( self, event ):
		event.Skip()

	def on_orig_BD_file( self, event ):
		event.Skip()

	def on_BD_filecheck( self, event ):
		event.Skip()

	def on_BD_file( self, event ):
		event.Skip()

	def on_export_BD_file( self, event ):
		event.Skip()

	def on_orig_PUDAT_file( self, event ):
		event.Skip()

	def on_PUDAT_filecheck( self, event ):
		event.Skip()

	def on_PUDAT_file( self, event ):
		event.Skip()

	def on_export_PUDAT( self, event ):
		event.Skip()

	def on_export_metrics( self, event ):
		event.Skip()

	def on_inputdat_template_file( self, event ):
		event.Skip()

	def on_default_input_template( self, event ):
		event.Skip()

	def on_NUMREPS( self, event ):
		event.Skip()

	def on_SCENNAME( self, event ):
		event.Skip()

	def on_marxan_CF( self, event ):
		event.Skip()

	def on_marxan_bound( self, event ):
		event.Skip()

	def on_inputdat_symmRadio( self, event ):
		event.Skip()

	def on_CSM( self, event ):
		event.Skip()

	def on_marxan_PU( self, event ):
		event.Skip()

	def on_marxan_Radio( self, event ):
		event.Skip()

	def on_marxanBit_Radio( self, event ):
		event.Skip()

	def on_generate_inputdat( self, event ):
		event.Skip()

	def on_inputdat_file( self, event ):
		event.Skip()

	def on_customize_inpudat( self, event ):
		event.Skip()

	def on_run_marxan( self, event ):
		event.Skip()

	def on_view_sum( self, event ):
		event.Skip()

	def on_view_mvbest( self, event ):
		event.Skip()

	def on_postHoc_category_choice( self, event ):
		event.Skip()

	def on_postHoc_output_choice( self, event ):
		event.Skip()

	def on_postHoc_file( self, event ):
		event.Skip()

	def on_export_postHoc( self, event ):
		event.Skip()

	def on_calc_postHoc( self, event ):
		event.Skip()

	def on_metric_shp_choice( self, event ):
		event.Skip()

	def on_metric_shp_choice1( self, event ):
		event.Skip()

	def on_plot_map_button( self, event ):
		event.Skip()

	def on_PUSHP_filecheck( self, event ):
		event.Skip()

	def on_PUSHP_file( self, event ):
		event.Skip()

	def on_PUCSV_filecheck( self, event ):
		event.Skip()

	def on_PUCSV_file( self, event ):
		event.Skip()

	def on_MAP_filecheck( self, event ):
		event.Skip()

	def on_MAP_file( self, event ):
		event.Skip()

	def on_plot_export_button( self, event ):
		event.Skip()


###########################################################################
## Class GettingStarted
###########################################################################

class GettingStarted ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marxan Connect: Getting Started", pos = wx.DefaultPosition, size = wx.Size( 1100,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer50 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer61 = wx.FlexGridSizer( 6, 1, 0, 0 )
		fgSizer61.AddGrowableRow( 0 )
		fgSizer61.SetFlexibleDirection( wx.BOTH )
		fgSizer61.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText100 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"Marxan Connect (henceforth the \"app\") is a Graphical User Interface (GUI) to help conservationists include \"connectivity\" in their protected area network planning. The term \"connectivity\" has a various applications (i.e. larval connectivity, genetic connectivity,  landscape connectivity, etc) and protected area networks can be optimized for various connectivity objectives. The app is intended to guide conservationists through the process of identifying important aspects of connectivity for their conservation scenarios, as well as highlighting the necessary data.\n\nTo use this software, please visit the Tutorial and the Glossary which can be accessed under the help menu, or the links below. Otherwise, if you would just like to get started, please proceed through all the tabs from left to right starting the \"Spatial Input\". After calculating the \"Connectivity Metrics\", you can choose to conduct a Marxan analysis in the app, export the connectivity metrics for use in a standalone custom Marxan analysis, or you can visualize the Connectivity Metrics using the \"Plotting Options\" tab. The app also includes a fully functional python module (in progress) that is operated via command line that can be used to reproduce an analysis using the project file generated by the GUI. If you would like to report any bugs or request a missing feature, please post an issue on the GitHub repository which is available in the help menu, or the link below.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )

		bSizer51.Add( self.m_staticText100, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer61.Add( bSizer51, 1, wx.EXPAND, 5 )

		fgSizer62 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer62.AddGrowableCol( 0 )
		fgSizer62.AddGrowableCol( 2 )
		fgSizer62.SetFlexibleDirection( wx.BOTH )
		fgSizer62.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_hyperlink2 = wx.adv.HyperlinkCtrl( self.m_panel27, wx.ID_ANY, u"Tutorial", u"docs\\tutorial.html", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		fgSizer62.Add( self.m_hyperlink2, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_hyperlink3 = wx.adv.HyperlinkCtrl( self.m_panel27, wx.ID_ANY, u"Glossary", u"docs\\glossary.html", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		fgSizer62.Add( self.m_hyperlink3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

		self.m_hyperlink4 = wx.adv.HyperlinkCtrl( self.m_panel27, wx.ID_ANY, u"Report Issues", u"https://github.com/remi-daigle/MarxanConnect/issues", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		fgSizer62.Add( self.m_hyperlink4, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )


		fgSizer61.Add( fgSizer62, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer63 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer63.AddGrowableCol( 0 )
		fgSizer63.AddGrowableRow( 1 )
		fgSizer63.AddGrowableRow( 2 )
		fgSizer63.SetFlexibleDirection( wx.BOTH )
		fgSizer63.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1001 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"With funding provided by:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1001.Wrap( -1 )

		fgSizer63.Add( self.m_staticText1001, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP|wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/CHONelogo-small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer63.Add( self.m_bitmap2, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 20 )

		self.m_bitmap10 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/NSERC_C_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer63.Add( self.m_bitmap10, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP|wx.TOP, 20 )


		bSizer52.Add( fgSizer63, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP|wx.EXPAND, 5 )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap3 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/icon_MarxanConnect.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer63.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )


		bSizer52.Add( bSizer63, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		fgSizer631 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer631.AddGrowableCol( 0 )
		fgSizer631.AddGrowableRow( 1 )
		fgSizer631.SetFlexibleDirection( wx.BOTH )
		fgSizer631.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText10013 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"With funding provided by:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10013.Wrap( -1 )

		fgSizer631.Add( self.m_staticText10013, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP|wx.ALL, 5 )

		self.m_bitmap41 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/University-of-Queensland-UQ-logo_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer631.Add( self.m_bitmap41, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer52.Add( fgSizer631, 1, wx.EXPAND, 5 )


		fgSizer61.Add( bSizer52, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer512 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1002 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"How to cite (will have DOI, etc later):\n\nDaigle, RM; Metaxas, A; Balbar, AC; McGowan, J; Treml, EA; Kuempel, CD; Possingham, HP; Beger, M. 2018. Marxan Connect v0.1.2-rc2019.01.24.11. https://github.com/remi-daigle/MarxanConnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1002.Wrap( -1 )

		bSizer512.Add( self.m_staticText1002, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer61.Add( bSizer512, 1, wx.EXPAND, 5 )

		self.m_staticText10012 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"Additional contributions by:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10012.Wrap( -1 )

		fgSizer61.Add( self.m_staticText10012, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		fgSizer78 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer78.AddGrowableCol( 0 )
		fgSizer78.AddGrowableCol( 1 )
		fgSizer78.AddGrowableCol( 2 )
		fgSizer78.SetFlexibleDirection( wx.BOTH )
		fgSizer78.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap5 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/800px-Leeds_University_logo_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer78.Add( self.m_bitmap5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

		self.m_bitmap4 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/The Nature Conservancy_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer78.Add( self.m_bitmap4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bitmap51 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/dal-logo-small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer78.Add( self.m_bitmap51, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_bitmap52 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/University_of_Melbourne_logo_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer78.Add( self.m_bitmap52, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_bitmap21 = wx.StaticBitmap( self.m_panel27, wx.ID_ANY, wx.Bitmap( u"docs/images/ceed_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer78.Add( self.m_bitmap21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		fgSizer61.Add( fgSizer78, 1, wx.EXPAND, 5 )


		self.m_panel27.SetSizer( fgSizer61 )
		self.m_panel27.Layout()
		fgSizer61.Fit( self.m_panel27 )
		bSizer50.Add( self.m_panel27, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer50 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class spec_customizer
###########################################################################

class spec_customizer ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer50 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spec_mainsizer = wx.FlexGridSizer( 2, 1, 0, 0 )
		spec_mainsizer.AddGrowableCol( 0 )
		spec_mainsizer.AddGrowableRow( 0 )
		spec_mainsizer.AddGrowableRow( 1 )
		spec_mainsizer.SetFlexibleDirection( wx.BOTH )
		spec_mainsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.spec_grid = wx.grid.Grid( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.spec_grid.CreateGrid( 0, 4 )
		self.spec_grid.EnableEditing( True )
		self.spec_grid.EnableGridLines( True )
		self.spec_grid.EnableDragGridSize( False )
		self.spec_grid.SetMargins( 0, 0 )

		# Columns
		self.spec_grid.AutoSizeColumns()
		self.spec_grid.EnableDragColMove( False )
		self.spec_grid.EnableDragColSize( False )
		self.spec_grid.SetColLabelSize( 30 )
		self.spec_grid.SetColLabelValue( 0, u"id" )
		self.spec_grid.SetColLabelValue( 1, u"target" )
		self.spec_grid.SetColLabelValue( 2, u"spf" )
		self.spec_grid.SetColLabelValue( 3, u"name" )
		self.spec_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.spec_grid.AutoSizeRows()
		self.spec_grid.EnableDragRowSize( False )
		self.spec_grid.SetRowLabelSize( 80 )
		self.spec_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.spec_grid.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		spec_mainsizer.Add( self.spec_grid, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		spec_button_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		spec_button_sizer.AddGrowableCol( 0 )
		spec_button_sizer.SetFlexibleDirection( wx.BOTH )
		spec_button_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.spacer_text = wx.StaticText( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacer_text.Wrap( -1 )

		spec_button_sizer.Add( self.spacer_text, 0, wx.ALL, 5 )

		self.spec_ok = wx.Button( self.m_panel27, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		spec_button_sizer.Add( self.spec_ok, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.spec_cancel = wx.Button( self.m_panel27, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		spec_button_sizer.Add( self.spec_cancel, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		spec_mainsizer.Add( spec_button_sizer, 1, wx.EXPAND, 5 )


		self.m_panel27.SetSizer( spec_mainsizer )
		self.m_panel27.Layout()
		spec_mainsizer.Fit( self.m_panel27 )
		bSizer50.Add( self.m_panel27, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer50 )
		self.Layout()
		bSizer50.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.spec_ok.Bind( wx.EVT_BUTTON, self.on_spec_ok )
		self.spec_cancel.Bind( wx.EVT_BUTTON, self.on_spec_cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_spec_ok( self, event ):
		event.Skip()

	def on_spec_cancel( self, event ):
		event.Skip()


