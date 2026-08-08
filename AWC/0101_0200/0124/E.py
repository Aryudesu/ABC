INF = 10**18
N, K = map(int, input().split())
A = list(map(int, input().split()))
# 1個前
data = dict()
# (Kの回数, 今回インデックス) = 最大スコア
data[(0, 0)] = A[0]
for idx in range(1, N):
    nextData = dict()
    maxValue = -INF
    maxValueK = K
    for key, value in data.items():
        k, pIdx = key
        # 1個移動
        if pIdx + 1 == idx:
            nextPIdx = idx
            nextValue = value + A[idx]
            nextK = k
            nextData[(nextK, nextPIdx)] = max(nextData.get((nextK, nextPIdx), -INF), nextValue)
            # その場にとどまる選択肢
            nextData[key] = max(nextData.get(key, -INF), value)
        # 1個前からの移動
        if pIdx + 2 == idx and k + 1 <= K:
            nextPIdx = idx
            nextValue = value + A[idx]
            nextK = k + 1
            nextData[(nextK, nextPIdx)] = max(nextData.get((nextK, nextPIdx), -INF), nextValue)
    data = nextData
    # print(data)
result = -10 ** 18
for key, value in data.items():
    k, idx = key
    if idx == N-1:
        result = max(result, value)
print(result)
