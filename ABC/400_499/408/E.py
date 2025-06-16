from collections import defaultdict

N, M = [int(l) for l in input().split()]
graph = defaultdict(list)
for m in range(M):
    u, v, w = [int(l) for l in input().split()]
    graph[u].append((v, w))
    graph[v].append((u, w))
print(graph)
