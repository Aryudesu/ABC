from atcoder.dsu import DSU

N, D = map(int, input().split())
XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
dsu = DSU(N)
DD = D * D
for i in range(N - 1):
    for j in range(i + 1, N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        dst = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if dst <= DD:
            dsu.merge(i, j)
for i in range(N):
    print("Yes" if dsu.same(i, 0) else "No")
