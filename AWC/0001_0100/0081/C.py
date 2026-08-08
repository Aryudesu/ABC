N, M, S = map(int, input().split())
INF = N + 100
result = [INF] * N
graph = [[] for _ in range(N)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
nodes = [S-1]
result[S-1] = 0
c = 1
while nodes:
    nextNodes = []
    for node in nodes:
        for nextNode in graph[node]:
            if result[nextNode] <= c:
                continue
            result[nextNode] = c
            nextNodes.append(nextNode)
    c += 1
    nodes = nextNodes
res = max(result)
if INF == res:
    print(-1)
else:
    print(res)
