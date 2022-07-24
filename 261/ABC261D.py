N, M = [int(l) for l in input().split()]
X = [0] + [int(l) for l in input().split()]
CY = [0 for l in range(N + 1)]

# ボーナスを整理
for m in range(M):
    C, Y = [int(l) for l in input().split()]
    CY[C] += Y

# 開始前は0点
res = [[0 for l in range(N + 1)]]
for n in range(1, N + 1):
    # 1回前の結果
    bdat = res[n - 1]
    # 今回の結果
    tmp = [0 for l in range(N + 1)]
    # 初期に戻る際に最大値を選ぶ
    m = 0
    # 各カウントに対しての最大値
    for idx in range(0, n):
        # 今回の結果 = 前回の結果 + 今回の得点 + 今回のカウントボーナス
        nx = bdat[idx] + X[n] + CY[idx + 1]
        if m < bdat[idx]:
            m = bdat[idx]
        # このカウントが前回のカウントより大きければ更新
        if bdat[idx + 1] < nx:
            tmp[idx + 1] = nx
        else:
            tmp[idx + 1] = bdat[idx + 1]
    # カウント0の時最大値を選びたい
    if bdat[0] < m:
        tmp[0] = m
    res.append(tmp)
print(max(res[-1]))
