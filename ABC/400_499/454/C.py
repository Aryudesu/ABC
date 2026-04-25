from collections import defaultdict
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
def calc(node: int, graph: dict[int, list[int]], memo: set[int]):
    nextNodes = graph[node]
    for nextNode in nextNodes:
        if nextNode in memo:
            continue
        memo.add(nextNode)
        calc(nextNode, graph, memo)

N, M = map(int, input().split())
result = [False] * (N + 1)
result = set()
result.add(1)
graph = defaultdict(list)
for m in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
calc(1, graph, result)
print(len(result))
