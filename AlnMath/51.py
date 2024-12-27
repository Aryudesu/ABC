def inverseMod(num, MOD):
    return pow(num, MOD-2, MOD)


X, Y = [int(l) for l in input().split()]
A = min([X, Y])
MOD = 1000000007
res1 = 1
for i in range(X + Y, X + Y - A, -1):
    res1 = (res1 * i) % MOD
res2 = 1
for i in range(1, A + 1):
    res2 = (res2 * i) % MOD
result = (res1 * inverseMod(res2, MOD)) % MOD
print(result)
