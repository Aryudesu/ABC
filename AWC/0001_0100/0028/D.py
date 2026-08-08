from collections import defaultdict
from sortedcontainers import SortedSet

N, M = map(int, input().split())
graph = defaultdict(set)
data = defaultdict(set)
leaf = SortedSet(range(1, N + 1))
for m in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    data[b].add(a)
    leaf.discard(b)
# print(graph)
# print(data)
# print(leaf)
result = []
while leaf:
    nowNode = leaf.pop(0)
    result.append(nowNode)
    nextNodes = graph[nowNode]
    for nextNode in nextNodes:
        tmp = data[nextNode]
        tmp.discard(nowNode)
        if len(tmp) == 0:
            leaf.add(nextNode)
    # print(leaf)
print(*result)
