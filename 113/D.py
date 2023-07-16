N, M = [int(l) for l in input().split()]
PY = dict()
Data = []
for m in range(M):
    p, y = [int(l) for l in input().split()]
    Data.append([p, y, m])
Data.sort()
bp = None
for p, y, m in Data:
    if bp != p:
        pc = 1
    PY[m] = str(p).zfill(6) + str(pc).zfill(6)
    bp = p
    pc += 1
for m in range(M):
    print(PY.get(m))
