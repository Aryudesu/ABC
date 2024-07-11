N = int(input())
XY = []
for n in range(N):
    XY.append([int(l) for l in input().split()])


result = []
for n in range(N):
    x1, y1 = XY[n]
    r = 0
    d = 0
    for m in range(N):
        if n == m:
            continue
        x2, y2 = XY[m]
        td = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if d < td:
            r = m
            d = td
    result.append(r + 1)
for r in result:
    print(r)

