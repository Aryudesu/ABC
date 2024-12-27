N = int(input())
graph = dict()
# 辺が何本伸びているか
node_data = [0] * N
for n in range(N-1):
    u, v = [int(l) - 1 for l in input().split()]
    tmp = graph.get(u, [])
    tmp.append(v)
    graph[u] = tmp
    tmp = graph.get(v, [])
    tmp.append(u)
    graph[v] = tmp
    node_data[u] += 1
    node_data[v] += 1
max_tree = 0
for n in range(N):
    data = dict()
    nodes = graph.get(n, [])
    node_list = []
    for node in nodes:
        if not node_data[node] in data:
            node_list.append(node_data[node])
        data[node_data[node]] = data.get(node_data[node], 0) + 1
    node_list.sort(reverse=True)
    # print(data)
    num = 0
    for node in node_list:
        num += data.get(node, 0)
        tmp = num * node + 1
        max_tree = max([max_tree, tmp])
print(N - max_tree)
