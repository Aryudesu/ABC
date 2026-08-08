def bfs(graph: list[list[int]], start: int) -> list[int]:
    n = len(graph)
    dist = [-1] * n
    dist[start] = 0

    queue = [start]
    head = 0

    while head < len(queue):
        u = queue[head]
        head += 1

        for v in graph[u]:
            if dist[v] != -1:
                continue
            dist[v] = dist[u] + 1
            queue.append(v)

    return dist

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for m in range(M):
    u, v, s = map(int, input().split())
    if s == 1:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
res = bfs(graph, 0)
print(res[-1])
