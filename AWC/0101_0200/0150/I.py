from collections import deque, defaultdict
from sortedcontainers import SortedSet

class Graph:
    def __init__(self):
        self.nodes = set()
        self.graph = defaultdict(set)
        self.inData = [0] * N
        self.outData = [0] * N
        self.edgeCount = defaultdict(int)
        self.indegree = defaultdict(int)

    def add_edge(self, a, b):
        """辺の追加"""
        if self.edgeCount[(a, b)] == 0:
            self.indegree[b] += 1
        self.graph[a].add(b)
        self.edgeCount[(a, b)] += 1
        self.outData[a] += 1
        self.inData[b] += 1
        self.nodes.add(a)
        self.nodes.add(b)

    def pop_edge(self, a, b):
        """辺の削除"""
        self.edgeCount[(a, b)] -= 1
        if self.edgeCount[(a, b)] == 0:
            self.graph[a].discard(b)
            self.indegree[b] -= 1
        self.outData[a] -= 1
        self.inData[b] -= 1
        if not self.outData[a] and not self.inData[a]:
            self.nodes.discard(a)
        if not self.outData[b] and not self.inData[b]:
            self.nodes.discard(b)

    def sort(self):
        """
        トポロジカルソート
        戻り値は result[頂点番号] = 何番目か
        """
        queue = deque()
        indegree = self.indegree.copy()
        for i in self.nodes:
            if indegree[i] == 0:
                queue.append(i)
        topo_order = []
        while queue:
            current = queue.popleft()
            topo_order.append(current)
            for neighbor in self.graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(topo_order) != len(self.nodes):
            return []
        return topo_order

N, M = map(int, input().split())
g = Graph()
Plist = defaultdict(list)
MaxEdgeW = defaultdict(int)
Wsort = SortedSet()
minX = 0
resultX = []
for m in range(M):
    W, K, *P = map(int, input().split())
    if minX < W:
        Plist[W].append(P)
        Wsort.add(W)
        for k in range(K-1):
            g.add_edge(P[k]-1, P[k+1]-1)
            key = (P[k]-1, P[k+1]-1)
            w = MaxEdgeW[key]
            MaxEdgeW[key] = max(w, W)
    res = g.sort()
    if res:
        resultX.append(minX)
    else:
        while not res:
            if not Wsort:
                break
            minX = Wsort.pop(0)
            for P in Plist[minX]:
                K = len(P)
                for k in range(K-1):
                    g.pop_edge(P[k]-1, P[k+1]-1)
            res = g.sort()
        resultX.append(minX)
print(*resultX)
result = []
nokori = [False] * N
for r in res:
    result.append(r + 1)
    nokori[r] = True
for n in range(N):
    if not nokori[n]:
        result.append(n + 1)
print(*result)
