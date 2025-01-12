from atcoder.dsu import DSU
from atcoder.scc import SCCGraph


def dp(data):
    pass

def calc(data):
    pass

N, M = [int(l) for l in input().split()]
A = [int(l) - 1 for l in input().split()]
g = SCCGraph(N)
d = DSU(N)
data = dict()
for i in range(N):
    g.add_edge(i, A[i])
    d.merge(i, A[i])
scc = g.scc()
for s in scc:
    node = s[0]
    l = d.leader(node)
    data[l] = data.get(l, 0) + 1
print(data)
