from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def calc(graph: dict, node: int, result:list, memo: set = set()) -> int:
    nodes = graph[node]
    res = -1
    for next_node in nodes:
        if next_node in memo:
            continue
        memo.add(next_node)
        tmp = calc(graph, next_node, result, memo)
        res = max(tmp, res)
        memo.discard(next_node)
    result[node] = res + 1
    return result[node]


N, T = [int(l) for l in input().split()]
T -= 1
graph = defaultdict(set)
for _ in range(N-1):
    a, b = [int(l) - 1 for l in input().split()]
    graph[a].add(b)
    graph[b].add(a)
result = [0] * N
calc(graph, T, result, {T})
print(*result)

