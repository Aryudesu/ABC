N = int(input())
V = list(map(int, input().split()))
cost = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        cost[i][j] = abs(V[i] - V[j]) * abs(i - j)

INF = 10 ** 18
# dp[マスク][現在位置] = 最短距離
dp = [[INF] * N for _ in range(1<<N)]
dp[1][0] = 0

goal = (1 << N) - 1
for mask in range(1, 1 << N):
    remain = goal ^ mask
    nowM = mask
    while nowM:
        nowPos = nowM.bit_length() - 1
        nowM = nowM ^ (1 << nowPos)
        nowDist = dp[mask][nowPos]
        nxtM = remain
        while nxtM:
            nextPos = nxtM.bit_length() - 1
            nxtM = nxtM ^ (1 << nextPos)
            if mask & (1 << nextPos) != 0:
                continue
            nextMask = mask | (1 << nextPos)
            nextDist = nowDist + cost[nowPos][nextPos]
            dp[nextMask][nextPos] = min(dp[nextMask][nextPos], nextDist)
print(min(dp[-1]))
