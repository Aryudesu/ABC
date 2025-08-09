from sortedcontainers import SortedSet
from collections import defaultdict

N, M, K = [int(l) for l in input().split()]
graph = defaultdict(set)
memo = defaultdict(lambda: -1)
for m in range(M):
    a, b = [int(l) for l in input().split()]
    graph[a].add(b)
    graph[b].add(a)
sg = SortedSet()
for k in range(K):
    p, h = [int(l) for l in input().split()]
    sg.add((-h, p))
    memo[p] = h

while sg:
    h, p = sg.pop(0)
    h = -h
    for node in graph[p]:
        if memo[node] > h - 1:
            continue
        if h - 1 < 0:
            continue
        memo[node] = h - 1
        sg.add((-h + 1, node))
result = []
for i in range(N + 1):
    if memo[i] >= 0:
        result.append(i)
print(len(result))
print(*result)
