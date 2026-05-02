from itertools import permutations
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

def nextPermutation(data):
    """next_permutation"""
    size = len(data)
    left = size - 2
    while left >= 0 and data[left] >= data[left + 1]:
        left -= 1
    if left < 0:
        return 0
    right = size - 1
    while data[left] >= data[right]:
        right -= 1
    data[left], data[right] = data[right], data[left]
    left += 1
    right = size - 1
    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return 1

M = int(input())
graph = defaultdict(list)
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

P = list(map(int, input().split()))
start = [0] * 9
memo = set(range(9))
for i in range(8):    
    start[P[i]-1] = i
    memo.discard(P[i]-1)
start[memo.pop()] = 8
start = tuple(start)
goal = tuple(range(9))

field = list(range(9))
g = Graph()
while nextPermutation(field):
    for u in range(9):
        if field[u] != 8:
            continue
        if u not in graph:
            continue
        data = tuple(field)
        for v in graph[u]:
            field[u], field[v] = field[v], field[u]
            g.add_edge(data, tuple(field), 1)
            field[u], field[v] = field[v], field[u]
        break
d = Dijkstra(g, start)
res = d.shortest_distance(goal)
print(res if res < INF else -1)
