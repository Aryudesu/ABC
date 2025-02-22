import sys

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
memo = dict()

def dfs(graph, now_node, prev_node):
    """そのノードに接続される最大数を計算する"""
    memotmp = tuple([prev_node, now_node])
    if not prev_node is None and memotmp in memo:
        return memo[memotmp]
    nodes = graph.get(now_node, [])
    # 3次以下であればそのノードで打ち切りになる
    if len(nodes) <= 3:
        return 1
    # 始点の隣のデータは残しておく
    data = [0, 0, 0, 0]
    for next_node in nodes:
        # 逆流防止
        if prev_node == next_node:
            continue
        r = dfs(graph, next_node, now_node)
        if data[3] > r:
            continue
        if data[0] <= r:
            data[3] = data[2]
            data[2] = data[1]
            data[1] = data[0]
            data[0] = r
        elif data[1] <= r:
            data[3] = data[2]
            data[2] = data[1]
            data[1] = r
        elif data[2] <= r:
            data[3] = data[2]
            data[2] = r
        elif data[3] <= r:
            data[3] = r
    if not prev_node is None:
        data[3] = 0
    result = data[0] + data[1] + data[2] + data[3] + 1
    memo[memotmp] = result
    return result


N = int(input())
graph = dict()
for n in range(N - 1):
    a, b = [int(l) - 1 for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp
# print(graph)
fourNodes = set()
for i in range(N):
    nodes = graph.get(i, [])
    if len(nodes) >= 4:
        fourNodes.add(i)
# print(fourNodes)
result = -1
for i in range(N):
    if i in fourNodes:
        r = dfs(graph, i, None)
        result = max([result, r])
print(result)
