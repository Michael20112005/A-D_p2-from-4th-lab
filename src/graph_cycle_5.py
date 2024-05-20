from collections import defaultdict, deque


def is_cyclic(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if bfs(node, graph, visited):
                return True
    return False


def bfs(start, graph, visited):
    queue = deque([(start, -1)])
    visited.add(start)

    while queue:
        node, parent = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, node))
            elif neighbor != parent:
                return True
    return False


def read_graph_from_file(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as file:
        for line in file:
            node, *neighbors = map(int, line.strip().split())
            graph[node] = neighbors
    return graph


def main():
    graph = read_graph_from_file("input.txt")
    has_cycle = is_cyclic(graph)

    with open("output.txt", 'w') as file:
        file.write(str(has_cycle))


if __name__ == "__main__":
    main()
    
