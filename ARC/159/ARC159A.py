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


N, K = [int(l) for l in input().split()]
A = []
for n in range(N):
    A.append([int(l) for l in input().split()])
g = Graph()
for n in range(N):
    tmp = []
    for n_ in range(N):
        if A[n][n_]:
            g.add_edge(n, n_, 1)
D = []
for n in range(N):
    tmp = []
    d = Dijkstra(g, n)
    for n_ in range(N):
        dst = d.shortest_distance(n_)
        tmp.append(-1 if dst == INF else dst)
    D.append(tmp)

Q = int(input())
result = []
for q in range(Q):
    s, t = [int(l) - 1 for l in input().split()]
    s_, t_ = s//N, t//N
    if s_ == t_:
        result.append(D[s % N][t % N])
    else:
        m = -1
        for n in range(N):
            dst = -1
            if A[s % N][n]:
                if D[n][t % N] != -1:
                    dst = 1 + D[n][t % N]
                    if m > dst or m == -1:
                        m = dst
        result.append(m)
for r in result:
    print(r)
