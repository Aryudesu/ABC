from sortedcontainers import SortedSet
from typing import Tuple

def calc(startNode: int, graph: list[SortedSet[Tuple[int, int]]], michosa: set[int], result: list[int])->None:
    nowNode = startNode
    result.append(nowNode + 1)
    michosa.discard(nowNode)
    while True:
        if len(graph[nowNode]) == 0:
            break
        while True:
            if len(graph[nowNode]) == 0:
                return
            _, nextNode = graph[nowNode].pop()
            if nextNode in michosa:
                nowNode = nextNode
                break
        result.append(nowNode + 1)
        michosa.discard(nowNode)

N, M = map(int, input().split())
B = list(map(int, input().split()))
Bdata = []
for n in range(N):
    if n == 0:
        Bdata.append((N + 5, n))
    else:
        Bdata.append((B[n], n))
Bdata.sort()
graph = [SortedSet() for _ in range(N)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].add((B[v-1], v-1))
michosa = set()
for n in range(N):
    michosa.add(n)
result = []
while michosa:
    _, node = Bdata.pop()
    if node not in michosa:
        continue
    calc(node, graph, michosa, result)
print(*result)
