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

N, M, K = map(int, input().split())
V = list(map(int, input().split()))
g = Graph()
for m in range(M):
    a, b, c = map(int, input().split())
    g.add_edge(a, b, c)
    g.add_edge(b, a, c)
dist = [[0] * K for _ in range(K)]
oneDist = []
d = Dijkstra(g, 1)
for k in range(K):
    oneDist.append(d.shortest_distance(V[k]))
for k in range(K):
    d = Dijkstra(g, V[k])
    dist[k][k] = 0
    for l in range(k+1, K):
        dst = d.shortest_distance(V[l])
        dist[k][l] = dst
        dist[l][k] = dst

data = [[INF] * K for _ in range(1 << K)]
data[0] = 0
for k in range(K):
    b = 1 << k
    data[b][k] = oneDist[k]
goal = (1 << K) - 1
for mask in range(1, 1 << K):
    remain = goal ^ mask
    while remain:
        l = remain.bit_length() - 1
        b = 1 << l
        nextMask = mask | b
        for k in range(K):
            b2 = 1 << k
            if mask & b2 == 0:
                continue
            dst = data[mask][k]
            nextDist = dst + dist[k][l]
            data[nextMask][l] = min(data[nextMask][l], nextDist)
        remain ^= b
result = INF
for k in range(K):
    res = data[-1][k] + oneDist[k]
    result = min(result, res)
print(result)
