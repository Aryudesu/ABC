M = 1000000 + 5
MOD = 1000000007
frac = [1] * (M)
for n in range(1, M):
    frac[n] = (frac[n-1] * n) % MOD

N, K = map(int, input().split())
H = list(map(int, input().split()))
if K > 1:
    print(0)
    exit(0)
result = frac[sum(H)]
for h in H:
    if h != 1:
        result = (result * pow(frac[h], MOD-2, MOD)) % MOD
print(result)
