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

# 一筆書き可能な最大 + はみ出た部分 * 2　をやりたい
N, M = map(int, input().split())
zisuu = [0] * N
g = Graph()
allW = 0
E = []
for m in range(M):
    u, v, w = map(int, input().split())
    g.add_edge(u-1, v-1, w)
    g.add_edge(v-1, u-1, w)
    allW += w
    zisuu[u-1] += 1
    zisuu[v-1] += 1
    E.append((u-1, v-1))

# print(zisuu)
kisuPos = []
for i in range(N):
    if zisuu[i] % 2:
        kisuPos.append(i)
if len(kisuPos) == 0:
    print(allW)
    exit(0)
L = len(kisuPos)
dist = [[0] * L for _ in range(L)]
for i in range(L):
    p1 = kisuPos[i]
    d = Dijkstra(g, p1)
    for j in range(L):
        p2 = kisuPos[j]
        dist[i][j] = d.shortest_distance(p2)
# 奇数同士をつなぐ辺の最小部分を足して全部偶数次にしたやつが答え
# bit全探索すれば良い？
goal = 1 << L
INF = 10**12
data = [INF] * (1 << L)
for i in range(L):
    for j in range(L):
        if i == j:
            continue
        b1 = 1 << i
        b2 = 1 << j
        data[b1 | b2] = dist[i][j]

for mask in range(1 << L):
    if mask.bit_count() % 2:
        continue
    dst = data[mask]
    for i in range(L):
        b1 = 1 << i
        if b1 & mask:
            continue
        for j in range(L):
            b2 = 1 << j
            if b2 & mask:
                continue
            newMask = mask | b1 | b2
            newDist = dst + dist[i][j]
            data[newMask] = min(data[newMask], newDist)

print(data[-1] + allW)
