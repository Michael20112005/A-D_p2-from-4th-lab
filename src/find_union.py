class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x


def weddings_and_tribes(pairs_list):
    possible_pairs = set()

    disjoint_set = DisjointSet(max(max(pair) for pair in pairs_list) + 1)

    for pair in pairs_list:
        x, y = pair
        disjoint_set.union(x, y)

    tribe_1 = [i for i in range(1, max(max(pair) for pair in pairs_list) + 1) if i % 2 == 1]
    tribe_2 = [i for i in range(1, max(max(pair) for pair in pairs_list) + 1) if i % 2 == 0]

    for boy in tribe_1:
        for girl in tribe_2:
            if disjoint_set.find(boy) != disjoint_set.find(girl):
                possible_pairs.add((boy, girl))

    total_pairs = len(possible_pairs)

    return total_pairs, possible_pairs


pairs_list = [(1, 2), (2, 3), (3, 4), (5, 6)]

total_pairs, possible_pairs = weddings_and_tribes(pairs_list)
