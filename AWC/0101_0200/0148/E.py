N, M, K = map(int, input().split())
T = [-1] + list(map(int, input().split())) + [0]
INF = 10 ** 18
C = [[INF] * (N + 1) for _ in range(N)]
for n in range(N+1):
    c = list(map(int, input().split()))
    for m in range(n + 1, N + 1):
        C[n][m] = c[m-(n+1)+1]
for c in C:
    print(c)
dp = []
for n in range(N+1):
    tmp1 = []
    for m in range(N+1):
        tmp2 = [INF] * (1 << M)
        tmp1.append(tmp2)
    dp.append(tmp1)
# dp[現在位置][通った個数][マスク] = 最小体力消費
dp[0][0][0] = 0
result = INF
print(T)
# 始点
for src in range(N+1):
    # 通った個数
    for count in range(N+1):
        # マスク
        for mask in range(1 << M):
            if dp[src][count][mask] == INF:
                continue
            # 行き先
            for dst in range(src+1, N+2):
                nextPos = dst
                nextCount = count + (dst != N)
                nextMask = mask ^ (1 << (T[dst]-1))
                nextHP = dp[src][count][mask] + C[src][dst]
                if nextCount > N:
                    continue
                dp[nextPos][nextCount][nextMask] = min(dp[nextPos][nextCount][nextMask], nextHP)
result = INF
for count in range(K, N+1):
    hp = dp[-1][count][0]
    result = min(result, hp)
print(result)
