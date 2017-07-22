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

ID_GETTING_STARTED = 1000
ID_DEMOGRAPHIC_INPUT = 1001
ID_GENETIC_INPUT = 1002
ID_LANDSCAPE_INPUT = 1003
ID_CONNECTIVITY_METRICS = 1004
ID_MARXAN_ANALYSIS = 1005
ID_POSTMARXAN_EVALUATION = 1006
ID_PLOT_OPTIONS = 1007

###########################################################################
## Class MarxanConnectGUI
###########################################################################

class MarxanConnectGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 847,786 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.gettingStarted = wx.MenuItem( self.m_menu1, ID_GETTING_STARTED, u"Getting Started", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.gettingStarted )
		
		self.demographicInput = wx.MenuItem( self.m_menu1, ID_DEMOGRAPHIC_INPUT, u"Demographic Input", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.demographicInput )
		self.demographicInput.Check( True )
		
		self.geneticInput = wx.MenuItem( self.m_menu1, ID_GENETIC_INPUT, u"Genetic Input", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.geneticInput )
		self.geneticInput.Check( True )
		
		self.landscapeInput = wx.MenuItem( self.m_menu1, ID_LANDSCAPE_INPUT, u"Landscape Input", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.landscapeInput )
		self.landscapeInput.Check( True )
		
		self.connectivityMetrics = wx.MenuItem( self.m_menu1, ID_CONNECTIVITY_METRICS, u"Connectivity Metrics", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.connectivityMetrics )
		self.connectivityMetrics.Check( True )
		
		self.marxanAnalysis = wx.MenuItem( self.m_menu1, ID_MARXAN_ANALYSIS, u"Marxan Analysis", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.marxanAnalysis )
		self.marxanAnalysis.Check( True )
		
		self.postmarxanEvaluation = wx.MenuItem( self.m_menu1, ID_POSTMARXAN_EVALUATION, u"Post-Marxan Evaluation", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.postmarxanEvaluation )
		self.postmarxanEvaluation.Check( True )
		
		self.plotOptions = wx.MenuItem( self.m_menu1, ID_PLOT_OPTIONS, u"Plot Options", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu1.Append( self.plotOptions )
		self.plotOptions.Check( True )
		
		self.m_menubar1.Append( self.m_menu1, u"View" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_auinotebook2 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.gettingStarted1 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook2.AddPage( self.gettingStarted1, u"Getting Started", False, wx.NullBitmap )
		self.demographicInput1 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		demoMainSizer = wx.FlexGridSizer( 12, 0, 0, 0 )
		demoMainSizer.AddGrowableCol( 0 )
		demoMainSizer.AddGrowableRow( 1 )
		demoMainSizer.AddGrowableRow( 4 )
		demoMainSizer.AddGrowableRow( 6 )
		demoMainSizer.AddGrowableRow( 10 )
		demoMainSizer.SetFlexibleDirection( wx.VERTICAL )
		demoMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.m_staticText39 = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Input:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		self.m_staticText39.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		demoMainSizer.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		sizer0 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PU_def = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Describe Planning Units ...................  text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_def.Wrap( -1 )
		sizer0.Add( self.PU_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer0, 1, wx.EXPAND, 5 )
		
		sizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer1.AddGrowableCol( 1 )
		sizer1.SetFlexibleDirection( wx.HORIZONTAL )
		sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.PU_filetext = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Planning Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_filetext.Wrap( -1 )
		self.PU_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer1.Add( self.PU_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.PU_file = wx.FilePickerCtrl( self.demographicInput1, wx.ID_ANY, u"C:\\Program Files (x86)\\MarxanConnect\\data\\shapefiles\\marxan_pu.shp", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer1.Add( self.PU_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer1, 1, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		rescaleRadioBoxChoices = [ u"Identical Grids", u"Rescale Connectivity Matrix" ]
		self.rescaleRadioBox = wx.RadioBox( self.demographicInput1, wx.ID_ANY, u"Rescale Connectivity Matrix?", wx.DefaultPosition, wx.DefaultSize, rescaleRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.rescaleRadioBox.SetSelection( 1 )
		sizer2.Add( self.rescaleRadioBox, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		demoMainSizer.Add( sizer2, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CU_def = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Describe Connectivity Matrix Shapefile ....................................... text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CU_def.Wrap( -1 )
		sizer3.Add( self.CU_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer3, 1, wx.EXPAND, 5 )
		
		sizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer4.AddGrowableCol( 1 )
		sizer4.SetFlexibleDirection( wx.HORIZONTAL )
		sizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CU_filetext = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Connectivity Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CU_filetext.Wrap( -1 )
		self.CU_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer4.Add( self.CU_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CU_file = wx.FilePickerCtrl( self.demographicInput1, wx.ID_ANY, u"C:\\Program Files (x86)\\MarxanConnect\\data\\shapefiles\\connectivity_grid.shp", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer4.Add( self.CU_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer4, 1, wx.EXPAND, 5 )
		
		sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CM_def = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Dexcribe Connectivity Matrix .......................... text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_def.Wrap( -1 )
		sizer5.Add( self.CM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer5, 1, wx.EXPAND, 5 )
		
		sizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer6.AddGrowableCol( 1 )
		sizer6.SetFlexibleDirection( wx.HORIZONTAL )
		sizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		unitsRadioBoxChoices = [ u"Probability", u"Individuals" ]
		self.unitsRadioBox = wx.RadioBox( self.demographicInput1, wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, unitsRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.unitsRadioBox.SetSelection( 0 )
		sizer6.Add( self.unitsRadioBox, 0, wx.ALL, 5 )
		
		matrixRadioBox4Choices = [ u"Settlement", u"Connectivity", u"Migration", u"Local Immigration", u"Dispersal Flux" ]
		self.matrixRadioBox4 = wx.RadioBox( self.demographicInput1, wx.ID_ANY, u"Connectivity Matrix Type", wx.DefaultPosition, wx.DefaultSize, matrixRadioBox4Choices, 3, wx.RA_SPECIFY_COLS )
		self.matrixRadioBox4.SetSelection( 0 )
		sizer6.Add( self.matrixRadioBox4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer6, 1, wx.ALIGN_CENTER, 5 )
		
		sizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer7.AddGrowableCol( 1 )
		sizer7.SetFlexibleDirection( wx.HORIZONTAL )
		sizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CM_filetext = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_filetext.Wrap( -1 )
		sizer7.Add( self.CM_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CM_file = wx.FilePickerCtrl( self.demographicInput1, wx.ID_ANY, u"C:\\Program Files (x86)\\MarxanConnect\\data\\grid_connectivity_matrix.csv", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer7.Add( self.CM_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer7, 1, wx.EXPAND, 5 )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline2 = wx.StaticLine( self.demographicInput1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizer8.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Output:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		self.m_staticText38.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		sizer8.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		
		demoMainSizer.Add( sizer8, 1, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PUCM_def = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Describe Planning Unit Connectivity Matrix ...................  text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_def.Wrap( -1 )
		sizer9.Add( self.PUCM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer9, 1, wx.EXPAND, 5 )
		
		sizer71 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer71.AddGrowableCol( 1 )
		sizer71.SetFlexibleDirection( wx.HORIZONTAL )
		sizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.PUCM_filedirtext = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Output Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_filedirtext.Wrap( -1 )
		self.PUCM_filedirtext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer71.Add( self.PUCM_filedirtext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.PUCM_filedir = wx.DirPickerCtrl( self.demographicInput1, wx.ID_ANY, u"C:\\Program Files (x86)\\MarxanConnect\\data", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sizer71.Add( self.PUCM_filedir, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.PUCM_filetext = wx.StaticText( self.demographicInput1, wx.ID_ANY, u"Output Filename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_filetext.Wrap( -1 )
		self.PUCM_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer71.Add( self.PUCM_filetext, 0, wx.ALL, 5 )
		
		self.PUCM_filename = wx.TextCtrl( self.demographicInput1, wx.ID_ANY, u"PU_connectivity_matrix.csv", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer71.Add( self.PUCM_filename, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer71, 1, wx.EXPAND, 5 )
		
		
		self.demographicInput1.SetSizer( demoMainSizer )
		self.demographicInput1.Layout()
		demoMainSizer.Fit( self.demographicInput1 )
		self.m_auinotebook2.AddPage( self.demographicInput1, u"Demographic Input", True, wx.NullBitmap )
		self.geneticInput1 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.geneticInput1.Hide()
		
		self.m_auinotebook2.AddPage( self.geneticInput1, u"Genetic Input", False, wx.NullBitmap )
		self.landscapeInput1 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.landscapeInput1.Hide()
		
		self.m_auinotebook2.AddPage( self.landscapeInput1, u"Landscape Input", False, wx.NullBitmap )
		self.connectivityMetrics1 = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook2.AddPage( self.connectivityMetrics1, u"Connectivity Metrics", False, wx.NullBitmap )
		self.marxanAnalysis = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook2.AddPage( self.marxanAnalysis, u"Marxan Analysis", False, wx.NullBitmap )
		self.postMarxan = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook2.AddPage( self.postMarxan, u"Post-Marxan Analysis", False, wx.NullBitmap )
		self.plottingOptions = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		demoMainSizer1 = wx.FlexGridSizer( 12, 0, 0, 0 )
		demoMainSizer1.AddGrowableCol( 0 )
		demoMainSizer1.AddGrowableRow( 1 )
		demoMainSizer1.AddGrowableRow( 4 )
		demoMainSizer1.AddGrowableRow( 6 )
		demoMainSizer1.AddGrowableRow( 10 )
		demoMainSizer1.SetFlexibleDirection( wx.VERTICAL )
		demoMainSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		sizer01 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.plot_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer01.Add( self.plot_button, 0, wx.ALL, 5 )
		
		
		demoMainSizer1.Add( sizer01, 1, wx.EXPAND, 5 )
		
		
		self.plottingOptions.SetSizer( demoMainSizer1 )
		self.plottingOptions.Layout()
		demoMainSizer1.Fit( self.plottingOptions )
		self.m_auinotebook2.AddPage( self.plottingOptions, u"Plotting Options", False, wx.NullBitmap )
		self.plot = wx.Panel( self.m_auinotebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook2.AddPage( self.plot, u"Plot", False, wx.NullBitmap )
		
		bSizer3.Add( self.m_auinotebook2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.PU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PU_file )
		self.rescaleRadioBox.Bind( wx.EVT_RADIOBOX, self.on_rescaleRadioBox )
		self.CU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CU_file )
		self.unitsRadioBox.Bind( wx.EVT_RADIOBOX, self.on_unitsRadioBox )
		self.matrixRadioBox4.Bind( wx.EVT_RADIOBOX, self.on_unitsRadioBox )
		self.CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CM_file )
		self.PUCM_filedir.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_PUCM_filedir )
		self.PUCM_filename.Bind( wx.EVT_TEXT, self.on_PUCM_filenameText )
		self.PUCM_filename.Bind( wx.EVT_TEXT_ENTER, self.on_PUCM_filenameTextEnter )
		self.plot_button.Bind( wx.EVT_BUTTON, self.on_plot_button )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_PU_file( self, event ):
		event.Skip()
	
	def on_rescaleRadioBox( self, event ):
		event.Skip()
	
	def on_CU_file( self, event ):
		event.Skip()
	
	def on_unitsRadioBox( self, event ):
		event.Skip()
	
	
	def on_CM_file( self, event ):
		event.Skip()
	
	def on_PUCM_filedir( self, event ):
		event.Skip()
	
	def on_PUCM_filenameText( self, event ):
		event.Skip()
	
	def on_PUCM_filenameTextEnter( self, event ):
		event.Skip()
	
	def on_plot_button( self, event ):
		event.Skip()
	

