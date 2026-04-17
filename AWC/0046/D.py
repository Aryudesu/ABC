from atcoder.fenwicktree import FenwickTree
from bisect import bisect_left, bisect_right

N, K = map(int, input().split())
D = list(map(int, input().split()))
D.sort()
ft = FenwickTree(N)
for n in range(N):
    ft.add(n, D[n])
result = 10 ** 18
for i in range(N):
    d = D[i]
    dk = d + K - 1
    idxl = bisect_left(D, d)
    idxr = bisect_right(D, dk)
    lres = 0
    rres = 0
    if idxl > 0:
        lres = ft.sum(0, idxl)
    if idxr < N:
        rres = ft.sum(idxr, N)
    result = min(result, d * idxl - lres + rres - dk * (N - idxr))
print(result)
