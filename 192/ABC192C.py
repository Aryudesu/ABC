def inv_lu(d, x):
    for k, v in d.items():
        if x == v:
            return k


N, K = [int(l) for l in input().split()]
cash = dict()
res = -1
for n in range(0, K):
    # 最新の結果を文字列にする
    S = str(N)
    # その数字が過去に存在したか
    c = cash.get(S)
    # 存在した場合
    if c is not None:
        syuuki = n - c
        amari = (K-c)%syuuki
        kaisuu = c + amari
        res = int(inv_lu(cash, kaisuu))
        break
    # しなかった場合
    else:
        cash[S] = n
    A1 = int(''.join(sorted(S, reverse=True)))
    A2 = int(''.join(sorted(S)))
    N = A1 - A2

if res < 0:
    print(N)
else:
    print(res)
