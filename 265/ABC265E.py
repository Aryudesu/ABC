N, M = [int(l) for l in input().split()]
A, B, C, D ,E, F = [int(l) for l in input().split()]
XY = set()
MOD = 998244353

# 検索を簡単にするために各X座標に対してY座標を入れる
for m in range(M):
    X, Y = [int(l) for l in input().split()]
    XY.add((X,Y))

# 前回の結果
prev = dict()
prev[0] = 1
for n in range(N):
    # 今回の結果
    now_ = dict()
    # 前回のやつ総当り
    for pk in prev.keys():
        # 前回の(301α + β)
        abc = pk
        # α, β, γを片っ端から計算
        alpha = abc // (301)
        beta = abc % (301)
        gamma = n - alpha - beta
        x = A * alpha + C * beta + E * gamma
        y = B * alpha + D * beta + F * gamma
        # 次のやつのキー
        if (x + E, y + F) not in XY:
            now_.setdefault(abc, 0)
            now_[abc] = (now_[abc] + prev[pk]) % MOD
        if (x + C, y + D) not in XY:
            now_.setdefault(abc + 1, 0)
            now_[abc + 1] = (now_[abc + 1] + prev[pk]) % MOD
        if (x + A, y + B) not in XY:
            nex = now_.setdefault(abc + 301, 0)
            now_[abc + 301] = (now_[abc + 301] + prev[pk]) % MOD
    prev = now_
res = 0
for k in prev:
    res = (res + prev[k]) % MOD
print(res)
