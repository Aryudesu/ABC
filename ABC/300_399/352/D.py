from atcoder.segtree import SegTree

N, K = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]

data = []
iData = []
for n in range(N):
    data.append([P[n], n])
data.sort()
for dat in data:
    iData.append(dat[1])
maxSegTree = SegTree(max, -1, iData)
minSegTree = SegTree(min, 10**6, iData)
result = 10 ** 6
for i in range(N - K + 1):
    M = maxSegTree.prod(i, i + K)
    m = minSegTree.prod(i, i + K)
    if result > M - m:
        result= M - m
print(result)
