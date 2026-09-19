INF = 10 ** 18
N = int(input())
A = list(map(int, input().split()))
dp = [INF] * N
dp[0] = 0
for n in range(N):
    if n + 1 < N:
        dp[n + 1] = min(dp[n] + max(A[n + 1] - A[n], 0), dp[n + 1])
    if n + 2 < N:
        dp[n + 2] = min(dp[n] + max(A[n + 2] - A[n], 0), dp[n + 2])
print(dp[-1])
