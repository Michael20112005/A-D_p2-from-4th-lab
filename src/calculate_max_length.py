import math


def calculate_max_length(w, heights):
    n = len(heights)

    list = [[0.0, 0.0] for _ in range(n)]

    for i in range(1, n):
        min_height_i_minus_1 = 1
        max_height_i_minus_1 = heights[i - 1]
        min_height_i = 1
        max_height_i = heights[i]

        dist1 = math.sqrt(w ** 2 + (min_height_i_minus_1 - min_height_i) ** 2)
        dist2 = math.sqrt(w ** 2 + (min_height_i_minus_1 - max_height_i) ** 2)
        dist3 = math.sqrt(w ** 2 + (max_height_i_minus_1 - min_height_i) ** 2)
        dist4 = math.sqrt(w ** 2 + (max_height_i_minus_1 - max_height_i) ** 2)

        list[i][0] = max(list[i - 1][0] + dist1, list[i - 1][1] + dist3)
        list[i][1] = max(list[i - 1][0] + dist2, list[i - 1][1] + dist4)

    max_distance = max(list[n - 1][0], list[n - 1][1])

    return round(max_distance, 2)


def main():
    with open('input1.txt', 'r') as file:
        w = int(file.readline().strip())
        heights = list(map(int, file.readline().strip().replace(',', '').split()))

    result = calculate_max_length(w, heights)

    with open('output1.txt', 'w') as file:
        file.write(f"{result}\n")


if __name__ == "__main__":
    main()
