import numpy
import geopandas as gpd
import pandas
import igraph

def conmat2vertexdegree(conmat,mode='ALL'):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist())
    vertexdegree = g.degree(mode=mode)
    return vertexdegree

def conmat2betweencent(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist())
    betweencent = g.betweenness()
    return betweencent

def conmat2eigvectcent(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist())
    eigvectcent = g.evcent(weights='weight')
    return eigvectcent

def conmat2google(conmat):
    g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist())
    eigvectcent = g.pagerank(weights='weight')
    return eigvectcent

def conmat2outflow(conmat):
    cm = conmat.copy().as_matrix()
    numpy.fill_diagonal(cm, 0)
    return cm.sum(1).tolist()

def conmat2inflow(conmat):
    cm = conmat.copy().as_matrix()
    numpy.fill_diagonal(cm, 0)
    return cm.sum(0).tolist()

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

def conmat2recipients(conmat, area_filepath, pu_filepath, pu_id='ID',inverse=False):
    area_id = get_intersect_id(area_filepath, pu_filepath, pu_id)
    cm = conmat.copy().as_matrix()
    numpy.fill_diagonal(cm,0)
    for i in conmat.index:
        if i in area_id:
            cm[conmat.index == i,:] = 0
    if inverse:
        return abs(cm.sum(0) - max(cm.sum(0))).tolist()
    else:
        return cm.sum(0).tolist()

def conmat2donors(conmat, area_filepath, pu_filepath, pu_id='ID',inverse=False):
    area_id = get_intersect_id(area_filepath, pu_filepath, pu_id)
    cm = conmat.copy().as_matrix()
    numpy.fill_diagonal(cm, 0)
    for i in conmat.index:
        if i in area_id:
            cm[:, conmat.index == i] = 0
    if inverse:
        return abs(cm.sum(1)-max(cm.sum(1))).tolist()
    else:
        return cm.sum(1).tolist()

def conmat2connboundary(conmat):
    cm = conmat.copy()
    cm['id1'] = cm.index
    boundary_dat = cm.melt(id_vars=['id1'])
    boundary_dat.columns = ['id1', 'id2', 'boundary']
    boundary_dat = boundary_dat.query('boundary>0').to_json(orient='split')
    return boundary_dat

# def conmat2minplanarboundary(conmat):
#     g = igraph.Graph.Weighted_Adjacency(conmat.as_matrix().tolist()).spanning_tree(weights='weight')
#     mpgmat = g.get_adjacency().data
#     mpgmat = pandas.DataFrame(mpgmat)
#     mpgmat.columns = conmat.columns
#     mpgmat['id1'] = conmat.index
#     boundary_dat = mpgmat.melt(id_vars=['id1'])
#     boundary_dat.columns = ['id1', 'id2', 'boundary']
#     boundary_dat = boundary_dat.query('boundary>0').to_json(orient='split')
#     return boundary_dat

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