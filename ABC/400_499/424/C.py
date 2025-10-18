from collections import defaultdict
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)


RESULT = set()
def calc(graph: dict, node: int, memo: set):
    RESULT.add(node)
    for next_node in graph[node]:
        if next_node in memo or next_node in RESULT:
            continue
        memo.add(next_node)
        calc(graph, next_node, memo)
        memo.discard(next_node)

N = int(input())
graph = defaultdict(list)
for n in range(N):
    a, b = [int(l) for l in input().split()]
    if a == 0 and b == 0:
        graph[0].append(n + 1)
    else:
        graph[a].append(n + 1)
        graph[b].append(n + 1)
calc(graph, 0, set())
print(len(RESULT) - 1)
