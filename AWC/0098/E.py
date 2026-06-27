from typing import Tuple
# [そのノードを請け負ったときの最小コスト, しなかったときの最小コスト]
def calc(node: int, graph: list[list[int]])->Tuple[int, int]:
    nextNodes = graph[node]
    for nextNode in nextNodes:
        res1, res2 = calc(nextNode, graph)

N = int(input())
graph = [[] for _ in range(N)]
P = list(map(int, input().split()))
for n in range(N-1):
    graph[P[n]-1].append(n+1)
cost = []
for n in range(N):
    c, w = map(int, input().split())
    cost.append((c, w))
