from collections import defaultdict

from atcoder.dsu import DSU
from sortedcontainers import SortedSet

N, M = [int(l) for l in input().split()]
graph = defaultdict(set)
for m in range(M):
    u, v = [int(l) - 1 for l in input().split()]
    graph[v].add(u)
    graph[u].add(v)
# print(graph)
dsu = DSU(N)
delete_set = set()
result = []
set_data = defaultdict(set)
for i in range(N):
    set_data[i].add(i)

for i in range(0, N):
    next_nodes = graph[i]
    for node in next_nodes:
        if node < i:
            n_leader = dsu.leader(node)
            i_leader = dsu.leader(i)
            new_set = set()
            if n_leader != i_leader:
                if len(set_data[n_leader]) > len(set_data[i_leader]):
                    set_data[n_leader].update(set_data[i_leader])
                    new_set = set_data[n_leader]
                else:
                    set_data[i_leader].update(set_data[n_leader])
                    new_set = set_data[i_leader]
                dsu.merge(node, i)
                new_leader = dsu.leader(node)
                set_data[i_leader] = set()
                set_data[n_leader] = set()
                set_data[new_leader] = new_set
        else:
            delete_set.add(node)
    delete_set.discard(i)
    if dsu.same(0, i) and len(set_data[dsu.leader(0)]) == i + 1:
        result.append(len(delete_set))
    else:
        result.append(-1)
for r in result:
    print(r)
