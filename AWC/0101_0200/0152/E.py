from atcoder.scc import SCCGraph
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
scc = SCCGraph(N)
g1 = Graph()
for m in range(M):
    u, v = map(int, input().split())
    scc.add_edge(u-1, v-1)
    g1.add_edge(u-1, v-1)
scc = scc.scc()
circleData = set()
for dat in scc:
    if len(dat) > 2:
        for d in dat:
            circleData.add(d)
dists = dict()
canTotatsu = set()
for n in range(N):
    d = Dijkstra(g1, n)
    for m in range(N):
        dist = d.shortest_distance(m)
        if m in circleData:
            dists[(m, n)] = dist
        if dist < INF:
            canTotatsu.add((n, m))
resData = defaultdict(lambda: False)
for c in circleData:
    for s in range(N):
        for r in range(N):
            if s == r:
                continue
            ds = dists[(c, s)]
            dr = dists[(c, r)]
            if ds < dr or ((r, s) not in canTotatsu):
                resData[(s, r)] = True

Q = int(input())
result = []
for _ in range(Q):
    s, r = map(int, input().split())
    result.append("YES" if resData[(s, r)] else "NO")
print(*result, sep="\n")
