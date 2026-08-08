from atcoder.dsu import DSU
from collections import defaultdict

INF = 10 ** 18
N, K = map(int, input().split())
A = list(map(int, input().split()))
# どうにかして各数字での最大/最小になる範囲をとりたい
minDSU = DSU(N)
maxDSU = DSU(N)
minData = [(n, n) for n in range(N)]
maxData = [(n, n) for n in range(N)]
numIdx = defaultdict(list)
for idx in range(N):
    a = A[idx]
    numIdx[a].append(idx)
nums = sorted(numIdx.keys())
# minの範囲
for num in nums:
    idxes = numIdx[num]
    for idx in idxes:
        if idx > 0 and A[idx - 1] > A[idx]:
            leader = minDSU.leader(idx, idx - 1)
            minDSU.merge(idx, idx - 1)
            
