import sys

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

from collections import defaultdict

N, M = [int(l) for l in input().split()]
graph = defaultdict(list)
for m in range(M):
    a, b, w = [int(l) for l in input().split()]
    for i in range(1024):
        graph[(a, i)].append((b, i^w))

RESULT = -1
memo = set()
def dfs(node):
    global RESULT
    if node[0] == N:
        if RESULT == -1:
            RESULT = node[1]
        else:
            RESULT = min(RESULT, node[1])
    next_nodes = graph[node]
    for next in next_nodes:
        if next in memo:
            continue
        memo.add(next)
        dfs(next)
        # memo.discard(next)

dfs((1, 0))
print(RESULT)
