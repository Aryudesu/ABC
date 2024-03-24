def yakusu(L):
    res = []
    for i in range(1, L+1):
        if L%i == 0:
            res.append(i)
    return res


def makeDict(N, K, S, y):
    # 約数文字ごとに文字を分割
    L = [S[i:i+y] for i in range(0,len(S), y)]
    # 1文字ごとに結果を格納
    res = []
    for l in range(len(L[0])):
        res.append({})
    # 分割文字列ごとの捜査
    for l in range(len(L)):
        # 1文字に対して調べる
        for lidx in range(len(L[l])):
            # 該当文字数目
            d = res[lidx]
            c = d.setdefault(L[l][lidx], 0)
            d[L[l][lidx]] = c + 1
            res[lidx] = d
    return res


def calc(N, K, S):
    L = len(S)
    # 約数調べる
    Y = yakusu(L)
    res = N
    # 約数全部探索
    for y in Y:
        # 文字分割して辞書リスト
        D = makeDict(N, K, S, y)
        # 辞書回す
        count = 0
        # n文字目の辞書
        for d in D:
            keys = d.keys()
            # 一番使われてる文字数捜査
            k_max = 0
            for key in keys:
                if k_max < d[key]:
                    k_max = d[key]
            count += N//y - k_max
        if count > K:
            continue
        if res > y:
            res = y
    return res


N, K = [int(l) for l in input().split()]
S = input()
res = calc(N, K, S)
print(res)
