import numpy as np

adj_matrix = np.genfromtxt('islands.csv', delimiter=',')


def calculate_total_cable_length(adj_matrix):

    """
    Args:
    - adj_matrix (list of lists): An adjacency matrix representing the connectivity of vertices.
     The value at adj_matrix[i][j] indicates the length of the cable required to connect vertex i to vertex j.
     If there is no direct connection between vertices i and j, the value is set to float('inf').

    Note:
    - INF represents infinity, indicating no direct connection between vertices in the network.
    """
    INF = float('inf')
    num_vertices = len(adj_matrix)
    distances = adj_matrix.copy()

    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and np.isinf(distances[i][j]):
                distances[i][j] = INF

    distances[distances == INF] = 999999

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return np.sum(distances)


def main():

    total_cable_length = calculate_total_cable_length(adj_matrix)
    return total_cable_length
