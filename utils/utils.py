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

def print_output(cost_matrix,dijkstra_matrix):
    """
    Prints the initial matrix and the 3 computed matrix
    :param cost_matrix: Initial matrix
    :param dijkstra_matrix: Matrix of distance computed with Dijkstra
    """
    print("--------------------------------------------")
    print("Cost matrix : ")
    print(cost_matrix)
    print("--------------------------------------------")
    print("Dijkstra : ")
    print(dijkstra_matrix)
    print("--------------------------------------------")
    # TODO : Other matrix :)

def save_to_files(dijkstra_matrix):
    """
    Saves the results in files
    :param dijkstra_matrix: Matrix of distance computed with Dijkstra
    """
    f = open("results/dijkstra.txt", "w")
    f.write(str(dijkstra_matrix))
    f.close()
    # TODO : Other matrix :)