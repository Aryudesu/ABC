from itertools import combinations
from atcoder.dsu import DSU

INF = 10 ** 18
N, M, K = map(int, input().split())
UVW = [[INF] * N for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    UVW[u][v] = w
    UVW[v][u] = w

result = 10 ** 18
for dat in combinations(range(N), K):
    edges = []
    dsu = DSU(K)
    for i in range(K-1):
        for j in range(i+1, K):
            u = dat[i]
            v = dat[j]
            cost = UVW[u][v]
            if cost == INF:
                continue
            edges.append((cost, i, j))
    edges.sort()
    res = 0
    for w, i, j in edges:
        if dsu.same(i, j):
            continue
        dsu.merge(i, j)
        res += w
    if dsu.size(i) == K:
        result = min(res, result)
print(result)
