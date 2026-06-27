from heapq import heappop, heappush
N, M, Y = map(int, input().split())
graph = [dict() for _ in range(N)]
INF = 10 ** 18
for m in range(M):
    u, v, t = map(int, input().split())
    graph[u-1][v-1] = min(graph[u-1].get(v-1, INF), t)
    graph[v-1][u-1] = min(graph[v-1].get(u-1, INF), t)
X = list(map(int, input().split()))
dp = []
result = [INF] * N
result[0] = 0
heappush(dp, (0, 0))
mikakutei = set(range(1, N))
minX = INF
while dp:
    nextMikakutei = set()
    nowCost, nowPos = heappop(dp)
    if result[nowPos] < nowCost:
        continue
    mikakutei.discard(nowPos)
    for nextPos in graph[nowPos]:
        nextCost = nowCost + graph[nowPos][nextPos]
        if graph[nowPos][nextPos] <= X[nextPos] + Y:
            mikakutei.discard(nextPos)
        if result[nextPos] <= nextCost:
            continue
        result[nextPos] = nextCost
        heappush(dp, (nextCost, nextPos))
    if minX > nowCost + X[nowPos]:
        for nextPos in mikakutei:
            if nowCost + X[nextPos] + Y >= result[nextPos]:
                continue
            nextMikakutei.add(nextPos)
            nextCost = nowCost + X[nowPos] + X[nextPos] + Y
            if result[nextPos] <= nextCost:
                continue
            result[nextPos] = nextCost
            heappush(dp, (nextCost, nextPos))
        mikakutei = nextMikakutei
        minX = nowCost + X[nowPos]
print(*result[1:])

