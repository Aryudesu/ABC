from collections import defaultdict
from atcoder.dsu import DSU

N, Q = map(int, input().split())
height = [0] * N
score = [0] * N
hMemo = defaultdict(list)
hSet = set()
hData = []
scoreResult = []
bisectH = []
for n in range(N):
    a, b = map(int, input().split())
    height[n] = a
    score[n] = b
    hMemo[a].append(n)
    if a not in hSet:
        hData.append(a)
        hSet.add(a)
hData.sort()
bisectH = hData.copy()
viewH = [False] * N
dsu = DSU(N)

score = 0
scores = dict()
while hData:
    h = hData.pop()
    for hIdx in hMemo[h]:
        viewH[hIdx] = True
        if hIdx - 1 >= 0 and viewH[hIdx - 1]:
            dsu.merge(hIdx, hIdx - 1)
        if hIdx + 1 < N and viewH[hIdx + 1]:
            dsu.merge(hIdx, hIdx - 1)

for _ in range(Q):
    pass
