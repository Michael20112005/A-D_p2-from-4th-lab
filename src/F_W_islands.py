import numpy as np

adj_matrix = np.genfromtxt('islands.csv', delimiter=',')


def calculate_total_cable_length(adj_matrix):
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