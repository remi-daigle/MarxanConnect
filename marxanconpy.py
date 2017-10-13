import numpy
import geopandas as gpd
import pandas
import igraph
import wx
import os


def rescale_matrix(pu_filepath,pu_id,cu_filepath,cu_id,cm_filepath,matrixformat,progressbar=False):
    """
    rescale the connectivity matrix to match the scale of the planning units
    """
    # load shapefiles
    pu = gpd.GeoDataFrame.from_file(pu_filepath).to_crs({'init': 'epsg:4326'})
    cu = gpd.GeoDataFrame.from_file(cu_filepath).to_crs({'init': 'epsg:4326'})

    # load cu connectivity matrix
    # load correct demographic matrix and transform if necessary
    time=False
    if os.path.isfile(cm_filepath):
        if matrixformat == "Matrix":
            grid_conmat = pandas.read_csv(cm_filepath,index_col=0).as_matrix()
        elif matrixformat == "List":
            grid_conmat = pandas.read_csv(cm_filepath)
            grid_conmat = grid_conmat.pivot_table(values='value', index='id1',columns='id2').as_matrix()
        elif matrixformat == "List with Time":
            grid_conmat_time = pandas.read_csv(cm_filepath)
            grid_conmat = grid_conmat_time[['id1', 'id2', 'value']].groupby(['id1', 'id2']).mean()
            grid_conmat = grid_conmat.pivot_table(values='value', index='id1',columns='id2').as_matrix()
            time=True


    # quantify intersectional area
    if progressbar:
        if time:
            max = pu.shape[0] * 10 * len( grid_conmat_time['time'].unique())
        else:
            max = pu.shape[0] * 10
        dlg = wx.ProgressDialog("Rescale Connectivity Matrix",
                                "Please wait while the rescaled connectivity matrix is being generated.",
                                maximum = max,
                                parent=None,
                                style = wx.PD_AUTO_HIDE
                                | wx.PD_ELAPSED_TIME
                                | wx.PD_ESTIMATED_TIME
                                | wx.PD_REMAINING_TIME
                                )
        count = 0

    con_mat_pu = []
    for index, puID in pu.iterrows():
        if progressbar:
            count += 1
            dlg.Update(count)
        for index2, connID in cu.iterrows():
           if puID.geometry.intersects(connID.geometry):
               con_mat_pu.append({'geometry': puID.geometry.intersection(connID.geometry), 'puID':puID[pu_id], 'connID': connID[cu_id], 'puIndex': index, 'connIndex': index2,'int_area': puID.geometry.intersection(connID.geometry).area, 'conn_area': connID.geometry.area, 'pu_area': puID.geometry.area})


    # make intersection GeoDataFrame
    df = gpd.GeoDataFrame(con_mat_pu,columns=['geometry', 'puID', 'connID', 'puIndex', 'connIndex', 'int_area', 'conn_area', 'pu_area'])


    # populate rescaled pu connectivity matrix
    pu_conmat = numpy.zeros((len(pu),len(pu)))
    for source in pu[pu_id]:
        if progressbar:
            count += 9
            dlg.Update(count)
        for sink in pu[pu_id]:
            sources=df.puID==source
            sinks=df.puID==sink
            if any(sinks) and any(sources):
                temp_conn=grid_conmat[df.connIndex[sources],:][:,df.connIndex[sinks]]
                cov_source=df.int_area[sources]/sum(df.int_area[sources])
                cov_sink=df.int_area[sinks]/sum(df.int_area[sinks])
                pu_conmat[numpy.array(pu[pu_id]==source),numpy.array(pu[pu_id]==sink)]=sum(sum(((temp_conn*numpy.array(cov_sink)).T*numpy.array(cov_source))))
            else:
                pu_conmat[numpy.array(pu[pu_id]==source),numpy.array(pu[pu_id]==sink)]=0

    pu_conmat = pandas.DataFrame(pu_conmat, index=pu[pu_id], columns=pu[pu_id])
    pu_conmat.index.name = "puID"

    if time:
        # populate rescaled pu connectivity matrix
        for t in grid_conmat_time['time'].unique():
            pu_conmat_t = numpy.zeros((len(pu), len(pu)))
            for source in pu[pu_id]:
                if progressbar:
                    count += 9
                    dlg.Update(count)
                for sink in pu[pu_id]:
                    sources = df.puID == source
                    sinks = df.puID == sink
                    if any(sinks) and any(source):
                        temp_conn = grid_conmat[df.connIndex[sources], :][:, df.connIndex[sinks]]
                        cov_source = df.int_area[sources] / sum(df.int_area[sources])
                        cov_sink = df.int_area[sinks] / sum(df.int_area[sinks])
                        pu_conmat_t[numpy.array(pu[pu_id] == source), numpy.array(pu[pu_id] == sink)] = sum(
                            sum(((temp_conn * numpy.array(cov_sink)).T * numpy.array(cov_source))))
                    else:
                        pu_conmat_t[numpy.array(pu[pu_id] == source), numpy.array(pu[pu_id] == sink)] = 0

            pu_conmat_t = pandas.DataFrame(pu_conmat_t, index=pu[pu_id], columns=pu[pu_id])
            pu_conmat_t['id1'] = pu_conmat_t.index
            pu_conmat_t['time'] = t
            if t==grid_conmat_time['time'].unique()[0]:
                pu_conmat['id1'] = pu_conmat.index
                pu_conmat['time'] = 'mean'
            pu_conmat = pu_conmat.append(pu_conmat_t)
        # pu_conmat_time = pu_conmat.melt(id_vars=['time','id1'], var_name='id2', value_name='value')

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

def conmat2outflux(conmat):
    conmat.as_matrix().sum(1).tolist()
    return conmat.as_matrix().sum(1).tolist()

def conmat2selfrecruit(conmat):
    selfrecruit = numpy.diag(conmat.as_matrix()).tolist()
    return selfrecruit

def get_intersect_id(area_filepath, pu_filepath,pu_id='ID'):
    area = gpd.GeoDataFrame.from_file(area_filepath)
    pu = gpd.GeoDataFrame.from_file(pu_filepath)

    area_id = ()
    for index, arearow in area.iterrows():
        for index, purow in pu.iterrows():
            if purow.geometry.intersects(arearow.geometry):
                area_id = area_id + (purow[pu_id],)
                break
    return area_id

def conmat2sink(conmat, area_filepath, pu_filepath, pu_id='ID'):
    area_id = get_intersect_id(area_filepath, pu_filepath, pu_id)
    cm = conmat.copy().as_matrix()
    for i in conmat.index:
        if i in area_id:
            cm[conmat.index == i,:] = 0
    return cm.sum(0).tolist()


def conmat2source(conmat, area_filepath, pu_filepath, pu_id='ID'):
    area_id = get_intersect_id(area_filepath, pu_filepath, pu_id)
    cm = conmat.copy().as_matrix()
    for i in conmat.index:
        if i in area_id:
            cm[:, conmat.index == i] = 0
    return cm.sum(1).tolist()

def conmat2connboundary(conmat):
    cm = conmat.copy()
    cm['id1'] = cm.index
    boundary_dat = cm.melt(id_vars=['id1'])
    boundary_dat.columns = ['id1', 'id2', 'boundary']
    boundary_dat = boundary_dat.query('boundary>0').to_json(orient='split')
    return boundary_dat

def conmat2minplanarboundary(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist()).spanning_tree()
    mpgmat = g.get_adjacency().data
    mpgmat = pandas.DataFrame(mpgmat)
    mpgmat.columns = conmat.columns
    mpgmat['id1'] = conmat.index
    boundary_dat = mpgmat.melt(id_vars=['id1'])
    boundary_dat.columns = ['id1', 'id2', 'boundary']
    boundary_dat = boundary_dat.query('boundary>0').to_json(orient='split')
    return boundary_dat

def conmattime2temp_conn_cov(conmat_time, fa_filepath, pu_filepath):
    fa = gpd.GeoDataFrame.from_file(fa_filepath)
    pu = gpd.GeoDataFrame.from_file(pu_filepath)


    fa_id = ()
    for index, farow in fa.iterrows():
        for index, purow in pu.iterrows():
            if purow.geometry.intersects(farow.geometry):
                fa_id = fa_id + (purow.ID,)
                break
    if any([fid in conmat_time.id2.unique().tolist() for fid in fa_id]):
        cov_list = []
        for fa1 in fa_id:
            for fa2 in fa_id:
                if not fa1 == fa2:
                    con_fa = conmat_time.value[(conmat_time.id1 == fa1) & (conmat_time.id2 == fa2)]
                    for id1 in fa_id:
                        for id2 in conmat_time.id2.unique():
                            if not id1 == id2:
                                cov = \
                                numpy.cov(con_fa, conmat_time.value[(conmat_time.id1 == id1) &
                                                                    (conmat_time.id2 == id2)])[0, 1]
                                cov_list.append({'id2': id2, 'cov': cov})
        cov_list = pandas.DataFrame.from_dict(cov_list)

        score = -cov_list.groupby('id2').sum()
        return score['cov'].tolist()
    else:
        return [0] * len(conmat_time.id2.unique())
