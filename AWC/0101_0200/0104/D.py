from sortedcontainers import SortedList
from collections import defaultdict

N, M = map(int, input().split())
T = list(map(int, input().split()))
field = [0] * N
fieldR = [0] * N
fieldL = [0] * N
PB = defaultdict(list)
for m in range(M):
    p, b = map(int, input().split())
    PB[p - 1].append(b)
data = SortedList()
delDat = defaultdict(list)
s = 0
for n in range(N):
    s = max(0, s - len(data))
    fieldR[n] = s
    if n in PB:
        for b in PB[n]:
            s += b
            fieldR[n] += b
            data.add(b)
            delDat[n + b].append(b)
    if n in delDat:
        for b in delDat[n]:
            data.discard(b)
# print(fieldR)
data = SortedList()
delDat = defaultdict(list)
s = 0
for n in range(N-1,-1,-1):
    s = max(0, s - len(data))
    fieldL[n] += s
    if n in PB:
        for b in PB[n]:
            s += b
            fieldL[n] += b
            data.add(b)
            delDat[n - b].append(b)
    if n in delDat:
        for b in delDat[n]:
            data.discard(b)
# print(fieldL)
result = 0
for n in range(N):
    field[n] = fieldL[n] + fieldR[n]
    if n in PB:
        for b in PB[n]:
            field[n] -= b
    if field[n] <= T[n]:
        result = max(field[n], result)
# print(field)
print(result)
