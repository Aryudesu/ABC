N, M, S, K = map(int, input().split())
result = [False] * N
graph = [[] for _ in range(N)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

nodes = {S-1}
result[S-1] = True
for _ in range(K):
    nextNodes = set()
    for node in nodes:
        for nextNode in graph[node]:
            if result[nextNode]:
                continue
            result[nextNode] = True
            nextNodes.add(nextNode)
    nodes = nextNodes
print(sum(result))
