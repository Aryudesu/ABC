MOD = 10**9 + 7
N, K = map(int, input().split())
L = list(map(int, input().split()))
L.sort(reverse=True)
L[0] = (L[0] * pow(2, K, MOD)) % MOD
result = 0
for l in L:
    result = (result + l) % MOD
print(result)
