from atcoder.dsu import DSU

N, M = [int(l) for l in input().split()]
dsu = DSU(N)
AB = dict()
for _ in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    a, b = (a, b) if a < b else (b, a)
    tmp = AB.get(a, [])
    tmp.append(b)
    AB[a] = tmp

result = [0]
leader = set()
for n in range(N - 1, -1, -1):
    leader.add(n)
    nodes = AB.get(n, [])
    for node in nodes:
        la = dsu.leader(n)
        lb = dsu.leader(node)
        dsu.merge(n, node)
        if la != lb:
            lc = dsu.leader(n)
            ld, le = (la, lb) if la != lc else (lb, la)
            leader.remove(ld)
            leader.add(le)
    result.append(len(leader))
result.reverse()
for n in range(1, N + 1):
    print(result[n])
