N, M = [int(l) for l in input().split()]
graph = dict()
rev_graph = dict()
for m in range(M):
    X, Y = [int(l) for l in input().split()]
    # 要素の追加
    tmp = graph.get(X)
    if tmp is None:
        tmp = set()
    tmp.add(Y)
    graph[X] = tmp

    # 要素の追加
    tmp = rev_graph.get(Y)
    if tmp is None:
        tmp = set()
    tmp.add(X)
    rev_graph[Y] = tmp

    # 仮に分岐していたら
    tmp1 = rev_graph.get(X)
    tmp2 = rev_graph.get(Y)
    if tmp1 is not None and tmp2 is not None:
        rev_graph[Y] = {X}
    # 仮に分岐していたら
    tmp1 = graph.get(Y)
    tmp2 = graph.get(X)
    if tmp1 is not None and tmp2 is not None:
        # 共通のノードを見つける
        rev_graph[X] = {Y}
    print(graph)
    print(rev_graph)
print(graph)
print(rev_graph)
