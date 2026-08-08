from atcoder.segtree import SegTree

INF = 10**18
N = int(input())
A = list(map(int, input().split()))
allSum = sum(A)
lsum = [0]
ls = 0
for i in range(N):
    ls += A[i]
    lsum.append(ls)
lt = SegTree(min, INF, lsum)
result = 0
for i in range(N+1):
    nowS = lsum[i]
    lm = lt.prod(0, i+1)
    result = max(result, nowS - min(0, lm))
    # print(nowS, lm)
print(result)
