from collections import defaultdict
from heapq import heappop, heappush

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
        self.dist = [INF] * (H * W + 1)
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = [None] * (H * W + 1)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = max(dist_u, weight)
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


H, W, Y = [int(l) for l in input().split()]
A = []
for h in range(H):
    A.append([int(l) for l in input().split()])
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
g = Graph()
for h in range(H):
    for w in range(W):
        for dh, dw in dir:
            if h + dh >= H or h + dh < 0 or w + dw >= W or w + dw < 0:
                continue
            src = h * W + w
            dst = (h + dh) * W +  (w + dw)
            g.add_edge(src, dst, A[h+dh][w+dw])
start = H * W
for h in range(H):
    g.add_edge(start,h * W + 0, A[h][0])
    g.add_edge(start,h * W + (W-1), A[h][W-1])
for w in range(W):
    g.add_edge(start,0 * W +  w, A[0][w])
    g.add_edge(start,(H-1) * W + w, A[H-1][w])

d = Dijkstra(g, start)
result = defaultdict(lambda: 0)
for h in range(0, H):
    for w in range(0, W):
        pos = h * W + w
        result[d.shortest_distance(pos)] += 1
s = 0
for y in range(1, Y + 1):
    s += result[y]
    print(H * W - s)
