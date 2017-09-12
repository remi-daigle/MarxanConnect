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
		self.file = wx.Menu()
		self.new_project = wx.MenuItem( self.file, wx.ID_ANY, u"New Project"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.new_project )
		
		self.save_project = wx.MenuItem( self.file, wx.ID_ANY, u"Save Project"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.save_project )
		
		self.save_project_as = wx.MenuItem( self.file, wx.ID_ANY, u"Save Project As..."+ u"\t" + u"Ctrl+Shift+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.save_project_as )
		
		self.load_project = wx.MenuItem( self.file, wx.ID_ANY, u"Load Project"+ u"\t" + u"Ctrl+L", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.load_project )
		
		self.m_menubar1.Append( self.file, u"File" ) 
		
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
		
		self.m_menubar1.Append( self.help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_TAB_EXTERNAL_MOVE|wx.aui.AUI_NB_TAB_MOVE|wx.aui.AUI_NB_TAB_SPLIT|wx.aui.AUI_NB_TOP|wx.aui.AUI_NB_WINDOWLIST_BUTTON )
		self.SpatialInput = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		demoMainSizer2 = wx.FlexGridSizer( 0, 1, 0, 0 )
		demoMainSizer2.AddGrowableCol( 0 )
		demoMainSizer2.AddGrowableRow( 1 )
		demoMainSizer2.AddGrowableRow( 2 )
		demoMainSizer2.AddGrowableRow( 4 )
		demoMainSizer2.AddGrowableRow( 5 )
		demoMainSizer2.SetFlexibleDirection( wx.VERTICAL )
		demoMainSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.m_staticText392 = wx.StaticText( self.SpatialInput, wx.ID_ANY, u"Planning Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText392.Wrap( -1 )
		self.m_staticText392.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		demoMainSizer2.Add( self.m_staticText392, 0, wx.ALL, 5 )
		
		sizer0 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PU_def = wx.StaticText( self.SpatialInput, wx.ID_ANY, u"Describe Planning Units ...................  text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_def.Wrap( -1 )
		sizer0.Add( self.PU_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer2.Add( sizer0, 1, wx.EXPAND, 5 )
		
		sizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer1.AddGrowableCol( 1 )
		sizer1.SetFlexibleDirection( wx.HORIZONTAL )
		sizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.PU_filetext = wx.StaticText( self.SpatialInput, wx.ID_ANY, u"Planning Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_filetext.Wrap( -1 )
		self.PU_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer1.Add( self.PU_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.PU_file = wx.FilePickerCtrl( self.SpatialInput, wx.ID_ANY, u"~\\data\\shapefiles\\marxan_pu.shp", u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer1.Add( self.PU_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer2.Add( sizer1, 1, wx.EXPAND, 5 )
		
		self.m_staticText391 = wx.StaticText( self.SpatialInput, wx.ID_ANY, u"Focus Areas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )
		self.m_staticText391.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		demoMainSizer2.Add( self.m_staticText391, 0, wx.ALL, 5 )
		
		sizer01 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PU_def1 = wx.StaticText( self.SpatialInput, wx.ID_ANY, u"For some of the connectivity metrics (e.g. Temporal Connectivity Correlation), it is important to consider 'focus areas' for which connectivity should be optimised. Such focus areas could include existing protected areas, important habitat for endangered species, and/or otherwise important habitats for connectivity (e.g. nursery grounds). Marxan with Connectivity assumes that the planning units within the 'focus areas' will otherwise be targeted as normal conservation targets in Marxan. Loading focus areas into Marxan with Connectivity allows users to set conservation targets for the areas that complement the 'focus areas'", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PU_def1.Wrap( -1 )
		sizer01.Add( self.PU_def1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer2.Add( sizer01, 1, wx.EXPAND, 5 )
		
		sizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer11.AddGrowableCol( 1 )
		sizer11.SetFlexibleDirection( wx.HORIZONTAL )
		sizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.FA_filetext = wx.StaticText( self.SpatialInput, wx.ID_ANY, u"Focus Areas Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FA_filetext.Wrap( -1 )
		self.FA_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer11.Add( self.FA_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.FA_file = wx.FilePickerCtrl( self.SpatialInput, wx.ID_ANY, wx.EmptyString, u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer11.Add( self.FA_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		demoMainSizer2.Add( sizer11, 1, wx.EXPAND, 5 )
		
		
		self.SpatialInput.SetSizer( demoMainSizer2 )
		self.SpatialInput.Layout()
		demoMainSizer2.Fit( self.SpatialInput )
		self.m_auinotebook1.AddPage( self.SpatialInput, u"Spatial Input", False, wx.NullBitmap )
		self.connectivityInput = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.AddGrowableCol( 0 )
		fgSizer25.AddGrowableRow( 0 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_choicebook3 = wx.Choicebook( self.connectivityInput, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.demographic = wx.Panel( self.m_choicebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		connMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		connMainSizer.AddGrowableCol( 0 )
		connMainSizer.AddGrowableRow( 2 )
		connMainSizer.AddGrowableRow( 5 )
		connMainSizer.AddGrowableRow( 8 )
		connMainSizer.SetFlexibleDirection( wx.VERTICAL )
		connMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CM_def = wx.StaticText( self.demographic, wx.ID_ANY, u"Dexcribe Connectivity Matrix .......................... text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_def.Wrap( -1 )
		sizer5.Add( self.CM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		connMainSizer.Add( sizer5, 1, wx.EXPAND, 5 )
		
		sizer6 = wx.FlexGridSizer( 0, 3, 0, 0 )
		sizer6.AddGrowableCol( 1 )
		sizer6.SetFlexibleDirection( wx.HORIZONTAL )
		sizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		unitsRadioBoxChoices = [ u"Probability", u"Individuals" ]
		self.unitsRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, unitsRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.unitsRadioBox.SetSelection( 0 )
		sizer6.Add( self.unitsRadioBox, 0, wx.ALL, 5 )
		
		matrixRadioBox4Choices = [ u"Settlement", u"Connectivity", u"Migration", u"Local Immigration", u"Dispersal Flux" ]
		self.matrixRadioBox4 = wx.RadioBox( self.demographic, wx.ID_ANY, u"Connectivity Matrix Type", wx.DefaultPosition, wx.DefaultSize, matrixRadioBox4Choices, 3, wx.RA_SPECIFY_COLS )
		self.matrixRadioBox4.SetSelection( 1 )
		sizer6.Add( self.matrixRadioBox4, 0, wx.ALL|wx.EXPAND, 5 )
		
		formatRadioBoxChoices = [ u"Matrix", u"List" ]
		self.formatRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Format", wx.DefaultPosition, wx.DefaultSize, formatRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.formatRadioBox.SetSelection( 0 )
		sizer6.Add( self.formatRadioBox, 0, wx.ALL, 5 )
		
		
		connMainSizer.Add( sizer6, 1, wx.ALIGN_CENTER, 5 )
		
		sizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer7.AddGrowableCol( 1 )
		sizer7.SetFlexibleDirection( wx.HORIZONTAL )
		sizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CM_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_filetext.Wrap( -1 )
		self.CM_filetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		sizer7.Add( self.CM_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CM_file = wx.FilePickerCtrl( self.demographic, wx.ID_ANY, u"~\\data\\grid_connectivity_matrix.csv", u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer7.Add( self.CM_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		connMainSizer.Add( sizer7, 1, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText63 = wx.StaticText( self.demographic, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		sizer2.Add( self.m_staticText63, 0, wx.ALL, 5 )
		
		rescaleRadioBoxChoices = [ u"Identical Grids", u"Rescale Connectivity Matrix" ]
		self.rescaleRadioBox = wx.RadioBox( self.demographic, wx.ID_ANY, u"Rescale Connectivity Matrix?", wx.DefaultPosition, wx.DefaultSize, rescaleRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.rescaleRadioBox.SetSelection( 1 )
		sizer2.Add( self.rescaleRadioBox, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		connMainSizer.Add( sizer2, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CU_def = wx.StaticText( self.demographic, wx.ID_ANY, u"Describe Connectivity Matrix Shapefile ....................................... text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CU_def.Wrap( -1 )
		sizer3.Add( self.CU_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		connMainSizer.Add( sizer3, 1, wx.EXPAND, 5 )
		
		sizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer4.AddGrowableCol( 1 )
		sizer4.SetFlexibleDirection( wx.HORIZONTAL )
		sizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CU_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Connectivity Unit Shapefile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CU_filetext.Wrap( -1 )
		self.CU_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer4.Add( self.CU_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CU_file = wx.FilePickerCtrl( self.demographic, wx.ID_ANY, u"~\\data\\shapefiles\\connectivity_grid.shp", u"Select a file", u"ESRI Shapefile (*.shp)|*.shp|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sizer4.Add( self.CU_file, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		connMainSizer.Add( sizer4, 1, wx.EXPAND, 5 )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline2 = wx.StaticLine( self.demographic, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizer8.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.PUCM_outputtext = wx.StaticText( self.demographic, wx.ID_ANY, u"Output:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_outputtext.Wrap( -1 )
		self.PUCM_outputtext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		sizer8.Add( self.PUCM_outputtext, 0, wx.ALL, 5 )
		
		
		connMainSizer.Add( sizer8, 1, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PUCM_def = wx.StaticText( self.demographic, wx.ID_ANY, u"Describe Planning Unit Connectivity Matrix ...................  text text text text text text text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text texttext text text text text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_def.Wrap( -1 )
		sizer9.Add( self.PUCM_def, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		connMainSizer.Add( sizer9, 1, wx.EXPAND, 5 )
		
		sizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer10.AddGrowableCol( 1 )
		sizer10.SetFlexibleDirection( wx.HORIZONTAL )
		sizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.PUCM_filetext = wx.StaticText( self.demographic, wx.ID_ANY, u"Output Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PUCM_filetext.Wrap( -1 )
		self.PUCM_filetext.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial" ) )
		
		sizer10.Add( self.PUCM_filetext, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.PUCM_file = wx.FilePickerCtrl( self.demographic, wx.ID_ANY, u"~\\Documents\\PU_connectivity_matrix.csv", u"Select a file", u"Comma Separated Values (*.csv)|*.csv|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		sizer10.Add( self.PUCM_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		connMainSizer.Add( sizer10, 1, wx.EXPAND, 5 )
		
		self.rescale_button = wx.Button( self.demographic, wx.ID_ANY, u"Rescale Connectivity Matrix", wx.DefaultPosition, wx.DefaultSize, 0 )
		connMainSizer.Add( self.rescale_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.demographic.SetSizer( connMainSizer )
		self.demographic.Layout()
		connMainSizer.Fit( self.demographic )
		self.m_choicebook3.AddPage( self.demographic, u"Demographic Input", True )
		self.genetic = wx.Panel( self.m_choicebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_choicebook3.AddPage( self.genetic, u"Genetic Input", False )
		self.landscape = wx.Panel( self.m_choicebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_choicebook3.AddPage( self.landscape, u"Landscape Input", False )
		fgSizer25.Add( self.m_choicebook3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.connectivityInput.SetSizer( fgSizer25 )
		self.connectivityInput.Layout()
		fgSizer25.Fit( self.connectivityInput )
		self.m_auinotebook1.AddPage( self.connectivityInput, u"Connectivity Input", False, wx.NullBitmap )
		self.connectivityMetrics = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		metricsMainSizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		metricsMainSizer.AddGrowableCol( 0 )
		metricsMainSizer.AddGrowableRow( 1 )
		metricsMainSizer.AddGrowableRow( 4 )
		metricsMainSizer.SetFlexibleDirection( wx.BOTH )
		metricsMainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText19 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Conservation Targets", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		metricsMainSizer.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
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
		self.ct_demo_vertex_degree.SetValue(True) 
		self.ct_demo_vertex_degree.SetToolTipString( u"The vertex degree indicates the number of connections for each planning unit" )
		
		bSizer9.Add( self.ct_demo_vertex_degree, 0, wx.ALL, 5 )
		
		self.ct_demo_between_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Betweenness Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ct_demo_between_cent.SetValue(True) 
		self.ct_demo_between_cent.SetToolTipString( u"Betweenness Centrality is an indicator of a planning unit's centrality in a network. It is equal to the number of shortest paths from all connections to all others that pass through that planning unit." )
		
		bSizer9.Add( self.ct_demo_between_cent, 0, wx.ALL, 5 )
		
		self.ct_demo_eig_vect_cent = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Eigen Vector Centrality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ct_demo_eig_vect_cent.SetValue(True) 
		self.ct_demo_eig_vect_cent.SetToolTipString( u"Eigen Vector Centrality is a measure of the influence of a planning unit in a network. It assigns relative scores to all planning unitin the network based on the concept that connections to high-scoring planning unit contribute more to the score of the planning unit in question than equal connections to low-scoring nodes" )
		
		bSizer9.Add( self.ct_demo_eig_vect_cent, 0, wx.ALL, 5 )
		
		self.ct_demo_self_recruit = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Self Recruitment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ct_demo_self_recruit.SetValue(True) 
		self.ct_demo_self_recruit.SetToolTipString( u"Self Recruitment is the propotion of new recruits from a planning unit that will stay in that planning unit." )
		
		bSizer9.Add( self.ct_demo_self_recruit, 0, wx.ALL, 5 )
		
		self.ct_demo_stochasticity = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Temporal Connectivity Correlation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ct_demo_stochasticity.SetValue(True) 
		bSizer9.Add( self.ct_demo_stochasticity, 0, wx.ALL, 5 )
		
		
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
		
		
		metricsMainSizer.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		metricsMainSizer.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText161 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"Boundary Definition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		self.m_staticText161.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		metricsMainSizer.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
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
		bSizer131.Add( self.bd_demo_conn_boundary, 0, wx.ALL, 5 )
		
		self.bd_demo_min_plan_graph = wx.CheckBox( self.connectivityMetrics, wx.ID_ANY, u"Minimum Planar Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bd_demo_min_plan_graph.SetValue(True) 
		bSizer131.Add( self.bd_demo_min_plan_graph, 0, wx.ALL, 5 )
		
		
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
		
		
		metricsMainSizer.Add( fgSizer81, 1, wx.EXPAND, 5 )
		
		self.m_staticline5 = wx.StaticLine( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		metricsMainSizer.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer20 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer20.AddGrowableCol( 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.spacertext = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spacertext.Wrap( -1 )
		fgSizer20.Add( self.spacertext, 0, wx.ALL, 5 )
		
		self.calc_metrics = wx.Button( self.connectivityMetrics, wx.ID_ANY, u"Calculate Metrics", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.calc_metrics, 0, wx.ALL, 5 )
		
		self.m_staticText53 = wx.StaticText( self.connectivityMetrics, wx.ID_ANY, u"For:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		fgSizer20.Add( self.m_staticText53, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		calc_metrics_typeChoices = [ u"Planning Units", u"Connectivity Units" ]
		self.calc_metrics_type = wx.Choice( self.connectivityMetrics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, calc_metrics_typeChoices, 0 )
		self.calc_metrics_type.SetSelection( 0 )
		fgSizer20.Add( self.calc_metrics_type, 0, wx.ALL, 5 )
		
		
		metricsMainSizer.Add( fgSizer20, 1, wx.EXPAND, 5 )
		
		
		self.connectivityMetrics.SetSizer( metricsMainSizer )
		self.connectivityMetrics.Layout()
		metricsMainSizer.Fit( self.connectivityMetrics )
		self.m_auinotebook1.AddPage( self.connectivityMetrics, u"Connectivity Metrics", True, wx.NullBitmap )
		self.marxanAnalysis = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.marxanAnalysis, u"Marxan Analysis", False, wx.NullBitmap )
		self.postMarxan = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.postMarxan, u"Post-Marxan Analysis", False, wx.NullBitmap )
		self.plottingOptions = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		demoMainSizer1 = wx.FlexGridSizer( 15, 0, 0, 0 )
		demoMainSizer1.AddGrowableCol( 0 )
		demoMainSizer1.AddGrowableRow( 2 )
		demoMainSizer1.AddGrowableRow( 4 )
		demoMainSizer1.AddGrowableRow( 6 )
		demoMainSizer1.AddGrowableRow( 7 )
		demoMainSizer1.AddGrowableRow( 10 )
		demoMainSizer1.SetFlexibleDirection( wx.BOTH )
		demoMainSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.mapoptions = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Map Plotting Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mapoptions.Wrap( -1 )
		self.mapoptions.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		
		demoMainSizer1.Add( self.mapoptions, 0, wx.ALL, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bmap_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Basemap:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_txt.Wrap( -1 )
		self.bmap_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer22.Add( self.bmap_txt, 0, wx.ALL, 5 )
		
		self.bmap_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bmap_plot_check.SetValue(True) 
		bSizer22.Add( self.bmap_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		demoMainSizer1.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		bmap_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
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
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr1_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"First Layer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr1_txt.Wrap( -1 )
		self.lyr1_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer19.Add( self.lyr1_txt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.lyr1_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr1_plot_check.SetValue(True) 
		bSizer19.Add( self.lyr1_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		demoMainSizer1.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		lyr1_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr1_choice = wx.Choicebook( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_TOP )
		self.pu_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer111 = wx.FlexGridSizer( 2, 5, 0, 0 )
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
		
		self.pu_metric_legend_txt = wx.StaticText( self.pu_plot_opt, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_legend_txt.Wrap( -1 )
		fgSizer111.Add( self.pu_metric_legend_txt, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		pu_metric_choiceChoices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.pu_metric_choice = wx.Choice( self.pu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_choiceChoices, 0 )
		self.pu_metric_choice.SetSelection( 2 )
		fgSizer111.Add( self.pu_metric_choice, 0, wx.ALL, 5 )
		
		self.pu_metric_lowcol = wx.ColourPickerCtrl( self.pu_plot_opt, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_lowcol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer111.Add( self.pu_metric_lowcol, 0, wx.ALL, 5 )
		
		self.pu_metric_hicol = wx.ColourPickerCtrl( self.pu_plot_opt, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.pu_metric_hicol.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer111.Add( self.pu_metric_hicol, 0, wx.ALL, 5 )
		
		self.pu_metric_alpha = wx.Slider( self.pu_plot_opt, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer111.Add( self.pu_metric_alpha, 0, wx.ALL, 5 )
		
		pu_metric_legendChoices = [ u"Top", u"Bottom", u"None" ]
		self.pu_metric_legend = wx.Choice( self.pu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_legendChoices, 0 )
		self.pu_metric_legend.SetSelection( 1 )
		fgSizer111.Add( self.pu_metric_legend, 0, wx.ALL, 5 )
		
		
		self.pu_plot_opt.SetSizer( fgSizer111 )
		self.pu_plot_opt.Layout()
		fgSizer111.Fit( self.pu_plot_opt )
		self.lyr1_choice.AddPage( self.pu_plot_opt, u"Planning Units", True )
		self.cu_plot_opt = wx.Panel( self.lyr1_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer11 = wx.FlexGridSizer( 0, 5, 0, 0 )
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
		
		self.cu_metric_legend_txt = wx.StaticText( self.cu_plot_opt, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_legend_txt.Wrap( -1 )
		fgSizer11.Add( self.cu_metric_legend_txt, 0, wx.ALL, 5 )
		
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
		
		cu_metric_legendChoices = [ u"Top", u"Bottom", u"None" ]
		self.cu_metric_legend = wx.Choice( self.cu_plot_opt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_legendChoices, 0 )
		self.cu_metric_legend.SetSelection( 1 )
		fgSizer11.Add( self.cu_metric_legend, 0, wx.ALL, 5 )
		
		
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
		self.lyr1_choice.AddPage( self.pu_poly_plot_opt, u"Planning Unit (polygons)", False )
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
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr2_txt = wx.StaticText( self.plottingOptions, wx.ID_ANY, u"Second Layer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr2_txt.Wrap( -1 )
		self.lyr2_txt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		
		bSizer20.Add( self.lyr2_txt, 0, wx.ALL, 5 )
		
		self.lyr2_plot_check = wx.CheckBox( self.plottingOptions, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lyr2_plot_check.SetValue(True) 
		bSizer20.Add( self.lyr2_plot_check, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		demoMainSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		lyr2_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lyr2_choice = wx.Choicebook( self.plottingOptions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_TOP )
		self.pu_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1111 = wx.FlexGridSizer( 0, 5, 0, 0 )
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
		
		self.pu_metric_legend_txt1 = wx.StaticText( self.pu_plot_opt1, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pu_metric_legend_txt1.Wrap( -1 )
		fgSizer1111.Add( self.pu_metric_legend_txt1, 0, wx.ALL, 5 )
		
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
		
		self.pu_metric_alpha1 = wx.Slider( self.pu_plot_opt1, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer1111.Add( self.pu_metric_alpha1, 0, wx.ALL, 5 )
		
		pu_metric_legend1Choices = [ u"Top", u"Bottom", u"None" ]
		self.pu_metric_legend1 = wx.Choice( self.pu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pu_metric_legend1Choices, 0 )
		self.pu_metric_legend1.SetSelection( 0 )
		fgSizer1111.Add( self.pu_metric_legend1, 0, wx.ALL, 5 )
		
		
		self.pu_plot_opt1.SetSizer( fgSizer1111 )
		self.pu_plot_opt1.Layout()
		fgSizer1111.Fit( self.pu_plot_opt1 )
		self.lyr2_choice.AddPage( self.pu_plot_opt1, u"Planning Units", False )
		self.cu_plot_opt1 = wx.Panel( self.lyr2_choice, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer112 = wx.FlexGridSizer( 0, 5, 0, 0 )
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
		
		self.cu_metric_legend_txt1 = wx.StaticText( self.cu_plot_opt1, wx.ID_ANY, u"Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cu_metric_legend_txt1.Wrap( -1 )
		fgSizer112.Add( self.cu_metric_legend_txt1, 0, wx.ALL, 5 )
		
		cu_metric_choice1Choices = [ u"Vertex Degree", u"Betweenness Centrality", u"Eigen Vector Centrality", u"Self Recruitment" ]
		self.cu_metric_choice1 = wx.Choice( self.cu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_choice1Choices, 0 )
		self.cu_metric_choice1.SetSelection( 2 )
		fgSizer112.Add( self.cu_metric_choice1, 0, wx.ALL, 5 )
		
		self.cu_metric_lowcol1 = wx.ColourPickerCtrl( self.cu_plot_opt1, wx.ID_ANY, wx.Colour( 255, 247, 236 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_lowcol1.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer112.Add( self.cu_metric_lowcol1, 0, wx.ALL, 5 )
		
		self.cu_metric_hicol1 = wx.ColourPickerCtrl( self.cu_plot_opt1, wx.ID_ANY, wx.Colour( 127, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.cu_metric_hicol1.SetToolTipString( u"Double-click on the colour box, or manually enter colour values in the text box (as shown or hex format, e.g. #fff7ec)" )
		
		fgSizer112.Add( self.cu_metric_hicol1, 0, wx.ALL, 5 )
		
		self.cu_metric_alpha1 = wx.Slider( self.cu_plot_opt1, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer112.Add( self.cu_metric_alpha1, 0, wx.ALL, 5 )
		
		cu_metric_legend1Choices = [ u"Top", u"Bottom", u"None" ]
		self.cu_metric_legend1 = wx.Choice( self.cu_plot_opt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_metric_legend1Choices, 0 )
		self.cu_metric_legend1.SetSelection( 0 )
		fgSizer112.Add( self.cu_metric_legend1, 0, wx.ALL, 5 )
		
		
		self.cu_plot_opt1.SetSizer( fgSizer112 )
		self.cu_plot_opt1.Layout()
		fgSizer112.Fit( self.cu_plot_opt1 )
		self.lyr2_choice.AddPage( self.cu_plot_opt1, u"Connectivity Units", True )
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
		
		self.pu_poly_alpha1 = wx.Slider( self.pu_poly_plot_opt1, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer11122.Add( self.pu_poly_alpha1, 0, wx.ALL, 5 )
		
		
		self.pu_poly_plot_opt1.SetSizer( fgSizer11122 )
		self.pu_poly_plot_opt1.Layout()
		fgSizer11122.Fit( self.pu_poly_plot_opt1 )
		self.lyr2_choice.AddPage( self.pu_poly_plot_opt1, u"Planning Unit (polygons)", False )
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
		
		self.cu_poly_alpha1 = wx.Slider( self.cu_poly_plot_opt1, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer111211.Add( self.cu_poly_alpha1, 0, wx.ALL, 5 )
		
		
		self.cu_poly_plot_opt1.SetSizer( fgSizer111211 )
		self.cu_poly_plot_opt1.Layout()
		fgSizer111211.Fit( self.cu_poly_plot_opt1 )
		self.lyr2_choice.AddPage( self.cu_poly_plot_opt1, u"Connectivity Unit (polygons)", False )
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
		self.m_auinotebook1.AddPage( self.plottingOptions, u"Plotting Options", False, wx.NullBitmap )
		
		bSizer3.Add( self.m_auinotebook1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
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
		self.unitsRadioBox.Bind( wx.EVT_RADIOBOX, self.on_unitsRadioBox )
		self.matrixRadioBox4.Bind( wx.EVT_RADIOBOX, self.on_unitsRadioBox )
		self.formatRadioBox.Bind( wx.EVT_RADIOBOX, self.on_formatRadioBox )
		self.CM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CM_file )
		self.rescaleRadioBox.Bind( wx.EVT_RADIOBOX, self.on_rescaleRadioBox )
		self.CU_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_CU_file )
		self.PUCM_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_PUCM_file )
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
	
	def on_unitsRadioBox( self, event ):
		event.Skip()
	
	
	def on_formatRadioBox( self, event ):
		event.Skip()
	
	def on_CM_file( self, event ):
		event.Skip()
	
	def on_rescaleRadioBox( self, event ):
		event.Skip()
	
	def on_CU_file( self, event ):
		event.Skip()
	
	def on_PUCM_file( self, event ):
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
	

