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
        if boy % 2 == 0:
            boy_id = boy + 1
        else:
            boy_id = boy

        if girl % 2 == 0:
            girl_id = girl + 1
        else:
            girl_id = girl

        root_boy = ds.find(boy_id)
        root_girl = ds.find(girl_id)

        if root_boy != root_girl:
            ds.union(boy_id, girl_id)

            root = ds.find(boy_id)
            if root not in tribes:
                tribes[root] = 2
            else:
                tribes[root] += 2

    count = sum(size // 2 for size in tribes.values())

    return count
