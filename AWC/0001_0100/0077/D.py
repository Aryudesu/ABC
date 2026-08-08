from heapq import heappop, heappush

N, M, K = map(int, input().split())
F = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for m in range(M):
    u, v, t = map(int, input().split())
    graph[u-1].append((v-1, t))
    graph[v-1].append((u-1, t))
INF = 10**18

result = [[INF, INF, INF, INF, INF, INF] for _ in range(N)]
# 距離, もこもこ度, 現在位置
dijkData = []
heappush(dijkData, (0, F[0], 0))
result[0][F[0]] = 0
while dijkData:
    nowDist, nowMoko, nowPos = heappop(dijkData)
    if nowDist > result[nowPos][nowMoko]:
        continue
    for nextPos, t in graph[nowPos]:
        nextDist = nowDist + nowMoko * t
        nextMoko = min(nowMoko, F[nextPos])
        isOk = True
        for nm in range(1, nextMoko + 1):
            if nextDist >= result[nextPos][nm]:
                isOk = False
                break
        if isOk:
            result[nextPos][nextMoko] = nextDist
            heappush(dijkData, (nextDist, nextMoko, nextPos))
res = min(result[-1])
print(res if res < INF else -1)
