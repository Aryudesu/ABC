from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)
for m in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
nodes = {1}
data = [None] * (N + 1)
data[1] = 0
while nodes:
    newNodes = set()
    for node in nodes:
        for nextNode in graph[node]:
            if data[nextNode] is not None:
                continue
            data[nextNode] = node
            newNodes.add(nextNode)
    nodes = newNodes
result = []
node = N
while node != 0:
    result.append(node)
    node = data[node]
result.reverse()
print(*result)
