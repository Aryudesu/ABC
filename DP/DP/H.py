H, W = [int(l) for l in input().split()]
dp = {0: 1}
MOD = 10**9 + 7
for h in range(H):
    new_dp = {-1: 0}
    A = input()
    for w in range(W):
        new_dp[w] = (new_dp[w-1] + dp.get(w, 0)) % MOD if A[w] == "." else 0
    dp = new_dp
print(dp[W-1])
