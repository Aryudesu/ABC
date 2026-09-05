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
g = Graph()
for m in range(M):
    u, v, w = map(int, input().split())
    g.add_edge(u-1, v-1, w)
    g.add_edge(v-1, u-1, w)
C = [int(l) - 1 for l in input().split()]
STC = []
CTT = []
distData = [[None] * K for _ in range(K)]
d = Dijkstra(g, 0)
for k in range(K):
    STC.append(d.shortest_distance(C[k]))
d = Dijkstra(g, N-1)
for k in range(K):
    CTT.append(d.shortest_distance(C[k]))
for k in range(K):
    distData[k][k] = 0
    d = Dijkstra(g, C[k])
    for l in range(K):
        dist = d.shortest_distance(C[l])
        distData[k][l] = dist
if K == 1:
    result = STC[0] + CTT[0]
    print(result)
    exit(0)
INF = 10 ** 18
# マスク: (現在位置: 距離)
dp = dict()
for k in range(K):
    dp[1 << k] = {k: STC[k]}
result = INF
goal = (1 << K) - 1
while dp:
    newDP = dict()
    for mask, inner in dp.items():
        for nowP, nowDist in inner.items():
            remain = goal ^ mask
            while remain:
                b = remain & -remain
                newP = b.bit_length() - 1
                remain ^= b

                d = distData[nowP][newP]
                if d == INF:
                    continue

                newMask = mask | (1 << newP)
                newDist = nowDist + d
                if newMask == goal:
                    back = CTT[newP]
                    if back != INF:
                        res = newDist + back
                        if result > res:
                            result = res
                else:
                    if newMask not in newDP:
                        newDP[newMask] = {newP: newDist}
                    else:
                        old = newDP[newMask].get(newP)
                        if old is None or old > newDist:
                            newDP[newMask][newP] = newDist
    dp = newDP
print(result)
