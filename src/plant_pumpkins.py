def plant_pumpkins_route(matrix):
    m = len(matrix)
    n = len(matrix[0])
    pumpkins_to_plant = []

    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                pumpkins_to_plant.append(matrix[i][j])
        else:
            for j in range(n - 1, -1, -1):
                pumpkins_to_plant.append(matrix[i][j])

    return pumpkins_to_plant
