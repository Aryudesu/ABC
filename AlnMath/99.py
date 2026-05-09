from collections import defaultdict
from typing import Tuple
import sys
sys.setrecursionlimit(10**6)

def dfs(N: int, graph: dict[int, list[int]], node: int, prev: int)->Tuple[int, int]:
    num = 1
    dist = 0
    for nextNode in graph[node]:
        if nextNode == prev:
            continue
        n, d = dfs(N, graph, nextNode, node)
        num += n
        dist += d
    return (num, dist + (N - num) * num)

N = int(input())
graph = defaultdict(list)
for n in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
n, dist = dfs(N, graph, 1, 0)
print(dist)
