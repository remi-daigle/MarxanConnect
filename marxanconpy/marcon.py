import os
import json
MarxanConnectVersion = "v0.1.1"

def new_project():
    """
    Create a new project dictionary
    :return: dict
    """
    # create project list to store project specific data
    project = {}
    project['version'] = MarxanConnectVersion
    project['filepaths'] = {}
    project['options'] = {}

    # set default options
    project['options']['fa_status'] = "Status-quo"
    project['options']['aa_status'] = "Status-quo"
    project['options']['demo_pu_cm_progress'] = True
    project['options']['demo_conmat_type'] = "Probability"
    project['options']['demo_conmat_format'] = "Matrix"
    project['options']['demo_conmat_rescale'] = "Identical Grids"
    project['options']['demo_conmat_rescale_edge'] = "Proportional to overlap"
    project['options']['land_hab_buff'] = "1"
    project['options']['land_hab_thresh'] = "0.001"
    project['options']['land_pu_cm_progress'] = True
    project['options']['land_conmat_type'] = "Habitat Type + Resistance"
    project['options']['land_res_matrixType'] = "Least-Cost Path"
    project['options']['calc_metrics_pu'] = True
    project['options']['calc_metrics_cu'] = False
    project['options']['metricsCalculated'] = False

    project['options']['demo_metrics'] = {}
    project['options']['demo_metrics']['in_degree'] = False
    project['options']['demo_metrics']['out_degree'] = False
    project['options']['demo_metrics']['between_cent'] = False
    project['options']['demo_metrics']['eig_vect_cent'] = False
    project['options']['demo_metrics']['google'] = False
    project['options']['demo_metrics']['self_recruit'] = False
    project['options']['demo_metrics']['local_retention'] = False
    project['options']['demo_metrics']['outflow'] = False
    project['options']['demo_metrics']['inflow'] = False
    project['options']['demo_metrics']['stochasticity'] = False
    project['options']['demo_metrics']['fa_recipients'] = False
    project['options']['demo_metrics']['fa_donors'] = False
    project['options']['demo_metrics']['aa_recipients'] = False
    project['options']['demo_metrics']['aa_donors'] = False

    project['options']['demo_metrics']['conn_boundary'] = False

    project['options']['land_metrics'] = {}
    project['options']['land_metrics']['in_degree'] = False
    project['options']['land_metrics']['out_degree'] = False
    project['options']['land_metrics']['between_cent'] = False
    project['options']['land_metrics']['eig_vect_cent'] = False
    project['options']['land_metrics']['google'] = False
    project['options']['land_metrics']['fa_recipients'] = False
    project['options']['land_metrics']['fa_donors'] = False
    project['options']['land_metrics']['aa_recipients'] = False
    project['options']['land_metrics']['aa_donors'] = False

    project['options']['land_metrics']['conn_boundary'] = False

    project['options']['cf_export'] = "Append"

    project['options']['bd_filecheck'] = True
    project['options']['pudat_filecheck'] = True

    project['options']['marxan_bit'] = "64-bit"
    project['options']['marxan'] = "Marxan"
    project['options']['inputdat_boundary'] = "Asymmetric"

    project['options']['pushp_filecheck'] = True
    project['options']['pucsv_filecheck'] = True
    project['options']['map_filecheck'] = True

    # set default file paths
    # spatial input
    project['filepaths']['pu_filepath'] = ""
    project['filepaths']['pu_file_pu_id'] = ""
    project['filepaths']['fa_filepath'] = ""
    project['filepaths']['aa_filepath'] = ""

    # connectivity input
    project['filepaths']['demo_cu_filepath'] = ""
    project['filepaths']['demo_cu_file_pu_id'] = ""
    project['filepaths']['demo_cu_cm_filepath'] = ""
    project['filepaths']['demo_pu_cm_filepath'] = ""
    project['filepaths']['land_cu_filepath'] = ""
    project['filepaths']['land_cu_file_hab_id'] = ""
    project['filepaths']['land_res_mat_filepath'] = ""
    project['filepaths']['land_res_filepath'] = ""
    project['filepaths']['land_res_file_hab_id'] = ""
    project['filepaths']['land_pu_cm_filepath'] = ""
    project['filepaths']['lp_filepath'] = ""

    # Marxan metrics files
    project['filepaths']['cf_filepath'] = os.path.join("~", "input", "puvspr2.dat")
    project['filepaths']['spec_filepath'] = os.path.join("~", "input", "spec.dat")
    project['filepaths']['bd_filepath'] = os.path.join("~", "input", "boundary.dat")
    project['filepaths']['pudat_filepath'] = os.path.join("~", "input", "pu.dat")

    # Marxan analysis
    project['filepaths']['marxan_input'] = os.path.join("~", "input.dat")
    project['filepaths']['marxan_dir'] = os.path.join("~", "Marxan243")

    # Export plot data
    project['filepaths']['pushp'] = os.path.join("~", "pu.shp")
    project['filepaths']['pucsv'] = os.path.join("~", "pu.csv")
    project['filepaths']['map'] = os.path.join("~", "map.png")

    return project

def load_project(filename):
    """
    Loads the project dictionary from a .MarCon file.
    :param filename:
    :return: dict
    """
    with open(filename, 'r') as fp:
        project = json.loads(fp.read())
    validate_project(project)
    return project

def edit_working_directory(project,wd,type="relative"):
    """
    Edits the filepath in the project dictionary. If type = 'relative', the absolute paths that contain the working
    directory are changed to relative paths and vice versa for type = 'absolute'
    :param project: the project dictionary
    :param wd: the working directory
    :param type: either 'relative' or 'absolute'
    :return: dict
    """
    if type == "relative":
        for p in project['filepaths']:
            if p != "working_directory":
                project['filepaths'][p] = project['filepaths'][p].replace(wd + "\\", "~\\")
    elif type == "absolute":
        for p in project['filepaths']:
            if p != "working_directory":
                project['filepaths'][p] = project['filepaths'][p].replace("~\\", wd + "\\")
    return project

def save_project(project,projfile=False):
    """
    Saves the project dictionary to a .MarCon file.
    :param project: the project dictionary
    :param projfile: the (optional) filename for the project file to override the projfile entry given in the project
    dictionary.
    :return:
    """
    if projfile==False:
        projfile = project['filepaths']['projfile']
    with open(projfile, 'w') as fp:
        json.dump(project, fp, indent=4, sort_keys=True)

def validate_project(project):
    """
    A function to validate project dictionaries to ensure that they contains all necessary fields (i.e. keys).
    Different versions of marxanconpy may require slightly different fields.
    :param project: the project dictionary
    :return: dict
    """
    if project['version']!=MarxanConnectVersion:
        print("Warning: This project file was created with a different version of Marxan Connect. Attempting to "
              "update for compatibility")
        project['version'] = MarxanConnectVersion

    np = new_project()

    for k in np.keys():
        if k not in project:
            print('Warning: This project file does not contain all the required fields (' + k +
                  '). Attempting to update for compatibility')
            project[k] = np[k]
            for k2 in np[k].keys():
                if k2 not in project[k]:
                    print('Warning: This project file does not contain all the required fields (' + k2 +
                          '). Attempting to update for compatibility')
                    project[k][k2] = np[k][k2]
                    for k3 in np[k][k2].keys():
                        if k3 not in project[k][k2]:
                            print('Warning: This project file does not contain all the required fields (' + k3 +
                                  '). Attempting to update for compatibility')
                            project[k][k2][k3] = np[k][k2][k3]
