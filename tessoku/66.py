from atcoder.dsu import DSU

N, Q = map(int, input().split())
dsu = DSU(N + 1)
result = []
for q in range(Q):
    t, u, v = map(int, input().split())
    if t == 1:
        dsu.merge(u, v)
    else:
        result.append("Yes" if dsu.same(u, v) else "No")
for r in result:
    print(r)
