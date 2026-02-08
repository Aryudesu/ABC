from atcoder.dsu import DSU

N, M = map(int, input().split())
edge = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append((c, a-1, b-1))
edge.sort()
dsu = DSU(N)
result = 0
for c, a, b in edge:
    if dsu.same(a, b):
        continue
    dsu.merge(a, b)
    result += c
print(result)
