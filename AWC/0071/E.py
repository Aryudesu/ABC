from atcoder.maxflow import MFGraph
from collections import defaultdict
import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

def dfs(graph: dict[list[int]], node: int, memo: set[int], color: list[int], BLACK: list[int], WHITE: list[int], nowColor: int = 0):
    if nowColor:
        WHITE[0] += 1
    else:
        BLACK[0] += 1
    color[node] = nowColor
    nextColor = 0 if nowColor else 1
    nextNodes = graph[node]
    for nextNode in nextNodes:
        if nextNode in memo:
            continue
        memo.add(nextNode)
        dfs(graph, nextNode, memo, color, BLACK, WHITE, nextColor)

N, M = map(int, input().split())
graph = defaultdict(list)
UV = []
color = [None] * N
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
    UV.append(u-1, v-1)
result = 0
for i in range(N):
    BLACK = [0]
    WHITE = [0]
    if color[i] is not None:
        continue
    dfs(graph, i, {i}, color, BLACK, WHITE)
    result += min(BLACK[0], WHITE[0])
print(result)



N, M = map(int, input().split())
graph = MFGraph(N + 2)
st = N
gl = N + 1
for m in range(M):
    u, v = map(int, input().split())


