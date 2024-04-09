from collections import defaultdict, deque

def is_cyclic(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if dfs(node, graph, visited, None):
                return True
    return False

def dfs(start, graph, visited, parent):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(neighbor, graph, visited, start):
                return True
        elif neighbor != parent:
            return True
    return False

def read_graph_from_file(filename):
    graph = defaultdict(list)
    with open(filename, "r") as file:
        for line in file:
            data = line.split()
            node = int(data[0])
            neighbors = [int(x) for x in data[1:]]
            graph[node] = neighbors
    return graph

def main():
    graph = read_graph_from_file("input.txt")
    cyclic = is_cyclic(graph)

    with open("output.txt", "w") as output_file:
        output_file.write(str(cyclic))


if __name__ == "__main__":
    main()
