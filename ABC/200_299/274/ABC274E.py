from collections import defaultdict

INF = 10 ** 12
N, M = map(int, input().split())

mData: int = 0
for i in range(N+M):
    if i < M:
        mData = mData*2 + 1
    else:
        mData *= 2
nData: int = (1 << N) - 1

XY = []
for i in range(N+M):
    XY.append(list(map(int, input().split())))
distData = []
for i in range(N+M):
    tmp = []
    for j in range(N+M):
        if i == j:
            tmp.append(0)
            continue
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        d = (x1-x2)**2 + (y1-y2)**2
        tmp.append(d**0.5)
    distData.append(tmp)
result = INF
dp = defaultdict(lambda: INF)
dp[1] = 0
while dp:
    newDP = defaultdict(lambda: INF)
    for key in dp:
        b, n = key//100, key%100
        d = dp[key]
        # Mの到着数
        mtmp: int = b & mData
        mNum = mtmp.bit_count()
        # 全部訪問済の場合
        ntmp: int = b & nData
        if ntmp.bit_count() == N:
            result = min(result, d + distData[n][0]/pow(2, mNum))
        for i in range(N+M):
            i_p = 1 << i
            if (b & i_p) == 1:
                continue
            # 到着させる
            new_b = b | i_p
            new_n = i
            # 距離
            dist = distData[n][i]
            # 新しいキー
            new_key = new_b * 100 + new_n
            new_dist = d + dist/pow(2, mNum)
            newDP[new_key] = min(new_dist, newDP[new_key])
    dp = newDP
    print(dp)
print(dp)
print(result)
