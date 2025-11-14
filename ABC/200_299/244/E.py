from collections import defaultdict

MOD = 998244353
N, M, K, S, T, X = map(int, input().split())
graph = defaultdict(list)
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# [移動回数][点][Xの偶奇] = 通り数
dp = [[[0] * 2 for _ in range(N + 1)] for _ in range(K + 1)]
dp[0][S][0] = 1
# スタート地点になる箇所
stP = {(S, 0)}
for k in range(K):
    nxtP = set()
    for p, g in stP:
        for np in graph[p]:
            # 次がXのとき
            if np == X:
                dp[k+1][np][1 - g] = (dp[k+1][np][1 - g] + dp[k][p][g]) % MOD
                nxtP.add((np, 1-g))
            else:
                dp[k+1][np][g] = (dp[k+1][np][g] + dp[k][p][g]) % MOD
                nxtP.add((np, g))
    stP = nxtP
print(dp[-1][T][0])

