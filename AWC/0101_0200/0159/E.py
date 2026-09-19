from bisect import bisect_left

N, K, X = map(int, input().split())
A = list(map(int, input().split()))
M = N // 2
L = N - M
B = A[:M]
C = A[M:]
# print(M, L, B, C)
Mdata = dict()
for mask in range(1 << M):
    if mask.bit_count() > K:
        continue
    tmp = 0
    for m in range(M):
        b = 1 << m
        if mask & b:
            tmp += B[m]
    key = (tmp, mask.bit_count())
    Mdata[key] = Mdata.get(key, 0) + 1
MNums = [[] for _ in range(K+1)]
for num, bc in Mdata:
    MNums[bc].append(num)
for k in range(K+1):
    MNums[k].sort(reverse=True)
Mcounts = [[] for _ in range(K+1)]
for k in range(K+1):
    s = 0
    for mn in MNums[k]:
        s += Mdata[(mn, k)]
        Mcounts[k].append(s)
for k in range(K+1):
    MNums[k].reverse()
    Mcounts[k].reverse()
# print(MNums)
# print(Mcounts)
result = 0
for mask in range(1 << L):
    if mask.bit_count() > K:
        continue
    tmp = 0
    for l in range(L):
        b = 1 << l
        if mask & b:
            tmp += C[l]
    bc = mask.bit_count()
    mIdx = bisect_left(MNums[K-bc], X-tmp)
    if mIdx >= len(Mcounts[K-bc]):
        continue
    result += Mcounts[K-bc][mIdx]
print(result)
