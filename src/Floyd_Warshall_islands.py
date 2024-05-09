import numpy as np
import csv


def read_adj_matrix_from_file(filename):
    """
    Reads an adjacency matrix from a CSV file and converts it into a NumPy array.

    Args:
        filename (str): The name of the CSV file containing the adjacency matrix.

    Returns:
        np.array: The adjacency matrix stored as a NumPy array.
    """

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        adj_matrix = np.array([[float(val) if val != 'inf' else float('inf') for val in row] for row in reader])

    return adj_matrix


def calculate_total_cable_length(adj_matrix):
    """
    Calculates the total length of cable required to connect all vertices in the graph represented by the adjacency matr

    Args:
        adj_matrix (np.array): The adjacency matrix representing the graph.

    Returns:
        float: The total length of cable required to connect all vertices.
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
    """
    Main function that reads the adjacency matrix from a file and calculates the total cable length required.

    Returns:
        float: The total cable length required to connect all vertices in the graph.
    """

    adj_matrix = read_adj_matrix_from_file('islands.csv')
    total_cable_length = calculate_total_cable_length(adj_matrix)

    return total_cable_length


if __name__ == '__main__':
    main()
