import numpy

def convert_matrix_type(current,desired,matrix,localProd):
    print("converting ",current," to ",desired)
    if current == desired:
        return matrix
    elif current == "Probability":
        if desired == "Migration":
            matrix = matrix * localProd['production'].values[:, numpy.newaxis]
            matrix = matrix / matrix.sum(axis=0)
        elif desired == "Flow":
            matrix = matrix * localProd['production'].values[:, numpy.newaxis]
        else:
            print("Warning: " + desired + " not a recognized matrix type.")
    elif current == "Migration":
        print("Warning: Migration Matrices cannot be converted without knowing local recruitment")
    elif current == "Flow":
        if desired == "Migration":
            matrix = matrix / matrix.sum(axis=0)
        elif desired == "Probability":
            matrix = matrix.divide(matrix.sum(axis=1).values,axis="rows")
        else:
            print("Warning: " + desired + " not a recognized matrix type.")
    else:
        print("Warning: " + current + " not a recognized matrix type.")
    return matrix.fillna(0)