N = int(input())
A = [int(l) for l in input().split()]
MOD = 998244353
ans = 0

# 1個～N個分の平均値ごとにDPを走らせる
for i in range(1, N + 1):
    dp = [[[0] * i for m in range(i + 1)] for n in range(N + 1)]
    dp[0][0][0] = 1
    # 要素A[j]について考える
    for j in range(N):
        # これまでに選んだ総数について全走査する
        for k in range(i + 1):
            # 選んだ和をiで割った余りについて全走査する
            for l in range(i):
                # A[j]を足さない場合，k個選んだ結果の通り数がそのまま次に引き継がれる
                dp[j + 1][k][l] += dp[j][k][l]
                # A[j]を足す場合
                # i個まだ選んでなかった場合でないと駄目
                if k != i:
                    # それまでの和にA[j]を足した結果について考える
                    dp[j + 1][k + 1][(l + A[j]) % i] += dp[j][k][l]
                    dp[j + 1][k + 1][(l + A[j]) % i] %= MOD
    # i個の場合の通り数を足す
    ans = (ans + dp[N][i][0]) % MOD
print(ans)
