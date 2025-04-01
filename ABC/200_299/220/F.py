import sys
from collections import defaultdict

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self):
        # そのノードのdist
        self.allDist = 0
        # その辺につながってるノードの総数
        self.nums = defaultdict(lambda:0)
        # その辺から枝までの距離
        self.dist = defaultdict(lambda:0)

def dfs1(N, graph, data, now_node, prev_node, memo: set):
    next_node = graph[now_node]
    dist = 0
    node_nums = 1
    for nn in next_node:
        if nn in memo:
            continue
        memo.add(nn)
        d, n = dfs1(N, graph, data, nn, now_node, memo)
        data[now_node].nums[nn] = n
        data[now_node].dist[nn] = d + n
        dist += d + n
        node_nums += n
        memo.remove(nn)
    data[now_node].nums[prev_node] = N - node_nums
    return dist, node_nums

def dfs2(N, graph, data, now_node, now_dist, memo: set):
    next_node = graph[now_node]
    data[now_node].allDist = now_dist
    for nn in next_node:
        if nn in memo:
            continue
        memo.add(nn)
        dfs2(N, graph, data, nn, now_dist - data[now_node].nums[nn] + (N - data[now_node].nums[nn]), memo)
        memo.remove(nn)

N = int(input())
graph = defaultdict(list)
for n in range(N-1):
    u, v = [int(l) - 1 for l in input().split()]
    graph[u].append(v)
    graph[v].append(u)
result = defaultdict(lambda:Node())
for i in range(N):
    if len(graph[i]) == 1:
        lf = i
        break
d, n = dfs1(N, graph, result, lf, None, {lf})
dfs2(N, graph, result, lf, d, {lf})
for i in range(N):
    print(result[i].allDist)
