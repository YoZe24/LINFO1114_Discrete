import numpy

INFINITY = float("inf")
nb_nodes = 0
nb_edges = 0

def bellman_ford(graph):
    """
    Main function that computes the bellman_ford algorithm on each node of the graph
    to concatenate all the minimal distances 1D array, which form a 2D array at the end.
    :param graph: 2D array : Matrix of costs representing the graph.
    :return: 2D array : Matrix with all the minimal distances between every nodes.
    """
    global nb_nodes
    nb_nodes = len(graph)

    global nb_edges
    nb_edges = count_nb_edges(graph)

    shortest_dists = numpy.zeros(shape = (nb_nodes, nb_nodes))
    for i in range(len(graph)):
        shortest_dists[i] = compute_bellman_ford_from_src(graph, i)

    return shortest_dists

def compute_bellman_ford_from_src(graph, src):
    """
    Computes the bellman_ford algorithm on a graph, it computes all the shortest path from
    a source to all the other nodes of the graph and returns an array with the minimal distances.
    :param graph: 2D array : Matrix of costs representing the graph.
    :param src: Index of the node from which we want to compute all the shortest distances
    to the other nodes.
    :return: 1D array containing the computed shortest distances from the source to all the other nodes
    """
    dists = [INFINITY] * nb_nodes
    dists[src] = 0

    n = 0
    while n < int(nb_edges - 1):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] != INFINITY and i != j:
                    if dists[i] != INFINITY and dists[i] + graph[i][j] < dists[j]:
                        dists[j] = dists[i] + graph[i][j]
        n += 1

    return dists

def count_nb_edges(graph):
    """
    Counts the number of edges in the graph
    :param graph: 2D array : Matrix of costs representing the graph.
    :return: Number of edges in the graph
    """
    nb = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != INFINITY and i != j:
                nb += 1

    nb /= 2
    return nb