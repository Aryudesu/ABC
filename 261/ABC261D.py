N, M = [int(l) for l in input().split()]
X = [int(l) for l in input().split()]
X = [0] + X
CY = [0 for l in range(N + 1)]

for m in range(M):
    C, Y = [int(l) for l in input().split()]
    CY[C] += Y

# print(X)
# print(CY)
# 開始前は0点
res = [[0 for l in range(N + 1)]]
ZERO = 0
for n in range(1, N + 1):
    # 1回前の結果
    bdat = res[n - 1]
    # 今回の結果
    tmp = [0 for l in range(N + 1)]
    # 各カウントに対しての最大値
    m = 0
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
    if bdat[0] < m:
        tmp[0] = m
    res.append(tmp)
    # print(res)
print(max(res[-1]))
