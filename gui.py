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

###########################################################################
## Class MarxanConnectGUI
###########################################################################

class MarxanConnectGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marxan with Connectivity", pos = wx.DefaultPosition, size = wx.Size( 1005,786 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.new_project = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"New Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.new_project )
		
		self.save_project = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Save Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.save_project )
		
		self.load_project = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Load Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.load_project )
		
		self.m_menubar1.Append( self.m_menu2, u"File" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menubar1.Append( self.m_menu3, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_TAB_EXTERNAL_MOVE|wx.aui.AUI_NB_TAB_MOVE|wx.aui.AUI_NB_TAB_SPLIT|wx.aui.AUI_NB_TOP|wx.aui.AUI_NB_WINDOWLIST_BUTTON )
		self.gettingStarted = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.gettingStarted.Enable( False )
		self.gettingStarted.Hide()
		
		self.m_auinotebook1.AddPage( self.gettingStarted, u"Getting Started", False, wx.NullBitmap )
		self.demographicInput = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		demoMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		demoMainSizer.AddGrowableCol( 0 )
		demoMainSizer.AddGrowableRow( 1 )
		demoMainSizer.AddGrowableRow( 4 )
		demoMainSizer.AddGrowableRow( 6 )
		demoMainSizer.AddGrowableRow( 10 )
		demoMainSizer.SetFlexibleDirection( wx.VERTICAL )
		demoMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.m_staticText39 = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Input:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		self.m_staticText39.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		demoMainSizer.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		sizer0 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PU_def = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Describe Planning Units ...................  text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_def.Wrap( -1 )
		sizer0.Add( self.PU_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer0, 1, wx.EXPAND, 5 )
		
		sizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer1.AddGrowableCol( 1 )
		sizer1.SetFlexibleDirection( wx.HORIZONTAL )
		sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.PU_filetext = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Planning Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_filetext.Wrap( -1 )
		self.PU_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer1.Add( self.PU_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.PU_file = wx.FilePickerCtrl( self.demographicInput, wx.ID_ANY, u"~\\data\\shapefiles\\marxan_pu.shp", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer1.Add( self.PU_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer1, 1, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		rescaleRadioBoxChoices = [ u"Identical Grids", u"Rescale Connectivity Matrix" ]
		self.rescaleRadioBox = wx.RadioBox( self.demographicInput, wx.ID_ANY, u"Rescale Connectivity Matrix?", wx.DefaultPosition, wx.DefaultSize, rescaleRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.rescaleRadioBox.SetSelection( 1 )
		sizer2.Add( self.rescaleRadioBox, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		demoMainSizer.Add( sizer2, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CU_def = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Describe Connectivity Matrix Shapefile ....................................... text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CU_def.Wrap( -1 )
		sizer3.Add( self.CU_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer3, 1, wx.EXPAND, 5 )
		
		sizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer4.AddGrowableCol( 1 )
		sizer4.SetFlexibleDirection( wx.HORIZONTAL )
		sizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CU_filetext = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Connectivity Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CU_filetext.Wrap( -1 )
		self.CU_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer4.Add( self.CU_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CU_file = wx.FilePickerCtrl( self.demographicInput, wx.ID_ANY, u"~\\data\\shapefiles\\connectivity_grid.shp", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer4.Add( self.CU_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer4, 1, wx.EXPAND, 5 )
		
		sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CM_def = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Dexcribe Connectivity Matrix .......................... text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_def.Wrap( -1 )
		sizer5.Add( self.CM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer5, 1, wx.EXPAND, 5 )
		
		sizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer6.AddGrowableCol( 1 )
		sizer6.SetFlexibleDirection( wx.HORIZONTAL )
		sizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		unitsRadioBoxChoices = [ u"Probability", u"Individuals" ]
		self.unitsRadioBox = wx.RadioBox( self.demographicInput, wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, unitsRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.unitsRadioBox.SetSelection( 0 )
		sizer6.Add( self.unitsRadioBox, 0, wx.ALL, 5 )
		
		matrixRadioBox4Choices = [ u"Settlement", u"Connectivity", u"Migration", u"Local Immigration", u"Dispersal Flux" ]
		self.matrixRadioBox4 = wx.RadioBox( self.demographicInput, wx.ID_ANY, u"Connectivity Matrix Type", wx.DefaultPosition, wx.DefaultSize, matrixRadioBox4Choices, 3, wx.RA_SPECIFY_COLS )
		self.matrixRadioBox4.SetSelection( 1 )
		sizer6.Add( self.matrixRadioBox4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer6, 1, wx.ALIGN_CENTER, 5 )
		
		sizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer7.AddGrowableCol( 1 )
		sizer7.SetFlexibleDirection( wx.HORIZONTAL )
		sizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CM_filetext = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_filetext.Wrap( -1 )
		sizer7.Add( self.CM_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CM_file = wx.FilePickerCtrl( self.demographicInput, wx.ID_ANY, u"~\\data\\grid_connectivity_matrix.csv", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer7.Add( self.CM_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer7, 1, wx.EXPAND, 5 )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline2 = wx.StaticLine( self.demographicInput, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizer8.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Output:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		self.m_staticText38.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		sizer8.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		
		demoMainSizer.Add( sizer8, 1, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PUCM_def = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Describe Planning Unit Connectivity Matrix ...................  text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_def.Wrap( -1 )
		sizer9.Add( self.PUCM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer9, 1, wx.EXPAND, 5 )
		
		sizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer10.AddGrowableCol( 1 )
		sizer10.SetFlexibleDirection( wx.HORIZONTAL )
		sizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.PUCM_filedirtext = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Output Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_filedirtext.Wrap( -1 )
		self.PUCM_filedirtext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer10.Add( self.PUCM_filedirtext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.PUCM_filedir = wx.DirPickerCtrl( self.demographicInput, wx.ID_ANY, u"~\\documents", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sizer10.Add( self.PUCM_filedir, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.PUCM_filetext = wx.StaticText( self.demographicInput, wx.ID_ANY, u"Output Filename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_filetext.Wrap( -1 )
		self.PUCM_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer10.Add( self.PUCM_filetext, 0, wx.ALL, 5 )
		
		self.PUCM_filename = wx.TextCtrl( self.demographicInput, wx.ID_ANY, u"PU_connectivity_matrix.csv", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer10.Add( self.PUCM_filename, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer.Add( sizer10, 1, wx.EXPAND, 5 )
		
		self.rescale_button = wx.Button( self.demographicInput, wx.ID_ANY, u"Rescale Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		demoMainSizer.Add( self.rescale_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.demographicInput.SetSizer( demoMainSizer )
		self.demographicInput.Layout()
		demoMainSizer.Fit( self.demographicInput )
		self.m_auinotebook1.AddPage( self.demographicInput, u"Demographic Input", False, wx.NullBitmap )
		self.geneticInput = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.geneticInput, u"Genetic Input", False, wx.NullBitmap )
		self.landscapeInput = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.landscapeInput, u"Landscape Input", False, wx.NullBitmap )
		self.connectivityMetrics = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer9 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer9.AddGrowableCol( 0 )
		fgSizer9.AddGrowableRow( 1 )
		fgSizer9.AddGrowableRow( 4 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText19 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Conservation Targets", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		fgSizer9.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer8.AddGrowableCol( 0 )
		fgSizer8.AddGrowableCol( 1 )
		fgSizer8.AddGrowableCol( 2 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.demo_ct = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Demographic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.demo_ct.Wrap( -1 )
		self.demo_ct.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer9.Add( self.demo_ct, 0, wx.ALL, 5 )
		
		self.ct_demo_vertex_degree = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Vertex Degree", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ct_demo_vertex_degree.SetToolTipString( u"The vertex degree indicates the number of connections for each planning unit" )
		
		bSizer9.Add( self.ct_demo_vertex_degree, 0, wx.ALL, 5 )
		
		self.ct_demo_between_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Betweenness Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ct_demo_between_cent.SetToolTipString( u"Betweenness Centrality is an indicator of a planning unit's centrality in a network. It is equal to the number of shortest paths from all connections to all others that pass through that planning unit" )
		
		bSizer9.Add( self.ct_demo_between_cent, 0, wx.ALL, 5 )
		
		self.ct_demo_eig_vect_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Eigen Vector Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ct_demo_eig_vect_cent.SetValue(True) 
		self.ct_demo_eig_vect_cent.SetToolTipString( u"Eigen Vector Centrality is a measure of the influence of a planning unit in a network. It assigns relative scores to all planning unitin the network based on the concept that connections to high-scoring planning unit contribute more to the score of the planning unit in question than equal connections to low-scoring nodes" )
		
		bSizer9.Add( self.ct_demo_eig_vect_cent, 0, wx.ALL, 5 )
		
		self.ct_demo_self_recruit = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Self Recruitment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ct_demo_self_recruit.SetToolTipString( u"Self Recruitment is the propotion of new recruits from a planning unit that will stay in that planning unit." )
		
		bSizer9.Add( self.ct_demo_self_recruit, 0, wx.ALL, 5 )
		
		
		fgSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText13 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Genetic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer10.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		
		fgSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer11.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		
		fgSizer8.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		fgSizer9.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer9.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText161 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Boundary Definition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		self.m_staticText161.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		fgSizer9.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
		fgSizer81 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer81.AddGrowableCol( 0 )
		fgSizer81.AddGrowableCol( 1 )
		fgSizer81.AddGrowableCol( 2 )
		fgSizer81.SetFlexibleDirection( wx.BOTH )
		fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText171 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Demographic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		self.m_staticText171.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer131.Add( self.m_staticText171, 0, wx.ALL, 5 )
		
		self.bd_demo_conn_boundary = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Connectivity as boundary", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_demo_conn_boundary.SetValue(True) 
		bSizer131.Add( self.bd_demo_conn_boundary, 0, wx.ALL, 5 )
		
		
		fgSizer81.Add( bSizer131, 1, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText181 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Genetic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )
		self.m_staticText181.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer141.Add( self.m_staticText181, 0, wx.ALL, 5 )
		
		
		fgSizer81.Add( bSizer141, 1, wx.EXPAND, 5 )
		
		bSizer211 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText201 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )
		self.m_staticText201.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer211.Add( self.m_staticText201, 0, wx.ALL, 5 )
		
		
		fgSizer81.Add( bSizer211, 1, wx.EXPAND, 5 )
		
		
		fgSizer9.Add( fgSizer81, 1, wx.EXPAND, 5 )
		
		self.m_staticline5 = wx.StaticLine( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer9.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.calc_metrics = wx.Button( self.connectivityMetrics, wx.ID_ANY, u"Calculate Metrics", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.calc_metrics, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.connectivityMetrics.SetSizer( fgSizer9 )
		self.connectivityMetrics.Layout()
		fgSizer9.Fit( self.connectivityMetrics )
		self.m_auinotebook1.AddPage( self.connectivityMetrics, u"Connectivity Metrics", False, wx.NullBitmap )
		self.marxanAnalysis = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.marxanAnalysis, u"Marxan Analysis", False, wx.NullBitmap )
		self.postMarxan = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.postMarxan, u"Post-Marxan Analysis", False, wx.NullBitmap )
		self.plottingOptions = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		demoMainSizer1 = wx.FlexGridSizer( 15, 0, 0, 0 )
		demoMainSizer1.AddGrowableCol( 0 )
		demoMainSizer1.AddGrowableRow( 7 )
		demoMainSizer1.AddGrowableRow( 10 )
		demoMainSizer1.SetFlexibleDirection( wx.BOTH )
		demoMainSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.mapoptions = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Map Plotting Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mapoptions.Wrap( -1 )
		demoMainSizer1.Add( self.mapoptions, 0, wx.ALL, 5 )
		
		self.bmap_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Basemap:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_txt.Wrap( -1 )
		demoMainSizer1.Add( self.bmap_txt, 0, wx.ALL, 5 )
		
		bmap_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bmap_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_plot_check.SetValue(True) 
		bmap_sizer.Add( self.bmap_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		fgSizer113 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer113.SetFlexibleDirection( wx.BOTH )
		fgSizer113.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bmap_landcol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Land Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_landcol_txt.Wrap( -1 )
		fgSizer113.Add( self.bmap_landcol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.bmap_lakecol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Lake Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_lakecol_txt.Wrap( -1 )
		fgSizer113.Add( self.bmap_lakecol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.bmap_oceancol_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Ocean Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_oceancol_txt.Wrap( -1 )
		fgSizer113.Add( self.bmap_oceancol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.bmap_buffer_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Buffer (degrees)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_buffer_txt.Wrap( -1 )
		fgSizer113.Add( self.bmap_buffer_txt, 0, wx.ALL, 5 )
		
		self.bmap_landcol = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.Colour( 221, 170, 102 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.bmap_landcol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer113.Add( self.bmap_landcol, 0, wx.ALL, 5 )
		
		self.bmap_lakecol = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.Colour( 176, 196, 222 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.bmap_lakecol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer113.Add( self.bmap_lakecol, 0, wx.ALL, 5 )
		
		self.bmap_oceancol = wx.ColourPickerCtrl( self.plottingOptions, wx.ID_ANY, wx.Colour( 135, 206, 250 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.bmap_oceancol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer113.Add( self.bmap_oceancol, 0, wx.ALL, 5 )
		
		self.bmap_buffer = wx.TextCtrl( self.plottingOptions, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_buffer.SetToolTipString( u"Spatial Buffer around the shapefiles measured in decimal degrees" )
		
		fgSizer113.Add( self.bmap_buffer, 0, wx.ALL, 5 )
		
		
		bmap_sizer.Add( fgSizer113, 1, wx.EXPAND, 5 )
		
		
		demoMainSizer1.Add( bmap_sizer, 1, wx.EXPAND, 5 )
		
		self.lyr1_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"First Layer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr1_txt.Wrap( -1 )
		demoMainSizer1.Add( self.lyr1_txt, 0, wx.ALL, 5 )
		
		lyr1_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr1_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr1_plot_check.SetValue(True) 
		lyr1_sizer.Add( self.lyr1_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.lyr1_choice = wx.Choicebook( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_LEFT )
		self.pu_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer111 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer111.SetFlexibleDirection( wx.BOTH )
		fgSizer111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.pu_metric_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_txt.Wrap( -1 )
		fgSizer111.Add( self.pu_metric_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_hicol_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_hicol_txt.Wrap( -1 )
		fgSizer111.Add( self.pu_metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_hicol_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_hicol_txt.Wrap( -1 )
		fgSizer111.Add( self.pu_metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_alpha_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_alpha_txt.Wrap( -1 )
		fgSizer111.Add( self.pu_metric_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		pu_metric_choiceChoices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.pu_metric_choice = wx.Choice( self.pu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_choiceChoices, 0 )
		self.pu_metric_choice.SetSelection( 0 )
		fgSizer111.Add( self.pu_metric_choice, 0, wx.ALL, 5 )
		
		self.pu_metric_lowcol = wx.ColourPickerCtrl( self.pu_plot_opt, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_lowcol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer111.Add( self.pu_metric_lowcol, 0, wx.ALL, 5 )
		
		self.pu_metric_hicol = wx.ColourPickerCtrl( self.pu_plot_opt, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_hicol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer111.Add( self.pu_metric_hicol, 0, wx.ALL, 5 )
		
		self.pu_metric_alpha = wx.Slider( self.pu_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer111.Add( self.pu_metric_alpha, 0, wx.ALL, 5 )
		
		
		self.pu_plot_opt.SetSizer( fgSizer111 )
		self.pu_plot_opt.Layout()
		fgSizer111.Fit( self.pu_plot_opt )
		self.lyr1_choice.AddPage( self.pu_plot_opt, u"Planning Units", True )
		self.cu_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer11 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cu_metric_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_txt.Wrap( -1 )
		fgSizer11.Add( self.cu_metric_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_hicol_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_hicol_txt.Wrap( -1 )
		fgSizer11.Add( self.cu_metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_hicol_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_hicol_txt.Wrap( -1 )
		fgSizer11.Add( self.cu_metric_hicol_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_alpha_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_alpha_txt.Wrap( -1 )
		fgSizer11.Add( self.cu_metric_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		cu_metric_choiceChoices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.cu_metric_choice = wx.Choice( self.cu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_choiceChoices, 0 )
		self.cu_metric_choice.SetSelection( 0 )
		fgSizer11.Add( self.cu_metric_choice, 0, wx.ALL, 5 )
		
		self.cu_metric_lowcol = wx.ColourPickerCtrl( self.cu_plot_opt, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_lowcol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer11.Add( self.cu_metric_lowcol, 0, wx.ALL, 5 )
		
		self.cu_metric_hicol = wx.ColourPickerCtrl( self.cu_plot_opt, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_hicol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer11.Add( self.cu_metric_hicol, 0, wx.ALL, 5 )
		
		self.cu_metric_alpha = wx.Slider( self.cu_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer11.Add( self.cu_metric_alpha, 0, wx.ALL, 5 )
		
		
		self.cu_plot_opt.SetSizer( fgSizer11 )
		self.cu_plot_opt.Layout()
		fgSizer11.Fit( self.cu_plot_opt )
		self.lyr1_choice.AddPage( self.cu_plot_opt, u"Connectivity Units", False )
		self.pu_poly_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1112 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1112.SetFlexibleDirection( wx.BOTH )
		fgSizer1112.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.pu_poly_col_txt = wx.StaticText( self.pu_poly_plot_opt, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_poly_col_txt.Wrap( -1 )
		fgSizer1112.Add( self.pu_poly_col_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_poly_alpha_txt = wx.StaticText( self.pu_poly_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_poly_alpha_txt.Wrap( -1 )
		fgSizer1112.Add( self.pu_poly_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_poly_col = wx.ColourPickerCtrl( self.pu_poly_plot_opt, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_poly_col.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer1112.Add( self.pu_poly_col, 0, wx.ALL, 5 )
		
		self.pu_poly_alpha = wx.Slider( self.pu_poly_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer1112.Add( self.pu_poly_alpha, 0, wx.ALL, 5 )
		
		
		self.pu_poly_plot_opt.SetSizer( fgSizer1112 )
		self.pu_poly_plot_opt.Layout()
		fgSizer1112.Fit( self.pu_poly_plot_opt )
		self.lyr1_choice.AddPage( self.pu_poly_plot_opt, u"Planing Unit (polygons)", False )
		self.cu_poly_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer11121 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11121.SetFlexibleDirection( wx.BOTH )
		fgSizer11121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cu_poly_col_txt = wx.StaticText( self.cu_poly_plot_opt, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_poly_col_txt.Wrap( -1 )
		fgSizer11121.Add( self.cu_poly_col_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_poly_alpha_txt = wx.StaticText( self.cu_poly_plot_opt, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_poly_alpha_txt.Wrap( -1 )
		fgSizer11121.Add( self.cu_poly_alpha_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_poly_col = wx.ColourPickerCtrl( self.cu_poly_plot_opt, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_poly_col.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer11121.Add( self.cu_poly_col, 0, wx.ALL, 5 )
		
		self.cu_poly_alpha = wx.Slider( self.cu_poly_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer11121.Add( self.cu_poly_alpha, 0, wx.ALL, 5 )
		
		
		self.cu_poly_plot_opt.SetSizer( fgSizer11121 )
		self.cu_poly_plot_opt.Layout()
		fgSizer11121.Fit( self.cu_poly_plot_opt )
		self.lyr1_choice.AddPage( self.cu_poly_plot_opt, u"Connectivity Unit (polygons)", False )
		lyr1_sizer.Add( self.lyr1_choice, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		demoMainSizer1.Add( lyr1_sizer, 1, wx.EXPAND, 5 )
		
		self.lyr2_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Second Layer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr2_txt.Wrap( -1 )
		demoMainSizer1.Add( self.lyr2_txt, 0, wx.ALL, 5 )
		
		lyr2_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr2_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr2_plot_check.SetValue(True) 
		lyr2_sizer.Add( self.lyr2_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.lyr2_choice = wx.Choicebook( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_LEFT )
		self.pu_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1111 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer1111.SetFlexibleDirection( wx.BOTH )
		fgSizer1111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.pu_metric_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_txt1.Wrap( -1 )
		fgSizer1111.Add( self.pu_metric_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_hicol_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_hicol_txt1.Wrap( -1 )
		fgSizer1111.Add( self.pu_metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_hicol_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_hicol_txt1.Wrap( -1 )
		fgSizer1111.Add( self.pu_metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_metric_alpha_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_alpha_txt1.Wrap( -1 )
		fgSizer1111.Add( self.pu_metric_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		pu_metric_choice1Choices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.pu_metric_choice1 = wx.Choice( self.pu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_choice1Choices, 0 )
		self.pu_metric_choice1.SetSelection( 0 )
		fgSizer1111.Add( self.pu_metric_choice1, 0, wx.ALL, 5 )
		
		self.pu_metric_lowcol1 = wx.ColourPickerCtrl( self.pu_plot_opt1, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_lowcol1.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer1111.Add( self.pu_metric_lowcol1, 0, wx.ALL, 5 )
		
		self.pu_metric_hicol1 = wx.ColourPickerCtrl( self.pu_plot_opt1, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_hicol1.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer1111.Add( self.pu_metric_hicol1, 0, wx.ALL, 5 )
		
		self.pu_metric_alpha1 = wx.Slider( self.pu_plot_opt1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer1111.Add( self.pu_metric_alpha1, 0, wx.ALL, 5 )
		
		
		self.pu_plot_opt1.SetSizer( fgSizer1111 )
		self.pu_plot_opt1.Layout()
		fgSizer1111.Fit( self.pu_plot_opt1 )
		self.lyr2_choice.AddPage( self.pu_plot_opt1, u"Planning Units", False )
		self.cu_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer112 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer112.SetFlexibleDirection( wx.BOTH )
		fgSizer112.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cu_metric_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"Metric", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_txt1.Wrap( -1 )
		fgSizer112.Add( self.cu_metric_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_hicol_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"Low Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_hicol_txt1.Wrap( -1 )
		fgSizer112.Add( self.cu_metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_hicol_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"High Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_hicol_txt1.Wrap( -1 )
		fgSizer112.Add( self.cu_metric_hicol_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_metric_alpha_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_alpha_txt1.Wrap( -1 )
		fgSizer112.Add( self.cu_metric_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		cu_metric_choice1Choices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.cu_metric_choice1 = wx.Choice( self.cu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_choice1Choices, 0 )
		self.cu_metric_choice1.SetSelection( 0 )
		fgSizer112.Add( self.cu_metric_choice1, 0, wx.ALL, 5 )
		
		self.cu_metric_lowcol1 = wx.ColourPickerCtrl( self.cu_plot_opt1, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_lowcol1.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer112.Add( self.cu_metric_lowcol1, 0, wx.ALL, 5 )
		
		self.cu_metric_hicol1 = wx.ColourPickerCtrl( self.cu_plot_opt1, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_hicol1.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer112.Add( self.cu_metric_hicol1, 0, wx.ALL, 5 )
		
		self.cu_metric_alpha1 = wx.Slider( self.cu_plot_opt1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer112.Add( self.cu_metric_alpha1, 0, wx.ALL, 5 )
		
		
		self.cu_plot_opt1.SetSizer( fgSizer112 )
		self.cu_plot_opt1.Layout()
		fgSizer112.Fit( self.cu_plot_opt1 )
		self.lyr2_choice.AddPage( self.cu_plot_opt1, u"Connectivity Units", False )
		self.pu_poly_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer11122 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11122.SetFlexibleDirection( wx.BOTH )
		fgSizer11122.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.pu_poly_col_txt1 = wx.StaticText( self.pu_poly_plot_opt1, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_poly_col_txt1.Wrap( -1 )
		fgSizer11122.Add( self.pu_poly_col_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_poly_alpha_txt1 = wx.StaticText( self.pu_poly_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_poly_alpha_txt1.Wrap( -1 )
		fgSizer11122.Add( self.pu_poly_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.pu_poly_col1 = wx.ColourPickerCtrl( self.pu_poly_plot_opt1, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_poly_col1.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer11122.Add( self.pu_poly_col1, 0, wx.ALL, 5 )
		
		self.pu_poly_alpha1 = wx.Slider( self.pu_poly_plot_opt1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer11122.Add( self.pu_poly_alpha1, 0, wx.ALL, 5 )
		
		
		self.pu_poly_plot_opt1.SetSizer( fgSizer11122 )
		self.pu_poly_plot_opt1.Layout()
		fgSizer11122.Fit( self.pu_poly_plot_opt1 )
		self.lyr2_choice.AddPage( self.pu_poly_plot_opt1, u"Planing Unit (polygons)", False )
		self.cu_poly_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer111211 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer111211.SetFlexibleDirection( wx.BOTH )
		fgSizer111211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cu_poly_col_txt1 = wx.StaticText( self.cu_poly_plot_opt1, wx.ID_ANY, u"Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_poly_col_txt1.Wrap( -1 )
		fgSizer111211.Add( self.cu_poly_col_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_poly_alpha_txt1 = wx.StaticText( self.cu_poly_plot_opt1, wx.ID_ANY, u"Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_poly_alpha_txt1.Wrap( -1 )
		fgSizer111211.Add( self.cu_poly_alpha_txt1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.cu_poly_col1 = wx.ColourPickerCtrl( self.cu_poly_plot_opt1, wx.ID_ANY, wx.Colour( 153, 142, 195 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_poly_col1.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer111211.Add( self.cu_poly_col1, 0, wx.ALL, 5 )
		
		self.cu_poly_alpha1 = wx.Slider( self.cu_poly_plot_opt1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer111211.Add( self.cu_poly_alpha1, 0, wx.ALL, 5 )
		
		
		self.cu_poly_plot_opt1.SetSizer( fgSizer111211 )
		self.cu_poly_plot_opt1.Layout()
		fgSizer111211.Fit( self.cu_poly_plot_opt1 )
		self.lyr2_choice.AddPage( self.cu_poly_plot_opt1, u"Connectivity Unit (polygons)", True )
		lyr2_sizer.Add( self.lyr2_choice, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		demoMainSizer1.Add( lyr2_sizer, 1, wx.EXPAND, 5 )
		
		self.plot_map_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Plot Map", wx.DefaultPosition, wx.DefaultSize, 0 )
		demoMainSizer1.Add( self.plot_map_button, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		demoMainSizer1.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.graphoptions = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Graph Plotting Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.graphoptions.Wrap( -1 )
		self.graphoptions.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		demoMainSizer1.Add( self.graphoptions, 0, wx.ALL, 5 )
		
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
		
		
		demoMainSizer1.Add( sizer011, 1, wx.EXPAND, 5 )
		
		self.plot_graph_button = wx.Button( self.plottingOptions, wx.ID_ANY, u"Plot Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		demoMainSizer1.Add( self.plot_graph_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.plottingOptions.SetSizer( demoMainSizer1 )
		self.plottingOptions.Layout()
		demoMainSizer1.Fit( self.plottingOptions )
		self.m_auinotebook1.AddPage( self.plottingOptions, u"Plotting Options", True, wx.NullBitmap )
		
		bSizer3.Add( self.m_auinotebook1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_new_project, id = self.new_project.GetId() )
		self.Bind( wx.EVT_MENU, self.on_save_project, id = self.save_project.GetId() )
		self.Bind( wx.EVT_MENU, self.on_load_project, id = self.load_project.GetId() )
		self.PU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PU_file )
		self.rescaleRadioBox.Bind( wx.EVT_RADIOBOX, self.on_rescaleRadioBox )
		self.CU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CU_file )
		self.unitsRadioBox.Bind( wx.EVT_RADIOBOX, self.on_unitsRadioBox )
		self.matrixRadioBox4.Bind( wx.EVT_RADIOBOX, self.on_unitsRadioBox )
		self.CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CM_file )
		self.PUCM_filedir.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_PUCM_filedir )
		self.PUCM_filename.Bind( wx.EVT_TEXT_ENTER, self.on_PUCM_filenameTextEnter )
		self.rescale_button.Bind( wx.EVT_BUTTON, self.on_rescale_button )
		self.calc_metrics.Bind( wx.EVT_BUTTON, self.on_calc_metrics )
		self.lyr1_choice.Bind( wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.testcolourbox )
		self.lyr2_choice.Bind( wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.testcolourbox )
		self.plot_map_button.Bind( wx.EVT_BUTTON, self.on_plot_map_button )
		self.plot_graph_button.Bind( wx.EVT_BUTTON, self.on_plot_graph_button )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_new_project( self, event ):
		event.Skip()
	
	def on_save_project( self, event ):
		event.Skip()
	
	def on_load_project( self, event ):
		event.Skip()
	
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
	
	def on_PUCM_filenameTextEnter( self, event ):
		event.Skip()
	
	def on_rescale_button( self, event ):
		event.Skip()
	
	def on_calc_metrics( self, event ):
		event.Skip()
	
	def testcolourbox( self, event ):
		event.Skip()
	
	
	def on_plot_map_button( self, event ):
		event.Skip()
	
	def on_plot_graph_button( self, event ):
		event.Skip()
	

