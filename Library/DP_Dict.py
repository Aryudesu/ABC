"""
辞書式動的計画法テンプレートSample
ABC265 E-Warp

概要
Nが決まっていて空間計算量に自信が無い場合，
N+1進法で連想配列型に格納し，データの増加を抑えたら良いなと思っています．
"""

def back_calc(num, N, K):
    '''
    N+1進数の計算を逆算します
    -----------------------------------------------
    response
    res[0] + res[1] * (N+1) + res[2] * (N+1)^2 + ...
    '''
    res = []
    tmp = num
    for _ in range(K):
        res.append(tmp % (N+1))
        tmp //= (N+1)
    return res


def calc(N, params, MOD, Exc):
    '''
    Dict使ったDPテンプレート
    -----------------------------------------------
    N: 個数
    params: なんかパラメタ
    MOD: 計算する剰余
    Exc: 除外するモノ
    -----------------------------------------------
    response
    最終的なの通り数の総量 (mod MOD)
    '''
    # 前回の結果
    prev = dict()
    # 初期位置
    prev[0] = 0
    res = 0
    for n in range(N):
        # 今回の結果
        now_ = dict()
        # 前回のやつ総当り
        for pk in prev.keys():
            # 前回の(α + β(N + 1) + γ(N + 1)^2)
            # キーからα, β, γを逆算
            a, b, c, d, e, f = back_calc(pk, N, 6)
            # 現在の状態特定
            x = a + 2 * b + 3 * c + 4 * d + 5 * e + 6 * f
            # 次のやつのデータを作成する
            for m in range(6):
                now_[X + m] = now_[X + m]
        prev = now_
    res = 0
    for k in prev:
        res = (res + prev[k]) % MOD
    return res


N, M = [int(l) for l in input().split()]
params = [int(l) for l in input().split()]
XY = set()
MOD = 998244353

# setはタプル型でいけるらしいので行き止まり一覧を作成
for m in range(M):
    X, Y = [int(l) for l in input().split()]
    XY.add((X,Y))

print(calc(N, params, MOD, XY))
