from bisect import bisect


def LIS(N, A):
    INF = 10**10

    dp = [INF]*(N+1)
    dp[0] = -1
    for a in A:
        idx = bisect(dp, a-1)
        dp[idx] = min(a, dp[idx])
    return max(i for i in range(N+1) if dp[i] < INF)


N = int(input())
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]

C = []
for i in range(N):
    C.append([A[i], B[i]])
C.sort()
D = [C[l][1] for l in range(N)]
print(LIS(N, D) + N)
