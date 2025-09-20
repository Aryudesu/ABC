from collections import defaultdict
from heapq import heappop, heappush

INF = 10**18
class Dijkstra():
    def __init__(self, graph, start, weight):
        # startには(現在ノード, 体重)というデータをもたせる
        self.w = weight
        self.g = graph

        self.dist = defaultdict(lambda: INF)
        self.dist[start] = 0
        # (消費燃料, 体重, 現在ノード)のデータを持たせる
        self.Q = []
        heappush(self.Q, (self.dist[start], self.w[start], start))

        while self.Q:
            dist_u, weight_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v in self.g[u]:
                alt = dist_u + weight_u
                weight_u_tmp = weight_u + self.w[v]
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    heappush(self.Q, (alt, weight_u_tmp, v))
    
    def getResult(self, goal):
        return self.dist[goal]


N, M = [int(l) for l in input().split()]
W = [int(l) for l in input().split()]
graph = defaultdict(set)
for m in range(M):
    u, v = [int(l) - 1 for l in input().split()]
    graph[u].add(v)
    graph[v].add(u)
d = Dijkstra(graph, 0, W)
for i in range(N):
    print(d.getResult(i))
