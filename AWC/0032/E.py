from sortedcontainers import SortedSet
from atcoder.fenwicktree import FenwickTree
from math import isqrt

N, Q = map(int, input().split())
S = list(map(int, input().split()))
ft = FenwickTree(N + 5)

for i in range(N):
    ft.add(i, S[i])

P = isqrt(N)
queryData = [0] * 200005
result = []
for _ in range(Q):
    n, *q = map(int, input().split())
    if n == 1:
        k, v = q
        if k <= P:
            queryData[k] += v
        else:
            for i in range(k, N+1, k):
                ft.add(i-1, v)
    elif n == 2:
        x = q[0]
        diff = 0
        for y in range(1, P+1):
            if y > x:
                break
            diff += queryData[y] * (x//y)
        result.append(diff + ft.sum(0, x))
    else:
        raise ValueError()
for r in result:
    print(r)
