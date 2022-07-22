import bisect

N = int(input())
graph = [int(l) for l in input().split()]
for n in range(N - 1):
    L, R = [int(l) for l in input().split()]
    idx = bisect.bisect_left(graph, L)
    if idx % 2 == 1:
        graph[idx] = R
    else:
        #graph.insert(idx, L)
        idx2 = bisect.bisect_left(graph, R)
        if idx2 % 2 == 1:
            graph[idx]
    print(graph)
