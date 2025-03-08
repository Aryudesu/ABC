N, Q = [int(l) for l in input().split()]

# 巣番号ラベル逆引き用(巣ラベル -> 巣番号インデックス)
suDict = [n for n in range(N + 1)]
# 巣番号ラベル
suLabel = [n for n in range(N + 1)]
# 鳩aがいるインデックス
suIdx = [n for n in range(N + 1)]

result = []
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        q, a, b = query
        # 鳩aの場所を更新
        # ラベル逆引きを行う
        bIdx = suDict[b]
        # 対応するインデックスを保存
        suIdx[a] = bIdx
    elif query[0] == 2:
        q, a, b = query
        # 巣番号ラベル交換
        aIdx = suDict[a]
        bIdx = suDict[b]
        suLabel[aIdx], suLabel[bIdx] = suLabel[bIdx], suLabel[aIdx]
        suDict[a] = bIdx
        suDict[b] = aIdx
    elif query[0] == 3:
        q, a = query
        # aが今いるインデックスからラベルを取得する
        bashoIdx = suIdx[a]
        label = suLabel[bashoIdx]
        result.append(label)
    else:
        raise Exception()
#     print("=== Debug ===")
#     print(suLabel)
#     print(suIdx)
# print("=== Debug ===")
for r in result:
    print(r)
