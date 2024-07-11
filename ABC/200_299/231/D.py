from atcoder import scc

N, M = [int(l) for l in input().split()]
sc = scc.SCCGraph(N)
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    sc.add_edge(a, b)

res = sc.scc()
print(res)
