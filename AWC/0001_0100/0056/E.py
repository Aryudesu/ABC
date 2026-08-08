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


def calc(K: int, dist: list[list[int]], sd: list[int])->int:
    # mask, pos = dist
    dp = dict()
    for k in range(K):
        dp[(1 << k, k)] = sd[k]
    goal = (1 << K) - 1
    for i in range(K - 1):
        nextDP = dict()
        for key in dp:
            mask, pos = key
            dst = dp[key]
            remain: int = goal ^ mask
            while remain:
                nextPos = remain.bit_length() - 1
                b = 1 << nextPos
                remain = remain ^ b
                nextMask = mask | b
                nextDst = dst + dist[pos][nextPos]
                nextKey = (nextMask, nextPos)
                if nextKey not in nextDP or nextDP[nextKey] > nextDst:
                    nextDP[nextKey] = nextDst
        dp = nextDP
    if len(dp) == 0:
        raise Exception()
    result = 10 ** 18
    for key in dp:
        mask, pos = key
        dst = dp[key]
        result = min(result, dst + sd[pos])
    return result


N, M = map(int, input().split())
INF = 10 ** 10
graph = dict()
for m in range(M):
    u, v, w = map(int, input().split())
    graph[(u, v)] = min(graph.get((u, v), INF), w)
    graph[(v, u)] = min(graph.get((v, u), INF), w)
g = Graph()
for key in graph:
    u, v = key
    w = graph[key]
    g.add_edge(u, v, w)
S, K = map(int, input().split())
D = list(map(int, input().split()))
sd = [INF] * K
dist = [[INF for _ in range(K)] for _ in range(K)]
for i in range(K):
    p = D[i]
    d = Dijkstra(g, p)
    for j in range(K):
        dst = d.shortest_distance(D[j])
        dist[i][j] = dst
        dist[j][i] = dst
    sd[i] = d.shortest_distance(S)
print(calc(K, dist, sd))
