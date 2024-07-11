import sys

from atcoder.dsu import DSU

sys.setrecursionlimit(10**6)

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
dsu = DSU(N + 1)
graph = dict()
UV = []
for m in range(M):
    u, v = [int(l) for l in input().split()]
    UV.append((u, v))
    if A[u-1] == A[v-1]:
        dsu.merge(u, v)

for m in range(M):
    u, v = UV[m]
    if dsu.same(u, v):
        continue
    if A[u - 1] <= A[v - 1]:
        tmp = graph.get(dsu.leader(u), set())
        tmp.add(dsu.leader(v))
        graph[dsu.leader(u)] = tmp
    if A[v - 1] <= A[u - 1]:
        tmp = graph.get(dsu.leader(v), set())
        tmp.add(dsu.leader(u))
        graph[dsu.leader(v)] = tmp
nleader = dsu.leader(N)
nodes = set([dsu.leader(1)])
if dsu.same(1, N):
    print(1)
else:
    count = 1
    result = 0
    while nodes:
        new_nodes = set()
        for node in nodes:
            new_nodes.update(graph.get(node, set()))
        nodes = new_nodes
        count += 1
        if nleader in nodes:
            result = count
    print(result)
