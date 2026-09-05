# なんでこたえあわないのおおおおおおおおおおお
N = int(input())
C = list(map(int, input().split()))
W = [list(map(int, input().split())) for _ in range(N)]
cost = []
for n in range(N):
    tmp = []
    for mask in range(1 << N):
        c = 0
        for i in range(N):
            b = 1 << i
            if mask & b:
                c += W[n][i]
        tmp.append(c)
    cost.append(tmp)
INF = 10 ** 18
dp = [INF for _ in range(1 << N)]
dp[0] = 0
for mask in range(1 << N):
    for i in range(N):
        b = 1 << i
        if mask & b:
            continue
        nextMask = mask | b
        nextCost = dp[mask] + cost[i][mask]
        dp[nextMask] = min(dp[nextMask], nextCost)
print(dp[-1] + sum(C))
