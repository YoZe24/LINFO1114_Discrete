import copy

INFINITY = float("inf")
nb_nodes = 0

def floyd_warshall(graph):
    """
    Computes the floyd_warshall algorithm on a graph, it computes all the shortest path from
    all sources to all the other nodes of the graph and returns a matrix with the minimal distances.
    :param graph: 2D array : Matrix of costs representing the graph.
    :return: 2D array : Matrix containing all the computed shortest distances in the graph
    """
    global nb_nodes
    nb_nodes = len(graph)

    shortest_dists = copy.deepcopy(graph)
    for k in range(nb_nodes):
        for i in range(nb_nodes):
            for j in range(nb_nodes):
                shortest_dists[i][j] = min(shortest_dists[i][j],shortest_dists[i][k] + shortest_dists[k][j])
    return shortest_dists