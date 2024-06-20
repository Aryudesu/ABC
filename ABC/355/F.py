class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            return True
        return False

def kruskal(N, edges):
    uf = UnionFind(N)
    mst_weight = 0
    mst_edges = []
    edges.sort(key=lambda x: x[2])
    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
    return mst_weight, mst_edges

def process_queries(N, initial_edges, queries):
    mst_weight, mst_edges = kruskal(N, initial_edges)
    current_edges = initial_edges[:]
    results = []

    for u, v, w in queries:
        current_edges.append((u, v, w))
        new_weight, new_mst_edges = kruskal(N, current_edges)
        results.append(new_weight)

    return results

# Reading input
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
edges = []
index = 2
for _ in range(N - 1):
    a = int(data[index]) - 1
    b = int(data[index + 1]) - 1
    c = int(data[index + 2])
    edges.append((a, b, c))
    index += 3

queries = []
for _ in range(Q):
    u = int(data[index]) - 1
    v = int(data[index + 1]) - 1
    w = int(data[index + 2])
    queries.append((u, v, w))
    index += 3

# Processing the queries
results = process_queries(N, edges, queries)
for result in results:
    print(result)
