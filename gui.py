# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 28 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marxan with Connectivity", pos = wx.DefaultPosition, size = wx.Size( 1005,786 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.help = wx.Menu()
		self.glossary = wx.MenuItem( self.help, wx.ID_ANY, u"Glossary", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.glossary )
		
		self.tutorial = wx.MenuItem( self.help, wx.ID_ANY, u"Tutorial", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.tutorial )
		
		self.github = wx.MenuItem( self.help, wx.ID_ANY, u"GitHub issues", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.github )
		
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
		spatialMainSizer.AddGrowableRow( 5 )
		spatialMainSizer.SetFlexibleDirection( wx.VERTICAL )
		spatialMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.pu_title = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Planning Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_title.Wrap( -1 )
		self.pu_title.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		spatialMainSizer.Add( self.pu_title, 0, wx.ALL, 5 )
		
		pu_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PU_def = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Describe Planning Units ...................  text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		
		spatialMainSizer.Add( pu_file_sizer1, 1, wx.EXPAND, 5 )
		
		self.fa_title = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Focus Areas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fa_title.Wrap( -1 )
		self.fa_title.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		spatialMainSizer.Add( self.fa_title, 0, wx.ALL, 5 )
		
		fa_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.FA_def = wx.StaticText( self.spatialInput, wx.ID_ANY, u"For some of the connectivity metrics (e.g. Temporal Connectivity Correlation), it is important to consider 'focus areas' for which connectivity should be optimised. Such focus areas could include existing protected areas, important habitat for endangered species, and/or otherwise important habitats for connectivity (e.g. nursery grounds, genetically unique and potentially adaptively advantageous populations). Marxan with Connectivity assumes that the planning units within the 'focus areas' will otherwise be targeted as normal conservation targets in Marxan. Loading focus areas into Marxan with Connectivity allows users to set conservation targets for the areas that complement the 'focus areas'", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FA_def.Wrap( -1 )
		fa_def_sizer.Add( self.FA_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		spatialMainSizer.Add( fa_def_sizer, 1, wx.EXPAND, 5 )
		
		fa_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		fa_file_sizer.AddGrowableCol( 1 )
		fa_file_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		fa_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.FA_filetext = wx.StaticText( self.spatialInput, wx.ID_ANY, u"Focus Areas Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FA_filetext.Wrap( -1 )
		self.FA_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		fa_file_sizer.Add( self.FA_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.FA_file = wx.FilePickerCtrl( self.spatialInput, wx.ID_ANY, wx.EmptyString, u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fa_file_sizer.Add( self.FA_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		spatialMainSizer.Add( fa_file_sizer, 1, wx.EXPAND, 5 )
		
		
		self.spatialInput.SetSizer( spatialMainSizer )
		self.spatialInput.Layout()
		spatialMainSizer.Fit( self.spatialInput )
		self.auinotebook.AddPage( self.spatialInput, u"1) Spatial Input", False, wx.NullBitmap )
		self.connectivityInput = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		conn_input_mainsizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		conn_input_mainsizer.AddGrowableCol( 0 )
		conn_input_mainsizer.AddGrowableRow( 0 )
		conn_input_mainsizer.AddGrowableRow( 2 )
		conn_input_mainsizer.SetFlexibleDirection( wx.BOTH )
		conn_input_mainsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		con_input_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.con_input_def_txt = wx.StaticText( self.connectivityInput, wx.ID_ANY, u"Connectivity data come from many sources and to simplify the input procedure has been divided into three main categories, demographic, genetic, and landscape connectivity. Choosing a different category will not erase any input and input from multiple categories can be used simultaneously in the analyses in the next steps", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.demographic = wx.Panel( self.conn_category_choicebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		demoMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		demoMainSizer.AddGrowableCol( 0 )
		demoMainSizer.AddGrowableRow( 0 )
		demoMainSizer.AddGrowableRow( 2 )
		demoMainSizer.AddGrowableRow( 3 )
		demoMainSizer.AddGrowableRow( 4 )
		demoMainSizer.AddGrowableRow( 5 )
		demoMainSizer.AddGrowableRow( 7 )
		demoMainSizer.AddGrowableRow( 8 )
		demoMainSizer.SetFlexibleDirection( wx.VERTICAL )
		demoMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		demo_cm_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.demo_CM_def = wx.StaticText( self.demographic, wx.ID_ANY, u"Dexcribe Connectivity Matrix .......................... text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		demo_rescale_sizer = wx.BoxSizer( wx.VERTICAL )
		
		demo_rescale_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.demo_rescale_def_txt = wx.StaticText( self.demographic, wx.ID_ANY, u"The demographic connectivity data does not need to be at the same spatial scale as the Marxan planning units. If there is a mismatch, rescale the connectivity data below.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_rescale_def_txt.Wrap( -1 )
		demo_rescale_def_sizer.Add( self.demo_rescale_def_txt, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demo_rescale_sizer.Add( demo_rescale_def_sizer, 1, wx.EXPAND, 5 )
		
		demo_rescaleRadioBoxChoices = [ u"Identical Grids", u"Rescale Connectivity Matrix" ]
		self.demo_rescaleRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Rescale Connectivity Matrix?", wx.DefaultPosition, wx.DefaultSize, demo_rescaleRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.demo_rescaleRadioBox.SetSelection( 0 )
		demo_rescale_sizer.Add( self.demo_rescaleRadioBox, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		demoMainSizer.Add( demo_rescale_sizer, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		demo_cu_def_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.demo_CU_def = wx.StaticText( self.demographic, wx.ID_ANY, u"Describe Connectivity Matrix Shapefile ....................................... text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		self.demo_PU_CM_def = wx.StaticText( self.demographic, wx.ID_ANY, u"Describe Planning Unit Connectivity Matrix ...................  text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_PU_CM_def.Wrap( -1 )
		self.demo_PU_CM_def.Enable( False )
		
		demo_pucm_def_sizer.Add( self.demo_PU_CM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( demo_pucm_def_sizer, 1, wx.EXPAND, 5 )
		
		demo_pucm_sizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		demo_pucm_sizer.AddGrowableCol( 2 )
		demo_pucm_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		demo_pucm_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.demo_PU_CM_check = wx.CheckBox( self.demographic, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_PU_CM_check.Enable( False )
		
		demo_pucm_sizer.Add( self.demo_PU_CM_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.demo_PU_CM_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Output Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.genetic = wx.Panel( self.conn_category_choicebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.conn_category_choicebook.AddPage( self.genetic, u"Genetic Input", False )
		self.landscape = wx.Panel( self.conn_category_choicebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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
		metricsMainSizer.AddGrowableRow( 5 )
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
		self.cf_demo_vertex_degree.SetValue(True) 
		self.cf_demo_vertex_degree.SetToolTip( u"The vertex degree indicates the number of connections for each planning unit" )
		
		demo_cf_sizer.Add( self.cf_demo_vertex_degree, 0, wx.ALL, 5 )
		
		self.cf_demo_between_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Betweenness Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_between_cent.SetValue(True) 
		self.cf_demo_between_cent.SetToolTip( u"Betweenness Centrality is an indicator of a planning unit's centrality in a network. It is equal to the number of shortest paths from all connections to all others that pass through that planning unit." )
		
		demo_cf_sizer.Add( self.cf_demo_between_cent, 0, wx.ALL, 5 )
		
		self.cf_demo_eig_vect_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Eigen Vector Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_eig_vect_cent.SetValue(True) 
		self.cf_demo_eig_vect_cent.SetToolTip( u"Eigen Vector Centrality is a measure of the influence of a planning unit in a network. It assigns relative scores to all planning unitin the network based on the concept that connections to high-scoring planning unit contribute more to the score of the planning unit in question than equal connections to low-scoring nodes" )
		
		demo_cf_sizer.Add( self.cf_demo_eig_vect_cent, 0, wx.ALL, 5 )
		
		self.cf_demo_self_recruit = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Self Recruitment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_self_recruit.SetValue(True) 
		self.cf_demo_self_recruit.SetToolTip( u"Self Recruitment is the propotion of new recruits from a planning unit that will stay in that planning unit." )
		
		demo_cf_sizer.Add( self.cf_demo_self_recruit, 0, wx.ALL, 5 )
		
		self.cf_demo_stochasticity_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.cf_demo_stochasticity_panel.SetToolTip( u"Uses spatial and temporal stochasticity in connectivity to identify planning units that increase metapopulation growth and stability. It is only available if a connectivity 'List with Time' was provided unde Demographic Input in the Connectivity Input tab." )
		
		cf_demo_stochasticity_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cf_demo_stochasticity = wx.CheckBox( self.cf_demo_stochasticity_panel, wx.ID_ANY, u"Temporal Connectivity Correlation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_demo_stochasticity.Enable( False )
		
		cf_demo_stochasticity_sizer.Add( self.cf_demo_stochasticity, 0, wx.ALL, 5 )
		
		
		self.cf_demo_stochasticity_panel.SetSizer( cf_demo_stochasticity_sizer )
		self.cf_demo_stochasticity_panel.Layout()
		cf_demo_stochasticity_sizer.Fit( self.cf_demo_stochasticity_panel )
		demo_cf_sizer.Add( self.cf_demo_stochasticity_panel, 1, wx.EXPAND, 5 )
		
		
		cf_sizer.Add( demo_cf_sizer, 1, wx.EXPAND, 5 )
		
		gen_cf_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.gen_cf_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Genetic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gen_cf_txt.Wrap( -1 )
		self.gen_cf_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		gen_cf_sizer.Add( self.gen_cf_txt, 0, wx.ALL, 5 )
		
		
		cf_sizer.Add( gen_cf_sizer, 1, wx.EXPAND, 5 )
		
		land_cf_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.land_cf_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_cf_txt.Wrap( -1 )
		self.land_cf_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		land_cf_sizer.Add( self.land_cf_txt, 0, wx.ALL, 5 )
		
		
		cf_sizer.Add( land_cf_sizer, 1, wx.EXPAND, 5 )
		
		
		metricsMainSizer.Add( cf_sizer, 1, wx.EXPAND, 5 )
		
		cf_export_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		cf_export_sizer.AddGrowableCol( 1 )
		cf_export_sizer.SetFlexibleDirection( wx.BOTH )
		cf_export_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		cf_export_radioBoxChoices = [ u"Export", u"Append" ]
		self.cf_export_radioBox = wx.RadioBox( self.connectivityMetrics, wx.ID_ANY, u"Metrics", wx.DefaultPosition, wx.DefaultSize, cf_export_radioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.cf_export_radioBox.SetSelection( 0 )
		cf_export_sizer.Add( self.cf_export_radioBox, 0, wx.ALL, 5 )
		
		cf_file_export_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		cf_file_export_sizer.AddGrowableCol( 1 )
		cf_file_export_sizer.SetFlexibleDirection( wx.BOTH )
		cf_file_export_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cf_export_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Planning Unit versus Conservation Feature File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_export_txt.Wrap( -1 )
		cf_file_export_sizer.Add( self.cf_export_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CF_file = wx.FilePickerCtrl( self.connectivityMetrics, wx.ID_ANY, u"~\\puvspr.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		cf_file_export_sizer.Add( self.CF_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.cf_targets_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Conservation Feature Targets:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cf_targets_txt.Wrap( -1 )
		cf_file_export_sizer.Add( self.cf_targets_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		cft_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cft_percent_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Percent of Feature Targeted:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cft_percent_txt.Wrap( -1 )
		cft_sizer.Add( self.cft_percent_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CFT_percent_slider = wx.Slider( self.connectivityMetrics, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		self.CFT_percent_slider.Enable( False )
		
		cft_sizer.Add( self.CFT_percent_slider, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.custom_spec_panel = wx.Panel( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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
		
		self.SPEC_filetxt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Conservation Feature File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SPEC_filetxt.Wrap( -1 )
		cf_file_export_sizer.Add( self.SPEC_filetxt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.SPEC_file = wx.FilePickerCtrl( self.connectivityMetrics, wx.ID_ANY, u"~\\spec.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		cf_file_export_sizer.Add( self.SPEC_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		cf_export_sizer.Add( cf_file_export_sizer, 1, wx.EXPAND, 5 )
		
		
		metricsMainSizer.Add( cf_export_sizer, 1, wx.EXPAND, 5 )
		
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
		
		gen_bd_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.gen_bd_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Genetic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gen_bd_txt.Wrap( -1 )
		self.gen_bd_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		gen_bd_sizer.Add( self.gen_bd_txt, 0, wx.ALL, 5 )
		
		
		bd_sizer.Add( gen_bd_sizer, 1, wx.EXPAND, 5 )
		
		land_bd_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.land_bd_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.land_bd_txt.Wrap( -1 )
		self.land_bd_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		land_bd_sizer.Add( self.land_bd_txt, 0, wx.ALL, 5 )
		
		
		bd_sizer.Add( land_bd_sizer, 1, wx.EXPAND, 5 )
		
		
		metricsMainSizer.Add( bd_sizer, 1, wx.EXPAND, 5 )
		
		bd_file_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		bd_file_sizer.AddGrowableCol( 1 )
		bd_file_sizer.SetFlexibleDirection( wx.BOTH )
		bd_file_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.BD_filecheck = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Export Boundary Definition to: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BD_filecheck.SetValue(True) 
		bd_file_sizer.Add( self.BD_filecheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.BD_file = wx.FilePickerCtrl( self.connectivityMetrics, wx.ID_ANY, u"~\\bound.dat", u"Select a file", u"Marxan Data Files (*.dat)|*.dat|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bd_file_sizer.Add( self.BD_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		metricsMainSizer.Add( bd_file_sizer, 1, wx.EXPAND, 5 )
		
		self.metrics_buttons_seperator = wx.StaticLine( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		metricsMainSizer.Add( self.metrics_buttons_seperator, 0, wx.EXPAND |wx.ALL, 5 )
		
		metrics_buttons_sizer = wx.FlexGridSizer( 0, 5, 0, 0 )
		metrics_buttons_sizer.AddGrowableCol( 0 )
		metrics_buttons_sizer.SetFlexibleDirection( wx.BOTH )
		metrics_buttons_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.spacertext = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertext.Wrap( -1 )
		metrics_buttons_sizer.Add( self.spacertext, 0, wx.ALL, 5 )
		
		self.calc_metrics = wx.Button( self.connectivityMetrics, wx.ID_ANY, u"Calculate Metrics", wx.DefaultPosition, wx.DefaultSize, 0 )
		metrics_buttons_sizer.Add( self.calc_metrics, 0, wx.ALL, 5 )
		
		self.export_metrics = wx.Button( self.connectivityMetrics, wx.ID_ANY, u"Export Metrics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.export_metrics.Enable( False )
		
		metrics_buttons_sizer.Add( self.export_metrics, 0, wx.ALL, 5 )
		
		self.metrics_for_txt = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"For:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.metrics_for_txt.Wrap( -1 )
		metrics_buttons_sizer.Add( self.metrics_for_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		calc_metrics_typeChoices = [ u"Planning Units", u"Connectivity Units" ]
		self.calc_metrics_type = wx.Choice( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, calc_metrics_typeChoices, 0 )
		self.calc_metrics_type.SetSelection( 0 )
		metrics_buttons_sizer.Add( self.calc_metrics_type, 0, wx.ALL, 5 )
		
		
		metricsMainSizer.Add( metrics_buttons_sizer, 1, wx.EXPAND, 5 )
		
		
		self.connectivityMetrics.SetSizer( metricsMainSizer )
		self.connectivityMetrics.Layout()
		metricsMainSizer.Fit( self.connectivityMetrics )
		self.auinotebook.AddPage( self.connectivityMetrics, u"3) Connectivity Metrics", True, wx.NullBitmap )
		self.marxanAnalysis = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.auinotebook.AddPage( self.marxanAnalysis, u"4) Marxan Analysis", False, wx.NullBitmap )
		self.postMarxan = wx.Panel( self.auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.auinotebook.AddPage( self.postMarxan, u"5) Post-Marxan Analysis", False, wx.NullBitmap )
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
		self.pu_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		pu_plot_opt_sizer = wx.FlexGridSizer( 2, 5, 0, 0 )
		pu_plot_opt_sizer.SetFlexibleDirection( wx.BOTH )
		pu_plot_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.pu_metric_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_txt.Wrap( -1 )
		pu_plot_opt_sizer.Add( self.pu_metric_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_hicol_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_hicol_txt.Wrap( -1 )
		pu_plot_opt_sizer.Add( self.pu_metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_hicol_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_hicol_txt.Wrap( -1 )
		pu_plot_opt_sizer.Add( self.pu_metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_alpha_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_alpha_txt.Wrap( -1 )
		pu_plot_opt_sizer.Add( self.pu_metric_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_legend_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_legend_txt.Wrap( -1 )
		pu_plot_opt_sizer.Add( self.pu_metric_legend_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		pu_metric_choiceChoices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.pu_metric_choice = wx.Choice( self.pu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_choiceChoices, 0 )
		self.pu_metric_choice.SetSelection( 2 )
		pu_plot_opt_sizer.Add( self.pu_metric_choice, 0, wx.ALL, 5 )
		
		self.pu_metric_lowcol = wx.ColourPickerCtrl( self.pu_plot_opt, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_lowcol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		pu_plot_opt_sizer.Add( self.pu_metric_lowcol, 0, wx.ALL, 5 )
		
		self.pu_metric_hicol = wx.ColourPickerCtrl( self.pu_plot_opt, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_hicol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		pu_plot_opt_sizer.Add( self.pu_metric_hicol, 0, wx.ALL, 5 )
		
		self.pu_metric_alpha = wx.Slider( self.pu_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		pu_plot_opt_sizer.Add( self.pu_metric_alpha, 0, wx.ALL, 5 )
		
		pu_metric_legendChoices = [ u"Top", u"Bottom", u"None" ]
		self.pu_metric_legend = wx.Choice( self.pu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_legendChoices, 0 )
		self.pu_metric_legend.SetSelection( 1 )
		pu_plot_opt_sizer.Add( self.pu_metric_legend, 0, wx.ALL, 5 )
		
		
		self.pu_plot_opt.SetSizer( pu_plot_opt_sizer )
		self.pu_plot_opt.Layout()
		pu_plot_opt_sizer.Fit( self.pu_plot_opt )
		self.lyr1_choice.AddPage( self.pu_plot_opt, u"Planning Units", True )
		self.cu_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cu_plot_opt_sizer = wx.FlexGridSizer( 0, 5, 0, 0 )
		cu_plot_opt_sizer.SetFlexibleDirection( wx.BOTH )
		cu_plot_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cu_metric_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_txt.Wrap( -1 )
		cu_plot_opt_sizer.Add( self.cu_metric_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_hicol_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_hicol_txt.Wrap( -1 )
		cu_plot_opt_sizer.Add( self.cu_metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_hicol_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_hicol_txt.Wrap( -1 )
		cu_plot_opt_sizer.Add( self.cu_metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_alpha_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_alpha_txt.Wrap( -1 )
		cu_plot_opt_sizer.Add( self.cu_metric_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_legend_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_legend_txt.Wrap( -1 )
		cu_plot_opt_sizer.Add( self.cu_metric_legend_txt, 0, wx.ALL, 5 )
		
		cu_metric_choiceChoices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.cu_metric_choice = wx.Choice( self.cu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_choiceChoices, 0 )
		self.cu_metric_choice.SetSelection( 0 )
		cu_plot_opt_sizer.Add( self.cu_metric_choice, 0, wx.ALL, 5 )
		
		self.cu_metric_lowcol = wx.ColourPickerCtrl( self.cu_plot_opt, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_lowcol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		cu_plot_opt_sizer.Add( self.cu_metric_lowcol, 0, wx.ALL, 5 )
		
		self.cu_metric_hicol = wx.ColourPickerCtrl( self.cu_plot_opt, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_hicol.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		cu_plot_opt_sizer.Add( self.cu_metric_hicol, 0, wx.ALL, 5 )
		
		self.cu_metric_alpha = wx.Slider( self.cu_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		cu_plot_opt_sizer.Add( self.cu_metric_alpha, 0, wx.ALL, 5 )
		
		cu_metric_legendChoices = [ u"Top", u"Bottom", u"None" ]
		self.cu_metric_legend = wx.Choice( self.cu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_legendChoices, 0 )
		self.cu_metric_legend.SetSelection( 1 )
		cu_plot_opt_sizer.Add( self.cu_metric_legend, 0, wx.ALL, 5 )
		
		
		self.cu_plot_opt.SetSizer( cu_plot_opt_sizer )
		self.cu_plot_opt.Layout()
		cu_plot_opt_sizer.Fit( self.cu_plot_opt )
		self.lyr1_choice.AddPage( self.cu_plot_opt, u"Connectivity Units", False )
		self.pu_poly_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		pu_poly_plot_opt_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		pu_poly_plot_opt_sizer.SetFlexibleDirection( wx.BOTH )
		pu_poly_plot_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.pu_poly_col_txt = wx.StaticText( self.pu_poly_plot_opt, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_poly_col_txt.Wrap( -1 )
		pu_poly_plot_opt_sizer.Add( self.pu_poly_col_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_poly_alpha_txt = wx.StaticText( self.pu_poly_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_poly_alpha_txt.Wrap( -1 )
		pu_poly_plot_opt_sizer.Add( self.pu_poly_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_poly_col = wx.ColourPickerCtrl( self.pu_poly_plot_opt, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_poly_col.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		pu_poly_plot_opt_sizer.Add( self.pu_poly_col, 0, wx.ALL, 5 )
		
		self.pu_poly_alpha = wx.Slider( self.pu_poly_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		pu_poly_plot_opt_sizer.Add( self.pu_poly_alpha, 0, wx.ALL, 5 )
		
		
		self.pu_poly_plot_opt.SetSizer( pu_poly_plot_opt_sizer )
		self.pu_poly_plot_opt.Layout()
		pu_poly_plot_opt_sizer.Fit( self.pu_poly_plot_opt )
		self.lyr1_choice.AddPage( self.pu_poly_plot_opt, u"Planning Unit (polygons)", False )
		self.cu_poly_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cu_poly_plot_opt_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		cu_poly_plot_opt_sizer.SetFlexibleDirection( wx.BOTH )
		cu_poly_plot_opt_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cu_poly_col_txt = wx.StaticText( self.cu_poly_plot_opt, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_poly_col_txt.Wrap( -1 )
		cu_poly_plot_opt_sizer.Add( self.cu_poly_col_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_poly_alpha_txt = wx.StaticText( self.cu_poly_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_poly_alpha_txt.Wrap( -1 )
		cu_poly_plot_opt_sizer.Add( self.cu_poly_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_poly_col = wx.ColourPickerCtrl( self.cu_poly_plot_opt, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_poly_col.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		cu_poly_plot_opt_sizer.Add( self.cu_poly_col, 0, wx.ALL, 5 )
		
		self.cu_poly_alpha = wx.Slider( self.cu_poly_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		cu_poly_plot_opt_sizer.Add( self.cu_poly_alpha, 0, wx.ALL, 5 )
		
		
		self.cu_poly_plot_opt.SetSizer( cu_poly_plot_opt_sizer )
		self.cu_poly_plot_opt.Layout()
		cu_poly_plot_opt_sizer.Fit( self.cu_poly_plot_opt )
		self.lyr1_choice.AddPage( self.cu_poly_plot_opt, u"Connectivity Unit (polygons)", False )
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
		self.pu_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		pu_plot_opt1_sizer = wx.FlexGridSizer( 0, 5, 0, 0 )
		pu_plot_opt1_sizer.SetFlexibleDirection( wx.BOTH )
		pu_plot_opt1_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.pu_metric_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_txt1.Wrap( -1 )
		pu_plot_opt1_sizer.Add( self.pu_metric_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_hicol_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_hicol_txt1.Wrap( -1 )
		pu_plot_opt1_sizer.Add( self.pu_metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_hicol_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_hicol_txt1.Wrap( -1 )
		pu_plot_opt1_sizer.Add( self.pu_metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_alpha_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_alpha_txt1.Wrap( -1 )
		pu_plot_opt1_sizer.Add( self.pu_metric_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_legend_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_legend_txt1.Wrap( -1 )
		pu_plot_opt1_sizer.Add( self.pu_metric_legend_txt1, 0, wx.ALL, 5 )
		
		pu_metric_choice1Choices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.pu_metric_choice1 = wx.Choice( self.pu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_choice1Choices, 0 )
		self.pu_metric_choice1.SetSelection( 0 )
		pu_plot_opt1_sizer.Add( self.pu_metric_choice1, 0, wx.ALL, 5 )
		
		self.pu_metric_lowcol1 = wx.ColourPickerCtrl( self.pu_plot_opt1, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_lowcol1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		pu_plot_opt1_sizer.Add( self.pu_metric_lowcol1, 0, wx.ALL, 5 )
		
		self.pu_metric_hicol1 = wx.ColourPickerCtrl( self.pu_plot_opt1, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_hicol1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		pu_plot_opt1_sizer.Add( self.pu_metric_hicol1, 0, wx.ALL, 5 )
		
		self.pu_metric_alpha1 = wx.Slider( self.pu_plot_opt1, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		pu_plot_opt1_sizer.Add( self.pu_metric_alpha1, 0, wx.ALL, 5 )
		
		pu_metric_legend1Choices = [ u"Top", u"Bottom", u"None" ]
		self.pu_metric_legend1 = wx.Choice( self.pu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_legend1Choices, 0 )
		self.pu_metric_legend1.SetSelection( 0 )
		pu_plot_opt1_sizer.Add( self.pu_metric_legend1, 0, wx.ALL, 5 )
		
		
		self.pu_plot_opt1.SetSizer( pu_plot_opt1_sizer )
		self.pu_plot_opt1.Layout()
		pu_plot_opt1_sizer.Fit( self.pu_plot_opt1 )
		self.lyr2_choice.AddPage( self.pu_plot_opt1, u"Planning Units", False )
		self.cu_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cu_plot_opt1_sizer = wx.FlexGridSizer( 0, 5, 0, 0 )
		cu_plot_opt1_sizer.SetFlexibleDirection( wx.BOTH )
		cu_plot_opt1_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cu_metric_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_txt1.Wrap( -1 )
		cu_plot_opt1_sizer.Add( self.cu_metric_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_hicol_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_hicol_txt1.Wrap( -1 )
		cu_plot_opt1_sizer.Add( self.cu_metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_hicol_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_hicol_txt1.Wrap( -1 )
		cu_plot_opt1_sizer.Add( self.cu_metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_alpha_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_alpha_txt1.Wrap( -1 )
		cu_plot_opt1_sizer.Add( self.cu_metric_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_legend_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_legend_txt1.Wrap( -1 )
		cu_plot_opt1_sizer.Add( self.cu_metric_legend_txt1, 0, wx.ALL, 5 )
		
		cu_metric_choice1Choices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.cu_metric_choice1 = wx.Choice( self.cu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_choice1Choices, 0 )
		self.cu_metric_choice1.SetSelection( 2 )
		cu_plot_opt1_sizer.Add( self.cu_metric_choice1, 0, wx.ALL, 5 )
		
		self.cu_metric_lowcol1 = wx.ColourPickerCtrl( self.cu_plot_opt1, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_lowcol1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		cu_plot_opt1_sizer.Add( self.cu_metric_lowcol1, 0, wx.ALL, 5 )
		
		self.cu_metric_hicol1 = wx.ColourPickerCtrl( self.cu_plot_opt1, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_hicol1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		cu_plot_opt1_sizer.Add( self.cu_metric_hicol1, 0, wx.ALL, 5 )
		
		self.cu_metric_alpha1 = wx.Slider( self.cu_plot_opt1, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		cu_plot_opt1_sizer.Add( self.cu_metric_alpha1, 0, wx.ALL, 5 )
		
		cu_metric_legend1Choices = [ u"Top", u"Bottom", u"None" ]
		self.cu_metric_legend1 = wx.Choice( self.cu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_legend1Choices, 0 )
		self.cu_metric_legend1.SetSelection( 0 )
		cu_plot_opt1_sizer.Add( self.cu_metric_legend1, 0, wx.ALL, 5 )
		
		
		self.cu_plot_opt1.SetSizer( cu_plot_opt1_sizer )
		self.cu_plot_opt1.Layout()
		cu_plot_opt1_sizer.Fit( self.cu_plot_opt1 )
		self.lyr2_choice.AddPage( self.cu_plot_opt1, u"Connectivity Units", True )
		self.pu_poly_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		pu_poly_plot_opt1_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		pu_poly_plot_opt1_sizer.SetFlexibleDirection( wx.BOTH )
		pu_poly_plot_opt1_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.pu_poly_col_txt1 = wx.StaticText( self.pu_poly_plot_opt1, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_poly_col_txt1.Wrap( -1 )
		pu_poly_plot_opt1_sizer.Add( self.pu_poly_col_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_poly_alpha_txt1 = wx.StaticText( self.pu_poly_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_poly_alpha_txt1.Wrap( -1 )
		pu_poly_plot_opt1_sizer.Add( self.pu_poly_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_poly_col1 = wx.ColourPickerCtrl( self.pu_poly_plot_opt1, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_poly_col1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		pu_poly_plot_opt1_sizer.Add( self.pu_poly_col1, 0, wx.ALL, 5 )
		
		self.pu_poly_alpha1 = wx.Slider( self.pu_poly_plot_opt1, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		pu_poly_plot_opt1_sizer.Add( self.pu_poly_alpha1, 0, wx.ALL, 5 )
		
		
		self.pu_poly_plot_opt1.SetSizer( pu_poly_plot_opt1_sizer )
		self.pu_poly_plot_opt1.Layout()
		pu_poly_plot_opt1_sizer.Fit( self.pu_poly_plot_opt1 )
		self.lyr2_choice.AddPage( self.pu_poly_plot_opt1, u"Planning Unit (polygons)", False )
		self.cu_poly_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cu_poly_plot_opt1_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		cu_poly_plot_opt1_sizer.SetFlexibleDirection( wx.BOTH )
		cu_poly_plot_opt1_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cu_poly_col_txt1 = wx.StaticText( self.cu_poly_plot_opt1, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_poly_col_txt1.Wrap( -1 )
		cu_poly_plot_opt1_sizer.Add( self.cu_poly_col_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_poly_alpha_txt1 = wx.StaticText( self.cu_poly_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_poly_alpha_txt1.Wrap( -1 )
		cu_poly_plot_opt1_sizer.Add( self.cu_poly_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_poly_col1 = wx.ColourPickerCtrl( self.cu_poly_plot_opt1, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_poly_col1.SetToolTip( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		cu_poly_plot_opt1_sizer.Add( self.cu_poly_col1, 0, wx.ALL, 5 )
		
		self.cu_poly_alpha1 = wx.Slider( self.cu_poly_plot_opt1, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		cu_poly_plot_opt1_sizer.Add( self.cu_poly_alpha1, 0, wx.ALL, 5 )
		
		
		self.cu_poly_plot_opt1.SetSizer( cu_poly_plot_opt1_sizer )
		self.cu_poly_plot_opt1.Layout()
		cu_poly_plot_opt1_sizer.Fit( self.cu_poly_plot_opt1 )
		self.lyr2_choice.AddPage( self.cu_poly_plot_opt1, u"Connectivity Unit (polygons)", False )
		lyr2_sizer.Add( self.lyr2_choice, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		plottingMainSizer.Add( lyr2_sizer, 1, wx.EXPAND, 5 )
		
		self.plot_map_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Plot Map", wx.DefaultPosition, wx.DefaultSize, 0 )
		plottingMainSizer.Add( self.plot_map_button, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.plot_opt_seperator = wx.StaticLine( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		plottingMainSizer.Add( self.plot_opt_seperator, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.graphoptions = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Graph Plotting Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.graphoptions.Wrap( -1 )
		self.graphoptions.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		plottingMainSizer.Add( self.graphoptions, 0, wx.ALL, 5 )
		
		sizer011 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choice21Choices = []
		self.m_choice21 = wx.Choice( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice21Choices, 0 )
		self.m_choice21.SetSelection( 0 )
		sizer011.Add( self.m_choice21, 0, wx.ALL, 5 )
		
		m_choice11Choices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment", wx.EmptyString ]
		self.m_choice11 = wx.Choice( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		sizer011.Add( self.m_choice11, 0, wx.ALL, 5 )
		
		self.m_colourPicker11 = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		sizer011.Add( self.m_colourPicker11, 0, wx.ALL, 5 )
		
		self.m_colourPicker21 = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		sizer011.Add( self.m_colourPicker21, 0, wx.ALL, 5 )
		
		
		plottingMainSizer.Add( sizer011, 1, wx.EXPAND, 5 )
		
		self.plot_graph_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Plot Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.Bind( wx.EVT_MENU, self.on_glossary, id = self.glossary.GetId() )
		self.Bind( wx.EVT_MENU, self.on_tutorial, id = self.tutorial.GetId() )
		self.Bind( wx.EVT_MENU, self.on_github, id = self.github.GetId() )
		self.Bind( wx.EVT_MENU, self.on_contributing, id = self.contributing.GetId() )
		self.Bind( wx.EVT_MENU, self.on_license, id = self.license.GetId() )
		self.Bind( wx.EVT_MENU, self.on_about, id = self.about.GetId() )
		self.Bind( wx.EVT_MENU, self.on_getting_started, id = self.start.GetId() )
		self.PU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PU_file )
		self.FA_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_FA_file )
		self.demo_matrixUnitsRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_matrixUnitsRadioBox )
		self.demo_matrixTypeRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_matrixTypeRadioBox )
		self.demo_matrixFormatRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_matrixFormatRadioBox )
		self.demo_CU_CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_demo_CU_CM_file )
		self.demo_rescaleRadioBox.Bind( wx.EVT_RADIOBOX, self.on_demo_rescaleRadioBox )
		self.demo_CU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CU_file )
		self.demo_PU_CM_check.Bind( wx.EVT_CHECKBOX, self.on_demo_PU_CM_check )
		self.demo_PU_CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_demo_PU_CM_file )
		self.demo_rescale_button.Bind( wx.EVT_BUTTON, self.on_demo_rescale_button )
		self.CF_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CT_file )
		self.CFT_percent_slider.Bind( wx.EVT_SCROLL, self.on_CFT_percent_slider )
		self.customize_spec.Bind( wx.EVT_BUTTON, self.on_customize_spec )
		self.SPEC_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CT_file_append )
		self.BD_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_BD_file )
		self.calc_metrics.Bind( wx.EVT_BUTTON, self.on_calc_metrics )
		self.export_metrics.Bind( wx.EVT_BUTTON, self.on_export_metrics )
		self.calc_metrics_type.Bind( wx.EVT_CHOICE, self.on_calc_metrics_type )
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
	
	def on_glossary( self, event ):
		event.Skip()
	
	def on_tutorial( self, event ):
		event.Skip()
	
	def on_github( self, event ):
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
	
	def on_FA_file( self, event ):
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
	
	def on_CU_file( self, event ):
		event.Skip()
	
	def on_demo_PU_CM_check( self, event ):
		event.Skip()
	
	def on_demo_PU_CM_file( self, event ):
		event.Skip()
	
	def on_demo_rescale_button( self, event ):
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
	
	def on_calc_metrics( self, event ):
		event.Skip()
	
	def on_export_metrics( self, event ):
		event.Skip()
	
	def on_calc_metrics_type( self, event ):
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
	

