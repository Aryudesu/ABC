N, K, M = map(int, input().split())
A = list(map(int, input().split()))
B = [pow(a, M-2, M) for a in A if a % M != 0]
dp = dict()
dp[0] = 1
for b in B:
    nextDP = dp.copy()
    for num in dp:
        value = dp[num]
        nextDP[num + 1] = (nextDP.get(num + 1, 0) + value * b) % M
    dp = nextDP
print(dp.get(K, 0))
