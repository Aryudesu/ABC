from collections import defaultdict

from sortedcontainers import SortedSet

H, W, rs, cs = [int(l) for l in input().split()]
N = int(input())
# 上からrマス目にある壁一覧
Rdata = defaultdict(lambda:SortedSet([0, W+1]))
# 左からcマス目にある壁一覧
Cdata = defaultdict(lambda:SortedSet([0, H+1]))
for n in range(N):
    r, c = [int(l) for l in input().split()]
    Rdata[r].add(c)
    Cdata[c].add(r)
Q = int(input())
res = []
for q in range(Q):
    tmp = None
    D, L = [l for l in input().split()]
    L = int(L)
    if D == "L":
        tmp = Rdata[rs].bisect(cs)
        cs = max(Rdata[rs][tmp-1] + 1, cs - L)
    elif D == "U":
        tmp = Cdata[cs].bisect(rs)
        rs = max(Cdata[cs][tmp-1] + 1, rs - L)
    elif D == "R":
        tmp = Rdata[rs].bisect(cs)
        cs = min(Rdata[rs][tmp] - 1, cs + L)
    elif D == "D":
        tmp = Cdata[cs].bisect(rs)
        rs = min(Cdata[cs][tmp] - 1, rs + L)
    res.append([rs, cs])
for r in res:
    print(*r)
