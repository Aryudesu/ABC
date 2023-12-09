H, W, N = [int(l) for l in input().split()]
LU = dict()
RU = dict()
LD = dict()
RD = dict()
for n in range(N):
    A, B, C, D = [int(l) for l in input().split()]
    LU[(A - 1, B - 1)] = LU.get((A - 1, B - 1), 0) + 1
    RU[(A - 1, D - 1)] = RU.get((A - 1, D - 1), 0) + 1
    LD[(C - 1, B - 1)] = LD.get((C - 1, B - 1), 0) + 1
    RD[(C - 1, D - 1)] = RD.get((C - 1, D - 1), 0) + 1
result = []
tmp = []
s = 0
for x in range(W):
    s += LU.get((0, x), 0)
    tmp.append(s)
    s -= RU.get((0, x), 0)
result.append(tmp)
for y in range(1, H):
    tmp = []
    s = result[y-1][0] - LD.get((y-1, 0), 0)
    tmp.append(s)
    for x in range(1, W):
        s += LU.get((y, x), 0)
        s -= LD.get((y - 1, x), 0)
        s += RD.get((y - 1, x), 0)
        tmp.append(s)
        s -= RU.get((y, x), 0)
    result.append(tmp)
for r in result:
    print(*r)