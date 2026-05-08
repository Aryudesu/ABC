from collections import defaultdict

alp = "abcdefghijklmnopqrstuvwxyz"
MOD = 998244353
N = int(input())
S1, S2, S3 = input().split()
result = 0
dp = defaultdict(int)
dp[(0, 0, 0)] = 1
for _ in range(N):
    newDP = defaultdict(int)
    for key in dp:
        a, b, c = key
        num = dp[key]
        for chr in alp:
            newA, newB, newC = key
            if a < len(S1) and S1[a] == chr:
                newA = a + 1
                if len(S1) == newA:
                    continue
            if b < len(S2) and S2[b] == chr:
                newB = b + 1
                if len(S2) == newB:
                    continue
            if c < len(S3) and S3[c] == chr:
                newC = c + 1
                if len(S3) == newC:
                    continue
            newKey = (newA, newB, newC)
            newDP[newKey] = (newDP[newKey] + num) % MOD
    dp = newDP
result = 0
for key, value in dp.items():
    result = (result + value) % MOD
print(result)
