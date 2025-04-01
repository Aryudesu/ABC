import sys
from collections import defaultdict

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

def calc(N, K, graph, memo: set, now_node: int):
    count = 0
    this_num = 1
    for node in graph[now_node]:
        if node in memo:
            continue
        memo.add(node)
        res = calc(N, K, graph, memo, node)
        memo.discard(node)
        if res == -1:
            return -1
        elif res > 0:
            count += 1
            if count > 2:
                return -1
        this_num += res
    if this_num == K:
        return 0
    if count <= 1:
        return this_num
    return -1


N, K = [int(l) for l in input().split()]
graph = defaultdict(list)
for i in range(N*K - 1):
    u, v = [int(l) for l in input().split()]
    graph[u].append(v)
    graph[v].append(u)
print("No" if calc(N, K, graph, {1}, 1) == -1 else "Yes")
