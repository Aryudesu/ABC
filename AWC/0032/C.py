from atcoder.fenwicktree import FenwickTree
from sortedcontainers import SortedSet

N, Q = map(int, input().split())
allP = 0
YP = []
Ydata = SortedSet()
for n in range(N):
    y, p = map(int, input().split())
    YP.append((y, p))
    Ydata.add(y)
    allP += p
data = dict()
ft = FenwickTree(len(Ydata) + 1)
c = 0
for y in Ydata:
    data[y] = c
    c+=1
for y, p in YP:
    ft.add(data[y], p)

result = []
for _ in range(Q):
    L = int(input())
    idx = Ydata.bisect_left(L)
    result.append(ft.sum(0, idx))
for r in result:
    print(allP - r)
