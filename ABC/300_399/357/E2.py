from atcoder.scc import SCCGraph

N = int(input())
A = [int(l)-1 for l in input().split()]
scc = SCCGraph(N)

for n in range(N):
    scc.add_edge(n, A[n])
print(scc.scc())
