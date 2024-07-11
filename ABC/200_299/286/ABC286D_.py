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
                if idx + a == S:
                    return True
                new_dp[idx + a] = True
        dp = new_dp
    return dp[S]


N, S = [int(l) for l in input().split()]
A = []
for n in range(N):
    a, b = [int(l) for l in input().split()]
    for k in range(b):
        A.append(a)
print('Yes' if ssp(A, S) else 'No')
