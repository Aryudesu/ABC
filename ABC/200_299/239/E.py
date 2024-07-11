from atcoder.dsu import DSU

N, Q = [int(l) for l in input().split()]
X = [int(l) for l in input().split()]
dsu = DSU(N)

for n in range(N-1):
    a, b = [int(l) - 1 for l in input().split()]
    dsu.merge(a, b)
node_data = dict()

for n in range(N):
    leader = dsu.leader(n)
    tmp = node_data.get(leader, [])
    tmp.append(X[n])
    node_data[leader] = tmp

for k in node_data:
    node_data[k].sort()


for q in range(Q):
    v, k = [int(l) for l in input().split()]

