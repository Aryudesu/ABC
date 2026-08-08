from heapq import heappop, heappush
import sys

read = sys.stdin.buffer.readline
INF = 10**18


def dijkstra(
    graph: list[list[tuple[int, int]]],
    start: int,
) -> tuple[list[int], list[int]]:
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    prev = [-1] * n
    pq = [(0, start)]
    push = heappush
    pop = heappop
    while pq:
        d, u = pop(pq)
        if d != dist[u]:
            continue
        for v, weight in graph[u]:
            nd = d + weight
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                push(pq, (nd, v))
    return dist, prev

N, M, Q = map(int, read().split())
g = [[] for _ in range(N)]
for m in range(M):
    u, v = map(int, read().split())
    g[u-1].append((v-1, 1))
data = [0] * (N + 1)
for n in range(N):
    dist, _ = dijkstra(g, n)
    maxDist = 0
    for d in dist:
        if d == N:
            maxDist = d
            break
        maxDist = max(d, maxDist)
    if maxDist <= N:
        data[maxDist] += 1
s = 0
for n in range(N + 1):
    s += data[n]
    data[n] = s
for _ in range(Q):
    K = int(read())
    print(data[K])
