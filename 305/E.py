# すみませんでした
N, M, K = [int(l) for l in input().split()]
yet = [True] * (N + 1)
nodeHP = [-1] * (N + 1)
graph = dict()
for m in range(M):
    a, b = [int(l) for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp
sg = set()
for k in range(K):
    p, h = [int(l) for l in input().split()]
    nodeHP[p] = h
    yet[p] = False
    sg.add((p, h))

while sg:
    new_sg = set()
    for s in sg:
        p, h = s
        if h == 0:
            continue
        node = graph.get(p, [])
        # print(node)
        for n in node:
            if nodeHP[n] <= h - 1 or yet[n]:
                nodeHP[n] = h-1
                new_sg.add((n, h-1))
                yet[n] = False
        # print(yet)
    sg = new_sg
result = []
count = 0
for i in range(1, N + 1):
    if not yet[i]:
        count += 1
        result.append(i)
print(count)
print(*result)
