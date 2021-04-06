from utils.utils import *
from algorithms.dijkstra import dijkstra

filename = "graph.csv"

def run():
    cost_matrix = read_csv_to_matrix(filename)
    dijkstra_matrix = dijkstra(cost_matrix)
    # bellman_ford = bellman_ford(cost_matrix)
    # floyd_warshall = floyd_warshall(cost_matrix)

    # TODO : Add other matrix
    print_output(cost_matrix,dijkstra_matrix)
    save_to_files(dijkstra_matrix)

run()