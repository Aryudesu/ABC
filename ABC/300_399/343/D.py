N, T = [int(l) for l in input().split()]
AB = []
result = []
score = set()
score.add(0)
# 誰が何点かのリスト
scoreList = [0] * N
# 何点が何人いるかの辞書
numData = {0: N}
for t in range(T):
    # 入力
    A, B = [int(l) for l in input().split()]
    A = A - 1
    # 加算前の点数取得
    sc = scoreList[A]
    # その点数が何人いるか
    tmp = numData.get(sc, 0)
    # 加算前に1人の場合は削除
    if tmp == 1:
        score.remove(sc)
    # 人数減らす
    numData[sc] = tmp - 1
    # 加算後の点数
    new_sc = sc + B
    # リスト更新
    scoreList[A] = new_sc
    # 人数増やす
    numData[new_sc] = numData.get(new_sc, 0) + 1
    # print(score)
    # スコア追加
    score.add(new_sc)
    # 個数数える
    result.append(len(score))
for r in result:
    print(r)
