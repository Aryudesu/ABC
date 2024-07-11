INF = 10**100


def calc(N, P):
    denom = []
    tmp = 1
    s = 0
    for n in range(N):
        s += tmp
        denom.append(s)
        tmp *= 0.9
    # n問目の問題が
    dp = [0] * N
    dp[0] = P[0]
    result = -INF
    if N == 1:
        return P[0] - 1200
    for n in range(1, N):
        new_dp = [0] * N
        # m問目として選ばれている場合の最高得点
        for m in range(n + 1):
            if m == 0:
                tmp = max(dp[0], P[n])
                new_dp[0] = tmp
            elif m < n:
                tmp = max(dp[m-1]*0.9 + P[n], dp[m])
                new_dp[m] = tmp
            else:
                tmp = dp[m-1] * 0.9 + P[n]
                new_dp[m] = tmp
            t = tmp/denom[m] - 1200/((m+1)**0.5)
            if result < t:
                result = t
        dp = new_dp
    return result


N = int(input())
P = [int(l) for l in input().split()]
print(calc(N, P))
