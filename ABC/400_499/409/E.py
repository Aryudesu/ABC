import sys
from collections import defaultdict

import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

N = int(input())
X = [int(l) for l in input().split()]
GRAPH = defaultdict(list)
for _ in range(N-1):
    u, v, w = [int(l) for l in input().split()]
    GRAPH[u-1].append((v-1, w))
    GRAPH[v-1].append((u-1, w))

RESULT = 0
def dfs(node: int, memo: set):
    next_nodes = GRAPH[node]
    global RESULT
    # そこにあるエネルギー量
    res = X[node]
    for next, w in next_nodes:
        if next in memo:
            continue
        memo.add(next)
        # 探索先から送られてくるエネルギー量
        num = dfs(next, memo)
        RESULT += w * abs(num)
        res += num
        memo.discard(next)
    # 返却するエネルギー量
    return res

res = dfs(0, {0})
print(RESULT)
