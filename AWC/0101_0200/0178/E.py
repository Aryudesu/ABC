from heapq import heappop, heappush
from sys import stdin

INF = 10**30


def dijkstra(
    graph: list[list[tuple[int, int]]],
    start: int,
    inf: int = INF,
) -> list[int]:
    """
    配列ベースの隣接リストに対する Dijkstra 法。

    Args:
        graph:
            graph[v] = [(to, cost), ...] の形式。
            辺重みは非負であること。
        start:
            始点。
        inf:
            到達不能頂点の距離として用いる値。

    Returns:
        start から各頂点への最短距離。

    計算量:
        O((N + M) log N)
    """
    n = len(graph)
    assert 0 <= start < n

    dist = [inf] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, v = heappop(pq)
        if d != dist[v]:
            continue

        for to, cost in graph[v]:
            nd = d + cost
            if nd < dist[to]:
                dist[to] = nd
                heappush(pq, (nd, to))

    return dist


readline = stdin.readline
N, M, K = map(int, readline().split())
B = []
C = []
for _ in range(M):
    *b, c = map(int, readline().split())
    mask = 0
    for idx in range(N):
        if b[idx]:
            mask |= 1 << idx
    B.append(mask)
    C.append(c)
F = [True] * (1 << N)
for _ in range(K):
    fmap = list(map(int, readline().split()))
    mask = 0
    for idx in range(N):
        if fmap[idx]:
            mask |= 1 << idx
    F[mask] = False
graph = [[] for _ in range(1 << N)]
for mask in range(1 << N):
    if not F[mask]:
        continue
    for idx in range(M):
        nextMask = mask ^ B[idx]
        if not F[nextMask]:
            continue
        graph[mask].append((nextMask, C[idx]))
res = dijkstra(graph, 0)
result = res[-1]
print(result if result < INF else -1)
