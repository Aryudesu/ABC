def ssp(A, S):
    # 部分和問題
    # 配列Aの要素を組み合わせた総和でSを作ることができるか
    dp = [False] * (S + 1)
    dp[0] = True
    for a in A:
        new_dp = [False] * (S + 1)
        for idx in range(S + 1):
            if dp[idx]:
                new_dp[idx] = dp[idx]
            if dp[idx] and idx + a < S + 1:
                new_dp[idx + a] = True
        dp = new_dp
    return dp[S]


N = 5
A = [1, 3, 7, 10, 13]
S = 21
print(ssp(A, S))
