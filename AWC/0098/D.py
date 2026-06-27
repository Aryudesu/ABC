N, M, K, Q = map(int, input().split())
graph = [set() for _ in range(N)]
P = list(map(int, input().split()))
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].add(b)

dp = dict()
for n in range(N):
    dp[n] = P[n] % Q
for k in range(2, K + 1):
    nextDp = dict()
    for pos, val in dp.items():
        for nextPos in graph[pos]:
            nextVal = val + (P[nextPos] * k) % Q
            nextDp[nextPos] = max(nextDp.get(nextPos, 0), nextVal)
    dp = nextDp
result = 0
for k, v in dp.items():
    result = max(result, v)
print(result)
