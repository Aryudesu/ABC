def inverseMod(num, MOD):
    return pow(num, MOD-2, MOD)


MOD = 998244353
N, K = [int(l) for l in input().split()]
# 1番目が黒である確率
x1 = 1
# 1番目以外が黒である確率
x2 = 0
invN = inverseMod(N**2, MOD)
for k in range(K):
    # 黒になる確率 = (黒の確率 * (自身同士を入れ替え + 自身以外を入れ替え) + 白の確率 * (自身と黒を入れ替え) * (a, bとb,aの2通り))
    new_x1 = ((x1 * (1 + (N - 1) ** 2) + (1 - x1) * 2) % MOD) * invN
    new_x2 = ((x2 * (1 + (N - 1) ** 2) + (1 - x2) * 2) % MOD) * invN
    x1, x2 = new_x1, new_x2
result = 0
result = x1
result = (result + x2 * ((N * (N + 1))// 2 - 1)) % MOD
print(result)
