from bisect import bisect


def LIS(N, A):
    INF = 10**10

    dp = [INF]*(N+1)
    dp[0] = -1
    for a in A:
        idx = bisect(dp, a-1)
        dp[idx] = min(a, dp[idx])
    return max(i for i in range(N+1) if dp[i] < INF)
