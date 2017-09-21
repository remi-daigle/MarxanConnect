import numpy
import geopandas as gpd
import pandas
import igraph
import wx


def rescale_matrix(pu_filepath,cu_filepath,cm_filepath,progressbar=False):
    """
    rescale the connectivity matrix to match the scale of the planning units
    """
    # load shapefiles
    pu = gpd.GeoDataFrame.from_file(pu_filepath)
    cu = gpd.GeoDataFrame.from_file(cu_filepath)

    # quantify intersectional area
    if progressbar:
        dlg = wx.ProgressDialog("Rescale Connectivity Matrix",
                                "Please wait while the rescaled connectivity matrix is being generated.",
                                maximum = pu.shape[0]*10,
                                parent=None,
                                style = wx.PD_CAN_ABORT
                                | wx.PD_APP_MODAL
                                | wx.PD_ELAPSED_TIME
                                | wx.PD_ESTIMATED_TIME
                                | wx.PD_REMAINING_TIME
                                )
    con_mat_pu = []
    count=0
    for index, puID in pu.iterrows():
        count += 1
        dlg.Update(count)
        for index2, connID in cu.iterrows():
           if puID.geometry.intersects(connID.geometry):
               con_mat_pu.append({'geometry': puID.geometry.intersection(connID.geometry), 'puID':puID.ID, 'connID': connID.ID, 'puIndex': index, 'connIndex': index2,'int_area': puID.geometry.intersection(connID.geometry).area, 'conn_area': connID.geometry.area, 'pu_area': puID.geometry.area})


    # make intersection GeoDataFrame
    df = gpd.GeoDataFrame(con_mat_pu,columns=['geometry', 'puID', 'connID', 'puIndex', 'connIndex', 'int_area', 'conn_area', 'pu_area'])

    # load cu connectivity matrix
    grid_conmat = pandas.read_csv(cm_filepath,index_col= 0).as_matrix()

    # populate rescaled pu connecectivity matrix
    pu_conmat = numpy.zeros((len(pu),len(pu)))
    for source in pu.ID:
        count += 9
        dlg.Update(count)
        for sink in pu.ID:
            sources=df.puID==source
            sinks=df.puID==sink
            if any(sinks) and any(source):
                temp_conn=grid_conmat[df.connIndex[sources],:][:,df.connIndex[sinks]]
                cov_source=df.int_area[sources]/sum(df.int_area[sources])
                cov_sink=df.int_area[sinks]/sum(df.int_area[sinks])
                pu_conmat[numpy.array(pu.ID==source),numpy.array(pu.ID==sink)]=sum(sum(((temp_conn*numpy.array(cov_sink)).T*numpy.array(cov_source))))
            else:
                pu_conmat[numpy.array(pu.ID==source),numpy.array(pu.ID==sink)]=0

    pu_conmat = pandas.DataFrame(pu_conmat, index=pu.ID, columns=pu.ID)
    pu_conmat.index.name = "puID"
    if progressbar:
        dlg.Destroy()
    return pu_conmat


def buffer_shp_corners(gdf_list, bufferwidth = 0):
    """
    Finds the lower left and upper right corners of a list of geopandas.GeoDataFrame objects. Optionally define a buffer (in degrees) around the list GeoDataFrames
    """
    lonmin = 181
    lonmax = -181
    latmin = 91
    latmax = -91
    for g in gdf_list:
        lonmintemp = g.total_bounds[0] - bufferwidth
        lonmaxtemp = g.total_bounds[2] + bufferwidth
        latmintemp = g.total_bounds[1] - bufferwidth
        latmaxtemp = g.total_bounds[3] + bufferwidth
        if(lonmintemp<lonmin): lonmin = lonmintemp
        if(lonmaxtemp>lonmax): lonmax = lonmaxtemp
        if(latmintemp<latmin): latmin = latmintemp
        if(latmaxtemp>latmax): latmax = latmaxtemp
    return lonmin, lonmax, latmin, latmax

def conmat2vertexdegree(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist())
    vertexdegree = g.degree()
    return vertexdegree

def conmat2betweencent(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist())
    betweencent = g.betweenness()
    return betweencent

def conmat2eigvectcent(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist())
    eigvectcent = g.evcent()
    return eigvectcent

def conmat2selfrecruit(conmat):
    selfrecruit = numpy.diag(conmat.as_matrix()).tolist()
    return selfrecruit

def conmat2connboundary(conmat):
    cm = conmat.copy()
    cm['id1'] = cm.index
    boundary_dat = cm.melt(id_vars=['id1'])
    boundary_dat.columns = ['id1', 'id2', 'boundary']
    boundary_dat = boundary_dat.to_json(orient='split')
    return boundary_dat

def conmat2minplanarboundary(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist()).spanning_tree()
    mpgmat = g.get_adjacency().data
    mpgmat = pandas.DataFrame(mpgmat)
    mpgmat.columns = conmat.columns
    mpgmat['id1'] = conmat.index
    boundary_dat = mpgmat.melt(id_vars=['id1'])
    boundary_dat.columns = ['id1', 'id2', 'boundary']
    boundary_dat = boundary_dat.to_json(orient='split')
    return boundary_dat
