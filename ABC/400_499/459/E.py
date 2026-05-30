from collections import defaultdict
from typing import Tuple
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

MOD = 998244353
INF = 1000001
N = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
D = [min(INF, int(l)) for l in input().split()]
leaf = set(range(N))
GRAPH = defaultdict(list)
for i in range(N-1):
    parent = P[i] - 1
    GRAPH[parent].append(i + 1)
    leaf.discard(parent)

def dfs(node: int)->Tuple[int, int]:
    nextNodes = GRAPH[node]
    if len(nextNodes) == 0:
        res = 1
        for n in range(D[node]):
            res = (res * (C[node] - n) * pow(n + 1, MOD - 2, MOD)) % MOD
        return (res, C[node] - D[node])
    cNum = C[node]
    res = 1
    for nextNode in nextNodes:
        res1, res2 = dfs(nextNode)
        res = (res * res1) % MOD
        cNum += res2
    for n in range(D[node]):
        res = (res * (cNum - n) * pow(n + 1, MOD - 2, MOD)) % MOD
    return (res, cNum - D[node])

res = dfs(0)
print(res[0])
