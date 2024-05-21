import math


def calculate_max_length(w, heights):

    if w < 1 or not heights:
        return 0.0

    n = len(heights)
    max_heights = []

    for i in range(n):
        if i % 2 == 0:
            max_heights.append(heights[i])
        else:
            max_heights.append(1)

    max_length = 0.0
    for i in range(n - 1):
        height_diff = heights[i] - heights[i + 1]
        max_length += math.sqrt(w ** 2 + height_diff ** 2)

    return round(max_length, 2)


def read_input(filename):
    with open(filename, 'r') as file:
        w = int(file.readline().strip())
        heights = list(map(int, file.readline().strip().split(',')))
    return w, heights


def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


if __name__ == '__main__':
    w, heights = read_input('input1.txt')
    result = calculate_max_length(w, heights)
    write_output('output1.txt', result)
