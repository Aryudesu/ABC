N, M = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    a, b, c = [int(l) for l in input().split()]
    tmp = graph.get(a)
    if tmp is None:
        tmp = dict()
    tmp2 = tmp.get(b, 0)
    tmp[b] = c if tmp2 < c else tmp2
    graph[a] = tmp
    tmp = graph.get(b)
    if tmp is None:
        tmp = dict()
    tmp2 = tmp.get(a, 0)
    tmp[a] = c if tmp2 < c else tmp2
    graph[b] = tmp

yet = set()


def calc(node, dist):
    result = dist
    g = graph.get(node)
    if g is None:
        return result
    for key in g:
        if key in yet:
            continue
        d = g.get(key)
        if d is None:
            continue
        yet.add(key)
        res = calc(key, dist + d)
        if result < res:
            result = res
        yet.remove(key)
    return result


result = 0
for i in range(1, N+1):
    yet.add(i)
    res = calc(i, 0)
    yet.remove(i)
    if result < res:
        result = res
print(result)
