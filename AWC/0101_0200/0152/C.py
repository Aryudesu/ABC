N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
data = [0] * K
data[0] = 1
for n in range(N):
    nextData = data.copy()
    a = A[n]
    for k in range(K):
        nextData[(k + a) % K] += data[k]
        nextData[(k + a) % K] %= MOD
    data = nextData
print((data[0] - 1) % MOD)
