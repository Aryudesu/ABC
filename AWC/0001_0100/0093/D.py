INF = 10**18
N, M, K = map(int, input().split())
H = list(map(int, input().split()))
graph = [[] for _ in range(N)]
result = [INF] * N
result[0] = H[0]
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
dp = set()
dp.add((H[0], 0))
count = 0
for k in range(K-1):
    nextDP = set()
    for h, pos in dp:
        if result[pos] < h:
            continue
        for nextPos in graph[pos]:
            nextH = max(h, H[nextPos])
            if result[nextPos] <= nextH:
                continue
            nextDP.add((nextH, nextPos))
            result[nextPos] = nextH
    dp = nextDP
print(result[-1] if result[-1] < INF else -1)
