MOD = 10**9 + 7
N = int(input())
S = input()
dp = [0] * (N + 2)
dp[0] += 1
for n in range(1, N+1):
    if S[n-1] == "#":
        continue
    dp[n] += dp[n-1]
    if n-2 >= 0:
        dp[n] += dp[n-2]
    if n-3 >= 0:
        dp[n] += dp[n-3]
    dp[n] %= MOD
# print(dp)
print(dp[N])
