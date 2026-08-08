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

    def prev_path(self, node):
        """
        startからgoalまでの最短経路についてnodeに至る1つ前の値
        """
        return self.prev[node]

    def __repr__(self):
        return f"Node index:{self.dist} prev:{self.prev}"

N, M = map(int, input().split())
S, T, P = map(int, input().split())
g = Graph()
for m in range(M):
    u, v, w = map(int, input().split())
    g.add_edge(u-1, v-1, w)
    g.add_edge(v-1, u-1, w)
anzendo = []
d = Dijkstra(g, P-1)
for i in range(N):
    anzendo.append(d.shortest_distance(i))
# print(anzendo)
data = []
heappush(data, (-anzendo[S-1], S-1))
result = [0] * N
result[S-1] = anzendo[S-1]
while data:
    nowAnzendo, nowPos = heappop(data)
    nowAnzendo = -nowAnzendo
    if result[nowPos] > nowAnzendo:
        continue
    for nextPos, _ in g.graph[nowPos]:
        nextAnzendo = min(nowAnzendo, anzendo[nextPos])
        if result[nextPos] >= nextAnzendo:
            continue
        result[nextPos] = max(nextAnzendo, result[nextPos])
        heappush(data, (-result[nextPos], nextPos))
res = result[T-1]
print(res if res < INF else "INF")
