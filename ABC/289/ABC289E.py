def calc(takahashi, aoki, C, graph, memo):
    Node = {(0, N - 1)}
    # 深さ優先探索を！！！組みたい！！！ orz
    while Node:
        pass


T = int(input())
for t in range(T):
    N, M = [int(l) for l in input().split()]
    C = [int(l) - 1 for l in input().split()]
    graph = dict()
    for m in range(M):
        u, v = [int(l) - 1 for l in input().split()]
        tmp = graph.get(u, [])
        tmp.append(v)
        graph[u] = tmp
        tmp = graph.get(v, [])
        tmp.append(u)
        graph[v] = tmp
