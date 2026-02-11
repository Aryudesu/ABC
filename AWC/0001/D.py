N, M, K = map(int, input().split())

AB = []
for n in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

dp = dict()
for n in range(N):
    print(dp[n])
