import sys
sys.setrecursionlimit(10**6)
N, M = [int(l) for l in input().split()]
visit = [False] * N
limit = 10**6
path = []
graph = dict()


def dfs(c):
    result = 0
    visit[c] = True
    g = graph.get(c, [])
    if not g:
        return 1
    for d in g:
        if result == limit:
            return limit
        if not visit[d]:
            result += dfs(d)
    visit[c] = False
    return result


for m in range(M):
    u, v = [int(l) - 1 for l in input().split()]
    tmp = graph.setdefault(u, [])
    tmp.append(v)
    graph[u] = tmp
    tmp = graph.setdefault(v, [])
    tmp.append(u)
    graph[v] = tmp

result = dfs(0)
print(result)
