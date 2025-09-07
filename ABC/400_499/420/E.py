from atcoder.dsu import DSU
from collections import defaultdict
N, Q = [int(l) for l in input().split()]
leaders = set()
# 黒いノードたち保存用
blackData = defaultdict(set)
nodeData = [False] * N
result = []
dsu = DSU(N)
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        n, u, v = query
        u, v = u - 1, v - 1
        l1 = dsu.leader(u)
        l2 = dsu.leader(v)
        if l1 == l2:
            continue
        blacks1 = blackData[l1]
        blacks2 = blackData[l2]
        dsu.merge(u, v)
        l3 = dsu.leader(u)
        if len(blacks1) < len(blacks2):
            blacks2.update(blacks1)
            blackData[l3] = blacks2
        else:
            blacks1.update(blacks2)
            blackData[l3] = blacks1
    elif query[0] == 2:
        n, v = query
        v = v - 1
        l1 = dsu.leader(v)
        if nodeData[v]:
            nodeData[v] = False
            blackData[l1].discard(v)
        else:
            nodeData[v] = True
            blackData[l1].add(v)
    elif query[0] == 3:
        n, v = query
        v = v - 1
        l1 = dsu.leader(v)
        if len(blackData[l1]) > 0:
            result.append("Yes")
        else:
            result.append("No")
    else:
        raise Exception()
for r in result:
    print(r)
