from atcoder.dsu import DSU

N, M = [int(l) for l in input().split()]
dsu = DSU(N)
result = 0
same_data = set()
for i in range(M):
    u, v = [int(l) - 1 for l in input().split()]
    if dsu.same(u, v):
        result += 1
    dsu.merge(u, v)
print(result)
