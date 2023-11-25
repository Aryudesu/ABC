def inverseMod(num, MOD):
    return pow(num, MOD-2, MOD)


N = int(input())
A = [int(l) for l in input().split()]
MOD = 998244353
MN = inverseMod(N, MOD)
denom = MN
prev = 0
result = 0
# もうムリポ・・・・・・
for n in range(N):
    next = ((prev + 1) * A[n] * MN) % MOD
    result = (result + next * (n+1) * MN) % MOD
    prev = (next + prev) % MOD
print(result)
