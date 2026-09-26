from atcoder.segtree import SegTree

INF = 10 ** 18
N, M = map(int, input().split())
P = [int(l) - 1 for l in input().split()]
idxData = [None] * N
for idx in range(N):
    idxData[P[idx]] = idx
minSt = SegTree(min, INF, P)
maxSt = SegTree(max, -INF, P)
for m in range(M):
    l, r = map(int, input().split())
    minNum = minSt.prod(l-1, r)
    maxNum = maxSt.prod(l-1, r)
    minIdx, maxIdx = idxData[minNum], idxData[maxNum]
    minSt.set(minIdx, maxNum)
    minSt.set(maxIdx, minNum)
    maxSt.set(minIdx, maxNum)
    maxSt.set(maxIdx, minNum)
    P[minIdx], P[maxIdx] = P[maxIdx], P[minIdx]
    idxData[minNum], idxData[maxNum] = maxIdx, minIdx
    # print(P)
    # print(idxData)
    # print("minNum, maxNum", minNum, maxNum)
disp = [p + 1 for p in P]
print(*disp)
