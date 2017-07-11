# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 28 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MarxanConnectGUI
###########################################################################

class MarxanConnectGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marxan Connect", pos = wx.DefaultPosition, size = wx.Size( 700,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook1.SetMinSize( wx.Size( 666,-1 ) )
		
		self.Spatial = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.defpufile = wx.StaticText( self.Spatial, wx.ID_ANY, u"Description of planning units: blah blah blah blahblah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defpufile.Wrap( 666 )
		fgSizer3.Add( self.defpufile, 0, wx.ALL, 5 )
		
		pu_file = wx.FlexGridSizer( 0, 2, 0, 0 )
		pu_file.SetFlexibleDirection( wx.BOTH )
		pu_file.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.Spatial, wx.ID_ANY, u"Planning Unit Shapefile:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		pu_file.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self.Spatial, wx.ID_ANY, u"data\\shapefiles\\marxan_pu.shp", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker1.SetMinSize( wx.Size( 500,-1 ) )
		
		pu_file.Add( self.m_filePicker1, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( pu_file, 1, wx.ALIGN_RIGHT, 5 )
		
		self.defcongrid = wx.StaticText( self.Spatial, wx.ID_ANY, u"Description of Connectivity Matrix: blah blah blah blahblah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defcongrid.Wrap( 666 )
		fgSizer3.Add( self.defcongrid, 0, wx.ALL, 5 )
		
		conmat = wx.FlexGridSizer( 0, 2, 0, 0 )
		conmat.SetFlexibleDirection( wx.BOTH )
		conmat.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText12 = wx.StaticText( self.Spatial, wx.ID_ANY, u"Grid Connectivity Matrix:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		conmat.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_filePicker12 = wx.FilePickerCtrl( self.Spatial, wx.ID_ANY, u"data\\grid_connectivity_matrix.csv", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker12.SetMinSize( wx.Size( 500,-1 ) )
		
		conmat.Add( self.m_filePicker12, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( conmat, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.defcongrid1 = wx.StaticText( self.Spatial, wx.ID_ANY, u"Description of Connectivity Grid: blah blah blah blahblah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah (if the scale and shape of the planning units matches the grid on which connectivity was assessed, leave Connectivity Grid Shapefile blank)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defcongrid1.Wrap( 666 )
		fgSizer3.Add( self.defcongrid1, 0, wx.ALL, 5 )
		
		m_radioBox2Choices = [ u"Identical grids", u"Rescale Connectivity Matrix" ]
		self.m_radioBox2 = wx.RadioBox( self.Spatial, wx.ID_ANY, u"Rescale Connectivity?", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox2.SetSelection( 0 )
		fgSizer3.Add( self.m_radioBox2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		congrid = wx.FlexGridSizer( 0, 2, 0, 0 )
		congrid.SetFlexibleDirection( wx.BOTH )
		congrid.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self.Spatial, wx.ID_ANY, u"Connectivity Grid Shapefile:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		congrid.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_filePicker11 = wx.FilePickerCtrl( self.Spatial, wx.ID_ANY, u"data\\shapefiles\\marxan_pu.shp", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker11.SetMinSize( wx.Size( 500,-1 ) )
		
		congrid.Add( self.m_filePicker11, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( congrid, 1, wx.ALIGN_RIGHT, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.Spatial, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.RescalingOutput1 = wx.StaticText( self.Spatial, wx.ID_ANY, u"Rescaling Output:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RescalingOutput1.Wrap( -1 )
		fgSizer11.Add( self.RescalingOutput1, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer11, 1, wx.EXPAND, 5 )
		
		fgSizer111 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer111.SetFlexibleDirection( wx.BOTH )
		fgSizer111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.filename = wx.StaticText( self.Spatial, wx.ID_ANY, u"Filename:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.filename.Wrap( -1 )
		fgSizer111.Add( self.filename, 0, wx.ALL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self.Spatial, wx.ID_ANY, u"pu_connectivity_matrix.csv", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl11.SetMinSize( wx.Size( 500,-1 ) )
		
		fgSizer111.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		self.directory = wx.StaticText( self.Spatial, wx.ID_ANY, u"Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.directory.Wrap( -1 )
		fgSizer111.Add( self.directory, 0, wx.ALL, 5 )
		
		self.m_dirPicker11 = wx.DirPickerCtrl( self.Spatial, wx.ID_ANY, u"data\\\n", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker11.SetMinSize( wx.Size( 500,-1 ) )
		
		fgSizer111.Add( self.m_dirPicker11, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer111, 1, wx.ALIGN_RIGHT, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.rescale = wx.Button( self.Spatial, wx.ID_ANY, u"Rescale", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.rescale, 0, wx.ALL, 5 )
		
		self.next = wx.Button( self.Spatial, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.next, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( wSizer2, 1, wx.ALIGN_RIGHT, 5 )
		
		
		self.Spatial.SetSizer( fgSizer3 )
		self.Spatial.Layout()
		fgSizer3.Fit( self.Spatial )
		self.m_notebook1.AddPage( self.Spatial, u"Spatial", False )
		self.Objectves = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		self.Objectves.SetSizer( fgSizer9 )
		self.Objectves.Layout()
		fgSizer9.Fit( self.Objectves )
		self.m_notebook1.AddPage( self.Objectves, u"Objectives", False )
		self.Metrics = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		self.Metrics.SetSizer( fgSizer5 )
		self.Metrics.Layout()
		fgSizer5.Fit( self.Metrics )
		self.m_notebook1.AddPage( self.Metrics, u"Metrics", True )
		self.PostMarxan = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		self.PostMarxan.SetSizer( fgSizer10 )
		self.PostMarxan.Layout()
		fgSizer10.Fit( self.PostMarxan )
		self.m_notebook1.AddPage( self.PostMarxan, u"Post-Marxan", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_SIZE, self.resizeAll )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def resizeAll( self, event ):
		event.Skip()
	

