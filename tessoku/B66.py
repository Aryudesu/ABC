from atcoder.dsu import DSU

N, M = [int(l) for l in input().split()]
# ノードをメモ
AB = dict()
for m in range(M):
    AB[m] = [int(l) - 1 for l in input().split()]
# クエリをメモ
Q = int(input())
query = []
deleteData = set()
for q in range(Q):
    tmp = [int(l) for l in input().split()]
    if tmp[0] == 1:
        x = tmp[1]
        query.append((1, x - 1))
        deleteData.add(x - 1)
    else:
        n, a, b = tmp
        query.append((n, a - 1, b - 1))
query.reverse()


dsu = DSU(N + 1)
for m in range(M):
    if m in deleteData:
        continue
    a, b = AB[m]
    dsu.merge(a, b)

result = []
for q in query:
    if q[0] == 1:
        x = q[1]
        a, b = AB[x]
        dsu.merge(a, b)
    else:
        n, a, b = q
        result.append("Yes" if dsu.same(a, b) else "No")
result.reverse()
for r in result:
    print(r)
