# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.grid

###########################################################################
## Class MarxanConnectGUI
###########################################################################

class MarxanConnectGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marxan with Connectivity", pos = wx.DefaultPosition, size = wx.Size( 1087,823 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.debug_mode = wx.MenuItem( self.debug, wx.ID_ANY, u"Debug Mode", wx.EmptyString, wx.ITEM_NORMAL )
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
		self.pu_title.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		spatialMainSizer.Add( self.pu_title, 0, wx.ALL, 5 )
		
		pu_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PU_def = wx.StaticText( self.spatialInput, wx.ID_ANY, u"The planning unit is the fundamental spatial polygon on which Marxan analyses are based. The units can be any shape. Often square or hexagonal regular grids, or based on habitat features (e.g. reefs). All futher analyses will be based on whether a feature is present or absent in the planning unit.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_def.Wrap( -1 )
		pu_def_sizer.Add( self.PU_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		spatialMainSizer.Add( pu_def_sizer, 1, wx.EXPAND, 5 )
		
		pu_file_sizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		pu_file_sizer1.AddGrowableCol( 1 )
		pu_file_sizer1.SetFlexibleDirection( wx.HORIZONTAL )
		pu_file_sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.PU_filetext = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Planning Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_filetext.Wrap( -1 )
		self.PU_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
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
		self.fa_title.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		spatialMainSizer.Add( self.fa_title, 0, wx.ALL, 5 )
		
		fa_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.FA_def = wx.StaticText( self.spatialInput, wx.ID_ANY, u"For some of the connectivity metrics (e.g. Temporal Connectivity Correlation), it is important to consider 'focus areas' for which connectivity should be optimised. Such focus areas could include existing protected areas, important habitat for endangered species, and/or otherwise important habitats for connectivity (e.g. nursery grounds, genetically unique and potentially adaptively advantageous populations). Marxan with Connectivity assumes that the planning units within the 'focus areas' will otherwise be targeted as normal conservation targets in Marxan. Loading focus areas into Marxan with Connectivity allows users to set conservation targets for the areas that are connected to the 'focus areas'", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FA_def.Wrap( -1 )
		fa_def_sizer.Add( self.FA_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		spatialMainSizer.Add( fa_def_sizer, 1, wx.EXPAND, 5 )
		
		fa_file_sizer = wx.FlexGridSizer( 1, 2, 0, 0 )
		fa_file_sizer.AddGrowableCol( 1 )
		fa_file_sizer.SetFlexibleDirection( wx.BOTH )
		fa_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.FA_filetext = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Focus Areas Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FA_filetext.Wrap( -1 )
		self.FA_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
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
		self.fa_status_radioBox.SetSelection( 0 )
		fa_status_sizer.Add( self.fa_status_radioBox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		spatialMainSizer.Add( fa_status_sizer, 1, wx.EXPAND, 5 )
		
		self.aa_title = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Avoidance Areas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.aa_title.Wrap( -1 )
		self.aa_title.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		spatialMainSizer.Add( self.aa_title, 0, wx.ALL, 5 )
		
		aa_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.AA_def = wx.StaticText( self.spatialInput, wx.ID_ANY, u"For some of the connectivity metrics (e.g. TBD), it is important to consider 'avoidance areas' for which connectivity should be avoided. Such avoidance areas could include areas heavily infested by invasive species, or areas that are more likely to be invaded (e.g. international shipping ports). Marxan with Connectivity assumes that the planning units within the 'avoidance areas' will otherwise be targeted as normal conservation targets in Marxan. Loading avoidance areas into Marxan with Connectivity allows users to set conservation targets for the areas connected to the 'avoidance areas'", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AA_def.Wrap( -1 )
		aa_def_sizer.Add( self.AA_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		spatialMainSizer.Add( aa_def_sizer, 1, wx.EXPAND, 5 )
		
		aa_file_sizer = wx.FlexGridSizer( 1, 2, 0, 0 )
		aa_file_sizer.AddGrowableCol( 1 )
		aa_file_sizer.SetFlexibleDirection( wx.BOTH )
		aa_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.AA_filetext = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Avoidance Areas Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AA_filetext.Wrap( -1 )
		self.AA_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
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
		aa_status_sizer.Add( self.aa_status_radioBox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		spatialMainSizer.Add( aa_status_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.spatialInput.SetSizer( spatialMainSizer )
		self.spatialInput.Layout()
		spatialMainSizer.Fit( self.spatialInput )
		self.auinotebook.AddPage( self.spatialInput, u"1) Spatial Input", False, wx.NullBitmap )
		self.connectivityInput = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		conn_input_mainsizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		conn_input_mainsizer.AddGrowableCol( 0 )
		conn_input_mainsizer.AddGrowableRow( 2 )
		conn_input_mainsizer.SetFlexibleDirection( wx.BOTH )
		conn_input_mainsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		con_input_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.con_input_def_txt = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Connectivity data come from many sources and to simplify the input procedure has been divided into two main categories: demographic connectivity and landscape connectivity. ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.con_input_def_txt.Wrap( -1 )
		con_input_def_sizer.Add( self.con_input_def_txt, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		conn_input_mainsizer.Add( con_input_def_sizer, 1, wx.EXPAND, 5 )
		
		con_input_choice_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.con_input_choice_txt = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Choose Connectivity Input Category:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.con_input_choice_txt.Wrap( -1 )
		self.con_input_choice_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		con_input_choice_sizer.Add( self.con_input_choice_txt, 0, wx.ALL, 5 )
		
		
		conn_input_mainsizer.Add( con_input_choice_sizer, 1, wx.EXPAND, 5 )
		
		self.conn_category_choicebook = wx.Choicebook( self.connectivityInput, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.conn_category_choicebook.SetToolTip( u"Choosing a different category will not erase any input and input from multiple categories can be used simultaneously in the analyses in the next steps" )
		
		self.demographic = wx.Panel( self.conn_category_choicebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.demographic.SetToolTip( u"Choosing a different category will not erase any input and input from multiple categories can be used simultaneously in the analyses in the next steps" )
		
		demoMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		demoMainSizer.AddGrowableCol( 0 )
		demoMainSizer.AddGrowableRow( 0 )
		demoMainSizer.AddGrowableRow( 2 )
		demoMainSizer.AddGrowableRow( 6 )
		demoMainSizer.SetFlexibleDirection( wx.VERTICAL )
		demoMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		demo_cm_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.demo_CM_def = wx.StaticText( self.demographic, wx.ID_ANY, u"The connectivity matrix (or list) is the fundamental input format for demographic data. It describes the movement from donor sites to recipient sites. It can be obtained by directly quantifying the movement of individual organisms (e.g. tagging) or  by modelling the dispersal of individual organisms (e.g. biophysical modelling of larval dispersal). Please indicate your connectivity data units, type, and format in the boxes below, and if necessary use the rescaling tools if the data was not gathered at the same spatial scale as the planning units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_CM_def.Wrap( -1 )
		demo_cm_def_sizer.Add( self.demo_CM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( demo_cm_def_sizer, 1, wx.EXPAND, 5 )
		
		demo_radio_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		demo_radio_sizer.AddGrowableCol( 1 )
		demo_radio_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		demo_radio_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		demo_matrixUnitsRadioBoxChoices = [ u"Probability", u"Individuals" ]
		self.demo_matrixUnitsRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, demo_matrixUnitsRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.demo_matrixUnitsRadioBox.SetSelection( 0 )
		demo_radio_sizer.Add( self.demo_matrixUnitsRadioBox, 0, wx.ALL, 5 )
		
		demo_matrixTypeRadioBoxChoices = [ u"Settlement", u"Connectivity", u"Migration", u"Local Immigration", u"Dispersal Flux" ]
		self.demo_matrixTypeRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Connectivity Matrix Type", wx.DefaultPosition, wx.DefaultSize, demo_matrixTypeRadioBoxChoices, 3, wx.RA_SPECIFY_COLS )
		self.demo_matrixTypeRadioBox.SetSelection( 1 )
		demo_radio_sizer.Add( self.demo_matrixTypeRadioBox, 0, wx.ALL|wx.EXPAND, 5 )
		
		demo_matrixFormatRadioBoxChoices = [ u"Matrix", u"List", u"List with Time" ]
		self.demo_matrixFormatRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Format", wx.DefaultPosition, wx.DefaultSize, demo_matrixFormatRadioBoxChoices, 2, wx.RA_SPECIFY_COLS )
		self.demo_matrixFormatRadioBox.SetSelection( 0 )
		demo_radio_sizer.Add( self.demo_matrixFormatRadioBox, 0, wx.ALL, 5 )
		
		
		demoMainSizer.Add( demo_radio_sizer, 1, wx.ALIGN_CENTER, 5 )
		
		demo_cu_cm_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		demo_cu_cm_file_sizer.AddGrowableCol( 1 )
		demo_cu_cm_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		demo_cu_cm_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.demo_CU_CM_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_CU_CM_filetext.Wrap( -1 )
		self.demo_CU_CM_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		demo_cu_cm_file_sizer.Add( self.demo_CU_CM_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.demo_CU_CM_file = wx.FilePickerCtrl( self.demographic, wx.ID_ANY, u"~\\data\\grid_connectivity_matrix.csv", u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		demo_cu_cm_file_sizer.Add( self.demo_CU_CM_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( demo_cu_cm_file_sizer, 1, wx.EXPAND, 5 )
		
		demo_rescale_txt_sizer = wx.BoxSizer( wx.VERTICAL )
		
		demo_rescale_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.demo_rescale_def_txt = wx.StaticText( self.demographic, wx.ID_ANY, u"The demographic connectivity data does not need to be at the same spatial scale as the Marxan planning units. If there is a mismatch, rescale the connectivity data below.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_rescale_def_txt.Wrap( -1 )
		demo_rescale_def_sizer.Add( self.demo_rescale_def_txt, 0, wx.ALIGN_BOTTOM|wx.ALL|wx.EXPAND, 5 )
		
		
		demo_rescale_txt_sizer.Add( demo_rescale_def_sizer, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( demo_rescale_txt_sizer, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		demo_rescale_sizer = wx.FlexGridSizer( 1, 2, 0, 0 )
		demo_rescale_sizer.AddGrowableCol( 0 )
		demo_rescale_sizer.AddGrowableCol( 1 )
		demo_rescale_sizer.SetFlexibleDirection( wx.BOTH )
		demo_rescale_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		demo_rescaleRadioBoxChoices = [ u"Identical Grids", u"Rescale Connectivity Matrix" ]
		self.demo_rescaleRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Rescale Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, demo_rescaleRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.demo_rescaleRadioBox.SetSelection( 0 )
		demo_rescale_sizer.Add( self.demo_rescaleRadioBox, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		demo_rescale_edgeRadioBoxChoices = [ u"Proportional to overlap", u"Assume homogenous connectivity" ]
		self.demo_rescale_edgeRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Rescaling edge handling", wx.DefaultPosition, wx.DefaultSize, demo_rescale_edgeRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.demo_rescale_edgeRadioBox.SetSelection( 0 )
		demo_rescale_sizer.Add( self.demo_rescale_edgeRadioBox, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		demoMainSizer.Add( demo_rescale_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		demo_cu_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.demo_CU_def = wx.StaticText( self.demographic, wx.ID_ANY, u"If the connectivity data was collected at a scale different than that of the planning units, you will need to supply a Connectivity Matrix Shapefile which describes the spatial polygons for which the data was gathered.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_CU_def.Wrap( -1 )
		self.demo_CU_def.Enable( False )
		
		demo_cu_def_sizer.Add( self.demo_CU_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( demo_cu_def_sizer, 1, wx.EXPAND, 5 )
		
		demo_cu_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		demo_cu_file_sizer.AddGrowableCol( 1 )
		demo_cu_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		demo_cu_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.demo_CU_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Connectivity Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_CU_filetext.Wrap( -1 )
		self.demo_CU_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
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
		
		self.demo_pucm_seperator = wx.StaticLine( self.demographic, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		demo_pucm_output_txt_sizer.Add( self.demo_pucm_seperator, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.demo_PU_CM_outputtext = wx.StaticText( self.demographic, wx.ID_ANY, u"Output:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_PU_CM_outputtext.Wrap( -1 )
		self.demo_PU_CM_outputtext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		self.demo_PU_CM_outputtext.Enable( False )
		
		demo_pucm_output_txt_sizer.Add( self.demo_PU_CM_outputtext, 0, wx.ALL, 5 )
		
		
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
		self.demo_PU_CM_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
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
		self.landscape.SetToolTip( u"Choosing a different category will not erase any input and input from multiple categories can be used simultaneously in the analyses in the next steps" )
		
		landMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		landMainSizer.AddGrowableCol( 0 )
		landMainSizer.AddGrowableRow( 0 )
		landMainSizer.AddGrowableRow( 3 )
		landMainSizer.AddGrowableRow( 5 )
		landMainSizer.AddGrowableRow( 8 )
		landMainSizer.SetFlexibleDirection( wx.VERTICAL )
		landMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		land_cm_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.land_CM_def = wx.StaticText( self.landscape, wx.ID_ANY, u"The connectivity matrix (or list) is the ultimate input format for landscape data, but there are multiple input types that can be used to calculate connectivity matrices. Users can 1) upload a connectivity matrix directly, 2) upload a resistance surface that can be used to calculate the connectivity matrix via least-cost path analysis, or 3) upload a habitat type shapefile and a resistance matrix, which can used to generate a resistance surface that can be used to calculate the connectivity matrix via least-cost path analysis. Please indicate your connectivity data type in the box below, and fill in the available filenames.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_CM_def.Wrap( -1 )
		land_cm_def_sizer.Add( self.land_CM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		landMainSizer.Add( land_cm_def_sizer, 1, wx.EXPAND, 5 )
		
		land_radio_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		land_radio_sizer.AddGrowableCol( 1 )
		land_radio_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_radio_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		land_matrixTypeRadioBoxChoices = [ u"Habitat Type + Resistance", u"Resistance Surface", u"Connectivity Matrix" ]
		self.land_matrixTypeRadioBox = wx.RadioBox( self.landscape, wx.ID_ANY, u"Landscape Input Type", wx.DefaultPosition, wx.DefaultSize, land_matrixTypeRadioBoxChoices, 3, wx.RA_SPECIFY_COLS )
		self.land_matrixTypeRadioBox.SetSelection( 0 )
		land_radio_sizer.Add( self.land_matrixTypeRadioBox, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		landMainSizer.Add( land_radio_sizer, 1, wx.ALIGN_CENTER, 5 )
		
		land_cu_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		land_cu_file_sizer.AddGrowableCol( 1 )
		land_cu_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_cu_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.land_HAB_filetext = wx.StaticText( self.landscape, wx.ID_ANY, u"Habitat Type Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_filetext.Wrap( -1 )
		self.land_HAB_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		land_cu_file_sizer.Add( self.land_HAB_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.land_HAB_file = wx.FilePickerCtrl( self.landscape, wx.ID_ANY, wx.EmptyString, u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		land_cu_file_sizer.Add( self.land_HAB_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		self.land_HAB_file_hab_id_txt = wx.StaticText( self.landscape, wx.ID_ANY, u"Habitat ID Column Label", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_file_hab_id_txt.Wrap( -1 )
		self.land_HAB_file_hab_id_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		land_cu_file_sizer.Add( self.land_HAB_file_hab_id_txt, 0, wx.ALL, 5 )
		
		land_HAB_file_hab_idChoices = []
		self.land_HAB_file_hab_id = wx.Choice( self.landscape, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, land_HAB_file_hab_idChoices, 0 )
		self.land_HAB_file_hab_id.SetSelection( 0 )
		land_cu_file_sizer.Add( self.land_HAB_file_hab_id, 0, wx.ALL, 5 )
		
		self.land_HAB_buff_txt = wx.StaticText( self.landscape, wx.ID_ANY, u"Habitat Connectivity Buffer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_HAB_buff_txt.Wrap( -1 )
		self.land_HAB_buff_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		land_cu_file_sizer.Add( self.land_HAB_buff_txt, 0, wx.ALL, 5 )
		
		self.land_HAB_buff = wx.TextCtrl( self.landscape, wx.ID_ANY, u"0.01", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cu_file_sizer.Add( self.land_HAB_buff, 0, wx.ALL, 5 )
		
		
		landMainSizer.Add( land_cu_file_sizer, 1, wx.EXPAND, 5 )
		
		land_cu_cm_file_sizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		land_cu_cm_file_sizer2.AddGrowableCol( 1 )
		land_cu_cm_file_sizer2.SetFlexibleDirection( wx.HORIZONTAL )
		land_cu_cm_file_sizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.land_RES_mat_filetext = wx.StaticText( self.landscape, wx.ID_ANY, u"Resistance Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_RES_mat_filetext.Wrap( -1 )
		self.land_RES_mat_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		land_cu_cm_file_sizer2.Add( self.land_RES_mat_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.land_RES_mat_file = wx.FilePickerCtrl( self.landscape, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		land_cu_cm_file_sizer2.Add( self.land_RES_mat_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		self.resistance_mat_customize = wx.Button( self.landscape, wx.ID_ANY, u"Customize", wx.DefaultPosition, wx.DefaultSize, 0 )
		land_cu_cm_file_sizer2.Add( self.resistance_mat_customize, 0, wx.ALL, 5 )
		
		
		landMainSizer.Add( land_cu_cm_file_sizer2, 1, wx.EXPAND, 5 )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline16 = wx.StaticLine( self.landscape, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer54.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		landMainSizer.Add( bSizer54, 1, wx.EXPAND, 5 )
		
		land_res_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.land_RES_def = wx.StaticText( self.landscape, wx.ID_ANY, u"Resistance surface shapefile description, is shapefile the best format for this (I don't think so). Think about integration with circuitscape output to use cicuit theory instead of least-cost path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_RES_def.Wrap( -1 )
		land_res_def_sizer.Add( self.land_RES_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		landMainSizer.Add( land_res_def_sizer, 1, wx.EXPAND, 5 )
		
		land_res_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		land_res_file_sizer.AddGrowableCol( 1 )
		land_res_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		land_res_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.land_RES_filetext = wx.StaticText( self.landscape, wx.ID_ANY, u"Resistance Surface Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_RES_filetext.Wrap( -1 )
		self.land_RES_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		land_res_file_sizer.Add( self.land_RES_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.land_RES_file = wx.FilePickerCtrl( self.landscape, wx.ID_ANY, wx.EmptyString, u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		land_res_file_sizer.Add( self.land_RES_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		self.land_res_file_res_id_txt = wx.StaticText( self.landscape, wx.ID_ANY, u"Resistance Column Label", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_res_file_res_id_txt.Wrap( -1 )
		self.land_res_file_res_id_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		land_res_file_sizer.Add( self.land_res_file_res_id_txt, 0, wx.ALL, 5 )
		
		land_RES_file_res_idChoices = []
		self.land_RES_file_res_id = wx.Choice( self.landscape, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, land_RES_file_res_idChoices, 0 )
		self.land_RES_file_res_id.SetSelection( 0 )
		land_res_file_sizer.Add( self.land_RES_file_res_id, 0, wx.ALL, 5 )
		
		
		landMainSizer.Add( land_res_file_sizer, 1, wx.EXPAND, 5 )
		
		land_pucm_output_txt_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.land_pucm_seperator = wx.StaticLine( self.landscape, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		land_pucm_output_txt_sizer.Add( self.land_pucm_seperator, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		landMainSizer.Add( land_pucm_output_txt_sizer, 1, wx.EXPAND, 5 )
		
		land_pucm_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.land_PU_CM_def = wx.StaticText( self.landscape, wx.ID_ANY, u"The Planning Unit Connectivity Matrix is either the only user input for the landscape category, or the output of the least-cost path analysis. It will be used to calcuate the Connectivity Metrics for the planning units.", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		self.land_PU_CM_filetext = wx.StaticText( self.landscape, wx.ID_ANY, u"Landscape Connectivity Matrix:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_PU_CM_filetext.Wrap( -1 )
		self.land_PU_CM_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
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
		
		
		self.connectivityInput.SetSizer( conn_input_mainsizer )
		self.connectivityInput.Layout()
		conn_input_mainsizer.Fit( self.connectivityInput )
		self.auinotebook.AddPage( self.connectivityInput, u"2) Connectivity Input", False, wx.NullBitmap )
		self.connectivityMetrics = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		metricsMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		metricsMainSizer.AddGrowableCol( 0 )
		metricsMainSizer.AddGrowableRow( 1 )
		metricsMainSizer.AddGrowableRow( 4 )
		metricsMainSizer.SetFlexibleDirection( wx.BOTH )
		metricsMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cf_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Conservation Features", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_txt.Wrap( -1 )
		self.cf_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		metricsMainSizer.Add( self.cf_txt, 0, wx.ALL, 5 )
		
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
		
		self.cf_demo_vertex_degree = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Vertex Degree", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_vertex_degree.SetToolTip( u"The vertex degree indicates the number of connections for each planning unit" )
		
		demo_cf_sizer.Add( self.cf_demo_vertex_degree, 0, wx.ALL, 5 )
		
		self.cf_demo_between_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Betweenness Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_between_cent.SetToolTip( u"Betweenness Centrality is an indicator of a planning unit's centrality in a network. It is equal to the number of shortest paths from all connections to all others that pass through that planning unit." )
		
		demo_cf_sizer.Add( self.cf_demo_between_cent, 0, wx.ALL, 5 )
		
		self.cf_demo_eig_vect_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Eigen Vector Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_eig_vect_cent.SetToolTip( u"Eigen Vector Centrality is a measure of the influence of a planning unit in a network. It assigns relative scores to all planning unitin the network based on the concept that connections to high-scoring planning unit contribute more to the score of the planning unit in question than equal connections to low-scoring nodes" )
		
		demo_cf_sizer.Add( self.cf_demo_eig_vect_cent, 0, wx.ALL, 5 )
		
		self.cf_demo_self_recruit = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Self Recruitment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_self_recruit.SetToolTip( u"Self Recruitment is the proportion of new recruits from a planning unit that will stay in that planning unit." )
		
		demo_cf_sizer.Add( self.cf_demo_self_recruit, 0, wx.ALL, 5 )
		
		self.cf_demo_import_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_demo_import_panel.SetToolTip( u"Import optimizes for areas which receive higher numbers of immigrants. This is only available if the units of the connectivity matrix is \"Individuals\". " )
		
		cf_demo_import_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_demo_import = wx.CheckBox( self.cf_demo_import_panel, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_import.SetToolTip( u"Import optimizes for areas which receive higher numbers of immigrants. This is only available if the units of the connectivity matrix is \"Individuals\". " )
		
		cf_demo_import_sizer.Add( self.cf_demo_import, 0, wx.ALL, 5 )
		
		
		self.cf_demo_import_panel.SetSizer( cf_demo_import_sizer )
		self.cf_demo_import_panel.Layout()
		cf_demo_import_sizer.Fit( self.cf_demo_import_panel )
		demo_cf_sizer.Add( self.cf_demo_import_panel, 1, 0, 5 )
		
		self.cf_demo_outflux_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_demo_outflux_panel.SetToolTip( u"Outflux optimizes for 'productive' areas. It gives a higher value to planning units from which greater numbers of individuals originate. This is only available if the units of the connectivity matrix is \"Individuals\". " )
		
		cf_demo_outflux_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_demo_outflux = wx.CheckBox( self.cf_demo_outflux_panel, wx.ID_ANY, u"Outflux", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_outflux.SetToolTip( u"Outflux optimizes for 'productive' areas. It gives a higher value to planning units from which greater numbers of individuals originate. This is only available if the units of the connectivity matrix is \"Individuals\". " )
		
		cf_demo_outflux_sizer.Add( self.cf_demo_outflux, 0, wx.ALL, 5 )
		
		
		self.cf_demo_outflux_panel.SetSizer( cf_demo_outflux_sizer )
		self.cf_demo_outflux_panel.Layout()
		cf_demo_outflux_sizer.Fit( self.cf_demo_outflux_panel )
		demo_cf_sizer.Add( self.cf_demo_outflux_panel, 1, 0, 5 )
		
		self.cf_demo_stochasticity_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_demo_stochasticity_panel.SetToolTip( u"Uses spatial and temporal stochasticity in connectivity to identify planning units that increase metapopulation growth and stability. It is only available if a connectivity 'List with Time' was provided under Demographic Input in the Connectivity Input tab as well as a focus area shapefile under the Spatial Input tab." )
		
		cf_demo_stochasticity_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_demo_stochasticity = wx.CheckBox( self.cf_demo_stochasticity_panel, wx.ID_ANY, u"Temporal Connectivity Covariance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_stochasticity.Enable( False )
		self.cf_demo_stochasticity.SetToolTip( u"Uses spatial and temporal stochasticity in connectivity to identify planning units that increase metapopulation growth and stability. It is only available if a connectivity 'List with Time' was provided under Demographic Input in the Connectivity Input tab as well as a focus area shapefile under the Spatial Input tab." )
		
		cf_demo_stochasticity_sizer.Add( self.cf_demo_stochasticity, 0, wx.ALL, 5 )
		
		
		self.cf_demo_stochasticity_panel.SetSizer( cf_demo_stochasticity_sizer )
		self.cf_demo_stochasticity_panel.Layout()
		cf_demo_stochasticity_sizer.Fit( self.cf_demo_stochasticity_panel )
		demo_cf_sizer.Add( self.cf_demo_stochasticity_panel, 1, 0, 0 )
		
		self.cf_demo_fa_recipients_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_demo_fa_recipients_panel.SetToolTip( u"Finds the planning units to which organisms will disperse from the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_demo_fa_recipients_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_demo_fa_recipients = wx.CheckBox( self.cf_demo_fa_recipients_panel, wx.ID_ANY, u"Focus Area Recipients", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_fa_recipients.Enable( False )
		self.cf_demo_fa_recipients.SetToolTip( u"Finds the planning units to which organisms will disperse from the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_demo_fa_recipients_sizer.Add( self.cf_demo_fa_recipients, 0, wx.ALL, 5 )
		
		
		self.cf_demo_fa_recipients_panel.SetSizer( cf_demo_fa_recipients_sizer )
		self.cf_demo_fa_recipients_panel.Layout()
		cf_demo_fa_recipients_sizer.Fit( self.cf_demo_fa_recipients_panel )
		demo_cf_sizer.Add( self.cf_demo_fa_recipients_panel, 1, 0, 0 )
		
		self.cf_demo_fa_donors_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_demo_fa_donors_panel.SetToolTip( u"Finds the planning units from which organisms will originate for the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_demo_fa_donors_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_demo_fa_donors = wx.CheckBox( self.cf_demo_fa_donors_panel, wx.ID_ANY, u"Focus Area Donors", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_fa_donors.Enable( False )
		self.cf_demo_fa_donors.SetToolTip( u"Finds the planning units from which organisms will originate for the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_demo_fa_donors_sizer.Add( self.cf_demo_fa_donors, 0, wx.ALL, 5 )
		
		
		self.cf_demo_fa_donors_panel.SetSizer( cf_demo_fa_donors_sizer )
		self.cf_demo_fa_donors_panel.Layout()
		cf_demo_fa_donors_sizer.Fit( self.cf_demo_fa_donors_panel )
		demo_cf_sizer.Add( self.cf_demo_fa_donors_panel, 1, 0, 0 )
		
		self.cf_demo_aa_recipients_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_demo_aa_recipients_panel.SetToolTip( u"Finds the planning units to which organisms will disperse from the avoidance areas. It is only available if a avoidance area shapefile was provided under the Spatial Input tab. Returns the inverse of the score since it is assumed connectivity is to be minimized" )
		
		cf_demo_aa_recipients_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_demo_aa_recipients = wx.CheckBox( self.cf_demo_aa_recipients_panel, wx.ID_ANY, u"Avoidance Area Recipients", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_aa_recipients.Enable( False )
		self.cf_demo_aa_recipients.SetToolTip( u"Finds the planning units to which organisms will disperse from the avoidance areas. It is only available if a avoidance area shapefile was provided under the Spatial Input tab. Returns the inverse of the score since it is assumed connectivity is to be minimized" )
		
		cf_demo_aa_recipients_sizer.Add( self.cf_demo_aa_recipients, 0, wx.ALL, 5 )
		
		
		self.cf_demo_aa_recipients_panel.SetSizer( cf_demo_aa_recipients_sizer )
		self.cf_demo_aa_recipients_panel.Layout()
		cf_demo_aa_recipients_sizer.Fit( self.cf_demo_aa_recipients_panel )
		demo_cf_sizer.Add( self.cf_demo_aa_recipients_panel, 1, 0, 0 )
		
		self.cf_demo_aa_donors_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_demo_aa_donors_panel.SetToolTip( u"Finds the planning units from which organisms will originate for the avoidance areas. It is only available if a avoidance area shapefile was provided under the Spatial Input tab.  Returns the inverse of the score since it is assumed connectivity is to be minimized" )
		
		cf_demo_aa_donors_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_demo_aa_donors = wx.CheckBox( self.cf_demo_aa_donors_panel, wx.ID_ANY, u"Avoidance Area Donors", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_aa_donors.Enable( False )
		self.cf_demo_aa_donors.SetToolTip( u"Finds the planning units from which organisms will originate for the avoidance areas. It is only available if a avoidance area shapefile was provided under the Spatial Input tab. Returns the inverse of the score since it is assumed connectivity is to be minimized" )
		
		cf_demo_aa_donors_sizer.Add( self.cf_demo_aa_donors, 0, wx.ALL, 5 )
		
		
		self.cf_demo_aa_donors_panel.SetSizer( cf_demo_aa_donors_sizer )
		self.cf_demo_aa_donors_panel.Layout()
		cf_demo_aa_donors_sizer.Fit( self.cf_demo_aa_donors_panel )
		demo_cf_sizer.Add( self.cf_demo_aa_donors_panel, 1, 0, 0 )
		
		
		cf_sizer.Add( demo_cf_sizer, 1, wx.EXPAND, 5 )
		
		land_cf_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.land_cf_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_cf_txt.Wrap( -1 )
		self.land_cf_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		land_cf_sizer.Add( self.land_cf_txt, 0, wx.ALL, 5 )
		
		self.cf_land_vertex_degree = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Vertex Degree", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_vertex_degree.Enable( False )
		self.cf_land_vertex_degree.SetToolTip( u"The vertex degree indicates the number of connections for each planning unit" )
		
		land_cf_sizer.Add( self.cf_land_vertex_degree, 0, wx.ALL, 5 )
		
		self.cf_land_between_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Betweenness Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_between_cent.Enable( False )
		self.cf_land_between_cent.SetToolTip( u"Betweenness Centrality is an indicator of a planning unit's centrality in a network. It is equal to the number of shortest paths from all connections to all others that pass through that planning unit." )
		
		land_cf_sizer.Add( self.cf_land_between_cent, 0, wx.ALL, 5 )
		
		self.cf_land_eig_vect_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Eigen Vector Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_eig_vect_cent.Enable( False )
		self.cf_land_eig_vect_cent.SetToolTip( u"Eigen Vector Centrality is a measure of the influence of a planning unit in a network. It assigns relative scores to all planning unitin the network based on the concept that connections to high-scoring planning unit contribute more to the score of the planning unit in question than equal connections to low-scoring nodes" )
		
		land_cf_sizer.Add( self.cf_land_eig_vect_cent, 0, wx.ALL, 5 )
		
		self.cf_land_self_recruit = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Self Recruitment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_self_recruit.SetValue(True) 
		self.cf_land_self_recruit.Hide()
		self.cf_land_self_recruit.SetToolTip( u"Self Recruitment is the propotion of new recruits from a planning unit that will stay in that planning unit." )
		
		land_cf_sizer.Add( self.cf_land_self_recruit, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )
		
		self.cf_land_import_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_land_import_panel.Hide()
		self.cf_land_import_panel.SetToolTip( u"Import optimizes for areas which receive higher numbers of immigrants. This is only available if the units of the connectivity matrix is \"Individuals\". " )
		
		cf_land_import_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_land_import = wx.CheckBox( self.cf_land_import_panel, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_import.SetToolTip( u"Import optimizes for areas which receive higher numbers of immigrants. This is only available if the units of the connectivity matrix is \"Individuals\". " )
		
		cf_land_import_sizer.Add( self.cf_land_import, 0, wx.ALL, 5 )
		
		
		self.cf_land_import_panel.SetSizer( cf_land_import_sizer )
		self.cf_land_import_panel.Layout()
		cf_land_import_sizer.Fit( self.cf_land_import_panel )
		land_cf_sizer.Add( self.cf_land_import_panel, 1, wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )
		
		self.cf_land_outflux = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Outflux", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_outflux.SetValue(True) 
		self.cf_land_outflux.Hide()
		self.cf_land_outflux.SetToolTip( u"Self Recruitment is the propotion of new recruits from a planning unit that will stay in that planning unit." )
		
		land_cf_sizer.Add( self.cf_land_outflux, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )
		
		self.cf_land_stochasticity_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_land_stochasticity_panel.Hide()
		self.cf_land_stochasticity_panel.SetToolTip( u"Finds the planning units to which organisms will disperse from the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_land_stochasticity_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_land_stochasticity = wx.CheckBox( self.cf_land_stochasticity_panel, wx.ID_ANY, u"Temporal Connectivity Covariance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_stochasticity.Enable( False )
		
		cf_land_stochasticity_sizer.Add( self.cf_land_stochasticity, 0, wx.ALL, 5 )
		
		
		self.cf_land_stochasticity_panel.SetSizer( cf_land_stochasticity_sizer )
		self.cf_land_stochasticity_panel.Layout()
		cf_land_stochasticity_sizer.Fit( self.cf_land_stochasticity_panel )
		land_cf_sizer.Add( self.cf_land_stochasticity_panel, 1, wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 0 )
		
		self.cf_land_fa_recipients_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_land_fa_recipients_panel.SetToolTip( u"Finds the planning units to which organisms will disperse to from the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_land_fa_recipients_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_land_fa_recipients = wx.CheckBox( self.cf_land_fa_recipients_panel, wx.ID_ANY, u"Focus Area Recipients", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_fa_recipients.Enable( False )
		self.cf_land_fa_recipients.SetToolTip( u"Finds the planning units to which organisms will disperse from the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_land_fa_recipients_sizer.Add( self.cf_land_fa_recipients, 0, wx.ALL, 5 )
		
		
		self.cf_land_fa_recipients_panel.SetSizer( cf_land_fa_recipients_sizer )
		self.cf_land_fa_recipients_panel.Layout()
		cf_land_fa_recipients_sizer.Fit( self.cf_land_fa_recipients_panel )
		land_cf_sizer.Add( self.cf_land_fa_recipients_panel, 1, 0, 0 )
		
		self.cf_land_fa_donors_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_land_fa_donors_panel.SetToolTip( u"Finds the planning units from which organisms will originate for the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_land_fa_donors_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_land_fa_donors = wx.CheckBox( self.cf_land_fa_donors_panel, wx.ID_ANY, u"Focus Area Donors", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_fa_donors.Enable( False )
		self.cf_land_fa_donors.SetToolTip( u"Finds the planning units from which organisms will originate for the focus areas. It is only available if a focus area shapefile was provided under the Spatial Input tab." )
		
		cf_land_fa_donors_sizer.Add( self.cf_land_fa_donors, 0, wx.ALL, 5 )
		
		
		self.cf_land_fa_donors_panel.SetSizer( cf_land_fa_donors_sizer )
		self.cf_land_fa_donors_panel.Layout()
		cf_land_fa_donors_sizer.Fit( self.cf_land_fa_donors_panel )
		land_cf_sizer.Add( self.cf_land_fa_donors_panel, 1, 0, 0 )
		
		self.cf_land_aa_recipients_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_land_aa_recipients_panel.SetToolTip( u"Finds the planning units to which organisms will disperse from the avoidance areas. It is only available if a avoidance area shapefile was provided under the Spatial Input tab. Returns the inverse of the score since it is assumed connectivity is to be minimized" )
		
		cf_land_aa_recipients_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_land_aa_recipients = wx.CheckBox( self.cf_land_aa_recipients_panel, wx.ID_ANY, u"Avoidance Area Recipients", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_aa_recipients.Enable( False )
		self.cf_land_aa_recipients.SetToolTip( u"Finds the planning units to which organisms will disperse from the avoidance areas. It is only available if a avoidance area shapefile was provided under the Spatial Input tab. Returns the inverse of the score since it is assumed connectivity is to be minimized" )
		
		cf_land_aa_recipients_sizer.Add( self.cf_land_aa_recipients, 0, wx.ALL, 5 )
		
		
		self.cf_land_aa_recipients_panel.SetSizer( cf_land_aa_recipients_sizer )
		self.cf_land_aa_recipients_panel.Layout()
		cf_land_aa_recipients_sizer.Fit( self.cf_land_aa_recipients_panel )
		land_cf_sizer.Add( self.cf_land_aa_recipients_panel, 1, 0, 0 )
		
		self.cf_land_aa_donors_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_land_aa_donors_panel.SetToolTip( u"Finds the planning units from which organisms will originate for the avoidance areas. It is only available if a avoidance area shapefile was provided under the Spatial Input tab. Returns the inverse of the score since it is assumed connectivity is to be minimized" )
		
		cf_land_aa_donors_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_land_aa_donors = wx.CheckBox( self.cf_land_aa_donors_panel, wx.ID_ANY, u"Avoidance Area Donors", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_land_aa_donors.Enable( False )
		self.cf_land_aa_donors.SetToolTip( u"Finds the planning units from which organisms will originate for the avoidance areas. It is only available if a avoidance area shapefile was provided under the Spatial Input tab. Returns the inverse of the score since it is assumed connectivity is to be minimized" )
		
		cf_land_aa_donors_sizer.Add( self.cf_land_aa_donors, 0, wx.ALL, 5 )
		
		
		self.cf_land_aa_donors_panel.SetSizer( cf_land_aa_donors_sizer )
		self.cf_land_aa_donors_panel.Layout()
		cf_land_aa_donors_sizer.Fit( self.cf_land_aa_donors_panel )
		land_cf_sizer.Add( self.cf_land_aa_donors_panel, 1, 0, 0 )
		
		
		cf_sizer.Add( land_cf_sizer, 1, wx.EXPAND, 5 )
		
		
		metricsMainSizer.Add( cf_sizer, 1, wx.EXPAND, 5 )
		
		self.metrics_seperator = wx.StaticLine( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		metricsMainSizer.Add( self.metrics_seperator, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.bd_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Boundary Definition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_txt.Wrap( -1 )
		self.bd_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		metricsMainSizer.Add( self.bd_txt, 0, wx.ALL, 5 )
		
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
		
		self.bd_demo_conn_boundary = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Connectivity as boundary", wx.DefaultPosition, wx.DefaultSize, 0 )
		demo_bd_sizer.Add( self.bd_demo_conn_boundary, 0, wx.ALL, 5 )
		
		self.bd_demo_min_plan_graph = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Minimum Planar Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_demo_min_plan_graph.SetValue(True) 
		demo_bd_sizer.Add( self.bd_demo_min_plan_graph, 0, wx.ALL, 5 )
		
		
		bd_sizer.Add( demo_bd_sizer, 1, wx.EXPAND, 5 )
		
		land_bd_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.land_bd_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_bd_txt.Wrap( -1 )
		self.land_bd_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		land_bd_sizer.Add( self.land_bd_txt, 0, wx.ALL, 5 )
		
		self.bd_land_conn_boundary = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Connectivity as boundary", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_land_conn_boundary.Enable( False )
		
		land_bd_sizer.Add( self.bd_land_conn_boundary, 0, wx.ALL, 5 )
		
		self.bd_land_min_plan_graph = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Minimum Planar Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_land_min_plan_graph.Enable( False )
		
		land_bd_sizer.Add( self.bd_land_min_plan_graph, 0, wx.ALL, 5 )
		
		
		bd_sizer.Add( land_bd_sizer, 1, wx.EXPAND, 5 )
		
		
		metricsMainSizer.Add( bd_sizer, 1, wx.EXPAND, 5 )
		
		metrics_buttons_sizer = wx.FlexGridSizer( 0, 6, 0, 0 )
		metrics_buttons_sizer.AddGrowableCol( 0 )
		metrics_buttons_sizer.SetFlexibleDirection( wx.BOTH )
		metrics_buttons_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.spacertext = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertext.Wrap( -1 )
		metrics_buttons_sizer.Add( self.spacertext, 0, wx.ALL, 5 )
		
		self.calc_metrics = wx.Button( self.connectivityMetrics, wx.ID_ANY, u"Calculate Metrics", wx.DefaultPosition, wx.DefaultSize, 0 )
		metrics_buttons_sizer.Add( self.calc_metrics, 0, wx.ALL, 5 )
		
		self.metrics_for_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"For:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metrics_for_txt.Wrap( -1 )
		metrics_buttons_sizer.Add( self.metrics_for_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.calc_metrics_pu = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Planning Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.calc_metrics_pu.SetValue(True) 
		metrics_buttons_sizer.Add( self.calc_metrics_pu, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.calc_metrics_cu = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Connectivity Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.calc_metrics_cu.SetToolTip( u"Calculating Connectivity Metrics is for plotting purposes only. These metrics will not be exported or appended to the Marxan input files." )
		
		metrics_buttons_sizer.Add( self.calc_metrics_cu, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		metricsMainSizer.Add( metrics_buttons_sizer, 1, wx.EXPAND, 5 )
		
		
		self.connectivityMetrics.SetSizer( metricsMainSizer )
		self.connectivityMetrics.Layout()
		metricsMainSizer.Fit( self.connectivityMetrics )
		self.auinotebook.AddPage( self.connectivityMetrics, u"3) Connectivity Metrics", True, wx.NullBitmap )
		self.preEvaluation = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		preEvalMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		preEvalMainSizer.AddGrowableCol( 0 )
		preEvalMainSizer.AddGrowableRow( 0 )
		preEvalMainSizer.AddGrowableRow( 2 )
		preEvalMainSizer.SetFlexibleDirection( wx.BOTH )
		preEvalMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		preEval_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.preEval_def_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"This tab will allow you to evaluate the metrics created on the previous tab. They can be removed if they are not appropriate for the Marxan analysis, transformed into discrete features which can be locked in or out. Most importantly, everything can be exported as Marxan formatted files.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_def_txt.Wrap( -1 )
		preEval_def_sizer.Add( self.preEval_def_txt, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		preEvalMainSizer.Add( preEval_def_sizer, 1, wx.EXPAND, 5 )
		
		preEval_choice_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.preEval_choice_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Choose Available Connectivity Metric to Discretize:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_choice_txt.Wrap( -1 )
		self.preEval_choice_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		preEval_choice_sizer.Add( self.preEval_choice_txt, 0, wx.ALL, 5 )
		
		preEval_metrics_opt_sizer = wx.FlexGridSizer( 2, 3, 0, 0 )
		preEval_metrics_opt_sizer.AddGrowableCol( 1 )
		preEval_metrics_opt_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_metrics_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.preEval_metric_shp_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_metric_shp_txt.Wrap( -1 )
		preEval_metrics_opt_sizer.Add( self.preEval_metric_shp_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
		self.preEval_metric_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_metric_txt.Wrap( -1 )
		preEval_metrics_opt_sizer.Add( self.preEval_metric_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
		self.preEval_metric_spacertxt = wx.StaticText( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_metric_spacertxt.Wrap( -1 )
		preEval_metrics_opt_sizer.Add( self.preEval_metric_spacertxt, 0, wx.ALL, 5 )
		
		preEval_metric_shp_choiceChoices = [ u"Planning Units (Demographic Data)", u"Planning Units (Landscape Data)" ]
		self.preEval_metric_shp_choice = wx.Choice( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, preEval_metric_shp_choiceChoices, 0 )
		self.preEval_metric_shp_choice.SetSelection( 0 )
		preEval_metrics_opt_sizer.Add( self.preEval_metric_shp_choice, 0, wx.ALL, 5 )
		
		preEval_metric_choiceChoices = [ u"Selection Frequency", u"Best Solution", u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment", u"Outflux", u"Temporal Connectivity Covariance", u"Focus Area Sink", u"Focus Area Source", u"Avoidance Area Sink", u"Avoidance Area Source" ]
		self.preEval_metric_choice = wx.Choice( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, preEval_metric_choiceChoices, 0 )
		self.preEval_metric_choice.SetSelection( 0 )
		preEval_metrics_opt_sizer.Add( self.preEval_metric_choice, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button18 = wx.Button( self.preEvaluation, wx.ID_ANY, u"Remove Selected Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_metrics_opt_sizer.Add( self.m_button18, 0, wx.ALL, 4 )
		
		
		preEval_choice_sizer.Add( preEval_metrics_opt_sizer, 1, wx.EXPAND, 5 )
		
		
		preEvalMainSizer.Add( preEval_choice_sizer, 1, wx.EXPAND, 5 )
		
		preEval_table_discrete_sizer = wx.FlexGridSizer( 1, 4, 0, 0 )
		preEval_table_discrete_sizer.AddGrowableCol( 1 )
		preEval_table_discrete_sizer.AddGrowableCol( 2 )
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
		
		preEval_table_sizer.Add( self.preEval_table_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
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
		self.preEval_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
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
		self.preEval_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.preEval_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		preEval_table_sizer.Add( self.preEval_grid, 0, wx.ALL, 5 )
		
		
		preEval_table_discrete_sizer.Add( preEval_table_sizer, 1, wx.EXPAND, 5 )
		
		preEval_discrete_from_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		preEval_discrete_from_sizer.AddGrowableCol( 0 )
		preEval_discrete_from_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_from_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.preEval_discrete_from_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Make discrete feature from:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_discrete_from_txt.Wrap( -1 )
		self.preEval_discrete_from_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		preEval_discrete_from_sizer.Add( self.preEval_discrete_from_txt, 0, wx.ALL, 5 )
		
		preEval_discrete_from_quartile_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		preEval_discrete_from_quartile_sizer.AddGrowableCol( 1 )
		preEval_discrete_from_quartile_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_from_quartile_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.preEval_discrete_from_quartile = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Quartile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_discrete_from_quartile.SetValue(True) 
		preEval_discrete_from_quartile_sizer.Add( self.preEval_discrete_from_quartile, 0, wx.ALL, 5 )
		
		preEval_discrete_from_quartile_radioChoices = [ u"Minimum", u"Lower Quartile", u"Median", u"Upper Quartile", u"Maximum" ]
		self.preEval_discrete_from_quartile_radio = wx.RadioBox( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, preEval_discrete_from_quartile_radioChoices, 1, wx.RA_SPECIFY_COLS )
		self.preEval_discrete_from_quartile_radio.SetSelection( 3 )
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
		preEval_discrete_from_value_sizer.Add( self.preEval_discrete_from_value, 0, wx.ALL, 5 )
		
		self.preEval_discrete_from_value_txtctrl = wx.TextCtrl( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_discrete_from_value_sizer.Add( self.preEval_discrete_from_value_txtctrl, 0, wx.ALL, 5 )
		
		
		preEval_discrete_from_sizer.Add( preEval_discrete_from_value_sizer, 1, wx.EXPAND, 5 )
		
		
		preEval_table_discrete_sizer.Add( preEval_discrete_from_sizer, 1, wx.EXPAND, 5 )
		
		preEval_discrete_to_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		preEval_discrete_to_sizer.AddGrowableCol( 0 )
		preEval_discrete_to_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_to_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.preEval_discrete_to_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Make discrete feature to:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_discrete_to_txt.Wrap( -1 )
		self.preEval_discrete_to_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		preEval_discrete_to_sizer.Add( self.preEval_discrete_to_txt, 0, wx.ALL, 5 )
		
		preEval_discrete_to_quartile_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		preEval_discrete_to_quartile_sizer.AddGrowableCol( 1 )
		preEval_discrete_to_quartile_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_discrete_to_quartile_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.preEval_discrete_to_quartile = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Quartile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preEval_discrete_to_quartile.SetValue(True) 
		preEval_discrete_to_quartile_sizer.Add( self.preEval_discrete_to_quartile, 0, wx.ALL, 5 )
		
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
		preEval_discrete_to_value_sizer.Add( self.preEval_discrete_to_value, 0, wx.ALL, 5 )
		
		self.preEval_discrete_to_value_txtctrl = wx.TextCtrl( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_discrete_to_value_sizer.Add( self.preEval_discrete_to_value_txtctrl, 0, wx.ALL, 5 )
		
		
		preEval_discrete_to_sizer.Add( preEval_discrete_to_value_sizer, 1, wx.EXPAND, 5 )
		
		
		preEval_table_discrete_sizer.Add( preEval_discrete_to_sizer, 1, wx.EXPAND, 5 )
		
		
		preEvalMainSizer.Add( preEval_table_discrete_sizer, 1, wx.EXPAND, 5 )
		
		preEval_metrics_buttons_sizer = wx.FlexGridSizer( 0, 6, 0, 0 )
		preEval_metrics_buttons_sizer.AddGrowableCol( 0 )
		preEval_metrics_buttons_sizer.SetFlexibleDirection( wx.BOTH )
		preEval_metrics_buttons_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.spacertext11 = wx.StaticText( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertext11.Wrap( -1 )
		preEval_metrics_buttons_sizer.Add( self.spacertext11, 0, wx.ALL, 5 )
		
		self.preEval_create_new = wx.Button( self.preEvaluation, wx.ID_ANY, u"Create New Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		preEval_metrics_buttons_sizer.Add( self.preEval_create_new, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		preEval_status_radioChoices = [ u"Locked in", u"Locked out", u"Status-quo" ]
		self.preEval_status_radio = wx.RadioBox( self.preEvaluation, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, preEval_status_radioChoices, 3, wx.RA_SPECIFY_COLS )
		self.preEval_status_radio.SetSelection( 2 )
		preEval_metrics_buttons_sizer.Add( self.preEval_status_radio, 0, wx.ALL, 5 )
		
		
		preEvalMainSizer.Add( preEval_metrics_buttons_sizer, 1, wx.EXPAND, 5 )
		
		self.m_staticline8 = wx.StaticLine( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		preEvalMainSizer.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		cf_export_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		cf_export_sizer.AddGrowableCol( 1 )
		cf_export_sizer.SetFlexibleDirection( wx.BOTH )
		cf_export_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		cf_export_radioBoxChoices = [ u"Export", u"Append" ]
		self.cf_export_radioBox = wx.RadioBox( self.preEvaluation, wx.ID_ANY, u"Metrics", wx.DefaultPosition, wx.DefaultSize, cf_export_radioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.cf_export_radioBox.SetSelection( 0 )
		cf_export_sizer.Add( self.cf_export_radioBox, 0, wx.ALL, 5 )
		
		cf_file_export_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		cf_file_export_sizer.AddGrowableCol( 1 )
		cf_file_export_sizer.SetFlexibleDirection( wx.BOTH )
		cf_file_export_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cf_export_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Planning Unit versus Conservation Feature File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_export_txt.Wrap( -1 )
		cf_file_export_sizer.Add( self.cf_export_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CF_file = wx.FilePickerCtrl( self.preEvaluation, wx.ID_ANY, u"~\\puvspr.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		cf_file_export_sizer.Add( self.CF_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.cf_targets_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Conservation Feature Targets:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_targets_txt.Wrap( -1 )
		cf_file_export_sizer.Add( self.cf_targets_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		cft_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		cft_sizer.AddGrowableCol( 1 )
		cft_sizer.SetFlexibleDirection( wx.BOTH )
		cft_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cft_percent_txt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Percent of Feature Targeted:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cft_percent_txt.Wrap( -1 )
		cft_sizer.Add( self.cft_percent_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CFT_percent_slider = wx.Slider( self.preEvaluation, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		self.CFT_percent_slider.Enable( False )
		
		cft_sizer.Add( self.CFT_percent_slider, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.custom_spec_panel = wx.Panel( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.custom_spec_panel.SetToolTip( u"To enable, please calculate  any Conservation Feature metrics" )
		
		custom_spec_panel_sizer = wx.FlexGridSizer( 1, 1, 0, 0 )
		custom_spec_panel_sizer.SetFlexibleDirection( wx.BOTH )
		custom_spec_panel_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.customize_spec = wx.Button( self.custom_spec_panel, wx.ID_ANY, u"Customize Conservation Feature File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.customize_spec.Enable( False )
		
		custom_spec_panel_sizer.Add( self.customize_spec, 0, wx.ALL, 14 )
		
		
		self.custom_spec_panel.SetSizer( custom_spec_panel_sizer )
		self.custom_spec_panel.Layout()
		custom_spec_panel_sizer.Fit( self.custom_spec_panel )
		cft_sizer.Add( self.custom_spec_panel, 1, wx.ALL, 5 )
		
		
		cf_file_export_sizer.Add( cft_sizer, 1, wx.EXPAND, 5 )
		
		self.SPEC_filetxt = wx.StaticText( self.preEvaluation, wx.ID_ANY, u"Conservation Feature File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SPEC_filetxt.Wrap( -1 )
		cf_file_export_sizer.Add( self.SPEC_filetxt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.SPEC_file = wx.FilePickerCtrl( self.preEvaluation, wx.ID_ANY, u"~\\spec.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		cf_file_export_sizer.Add( self.SPEC_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		cf_export_sizer.Add( cf_file_export_sizer, 1, wx.EXPAND, 5 )
		
		
		preEvalMainSizer.Add( cf_export_sizer, 1, wx.EXPAND, 5 )
		
		self.m_staticline81 = wx.StaticLine( self.preEvaluation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		preEvalMainSizer.Add( self.m_staticline81, 0, wx.EXPAND |wx.ALL, 5 )
		
		bd_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		bd_file_sizer.AddGrowableCol( 1 )
		bd_file_sizer.SetFlexibleDirection( wx.BOTH )
		bd_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.BD_filecheck = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Export Boundary Definition to: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BD_filecheck.SetValue(True) 
		bd_file_sizer.Add( self.BD_filecheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.BD_file = wx.FilePickerCtrl( self.preEvaluation, wx.ID_ANY, u"~\\bound.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		bd_file_sizer.Add( self.BD_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		preEvalMainSizer.Add( bd_file_sizer, 1, wx.EXPAND, 5 )
		
		pudat_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		pudat_file_sizer.AddGrowableCol( 1 )
		pudat_file_sizer.SetFlexibleDirection( wx.BOTH )
		pudat_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.PUDAT_filecheck = wx.CheckBox( self.preEvaluation, wx.ID_ANY, u"Export Planning Unit File to: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUDAT_filecheck.SetValue(True) 
		pudat_file_sizer.Add( self.PUDAT_filecheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.PUDAT_file = wx.FilePickerCtrl( self.preEvaluation, wx.ID_ANY, u"~\\pu.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		pudat_file_sizer.Add( self.PUDAT_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		preEvalMainSizer.Add( pudat_file_sizer, 1, wx.EXPAND, 5 )
		
		metrics_buttons_sizer = wx.FlexGridSizer( 0, 6, 0, 0 )
		metrics_buttons_sizer.AddGrowableCol( 0 )
		metrics_buttons_sizer.SetFlexibleDirection( wx.BOTH )
		metrics_buttons_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.spacertext = wx.StaticText( self.preEvaluation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertext.Wrap( -1 )
		metrics_buttons_sizer.Add( self.spacertext, 0, wx.ALL, 5 )
		
		self.export_metrics = wx.Button( self.preEvaluation, wx.ID_ANY, u"Export Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.export_metrics.Enable( False )
		
		metrics_buttons_sizer.Add( self.export_metrics, 0, wx.ALL, 5 )
		
		
		preEvalMainSizer.Add( metrics_buttons_sizer, 1, wx.EXPAND, 5 )
		
		
		self.preEvaluation.SetSizer( preEvalMainSizer )
		self.preEvaluation.Layout()
		preEvalMainSizer.Fit( self.preEvaluation )
		self.auinotebook.AddPage( self.preEvaluation, u"4) Pre-Evaluation", False, wx.NullBitmap )
		self.marxanAnalysis = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spatialMainSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
		spatialMainSizer1.AddGrowableCol( 0 )
		spatialMainSizer1.AddGrowableRow( 1 )
		spatialMainSizer1.AddGrowableRow( 2 )
		spatialMainSizer1.AddGrowableRow( 3 )
		spatialMainSizer1.AddGrowableRow( 4 )
		spatialMainSizer1.AddGrowableRow( 5 )
		spatialMainSizer1.SetFlexibleDirection( wx.VERTICAL )
		spatialMainSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.marxan_title = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Running Marxan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.marxan_title.Wrap( -1 )
		self.marxan_title.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		spatialMainSizer1.Add( self.marxan_title, 0, wx.ALL, 5 )
		
		marxan_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.marxan_def = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Marxan with Connectivity needs a separate Marxan installation to run the analyses. Please download, unzip, and indicate the directory that contains Marxan below. If properly configured, a command terminal will open to display progress when the \"Run Marxan\" button is pressed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.marxan_def.Wrap( -1 )
		marxan_def_sizer.Add( self.marxan_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		spatialMainSizer1.Add( marxan_def_sizer, 1, wx.EXPAND, 5 )
		
		self.marxanwebsite = wx.adv.HyperlinkCtrl( self.marxanAnalysis, wx.ID_ANY, u"Marxan Website", u"http://marxan.net/index.php/marxan", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		spatialMainSizer1.Add( self.marxanwebsite, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		marxan_dir_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		marxan_dir_sizer.AddGrowableCol( 1 )
		marxan_dir_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		marxan_dir_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.marxan_dirtext = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Marxan Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.marxan_dirtext.Wrap( -1 )
		self.marxan_dirtext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		marxan_dir_sizer.Add( self.marxan_dirtext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.marxan_dir = wx.DirPickerCtrl( self.marxanAnalysis, wx.ID_ANY, u"C:\\Users\\Remi-Work\\Desktop\\Marxan243", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		marxan_dir_sizer.Add( self.marxan_dir, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		spatialMainSizer1.Add( marxan_dir_sizer, 1, wx.EXPAND, 5 )
		
		inputdat_txt_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.inputdat_txt = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Specify the input file (i.e. input.dat) which dictates the number of replicates, the boundary length modifier, etc. Most importantly, the input file specifies which Conservation Feature, Planning unit vs Conservation Feature, and boundary files are used by Marxan. The 'Customize' button will allow you to create or customize the input file using Marxan Inedit.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputdat_txt.Wrap( -1 )
		inputdat_txt_sizer.Add( self.inputdat_txt, 0, wx.ALIGN_BOTTOM|wx.ALL|wx.EXPAND, 5 )
		
		
		spatialMainSizer1.Add( inputdat_txt_sizer, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		inputdat_file_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		inputdat_file_sizer.AddGrowableCol( 1 )
		inputdat_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		inputdat_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.inputdat_filetext = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, u"Marxan Input File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputdat_filetext.Wrap( -1 )
		self.inputdat_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		inputdat_file_sizer.Add( self.inputdat_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inputdat_file = wx.FilePickerCtrl( self.marxanAnalysis, wx.ID_ANY, u"C:\\Users\\Remi-Work\\Desktop\\MarxanConnectGUI\\data\\GBR\\input.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		inputdat_file_sizer.Add( self.inputdat_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		self.customize_inputdat = wx.Button( self.marxanAnalysis, wx.ID_ANY, u"Customize", wx.DefaultPosition, wx.DefaultSize, 0 )
		inputdat_file_sizer.Add( self.customize_inputdat, 0, wx.ALL, 5 )
		
		
		spatialMainSizer1.Add( inputdat_file_sizer, 1, wx.EXPAND, 5 )
		
		run_marxan_sizer = wx.FlexGridSizer( 1, 3, 0, 0 )
		run_marxan_sizer.AddGrowableCol( 0 )
		run_marxan_sizer.SetFlexibleDirection( wx.BOTH )
		run_marxan_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.spacertextrunmarxan = wx.StaticText( self.marxanAnalysis, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertextrunmarxan.Wrap( -1 )
		run_marxan_sizer.Add( self.spacertextrunmarxan, 0, wx.ALL, 5 )
		
		self.run_marxan_button = wx.Button( self.marxanAnalysis, wx.ID_ANY, u"Run Marxan", wx.DefaultPosition, wx.DefaultSize, 0 )
		run_marxan_sizer.Add( self.run_marxan_button, 0, wx.ALL, 5 )
		
		
		spatialMainSizer1.Add( run_marxan_sizer, 1, wx.EXPAND, 5 )
		
		
		self.marxanAnalysis.SetSizer( spatialMainSizer1 )
		self.marxanAnalysis.Layout()
		spatialMainSizer1.Fit( self.marxanAnalysis )
		self.auinotebook.AddPage( self.marxanAnalysis, u"5) Marxan Analysis", False, wx.NullBitmap )
		self.plottingOptions = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		plottingMainSizer = wx.FlexGridSizer( 15, 0, 0, 0 )
		plottingMainSizer.AddGrowableCol( 0 )
		plottingMainSizer.AddGrowableRow( 2 )
		plottingMainSizer.AddGrowableRow( 4 )
		plottingMainSizer.AddGrowableRow( 6 )
		plottingMainSizer.AddGrowableRow( 7 )
		plottingMainSizer.AddGrowableRow( 10 )
		plottingMainSizer.SetFlexibleDirection( wx.BOTH )
		plottingMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.mapoptions_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Map Plotting Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mapoptions_txt.Wrap( -1 )
		self.mapoptions_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		plottingMainSizer.Add( self.mapoptions_txt, 0, wx.ALL, 5 )
		
		bmap_txt_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bmap_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Basemap:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_txt.Wrap( -1 )
		self.bmap_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bmap_txt_sizer.Add( self.bmap_txt, 0, wx.ALL, 5 )
		
		self.bmap_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_plot_check.SetValue(True) 
		bmap_txt_sizer.Add( self.bmap_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		plottingMainSizer.Add( bmap_txt_sizer, 1, wx.EXPAND, 5 )
		
		bmap_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		bmap_options_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		bmap_options_sizer.SetFlexibleDirection( wx.BOTH )
		bmap_options_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bmap_landcol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Land Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_landcol_txt.Wrap( -1 )
		bmap_options_sizer.Add( self.bmap_landcol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.bmap_lakecol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Lake Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_lakecol_txt.Wrap( -1 )
		bmap_options_sizer.Add( self.bmap_lakecol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.bmap_oceancol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Ocean Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_oceancol_txt.Wrap( -1 )
		bmap_options_sizer.Add( self.bmap_oceancol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.bmap_buffer_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Buffer (degrees)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_buffer_txt.Wrap( -1 )
		bmap_options_sizer.Add( self.bmap_buffer_txt, 0, wx.ALL, 5 )
		
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
		
		
		plottingMainSizer.Add( bmap_sizer, 1, wx.EXPAND, 5 )
		
		lyr1_txt_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr1_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"First Layer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr1_txt.Wrap( -1 )
		self.lyr1_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		lyr1_txt_sizer.Add( self.lyr1_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.lyr1_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr1_plot_check.SetValue(True) 
		lyr1_txt_sizer.Add( self.lyr1_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		plottingMainSizer.Add( lyr1_txt_sizer, 1, wx.EXPAND, 5 )
		
		lyr1_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr1_choice = wx.Choicebook( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_TOP )
		self.metrics_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		metrics_opt_sizer = wx.FlexGridSizer( 4, 3, 0, 0 )
		metrics_opt_sizer.SetFlexibleDirection( wx.BOTH )
		metrics_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.metric_shp_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_shp_txt.Wrap( -1 )
		metrics_opt_sizer.Add( self.metric_shp_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
		self.metric_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_txt.Wrap( -1 )
		metrics_opt_sizer.Add( self.metric_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
		self.metric_lowcol_txt = wx.StaticText( self.metrics_opt, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_lowcol_txt.Wrap( -1 )
		metrics_opt_sizer.Add( self.metric_lowcol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
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
		
		
		plottingMainSizer.Add( lyr1_sizer, 1, wx.EXPAND, 5 )
		
		lyr2_txt_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr2_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Second Layer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr2_txt.Wrap( -1 )
		self.lyr2_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		lyr2_txt_sizer.Add( self.lyr2_txt, 0, wx.ALL, 5 )
		
		self.lyr2_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr2_plot_check.SetValue(True) 
		lyr2_txt_sizer.Add( self.lyr2_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		plottingMainSizer.Add( lyr2_txt_sizer, 1, wx.EXPAND, 5 )
		
		lyr2_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr2_choice = wx.Choicebook( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_TOP )
		self.metrics_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		metrics_opt_sizer1 = wx.FlexGridSizer( 4, 3, 0, 0 )
		metrics_opt_sizer1.SetFlexibleDirection( wx.BOTH )
		metrics_opt_sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.metric_shp_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_shp_txt1.Wrap( -1 )
		metrics_opt_sizer1.Add( self.metric_shp_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
		self.metric_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_txt1.Wrap( -1 )
		metrics_opt_sizer1.Add( self.metric_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
		self.metric_lowcol_txt1 = wx.StaticText( self.metrics_opt1, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metric_lowcol_txt1.Wrap( -1 )
		metrics_opt_sizer1.Add( self.metric_lowcol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
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
		
		
		plottingMainSizer.Add( lyr2_sizer, 1, wx.EXPAND, 5 )
		
		self.plot_map_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Plot Map", wx.DefaultPosition, wx.DefaultSize, 0 )
		plottingMainSizer.Add( self.plot_map_button, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.plot_opt_seperator = wx.StaticLine( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		plottingMainSizer.Add( self.plot_opt_seperator, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.graphoptions = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Graph Plotting Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.graphoptions.Wrap( -1 )
		self.graphoptions.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		self.graphoptions.Enable( False )
		
		plottingMainSizer.Add( self.graphoptions, 0, wx.ALL, 5 )
		
		sizer011 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choice21Choices = []
		self.m_choice21 = wx.Choice( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice21Choices, 0 )
		self.m_choice21.SetSelection( 0 )
		self.m_choice21.Enable( False )
		
		sizer011.Add( self.m_choice21, 0, wx.ALL, 5 )
		
		m_choice11Choices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment", wx.EmptyString ]
		self.m_choice11 = wx.Choice( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		self.m_choice11.Enable( False )
		
		sizer011.Add( self.m_choice11, 0, wx.ALL, 5 )
		
		self.m_colourPicker11 = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.m_colourPicker11.Enable( False )
		
		sizer011.Add( self.m_colourPicker11, 0, wx.ALL, 5 )
		
		self.m_colourPicker21 = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.m_colourPicker21.Enable( False )
		
		sizer011.Add( self.m_colourPicker21, 0, wx.ALL, 5 )
		
		
		plottingMainSizer.Add( sizer011, 1, wx.EXPAND, 5 )
		
		self.plot_graph_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Plot Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.plot_graph_button.Enable( False )
		
		plottingMainSizer.Add( self.plot_graph_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.plottingOptions.SetSizer( plottingMainSizer )
		self.plottingOptions.Layout()
		plottingMainSizer.Fit( self.plottingOptions )
		self.auinotebook.AddPage( self.plottingOptions, u"6) Plotting Options", False, wx.NullBitmap )
		
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
		self.PU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PU_file )
		self.PU_file_pu_id.Bind( wx.EVT_CHOICE, self.on_PU_file_pu_id )
		self.FA_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_FA_file )
		self.fa_status_radioBox.Bind( wx.EVT_RADIOBOX, self.on_fa_status_radioBox )
		self.AA_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_AA_file )
		self.aa_status_radioBox.Bind( wx.EVT_RADIOBOX, self.on_aa_status_radioBox )
		self.demo_matrixUnitsRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_matrixUnitsRadioBox )
		self.demo_matrixTypeRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_matrixTypeRadioBox )
		self.demo_matrixFormatRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_matrixFormatRadioBox )
		self.demo_CU_CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_demo_CU_CM_file )
		self.demo_rescaleRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_rescaleRadioBox )
		self.demo_rescale_edgeRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_rescale_edgeRadioBox )
		self.demo_CU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_demo_CU_file )
		self.demo_CU_file_pu_id.Bind( wx.EVT_CHOICE, self.on_demo_CU_file_pu_id )
		self.demo_PU_CM_progress.Bind( wx.EVT_CHECKBOX, self.on_demo_PU_CM_progress )
		self.demo_PU_CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_demo_PU_CM_file )
		self.demo_rescale_button.Bind( wx.EVT_BUTTON, self.on_demo_rescale_button )
		self.land_matrixTypeRadioBox.Bind( wx.EVT_RADIOBOX, self.on_land_matrixTypeRadioBox )
		self.land_HAB_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_land_HAB_file )
		self.land_HAB_file_hab_id.Bind( wx.EVT_CHOICE, self.on_land_HAB_file_hab_id )
		self.land_HAB_buff.Bind( wx.EVT_TEXT, self.on_land_HAB_buff )
		self.land_RES_mat_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_land_RES_mat_file )
		self.resistance_mat_customize.Bind( wx.EVT_BUTTON, self.on_resistance_mat_customize )
		self.land_RES_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_land_RES_file )
		self.land_RES_file_res_id.Bind( wx.EVT_CHOICE, self.on_land_RES_file_hab_id )
		self.land_PU_CM_progress.Bind( wx.EVT_CHECKBOX, self.on_land_PU_CM_progress )
		self.land_PU_CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_land_PU_CM_file )
		self.land_generate_button.Bind( wx.EVT_BUTTON, self.on_land_generate_button )
		self.bd_demo_conn_boundary.Bind( wx.EVT_CHECKBOX, self.on_bd_demo_conn_boundary )
		self.bd_demo_min_plan_graph.Bind( wx.EVT_CHECKBOX, self.on_bd_demo_min_plan_graph )
		self.bd_land_conn_boundary.Bind( wx.EVT_CHECKBOX, self.on_bd_land_conn_boundary )
		self.bd_land_min_plan_graph.Bind( wx.EVT_CHECKBOX, self.on_bd_land_min_plan_graph )
		self.calc_metrics.Bind( wx.EVT_BUTTON, self.on_calc_metrics )
		self.preEval_metric_shp_choice.Bind( wx.EVT_CHOICE, self.on_preEval_metric_shp_choice )
		self.preEval_metric_choice.Bind( wx.EVT_CHOICE, self.on_preEval_metric_choice )
		self.m_button18.Bind( wx.EVT_BUTTON, self.on_remove_metric )
		self.preEval_create_new.Bind( wx.EVT_BUTTON, self.on_preEval_create_new )
		self.CF_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CT_file )
		self.CFT_percent_slider.Bind( wx.EVT_SCROLL, self.on_CFT_percent_slider )
		self.customize_spec.Bind( wx.EVT_BUTTON, self.on_customize_spec )
		self.SPEC_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CT_file_append )
		self.BD_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_BD_file )
		self.PUDAT_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PUDAT_file )
		self.export_metrics.Bind( wx.EVT_BUTTON, self.on_export_metrics )
		self.marxan_dir.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_marxan_dir )
		self.inputdat_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_inputdat_file )
		self.customize_inputdat.Bind( wx.EVT_BUTTON, self.on_inedit )
		self.run_marxan_button.Bind( wx.EVT_BUTTON, self.on_run_marxan )
		self.metric_shp_choice.Bind( wx.EVT_CHOICE, self.on_metric_shp_choice )
		self.metric_shp_choice1.Bind( wx.EVT_CHOICE, self.on_metric_shp_choice1 )
		self.plot_map_button.Bind( wx.EVT_BUTTON, self.on_plot_map_button )
		self.plot_graph_button.Bind( wx.EVT_BUTTON, self.on_plot_graph_button )
	
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
	
	def on_demo_matrixUnitsRadioBox( self, event ):
		event.Skip()
	
	def on_demo_matrixTypeRadioBox( self, event ):
		event.Skip()
	
	def on_demo_matrixFormatRadioBox( self, event ):
		event.Skip()
	
	def on_demo_CU_CM_file( self, event ):
		event.Skip()
	
	def on_demo_rescaleRadioBox( self, event ):
		event.Skip()
	
	def on_demo_rescale_edgeRadioBox( self, event ):
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
	
	def on_land_matrixTypeRadioBox( self, event ):
		event.Skip()
	
	def on_land_HAB_file( self, event ):
		event.Skip()
	
	def on_land_HAB_file_hab_id( self, event ):
		event.Skip()
	
	def on_land_HAB_buff( self, event ):
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
	
	def on_bd_demo_conn_boundary( self, event ):
		event.Skip()
	
	def on_bd_demo_min_plan_graph( self, event ):
		event.Skip()
	
	def on_bd_land_conn_boundary( self, event ):
		event.Skip()
	
	def on_bd_land_min_plan_graph( self, event ):
		event.Skip()
	
	def on_calc_metrics( self, event ):
		event.Skip()
	
	def on_preEval_metric_shp_choice( self, event ):
		event.Skip()
	
	def on_preEval_metric_choice( self, event ):
		event.Skip()
	
	def on_remove_metric( self, event ):
		event.Skip()
	
	def on_preEval_create_new( self, event ):
		event.Skip()
	
	def on_CT_file( self, event ):
		event.Skip()
	
	def on_CFT_percent_slider( self, event ):
		event.Skip()
	
	def on_customize_spec( self, event ):
		event.Skip()
	
	def on_CT_file_append( self, event ):
		event.Skip()
	
	def on_BD_file( self, event ):
		event.Skip()
	
	def on_PUDAT_file( self, event ):
		event.Skip()
	
	def on_export_metrics( self, event ):
		event.Skip()
	
	def on_marxan_dir( self, event ):
		event.Skip()
	
	def on_inputdat_file( self, event ):
		event.Skip()
	
	def on_inedit( self, event ):
		event.Skip()
	
	def on_run_marxan( self, event ):
		event.Skip()
	
	def on_metric_shp_choice( self, event ):
		event.Skip()
	
	def on_metric_shp_choice1( self, event ):
		event.Skip()
	
	def on_plot_map_button( self, event ):
		event.Skip()
	
	def on_plot_graph_button( self, event ):
		event.Skip()
	

###########################################################################
## Class spec_customizer
###########################################################################

class spec_customizer ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		spec_mainsizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		spec_mainsizer.SetFlexibleDirection( wx.BOTH )
		spec_mainsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.spec_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.spec_grid.CreateGrid( 0, 4 )
		self.spec_grid.EnableEditing( True )
		self.spec_grid.EnableGridLines( True )
		self.spec_grid.EnableDragGridSize( False )
		self.spec_grid.SetMargins( 0, 0 )
		
		# Columns
		self.spec_grid.EnableDragColMove( False )
		self.spec_grid.EnableDragColSize( True )
		self.spec_grid.SetColLabelSize( 30 )
		self.spec_grid.SetColLabelValue( 0, u"id" )
		self.spec_grid.SetColLabelValue( 1, u"target" )
		self.spec_grid.SetColLabelValue( 2, u"spf" )
		self.spec_grid.SetColLabelValue( 3, u"name" )
		self.spec_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.spec_grid.EnableDragRowSize( True )
		self.spec_grid.SetRowLabelSize( 80 )
		self.spec_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.spec_grid.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		spec_mainsizer.Add( self.spec_grid, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		spec_button_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		spec_button_sizer.AddGrowableCol( 0 )
		spec_button_sizer.SetFlexibleDirection( wx.BOTH )
		spec_button_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.spacer_text = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacer_text.Wrap( -1 )
		spec_button_sizer.Add( self.spacer_text, 0, wx.ALL, 5 )
		
		self.spec_ok = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		spec_button_sizer.Add( self.spec_ok, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.spec_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		spec_button_sizer.Add( self.spec_cancel, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		spec_mainsizer.Add( spec_button_sizer, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( spec_mainsizer )
		self.Layout()
		spec_mainsizer.Fit( self )
		
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
	

