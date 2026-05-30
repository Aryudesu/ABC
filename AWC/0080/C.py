N, K = map(int, input().split())
# dp[持ってる荷物の数] = 現時点で最大の報酬
dp = [0] * (K + 1)
for n in range(N):
    t, a = map(int, input().split())
    match(t):
        case 1:
            # 乗せる
            for i in range(K, 0, -1):
                dp[i] = max(dp[i], dp[i-1] + a)
        case 0:
            # 降ろす
            dp[0] = max(dp[0], dp[0] + a)
            for i in range(0, K):
                dp[i] = max(dp[i], dp[i+1] + a)
        case _:
            raise ValueError()
print(dp[0])
