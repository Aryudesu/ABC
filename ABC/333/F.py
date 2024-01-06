def inverseMod(num, MOD):
    return pow(num, MOD-2, MOD)


MOD = 998244353
N = int(input())
data = [0] * N
print(2 * inverseMod(3, MOD))
