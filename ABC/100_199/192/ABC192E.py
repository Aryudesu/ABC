from collections import defaultdict
from heapq import heappop, heappush

INF = 10**18
class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)
    
    # ノードの数
    def __len__(self):
        return len(self.graph)

    # 辺追加
    def add_edge(self, src, dst, T=1, K=1):
        self.graph[src].append((dst, T, K))
    
    # ノード追加
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
            for v, T, K in self.g[u]:
                alt = dist_u + T + (K - dist_u % K) % K
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


N, M, X, Y = [int(l) for l in input().split()]
g = Graph()
for m in range(M):
    A, B, T, K = [int(l) for l in input().split()]
    g.add_edge(A, B, T, K)
    g.add_edge(B, A, T, K)


d = Dijkstra(g, X)
res = d.shortest_distance(Y)
print(-1 if res == INF else res)