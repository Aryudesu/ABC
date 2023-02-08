COUNT = 0


def calc(now, N, M, Node, graph):
    # print(now)
    global COUNT
    ALL[now] = True
    path = graph.get(now, [])
    Node[now] = True
    lp = len(path)
    # 行き止まり
    f = False
    for p in path:
        # 進める
        if not Node[p]:
            Node[p] = True
            f = True
            calc(p, N, M, Node, graph)
            Node[p] = False
    if not f:
        print(now)
        COUNT += 1
    Node[now] = False


N, M = [int(l) for l in input().split()]
ALL = [False] * N
graph = dict()
Node = [False] * N
for m in range(M):
    A, B = [int(l) for l in input().split()]
    tmp = graph.get(A - 1, [])
    tmp.append(B - 1)
    graph[A - 1] = tmp
    tmp = graph.get(B - 1, [])
    tmp.append(A-1)
    graph[B-1] = tmp
calc(0, N, M, Node, graph)
print(COUNT)
