from atcoder.dsu import DSU

N, M = [int(l) for l in input().split()]
uf = DSU(N)
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    uf.merge(a, b)
print("The graph is connected." if len(uf.groups()) == 1 else "The graph is not connected.")
