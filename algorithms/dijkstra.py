import numpy

INFINITY = float("inf")
nb_nodes = 0

def dijkstra(graph):
    """
    Main function that computes the dijkstra algorithm on each node of the graph
    to concatenate all the minimal distances 1D array, which form a 2D array at the end.
    :param graph: 2D array : Matrix of costs representing the graph.
    :return: 2D array : Matrix with all the minimal distances between every nodes.
    """
    global nb_nodes
    nb_nodes = len(graph)

    shortest_dists = numpy.zeros(shape = (nb_nodes, nb_nodes))
    for i in range(len(graph)):
        shortest_dists[i] = compute_dijkstra_from_src(graph, i)

    return shortest_dists

def compute_dijkstra_from_src(graph, src):
    """
    Computes the dijkstra algorithm on a graph, it computes all the shortest path from
    a source to all the other nodes of the graph and returns an array with the minimal distances.
    :param graph: 2D array : Matrix of costs representing the graph.
    :param src: Index of the node from which we want to compute all the shortest distances
    to the other nodes.
    :return: 1D array containing the computed shortest distances from the source to all the other nodes
    """
    dists = [INFINITY] * nb_nodes
    dists[src] = 0
    marked = [False] * nb_nodes

    n = 0
    while n < nb_nodes:
        x = get_min_dist_index(dists, marked)
        marked[x] = True

        for y in range(nb_nodes):
            if graph[x][y] > 0 and not marked[y] and dists[y] > dists[x] + graph[x][y]:
                dists[y] = dists[x] + graph[x][y]

        n += 1

    return dists

def get_min_dist_index(dists, marked):
    """
    This method works like a poll in an index priority queue, it returns the index of
    the node with the minimal distance.
    :param dists: Array of values representing the current distance of a node from the source.
    :param marked: Array of booleans representing the nodes that are already visited.
    :return: The index of the node with the minimal distance, the closest node.
    """
    val_min = INFINITY
    index_min = 0

    for v in range(nb_nodes):
        if dists[v] < val_min and not marked[v]:
            val_min = dists[v]
            index_min = v

    return index_min