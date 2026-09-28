from atcoder.fenwicktree import FenwickTree
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

N, Q = map(int, input().split())
g = Graph()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ftA = FenwickTree(N * 2)
for n in range(N * 2):
    ftA.add(n, A[n % N])
for n in range(N):
    g.add_edge(n, (n+1) % N, A[n])
    g.add_edge((n+1) % N, n, A[n])
    g.add_edge(n, N, B[n])
    g.add_edge(N, n, B[n])

d = Dijkstra(g, N)
result = []
for _ in range(Q):
    s, t = map(int, input().split())
    s, t = min(s, t) - 1, max(s, t) - 1
    if t < N:
        res1 = ftA.sum(s, t)
        res1 = min(res1, ftA.sum(t, s+N))
        res2 = d.shortest_distance(s) + d.shortest_distance(t)
        result.append(min(res1, res2))
    else:
        res2 = d.shortest_distance(s)
        result.append(res2)
print(*result, sep="\n")
