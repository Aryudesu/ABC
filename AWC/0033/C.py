from collections import defaultdict

N, M, K, T = map(int, input().split())
C = list(map(int, input().split()))
graph = defaultdict(list)
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
result = set(C)
nodes = set(C)
counter = [0] * (N + 1)
for c in C:
    counter[c] += 1
while nodes:
    newNodes = set()
    for node in nodes:
        nextNodes = graph[node]
        for nextNode in nextNodes:
            if nextNode in result:
                continue
            counter[nextNode] += 1
            if counter[nextNode] >= T:
                newNodes.add(nextNode)
                result.add(nextNode)
    nodes = newNodes
print(len(result))
