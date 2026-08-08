from collections import defaultdict
from atcoder.segtree import SegTree
XMax = 200005
N, Q = map(int, input().split())
ins = defaultdict(int)
insC = defaultdict(int)
delL = defaultdict(int)
delR = defaultdict(int)
for n in range(N):
    x, b = map(int, input().split())
    delR[x + b] += 1
    delL[x - b] += 1    
    ins[x] += b
    insC[x] += 1
imosL = [0] * XMax
imosR = [0] * XMax
imos = [0] * XMax
c = 0
power = 0
for x in range(XMax):
    power -= c
    if x in delR:
        c -= delR[x]
    if x in ins:
        power += ins[x]
        c += insC[x]
    imosR[x] = power
c = 0
power = 0
for x in range(XMax-1, -1, -1):
    power -= c
    if x in delL:
        c -= delL[x]
    if x in ins:
        power += ins[x]
        c += insC[x]
    imosL[x] = power
for x in range(XMax):
    imos[x] = imosL[x] + imosR[x]
    if x in ins:
        imos[x] -= ins[x]

INF = 10**18
st = SegTree(max, -INF, imos)
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    res = st.prod(l, r+1)
    result.append(res)
for r in result:
    print(r)
