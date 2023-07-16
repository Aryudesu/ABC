N, T, M = [int(l) for l in input().split()]
graph = dict()
Team = []
for t in range(T):
    tmp = set()
    Team.append(tmp)
bad = set()
for m in range(M):
    a, b = [int(l) for l in input().split()]
    bad.add(a)
    bad.add(b)
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp


def partition(AB, node):
    pass
