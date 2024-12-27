def isNibuGraph(graph, N):
    data = dict()
    memo = set()
    nums = set([i for i in range(N)])
    while nums:
        d = nums.pop()
        nodes = set([d])
        memo.add(d)
        data[d] = 1
        color = 0
        while nodes:
            new_nodes = set()
            for n in nodes:
                edge = graph.get(n, [])
                for e in edge:
                    if e in memo:
                        continue
                    data[e] = color
                    new_nodes.add(e)
                    memo.add(e)
                    nums.discard(e)
            nodes = new_nodes
            color = 1 - color
    for n in range(N):
        edge = graph.get(n, [])
        for e in edge:
            if data.get(e) == data.get(n):
                return False
    return True

N, M = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp
print("Yes" if isNibuGraph(graph, N) else "No")
