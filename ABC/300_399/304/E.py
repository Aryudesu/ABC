import sys
sys.setrecursionlimit(10**6)


def dfs(graph, num, node, result):
    nodes = graph.get(node)
    if nodes is None:
        return
    for n in nodes:
        if result[n] == -1:
            result[n] = num
            dfs(graph, num, n, result)


N, M = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    U, V = [int(l) for l in input().split()]
    tmp = graph.get(U)
    if tmp is None:
        tmp = set()
    tmp.add(V)
    graph[U] = tmp
    tmp = graph.get(V)
    if tmp is None:
        tmp = set()
    tmp.add(U)
    graph[V] = tmp

# ノードがどの小グラフに属するかを調べる
result = [-1] * (N + 1)
for i in range(1, N + 1):
    if result[i] == -1:
        result[i] = i
        dfs(graph, i, i, result)

# 繋いではいけない小グラフを調べる
K = int(input())
NG = set()
for _ in range(K):
    x, y = [int(l) for l in input().split()]
    nx, ny = result[x], result[y]
    NG.add((nx, ny))
# 質問回答フェーズ　繋いではいけないグラフ同士を繋ぐとNo
Q = int(input())
for q in range(Q):
    p, q = [int(l) for l in input().split()]
    np, nq = result[p], result[q]
    if (np, nq) in NG or (nq, np) in NG:
        print("No")
    else:
        print("Yes")
