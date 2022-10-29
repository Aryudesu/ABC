# 逆元の計算
def calc_inv(num, MOD):
    return pow(num, MOD - 2, MOD)


N, M, K = [int(l) for l in input().split()]
MOD = 998244353
# k回回して止まる場合の数
f = [0] * (N + 1)
# 一番最初は0スタート
f[0] = 1
res = 0
x = 1
# K回回す
for k in range(K):
    tf = [0] * (N + 1)
    # M個の出目
    for m in range(M):
        # 各マスについて調べる（ゴールスタートはないのでN-1まで）
        for km in range(N):
            # 新しい場所は (注目マス + 出目) から往復分を除外したもの
            p = (km + (m + 1)) % (2 * N)
            # ゴールを通り過ぎる場合引き返す
            if p > N:
                p = N - p - 1
            # そこに到達する通り数の計算
            tf[p] = (tf[p] + f[km]) % MOD
    # 結果保存
    f = tf
    x = (x * M) % MOD
    y = f[-1]
    res = (res + y * calc_inv(x, MOD)) % MOD
print(res)
