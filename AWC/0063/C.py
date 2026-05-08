MOD = 10**9 + 7
N, K = map(int, input().split())
S = list(map(int, input().split()))
print((sum(S) - max(S) + max(S) * pow(2, K, MOD)) % MOD)
