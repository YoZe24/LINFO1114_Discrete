from utils.utils import *
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford

filename = "graph.csv"

def run():
    cost_matrix = read_csv_to_matrix(filename)
    dijkstra_matrix = dijkstra(cost_matrix)
    bellman_ford_matrix = bellman_ford(cost_matrix)
    # floyd_warshall_matrix = floyd_warshall(cost_matrix)

    # TODO : Add other matrix
    verify = compare_matrix(dijkstra_matrix,bellman_ford_matrix)
    print_output(cost_matrix,dijkstra_matrix,bellman_ford_matrix,verify)
    save_to_files(dijkstra_matrix,bellman_ford_matrix)

run()