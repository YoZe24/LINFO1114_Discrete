import numpy

def read_csv_to_matrix(filename):
    """
    Reads a CSV file containing a costs matrix and returns the
    numpy matrix.
    - integer or float for normal costs
    - inf if no path between the nodes
    :param filename: Path and name of the input file
    :return: Numpy matrix of the costs
    """
    matrix = numpy.loadtxt(open(filename, "rb"), delimiter=",").astype(float)
    return matrix
