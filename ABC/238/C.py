MOD = 998244353
N = int(input())

data = [(10 ** n, 10 ** (n + 1) - 1) for n in range(19)]
result = 0
for dat in data:
    mi, ma = dat
    R = ma - mi + 1
    L = 1
    if ma <= N:
        result = (result + ((R + L) * (R - L + 1)) // 2) % MOD
    else:
        R = N - mi + 1
        result = (result + ((R + L) * (R - L + 1)) // 2) % MOD
        break
print(result)
