N = int(input())
# 結果
res = [0, 0, 0, 0, 0]
# 初期データ
TXA = [int(l) for l in input().split()]
if TXA[0] >= TXA[1]:
    res[TXA[1]] = TXA[2]
else:
    TXA = [0, 0, 0]
for n in range(N - 1):
    # 今回の結果
    tmp = [0, 0, 0, 0, 0]
    # 前回の入力
    BTXA = [TXA[0], TXA[1], TXA[2]]
    # 今回の入力
    TXA = [int(l) for l in input().split()]
    # 地点に行けない場合は除外
    if TXA[0] < TXA[1]:
        TXA = [BTXA[0], BTXA[1], BTXA[2]]
        continue
    # 前回クエリからの経過時間
    T = TXA[0] - BTXA[0]
    # 地点xについて
    for x in range(5):
        # 5点全部調べる
        for y in range(5):
            # 移動できる箇所について
            if abs(x - y) <= T:
                if x == TXA[1]:
                    # yにいた得点 + 追加得点
                    if tmp[x] < res[y] + TXA[2]:
                        tmp[x] = res[y] + TXA[2]
                else:
                    # yにいた得点
                    if tmp[x] < res[y]:
                        tmp[x] = res[y]
            else:
                # そこの得点
                if tmp[x] < res[x]:
                    tmp[x] = res[x]
    res = tmp
print(max(res))
