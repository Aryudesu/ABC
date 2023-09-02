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

    def __repr__(self):
        return f'Node index:{self.dist} prev:{self.prev}'


N1, N2, M = [int(l) for l in input().split()]
g1 = Graph()
g2 = Graph()
for m in range(M):
    a, b = [int(l) for l in input().split()]
    if a <= N1:
        g1.add_edge(a-1, b-1, 1)
        g1.add_edge(b-1, a-1, 1)
    else:
        g2.add_edge(a-N1-1, b-N1-1, 1)
        g2.add_edge(b-N1-1, a-N1-1, 1)

d1 = Dijkstra(g1, 0)
d2 = Dijkstra(g2, N2-1)
md1 = 0
for n in range(N1):
    sd = d1.shortest_distance(n)
    if md1 < sd:
        md1 = sd
md2 = 0
for n in range(N2):
    sd = d2.shortest_distance(n)
    if md2 < sd:
        md2 = sd
print(md1 + md2 + 1)
