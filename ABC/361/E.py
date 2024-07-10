import sys
from collections import deque

sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N)]
graph = dict()
AllCost = 0
for n in range(N-1):
    A, B, C = [int(l) for l in input().split()]
    A, B = A - 1, B - 1
    G[A].append((B, C))
    G[B].append((A, C))
    AllCost += C

def bfs(s):
    dist = [None]*N
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in G[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + c
            que.append(w)
    d = max(dist)
    return dist.index(d), d
u, _ = bfs(0)
v, d = bfs(u)
# print(v, d)
print(AllCost * 2 - d)
