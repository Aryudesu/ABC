def is_bipartite_graph(graph, N):
    node_color = [None for _ in range(N)]
    color_result = []
    # 探索
    for idx in range(N):
        # 色が塗られていない場合
        if node_color[idx] is None:
            node_color[idx] = True
            node = set()
            node.add(idx)
        else:
            continue
        t_count = 1
        f_count = 0
        while node:
            next_node = set()
            for n in node:
                # 接続しているノード一覧
                tmp = graph.get(n, [])
                # 次のノードでぶん回す
                for t in tmp:
                    # 次のノードの色が塗られていないなら
                    if node_color[t] is None:
                        # 次の探索のノード対象に追加
                        next_node.add(t)
                        node_color[t] = not node_color[n]
                        # 次の探索のノード対象に追加
                        if node_color[t]:
                            t_count += 1
                        else:
                            f_count += 1
                    else:
                        # 次のノードが同じ色で塗られていたら二部グラフではない
                        if node_color[t] == node_color[n]:
                            return False, []
            node = next_node
        color_result.append([t_count, f_count])
    return True, color_result


def calc(graph, N, M):
    ibg, color = is_bipartite_graph(graph, N)
    if not ibg:
        return 0
    all_num = 0
    c_num = 0
    for c in color:
        tmp = 0
        tmp += c[0] * c[1]
        tmp += (c[0] + c[1]) * c_num
        all_num += tmp
        c_num += c[0] + c[1]
    return all_num - M


N, M = [int(l) for l in input().split()]
graph = {n: [] for n in range(N)}
for m in range(M):
    u, v = [int(l) for l in input().split()]
    tmp = graph.get(u-1)
    tmp.append(v-1)
    graph[u-1] = tmp
    tmp = graph.get(v-1)
    tmp.append(u-1)
    graph[v-1] = tmp
print(calc(graph, N, M))
