from collections import defaultdict
from sortedcontainers import SortedList

INF = 10**18
N, D = map(int, input().split())
lData = defaultdict(list)
rData = defaultdict(list)
cData = defaultdict(list)
X = set()
for n in range(N):
    x, c = map(int, input().split())
    lData[x-D].append((c, n))
    rData[x+D+1].append((c, n))
    cData[x].append((c, n))
    X.add(x)
    X.add(x-D)
    X.add(x+D+1)
result = INF
data = SortedList()
X = sorted(X)
for x in X:
    if x in rData:
        for v in rData[x]:
            data.discard(v)
    if x in lData:
        for v in lData[x]:
            data.add(v)
    if x in cData:
        for v, idx in cData[x]:
            minVal, minIdx = data[0]
            if idx != minIdx:
                result = min(minVal + v, result)
if result == INF:
    print(-1)
else:
    print(result)
