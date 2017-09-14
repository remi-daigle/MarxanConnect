import numpy
import geopandas as gpd
import pandas
import igraph


def rescale_matrix(pu_filepath,cu_filepath,cm_filepath,pucm_filepath):
    """
    rescale the connectivity matrix to match the scale of the planning units
    """
    # load shapefiles
    pu = gpd.GeoDataFrame.from_file(pu_filepath)
    cu = gpd.GeoDataFrame.from_file(cu_filepath)

    # quantify intersectional area
    con_mat_pu = []
    for index, puID in pu.iterrows():
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
    pu_conmat.to_csv(pucm_filepath, index=True, header=True, sep=",")

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
    print(conmat.shape)
    cm = conmat.copy()
    cm['id1'] = cm.index
    boundary_dat = cm.melt(id_vars=['id1'])
    boundary_dat.columns = ['id1', 'id2', 'boundary']
    boundary_dat = boundary_dat.to_json(orient='split')
    print(conmat.shape)
    return boundary_dat

def conmat2minplanarboundary(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist()).spanning_tree()
    mpgmat = g.get_adjacency().data
    mpgmat = pandas.DataFrame(mpgmat)
    mpgmat['id1'] = mpgmat.index
    boundary_dat = mpgmat.melt(id_vars=['id1'])
    boundary_dat.columns = ['id1', 'id2', 'boundary']
    boundary_dat = boundary_dat.to_json(orient='split')
    return boundary_dat



# pu_filepath = r'C:\Program Files (x86)\MarxanConnect\data\shapefiles\marxan_pu.shp'
# cu_filepath = r'C:\Program Files (x86)\MarxanConnect\data\shapefiles\connectivity_grid.shp'

# pu = gpd.GeoDataFrame.from_file(pu_filepath)
#
# cm_filedir = r'C:\Program Files (x86)\MarxanConnect\data'
# cm_filename='connectivity_matrix.csv'
# cm_filepath = os.path.join(pucm_filedir, pucm_filename)
#

# pucm_filedir=r'C:\Users\Remi-Work\Documents'
# pucm_filename='PU_connectivity_matrix.csv'
# pucm_filepath = os.path.join(pucm_filedir, pucm_filename)
# conmat = pandas.read_csv(os.path.join(pucm_filedir, pucm_filename),index_col=0)
# eigvectcent=conmat2eigvectcent(conmat)
#
# conmat = pandas.read_csv(os.path.join(pucm_filedir, pucm_filename))
# boundary_dat = conmat.melt(id_vars=['puID'])
# boundary_dat.columns = ['id1', 'id2', 'boundary']
