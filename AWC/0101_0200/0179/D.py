MOD = 998244353
N = int(input())
S = input()
dp = [[0, 0] for _ in range(N)]
if S[0] == "A":
    dp[0][0] = 1
    dp[0][1] = 0
elif S[0] == "B":
    dp[0][0] = 0
    dp[0][1] = 1
else:
    dp[0][0] = 1
    dp[0][1] = 1

for i in range(1, N):
    match S[i]:
        case "A":
            dp[i][0] = dp[i-1][1]
            dp[i][1] = 0
        case "B":
            dp[i][0] = 0
            dp[i][1] = (dp[i-1][1] + dp[i-1][0]) % MOD
        case "C":
            dp[i][0] = dp[i-1][1]
            dp[i][1] = (dp[i-1][1] + dp[i-1][0]) % MOD
print(sum(dp[-1]) % MOD)
