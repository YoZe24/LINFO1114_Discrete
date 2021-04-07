from utils.utils import *
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.floyd_warshall import floyd_warshall

filename = "graph.csv"

# TODO : Improve comments / doc everywhere

def run():
    cost_matrix = read_csv_to_matrix(filename)
    dijkstra_matrix = dijkstra(cost_matrix)
    bellman_ford_matrix = bellman_ford(cost_matrix)
    floyd_warshall_matrix = floyd_warshall(cost_matrix)

    verify = compare_matrix(dijkstra_matrix,bellman_ford_matrix,floyd_warshall_matrix)
    print_output(cost_matrix,dijkstra_matrix,bellman_ford_matrix,floyd_warshall_matrix,verify)
    save_to_files(dijkstra_matrix,bellman_ford_matrix,floyd_warshall_matrix)

run()