from atcoder.scc import SCCGraph

N, M = [int(l) for l in input().split()]
scc = SCCGraph(N)
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    scc.add_edge(a, b)
data = scc.scc()
result = 0
for dat in data:
    num = len(dat)
    result += (num * (num - 1)) // 2
print(result)
