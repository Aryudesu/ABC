from collections import defaultdict
from functools import cache
# import pypyjit
import sys
sys.setrecursionlimit(10**6)
# pypyjit.set_param('max_unroll_recursion=-1')

MOD = 10**9 + 7
GRAPH = defaultdict(list)
@cache
def dfs(node: int, prevNode: int, prev: bool)->int:
    # 今見ているノード，遷移前のノード，遷移前は塗ったか
    nextNodes = GRAPH[node]
    if len(nextNodes) == 1 and nextNodes[0] == prevNode:
        if prev:
            return 1
        else:
            return 2
    fRes = 1
    tRes = 1
    for nextNode in nextNodes:
        if nextNode == prevNode:
            continue
        if prev:
            fRes *= dfs(nextNode, node, False)
        else:
            tRes *= dfs(nextNode, node, True)
            fRes *= dfs(nextNode, node, False)
        fRes %= MOD
        tRes %= MOD
    return (fRes + tRes) % MOD

N = int(input())
for n in range(N-1):
    x, y = map(int, input().split())
    GRAPH[x].append(y)
    GRAPH[y].append(x)
result = 0
if N == 1:
    result = 2
else:
    tRes = 1
    fRes = 1
    for node in GRAPH[1]:
        fRes *= dfs(node, 1, False)
        tRes *= dfs(node, 1, True)
        tRes %= MOD
        fRes %= MOD
    result = tRes + fRes
print(result)
