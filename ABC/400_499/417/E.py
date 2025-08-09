from collections import defaultdict
from sortedcontainers import SortedSet
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

RESULT = []
def calc(graph, src: int, goal: int, memo):
    if src == goal:
        return True
    f = False
    for node in graph[src]:
        if node in memo:
            continue
        memo.add(node)
        res = calc(graph, node, goal, memo)
        if res:
            RESULT.append(node)
            f = True
            break
    return f


T = int(input())
for t in range(T):
    graph = defaultdict(SortedSet)
    N, M, X, Y = [int(l) for l in input().split()]
    for m in range(M):
        u, v = [int(l) for l in input().split()]
        graph[u].add(v)
        graph[v].add(u)
    memo = set()
    memo.add(X)
    RESULT = []
    calc(graph, X, Y, memo)
    RESULT.append(X)
    RESULT.reverse()
    print(*RESULT)
