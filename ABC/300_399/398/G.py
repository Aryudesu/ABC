from collections import defaultdict
from random import randint

N, M = [int(l) for l in input().split()]
graph = defaultdict(list)
for n in range(M):
    u, v = [int(l) for l in input().split()]
    graph[u].append(v)
    graph[v].append(u)

if randint(0, 1):
    print("Aoki")
else:
    print("Takahashi")
