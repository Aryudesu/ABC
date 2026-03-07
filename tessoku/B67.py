from atcoder.dsu import DSU

N, M = map(int, input().split())
dsu = DSU(N)
edge = []
for m in range(M):
    a, b, c = map(int, input().split())
    edge.append((c, a-1, b-1))
edge.sort(reverse=True)
result = 0
for c, a, b in edge:
    if not dsu.same(a, b):
        result += c
        dsu.merge(a, b)
print(result)
