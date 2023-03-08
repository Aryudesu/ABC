def get_subgraphs(graph, node_num):
    """部分グラフに分割したい"""
    nodes = [False] * (node_num + 1)
    result = []
    for n in range(1, node_num + 1):
        # 既に訪問済なら飛ばす
        if nodes[n]:
            continue
        nodes[n] = True
        # nodeに追加
        t_res = []
        t_res.append(n)
        # 現在訪問ノード
        node = set()
        node.add(n)
        while node:
            new_node = set()
            # ノード全探索
            for no in node:
                tmp = graph.get(no, [])
                for t in tmp:
                    if nodes[t]:
                        continue
                    new_node.add(t)
                    t_res.append(t)
                    nodes[t] = True
            node = new_node
        result.append(t_res)
    return result


def calc(sbg, node):
    """分割した部分グラフがちゃんと条件を満たすか"""
    for sb in sbg:
        ls = len(sb)
        tmp = 0
        for s in sb:
            tmp += node.get(s, 0)
        if ls != tmp:
            return False
    return True


N, M = [int(l) for l in input().split()]
graph = dict()
node = dict()
for m in range(M):
    u, v = [int(l) for l in input().split()]
    tmp = graph.get(u, [])
    tmp.append(v)
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append(u)
    graph[v] = tmp
    tmp = node.get(u, 0)
    node[u] = tmp + 1
sbg = get_subgraphs(graph, N)
print("Yes" if calc(sbg, node) else "No")
