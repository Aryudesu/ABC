from atcoder.dsu import DSU

N, Q = [int(l) for l in input().split()]
M = N + Q
dsu = DSU(M)
Pcount = 0
XData = []
YData = []
for n in range(N):
    x, y = [int(l) for l in input().split()]
    XData.append([x + y, Pcount])
    YData.append([x - y, Pcount])
    Pcount += 1

result = []
for _ in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        n, a, b = query
        XData.append([a + b, Pcount])
        Pcount += 1
    elif query[0] == 2:
        n = query
    elif query[0] == 3:
        n, u, v = query
        u -= 1
        v -= 1
        if dsu.same(u, v):
            result.append("Yes")
        else:
            result.append("No")
