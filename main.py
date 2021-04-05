from utils.read_csv_to_matrix import *

filename = "graph.csv"

def run():
    matrix = read_csv_to_matrix(filename)
    print(matrix)

run()