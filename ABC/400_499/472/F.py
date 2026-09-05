from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
A = FenwickTree(N)
for n in range(N):
    l = n
    r = (n + 1) % N
    x1, y1 = XY[l]
    x2, y2 = XY[r]
    A.add(n, (abs(x2 - x1) * (y2 + y1) * 6))
GX = FenwickTree(N)
GY = FenwickTree(N)
for n in range(N):
    l = n
    r = (n + 1) % N
    x1, y1 = XY[l]
    x2, y2 = XY[r]
    GX.add(n, ((x2 ** 3  - x1 ** 3) * (y2 - y1) * 4 + (x2 ** 2 + x1 ** 2) * (x2 * y1 - x1 * y2) * 6)/(x2 - x1))
    GY.add(n, ((y2 ** 3  - y1 ** 3) * (x2 - x1) * 4 + (y2 ** 2 + y1 ** 2) * (y2 * x1 - y1 * x2) * 6)/(y2 - y1))

for _ in range(Q):
    u, v = map(int, input().split())
    if u < v:
        l = u
        r = v
        x1, y1 = XY[r - 1]
        x2, y2 = XY[l]
        s1 = A.sum(l, r)
        s2 = (abs(x2 - x1) * (y2 + y1) * 6)
        gx1 = GX.sum(l, r)
        gx2 = ((x2 ** 3  - x1 ** 3) * (y2 - y1) * 4 + (x2 ** 2 + x1 ** 2) * (x2 * y1 - x1 * y2) * 6)/(x2 - x1)
        gy1 = GY.sum(l, r)
        gy2 = ((y2 ** 3  - y1 ** 3) * (x2 - x1) * 4 + (y2 ** 2 + y1 ** 2) * (y2 * x1 - y1 * x2) * 6)/(y2 - y1)      
        print((gx1 + gx2)/(s1 + s2), (gy1 + gy2)/(s1 + s2))
    elif u > v:
        l = v + 1
        r = u - 1
    else:
        raise ValueError()
