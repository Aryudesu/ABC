DEBUG = False


def dfs(graph, color, node, nodes, result):
    # 見ているノードに繋がるノード一覧
    no = graph.get(node, [])
    if DEBUG:
        print(graph, color, node, nodes, result, no)
    # 深さ優先探索
    count = 0
    for n in no:
        if not nodes[n]:
            nodes[n] = True
            res = dfs(graph, color, n, nodes, result)
            nodes[n] = False
            if not res:
                return res
            count += 1
    # 末端（行き止まり）なら色特定
    if count == 0:
        result[node - 1] = color[no[0] - 1]
        # そこから繋がっている枝のノードの色も特定できる
        if result[no[0] - 1] is None:
            result[no[0] - 1] = color[node - 1]
        # もし既に特定されている場合
        else:
            # 色が噛み合わなければダメ
            if result[no[0] - 1] != color[node - 1]:
                return False
    # 行き止まりでないなら色が特定している中から選びたい
    else:
        B = 0
        W = 0
        parent = None
        for n in no:
            # 子のノードの色を数える
            if not result[n - 1] is None:
                if result[n - 1] == "B":
                    B += 1
                else:
                    W += 1
            # 親ノードの保存
            else:
                parent = n
            # 注目ノードの色が特定される場合，入力値と噛み合うかの判定
            if B > W:
                # 現在のノードの色特定
                if result[node - 1] is None:
                    result[node - 1] == "B"
                elif result[node - 1] != "B":
                    return False
            elif B < W:
                if result[node - 1] is None:
                    result[node - 1] == "W"
                elif result[node - 1] != "W":
                    return False
                return False
            # 同数の場合親の色により決定される
            else:
                if result[parent - 1] is None:
                    result[parent - 1] = color[node - 1]
                elif result[parent - 1] != color[node - 1]:
                    return False
    return True


def calc():
    graph = dict()
    N = int(input())
    nodes = [False] * (N + 1)
    nodes[1] = True
    result = [None] * N
    for n in range(N - 1):
        A, B = [int(l) for l in input().split()]
        tmp = graph.get(A, [])
        tmp.append(B)
        graph[A] = tmp
        tmp = graph.get(B, [])
        tmp.append(A)
        graph[B] = tmp
    S = input()
    if DEBUG:
        print(graph)
    judge = dfs(graph, S, 1, nodes, result)
    if judge:
        return "".join(result)
    else:
        return -1


T = int(input())
result = []
for t in range(T):
    result.append(calc())
for r in result:
    print(r)
