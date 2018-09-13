import numpy
import geopandas as gpd
import shapely
import pandas
import igraph
import wx
import os

def rescale_matrix(pu_filepath,pu_id,cu_filepath,cu_id,cm_filepath,matrixformat,edge,progressbar=False):
    """
    rescale the connectivity matrix to match the scale of the planning units
    """
    try:
        # load shapefiles
        pu = gpd.GeoDataFrame.from_file(pu_filepath).to_crs('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
        cu = gpd.GeoDataFrame.from_file(cu_filepath).to_crs('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')

        proj = get_appropriate_projection(pu, 'area')
        pu = pu.to_crs(proj)
        cu = cu.to_crs(proj)

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
                                    style = wx.PD_APP_MODAL
                                            | wx.PD_CAN_ABORT
                                            | wx.PD_AUTO_HIDE
                                            | wx.PD_ELAPSED_TIME
                                            | wx.PD_ESTIMATED_TIME
                                            | wx.PD_REMAINING_TIME
                                    )
            count = 0

        keepGoing = True
        while keepGoing:
            con_mat_pu = []
            for index, puID in pu.iterrows():
                if progressbar:
                    count += 1
                    (keepGoing, skip) = dlg.Update(count)
                for index2, connID in cu.iterrows():
                    if not keepGoing: break
                    if puID.geometry.intersects(connID.geometry):
                       con_mat_pu.append({'geometry': puID.geometry.intersection(connID.geometry), 'puID':puID[pu_id], 'connID': connID[cu_id], 'puIndex': index, 'connIndex': index2,'int_area': puID.geometry.intersection(connID.geometry).area, 'conn_area': connID.geometry.area, 'pu_area': puID.geometry.area})


            # make intersection GeoDataFrame
            df = gpd.GeoDataFrame(con_mat_pu,columns=['geometry', 'puID', 'connID', 'puIndex', 'connIndex', 'int_area', 'conn_area', 'pu_area'])


            # populate rescaled pu connectivity matrix
            pu_conmat = numpy.zeros((len(pu),len(pu)))
            for source in pu[pu_id]:
                if progressbar:
                    count += 9
                    (keepGoing, skip) = dlg.Update(count)
                for sink in pu[pu_id]:
                    if not keepGoing: break
                    sources=df.puID==source
                    sinks=df.puID==sink
                    if any(sinks) and any(sources):
                        if edge == "Proportional to overlap":
                            temp_conn=grid_conmat[df.connIndex[sources],:][:,df.connIndex[sinks]]
                            cov_source=df.int_area[sources]/sum(df.int_area[sources])
                            cov_sink=df.int_area[sinks]/sum(df.int_area[sinks])
                            pu_conmat[numpy.array(pu[pu_id] == source), numpy.array(pu[pu_id] == sink)] = sum(
                                sum(((temp_conn * numpy.array(cov_sink)).T * numpy.array(cov_source))))
                        else:
                            temp_conn = grid_conmat[df.connIndex[sources], :][:, df.connIndex[sinks]]
                            cov_source = df.int_area[sources] / df.pu_area[sources]
                            cov_sink = df.int_area[sinks] / df.pu_area[sinks]
                            pu_conmat[numpy.array(pu[pu_id] == source), numpy.array(pu[pu_id] == sink)] = sum(
                                sum(((temp_conn * numpy.array(cov_sink)).T * numpy.array(cov_source))))
                    else:
                        pu_conmat[numpy.array(pu[pu_id]==source),numpy.array(pu[pu_id]==sink)]=0
            pu_conmat = pandas.DataFrame(pu_conmat, index=pu[pu_id], columns=pu[pu_id])
            pu_conmat.index.name = "puID"

            if time:
                # populate rescaled pu connectivity matrix
                for t in grid_conmat_time['time'].unique():
                    if not keepGoing: break
                    pu_conmat_t = numpy.zeros((len(pu), len(pu)))
                    for source in pu[pu_id]:
                        if progressbar:
                            count += 9
                            (keepGoing, skip) = dlg.Update(count)
                        for sink in pu[pu_id]:
                            if not keepGoing: break
                            sources = df.puID == source
                            sinks = df.puID == sink
                            if any(sinks) and any(source):
                                if edge == "Proportional to overlap":
                                    temp_conn = grid_conmat[df.connIndex[sources], :][:, df.connIndex[sinks]]
                                    cov_source = df.int_area[sources] / sum(df.int_area[sources])
                                    cov_sink = df.int_area[sinks] / sum(df.int_area[sinks])
                                    pu_conmat_t[numpy.array(pu[pu_id] == source), numpy.array(pu[pu_id] == sink)] = sum(
                                        sum(((temp_conn * numpy.array(cov_sink)).T * numpy.array(cov_source))))
                                else:
                                    temp_conn = grid_conmat[df.connIndex[sources], :][:, df.connIndex[sinks]]
                                    cov_source = df.int_area[sources] / df.pu_area[sources]
                                    cov_sink = df.int_area[sinks] / df.pu_area[sinks]
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
            keepgoing = False
    except:
        print("Warning: Error in matrix rescaling")
        self.log.Show()
        dlg.Destroy()
        raise

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

def get_appropriate_projection(shapefile,equal='area'):
    lonmin, lonmax, latmin, latmax = buffer_shp_corners([shapefile])
    lon = (lonmin + lonmax) / 2
    lat = (latmin+latmax)/2
    if equal == 'area':
        if lat > 30:
            proj = '+proj=laea +lat_0='+str(lat)+' +lon_0='+str(lon)
        else:
            proj = '+proj=laea +lon_0=' + str(lon)
    elif equal == 'distance':
        if lat > 30:
            proj = '+proj=eqdc +lat_1='+str(latmin)+' +lat_2='+str(latmax)+' +lon_0='+str(lon)
        else:
            proj = '+proj=eqc +lon_0=' + str(lon)
    return proj

def habitatresistance2conmats(buff, hab_filepath, hab_id, res_mat_filepath, pu_filepath, pu_id, res_type, progressbar = False):
    try:
        pu = gpd.GeoDataFrame.from_file(pu_filepath).to_crs('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
        pu = pu.sort_values(pu_id)
        pu = pu.reset_index(drop=True)

        # progressbar
        if progressbar:
            max = pu.shape[0] * 12
            dlg = wx.ProgressDialog("Assessing Least-Cost Path",
                                    "Please wait while the least-cost path based connectivity matrices are being generated.",
                                    maximum=max,
                                    parent=None,
                                    style=wx.PD_APP_MODAL
                                          | wx.PD_CAN_ABORT
                                          |wx.PD_AUTO_HIDE
                                          | wx.PD_ELAPSED_TIME
                                          | wx.PD_ESTIMATED_TIME
                                          | wx.PD_REMAINING_TIME
                                    )
            count = 0

        keepGoing = True
        while keepGoing:

            area_proj = get_appropriate_projection(pu, 'area')
            dist_proj = get_appropriate_projection(pu, 'distance')

            pu_area = pu.to_crs(area_proj)
            pu_dist = pu.to_crs(dist_proj)
            pu_dist['buff'] = pu_dist.geometry.buffer(buff)

            hab = gpd.GeoDataFrame.from_file(hab_filepath).to_crs('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
            hab['diss'] = hab[hab_id]
            hab = hab.dissolve(by='diss')
            hab = hab.reset_index(drop=True)
            hab.crs = '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'
            hab = hab.sort_values(hab_id)

            hab_area = hab.to_crs(area_proj)
            hab_dist = hab.to_crs(dist_proj)


            habtypes = hab_dist[hab_id].values

            # habitat resistance
            if res_type == "Least-Cost Path":
                if os.path.isfile(res_mat_filepath):
                    habres = numpy.array(pandas.read_csv(res_mat_filepath, index_col=0).sort_index())
                else:
                    print("Resistance file not found")
            else:
                habres = numpy.ones([len(habtypes),len(habtypes)])

            G = igraph.Graph()
            G.add_vertices([str(i) for i in pu[pu_id]])

            area = pandas.DataFrame(numpy.zeros((len(pu), len(habtypes))),index=pu_area[pu_id], columns=habtypes)
            for index1, pu1row in pu_area.iterrows():
                if progressbar:
                    count += 1
                    (keepGoing, skip) = dlg.Update(count)
                for indexhab, habrow in hab_area.iterrows():
                    if not keepGoing: break
                    area.iloc[index1,indexhab] = pu1row.geometry.intersection(habrow.geometry).area
            for index1, pu1row in pu_dist.iterrows():
                if not keepGoing: break
                if progressbar:
                    count += 10
                    (keepGoing, skip) = dlg.Update(count)
                for index2, pu2row in pu_dist.iterrows():
                    if not keepGoing: break
                    if index1 != index2:
                        if pu1row.buff.intersects(pu2row.buff):
                            line = shapely.geometry.LineString([(pu1row.geometry.centroid.x, pu1row.geometry.centroid.y),
                                                                (pu2row.geometry.centroid.x, pu2row.geometry.centroid.y)])
                            lineinter = numpy.array(hab_dist.intersection(line).length)
                            if sum(lineinter)>(line.length*0.5):
                                lineinter = lineinter/sum(lineinter)*line.length
                                weights = dict(zip(habtypes, numpy.multiply(lineinter, habres).sum(1)))
                                dist = pu1row.geometry.centroid.distance(pu2row.geometry.centroid)
                                G.add_edge(str(pu1row[pu_id]), str(pu2row[pu_id]), **weights, distance=dist)


            conmat = pandas.DataFrame({'habitat': [], 'id1': [], 'id2': [], 'value': []})
            area = area.T.divide(area.values.sum(1)).T
            area.fillna(0,inplace=True) # remove nan's
            area[area<0.00001]=0
            for h in habtypes:
                if progressbar:
                    count += int(pu.shape[0]/len(habtypes))
                    (keepGoing, skip) = dlg.Update(count)

                if not keepGoing: break
                if G.ecount() > 0:
                    conmat_temp = pandas.DataFrame(G.shortest_paths_dijkstra(weights=h, mode='OUT'))
                    conmat_temp = (1 / (conmat_temp * conmat_temp)).replace(numpy.inf, 0)
                    conmat_temp = conmat_temp.divide(conmat_temp.sum(axis=1).max())
                    conmat_temp = conmat_temp.multiply(area[h].tolist(), axis=0)
                    conmat_temp = conmat_temp.multiply(area[h].tolist(), axis=1)
                    conmat_temp.columns = G.vs['name']
                    conmat_temp['id1'] = G.vs['name']
                    conmat_temp['habitat'] = h
                    conmat = conmat.append(conmat_temp.melt(id_vars=('habitat', 'id1'), var_name='id2', value_name='value'))
                else:
                    print("Warning: Habitat '"+str(h)+"' has no connectivity between planning units, excluding from further analyses")
            if progressbar:
                count = max
                (keepGoing, skip) = dlg.Update(count)
            return conmat.to_json(orient='split')
            keepGoing = False
    except:
        print("Warning: Error in habitatresistance2conmats")
        self.log.Show()
        dlg.Destroy()
        raise