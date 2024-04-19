class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def weddings_and_tribes(N, pairs):
    ds = DisjointSet(20001)

    tribes = {}

    for boy, girl in pairs:
        root_boy = ds.find(boy)
        root_girl = ds.find(girl)

        if root_boy != root_girl:
            ds.union(boy, girl)

            if root_boy not in tribes:
                tribes[root_boy] = 1
            else:
                tribes[root_boy] += 1

    count = sum(size // 2 for size in tribes.values())

    return count

N = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(N)]

result = weddings_and_tribes(N, pairs)
print(result)