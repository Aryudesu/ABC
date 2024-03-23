from collections import defaultdict
from heapq import heappop, heappush

from atcoder.dsu import DSU

INF = 10**18


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
    def __init__(self, graph, start):
        self.g = graph.graph

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = defaultdict(lambda: INF)
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = defaultdict(lambda: None)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):
        """
        startノードからgoalノードまでの最短距離
        """
        return self.dist[goal]

    def shortest_path(self, goal):
        """
        startノードからgoalノードまでの最短経路
        """
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]

    def prev_path(self, node):
        """
        startからgoalまでの最短経路についてnodeに至る1つ前の値
        """
        return self.prev[node]

    def __repr__(self):
        return f'Node index:{self.dist} prev:{self.prev}'

H, W = [int(l) for l in input().split()]
Ch, Cw = [int(l) - 1 for l in input().split()]
Dh, Dw = [int(l) - 1 for l in input().split()]
S = []
for h in range(H):
    S.append(input())
d = DSU(H * W)
for h in range(H):
    for w in range(W):
        p1 = h * W + w
        if h < H - 1:
            if S[h][w] == "." and S[h+1][w] == ".":
                p2 = (h+1) * W + w
                d.merge(p1, p2)
        if w < W - 1:
            if S[h][w] == "." and S[h][w+1] == ".":
                p2 = h * W + (w + 1)
                d.merge(p1, p2)
# [代表点] = 連番
pointer = dict()
# [連番] = 代表点
inv_pointer = dict()
c = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        p = h * W + w
        l = d.leader(p)
        tmp = pointer.get(l)
        if tmp is None:
            pointer[l] = c
            inv_pointer[c] = l
            c += 1

node = set()
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        p1 = h * W + w
        l1 = d.leader(p1)
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                if h + dh >= 0 and h + dh < H and w + dw >= 0 and w + dw < W:
                    if S[h + dh][w + dw] == "#":
                        continue
                    p2 = (h + dh) * W + (w + dw)
                    l2 = d.leader(p2)
                    if l1 != l2:
                        n1 = pointer.get(l1)
                        n2 = pointer.get(l2)
                        tmp1 = (n1, n2)
                        tmp2 = (n2, n1)
                        node.add(tmp1)
                        node.add(tmp2)


g = Graph()
for src, dst in node:
    g.add_edge(src, dst, 1)

ps = Ch * W + Cw
startNode = pointer.get(d.leader(ps))
pg = Dh * W + Dw
goalNode = pointer.get(d.leader(pg))

d = Dijkstra(g, startNode)
res = d.shortest_distance(goalNode)
print(-1 if res == INF else res)
