from sortedcontainers import SortedSet

INF = 10 ** 10
N, L, R = map(int, input().split())
X = list(map(int, input().split()))
idxData = dict()
for i in range(N):
    idxData[X[i]] = i
result = [INF] * N
result[0] = 0
nodes = SortedSet(X)
nodes.discard(0)
for n in range(N-1):
    thisCount = result[n]
    if X[n] in nodes:
        continue
    nextMin = X[n] + L
    nextMax = X[n] + R
    # 飛ぶ先で未訪問のものを全部探索
    delRange = list(nodes.irange(nextMin, nextMax))
    for num in delRange:
        nodes.discard(num)
        result[idxData[num]] = min(result[idxData[num]], thisCount + 1)
print(result[-1])
