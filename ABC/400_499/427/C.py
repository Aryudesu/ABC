from collections import defaultdict
from itertools import product

def calc(num: int, graph: dict, left: set, right: set):
    res = 0
    for i in range(num):
        if i in left:
            for node in graph[i]:
                if node in left and node != i:
                    res += 1
        if i in right:
            for node in graph[i]:
                if node in right and node != i:
                    res += 1
    return res // 2

N, M = [int(l) for l in input().split()]
graph = defaultdict(set)
for m in range(M):
    u, v = [int(l) - 1 for l in input().split()]
    graph[u].add(v)
    graph[v].add(u)
result = M ** 2
for data in product([0, 1], repeat = N):
    left = set()
    right = set()
    for d in range(N):
        if data[d] == 0:
            left.add(d)
        else:
            right.add(d)
    result = min(calc(N, graph, left, right), result)
print(result)
