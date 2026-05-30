from collections import defaultdict

alp = "abcdefghijklmnopqrstuvwxyz"

MOD = 998244353
N, K = map(int, input().split())
S = [input() for _ in range(K)]

result = 0
dp = defaultdict(int)
key = [0] * K
dp[tuple(key)] = 1

for _ in range(N):
    newDP = defaultdict(int)
    for key in dp:
        countData = list(key)
        num = dp[key]
        for chr in alp:
            newCountData = list(key)
            nextData = []
            isOk = True
            for k in range(K):
                if countData[k] < len(S[k]) and S[k][countData[k]] == chr:
                    newCountData[k] = countData[k] + 1
                    if len(S[k]) == newCountData[k]:
                        ifOk = False
                        break
            if not isOk:
                continue
            newKey = tuple(newCountData)
            newDP[newKey] = (newDP[newKey] + num) % MOD
    dp = newDP
result = 0
for key, value in dp.items():
    result = (result + value) % MOD
print(result)
