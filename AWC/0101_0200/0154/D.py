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

        self.count = defaultdict(int)

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
                    self.count[v] = 1
                    heappush(self.Q, (alt, v))
                elif self.dist[v] == alt:
                    self.count[v] += 1

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
            node = self.prev[node][0]
        return path[::-1]

    def prev_path(self, node):
        """
        startからgoalまでの最短経路についてnodeに至る1つ前の値
        """
        return self.prev[node][0]

    def __repr__(self):
        return f"Node index:{self.dist} prev:{self.prev}"

g = Graph()
rG = Graph()
N, M = map(int, input().split())
for _ in range(M):
    u, v, w = map(int, input().split())
    g.add_edge(u-1, v-1, w)
    rG.add_edge(v-1, u-1, w)

dist = [[INF] * N for _ in range(N)]
rDist = [[INF] * N for _ in range(N)]
for src in range(N):
    d = Dijkstra(g, src)
    rd = Dijkstra(rG, src)
    for dst in range(N):
        di = d.shortest_distance(dst)
        dist[src][dst] = di
        di = rd.shortest_distance(dst)
        rDist[src][dst] = di

result = [0] * N
for src in range(N):
    data = []
    maxDi = 0
    for dst in range(N):
        di = dist[src][dst]
        if di >= INF:
            continue
        maxDi = max(di, maxDi)
        heappush(data, (-di, dst))
    graph = rG.graph
    res = [0] * N
    while data:
        di, dst = heappop(data)
        di = -di
        for nextNode, weight in graph[dst]:
            nextWeight = di - weight
            if nextNode != src and nextWeight == dist[src][nextNode]:
                res[nextNode] += res[dst] + 1
    for n in range(N):
        result[n] += res[n]
print(*result, sep="\n")
