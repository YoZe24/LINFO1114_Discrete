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

def compare_matrix(dijkstra_matrix,bellman_ford_matrix,floyd_warshall_matrix):
    """
    Takes the 3 matrix and checks if they are the same
    :param dijkstra_matrix: Dijkstra output matrix
    :param bellman_ford_matrix: Bellman_ford output matrix
    :param floyd_warshall_matrix: Floyd_Warshall output matrix
    :return: True if they are the same
             False if they are not the same
    """
    if len(dijkstra_matrix) != len(bellman_ford_matrix) or len(dijkstra_matrix) != len(floyd_warshall_matrix):
        return False

    for i in range(len(dijkstra_matrix)):
        if len(dijkstra_matrix[i]) != len(bellman_ford_matrix[i]) or len(dijkstra_matrix[i]) != len(floyd_warshall_matrix[i]):
            return False

    for i in range(len(dijkstra_matrix)):
        for j in range(len(dijkstra_matrix)):
            if dijkstra_matrix[i][j] != bellman_ford_matrix[i][j] or dijkstra_matrix[i][j] != floyd_warshall_matrix[i][j]:
                return False

    return True

def print_output(cost_matrix,dijkstra_matrix,bellman_ford_matrix,floyd_warshall_matrix,verify):
    """
    Prints the initial matrix and the 3 computed matrix
    :param cost_matrix: Initial matrix
    :param dijkstra_matrix: Matrix of distance computed with Dijkstra
    :param bellman_ford_matrix: Matrix of distance computed with Bellman_ford
    :param floyd_warshall_matrix: Matrix of distance computed with Floyd_Warshall
    :param verify: Boolean that checks if the matrix are the same
    """
    print("--------------------------------------------")
    print("Cost matrix : ")
    print(cost_matrix)
    print("--------------------------------------------")
    print("Dijkstra : ")
    print(dijkstra_matrix)
    print("--------------------------------------------")
    print("Bellman Ford : ")
    print(bellman_ford_matrix)
    print("--------------------------------------------")
    print("Floyd Warshall : ")
    print(floyd_warshall_matrix)
    print("--------------------------------------------")
    print("The matrix are the same : ",verify)
    print("--------------------------------------------")


def save_to_files(dijkstra_matrix,bellman_ford_matrix,floyd_warshall_matrix):
    """
    Saves the results in files
    :param dijkstra_matrix: Matrix of distance computed with Dijkstra
    :param bellman_ford_matrix: Matrix of distance computed with Bellman_ford
    :param floyd_warshall_matrix: Matrix of distance computed with Floyd_Warshall
    """
    f = open("results/dijkstra.txt", "w")
    f.write(str(dijkstra_matrix))
    f.close()
    f = open("results/bellman_ford.txt", "w")
    f.write(str(bellman_ford_matrix))
    f.close()
    f = open("results/floyd_warshall.txt", "w")
    f.write(str(floyd_warshall_matrix))
    f.close()