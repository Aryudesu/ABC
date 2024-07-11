from atcoder.dsu import DSU

N, M = [int(l) for l in input().split()]
AB = []
dsu = DSU(N)
graph = dict()
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    AB.append((a, b))
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp
    dsu.merge(a, b)
leaders = set()
data = dict()
data2 = dict()
for n in range(N):
    leader = dsu.leader(n)
    s = graph.get(n, [])
    leaders.add(leader)
    data[leader] = data.get(leader, 0) + len(s)
    data2[leader] = data2.get(leader, 0) + 1
result = 0
for l in leaders:
    tmp1 = data2[l]
    result += (tmp1 * (tmp1 - 1)) // 2 - data[l]//2
print(result)
