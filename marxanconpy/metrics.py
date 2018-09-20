import numpy
import geopandas as gpd
import pandas
import igraph
import marxanconpy

def graph2vertexdegree(graph,mode='ALL'):
    vertexdegree = graph.degree(mode=mode)
    return vertexdegree

def graph2betweencent(graph):
    betweencent = graph.betweenness()
    return betweencent

def graph2eigvectcent(graph):
    eigvectcent = graph.evcent(weights=graph.es["weight"])
    return eigvectcent

def graph2google(graph):
    eigvectcent = graph.pagerank(weights=graph.es["weight"])
    return eigvectcent

def graph2outflow(graph):
    return graph.strength(mode="OUT", loops=False, weights=graph.es["weight"])

def graph2inflow(graph):
    return graph.strength(mode="IN", loops=False, weights=graph.es["weight"])

def graph2diagonal(graph):
    from_list = numpy.array([x[0] for x in graph.get_edgelist()])
    to_list = numpy.array([x[1] for x in graph.get_edgelist()])
    loops = from_list == to_list
    IDs = numpy.unique([numpy.unique(from_list), numpy.unique(to_list)])
    diag = numpy.repeat(0., len(IDs))
    for i in from_list[loops]:
        diag[IDs == i] = numpy.array(graph.es["weight"])[(from_list == i) & (to_list == i)]
    diag[IDs == i] = 1
    return diag

def get_intersect_id(area_filepath, pu_filepath,pu_id='ID'):
    area = gpd.GeoDataFrame.from_file(area_filepath)
    pu = gpd.GeoDataFrame.from_file(pu_filepath)

    if pu.crs!=area.crs:
        area_proj = marxanconpy.spatial.get_appropriate_projection(pu, 'area')
        area = area.to_crs(area_proj)
        pu = pu.to_crs(area_proj)

    area_id = ()
    for index, arearow in area.iterrows():
        for index, purow in pu.iterrows():
            if purow.geometry.intersects(arearow.geometry):
                area_id = area_id + (purow[pu_id],)
                break
    return area_id

def graph2recipients(graph, area_filepath, pu_filepath, pu_id='ID',inverse=False):
    area_id = get_intersect_id(area_filepath, pu_filepath, pu_id)
    recipients = graph.strength(area_id,mode="IN", loops=False, weights=graph.es["weight"])
    if inverse:
        return max(recipients)-recipients
    else:
        return recipients

def graph2donors(graph, area_filepath, pu_filepath, pu_id='ID',inverse=False):
    area_id = get_intersect_id(area_filepath, pu_filepath, pu_id)
    donors = graph.strength(area_id, mode="OUT", loops=False, weights=graph.es["weight"])
    if inverse:
        return max(donors)-donors
    else:
        return donors

def graph2connboundary(graph):
    id1 = numpy.array([x[0] for x in graph.get_edgelist()])
    id2 = numpy.array([x[1] for x in graph.get_edgelist()])
    boundary = graph.es["weight"]
    boundary_dat = pandas.DataFrame(data={"id1": id1,
                                          "id2": id2,
                                          "boundary": boundary}).to_json(orient='split')
    return boundary_dat

# def graph2minplanarboundary(graph):
#     mpgmat = graph.get_adjacency().data
#     mpgmat = pandas.DataFrame(mpgmat)
#     mpgmat.columns = graph.columns
#     mpgmat['id1'] = graph.index
#     boundary_dat = mpgmat.melt(id_vars=['id1'])
#     boundary_dat.columns = ['id1', 'id2', 'boundary']
#     boundary_dat = boundary_dat.query('boundary>0').to_json(orient='split')
#     return boundary_dat

def graphtime2temp_conn_cov(graph_time, fa_filepath, pu_filepath):
    fa = gpd.GeoDataFrame.from_file(fa_filepath)
    pu = gpd.GeoDataFrame.from_file(pu_filepath)


    fa_id = ()
    for index, farow in fa.iterrows():
        for index, purow in pu.iterrows():
            if purow.geometry.intersects(farow.geometry):
                fa_id = fa_id + (purow.ID,)
                break
    if any([fid in graph_time.id2.unique().tolist() for fid in fa_id]):
        cov_list = []
        for fa1 in fa_id:
            for fa2 in fa_id:
                if not fa1 == fa2:
                    con_fa = graph_time.value[(graph_time.id1 == fa1) & (graph_time.id2 == fa2)]
                    for id1 in fa_id:
                        for id2 in graph_time.id2.unique():
                            if not id1 == id2:
                                cov = \
                                numpy.cov(con_fa, graph_time.value[(graph_time.id1 == id1) &
                                                                    (graph_time.id2 == id2)])[0, 1]
                                cov_list.append({'id2': id2, 'cov': cov})
        cov_list = pandas.DataFrame.from_dict(cov_list)

        score = -cov_list.groupby('id2').sum()
        return score['cov'].tolist()
    else:
        return [0] * len(graph_time.id2.unique())