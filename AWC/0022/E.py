from collections import defaultdict
from typing import Tuple
from atcoder.dsu import DSU
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

def calc(N: int, M: int, distData: list[list[Tuple[int, int]]])->int:
    INF = 10 ** 18
    goal = (1 << N) - 1
    result = INF
    # 現在地, マスク: 距離
    dp = {(0, 1): 0}
    for n in range(N):
        newDP = dict()
        for key in dp:
            nowP, mask = key
            dist = dp[key]
            for i in range(N):
                m = 1 << i
                if mask & m:
                    continue
                d, msk = distData[nowP][i]
                newDist = dist + d
                newP = i
                newMask = mask | msk
                if newMask == goal:
                    d, m = distData[newP][0]
                    result = min(result, newDist + d)
                else:
                    newDP[(newP, newMask)] = min(newDP.get((newP, newMask), INF), newDist)
        dp = newDP
    return result


N, M = map(int, input().split())
g = Graph()
dsu = DSU(N)

for m in range(M):
    u, v, w = map(int, input().split())
    dsu.merge(u-1, v-1)
    g.add_edge(u-1, v-1, w)
    g.add_edge(v-1, u-1, w)

if dsu.size(0) != N:
    print(-1)
    exit(0)

distData = [[0] * N for _ in range(N)]

for i in range(N):
    d = Dijkstra(g, i)
    for j in range(N):
        mask = 0
        dist = d.shortest_distance(j)
        for m in d.shortest_path(j):
            mask |= 1 << m
        distData[i][j] = (dist, mask)

print(calc(N, M, distData))

# すみません　一旦落ちますorz
