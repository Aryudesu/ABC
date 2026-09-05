from collections import deque, defaultdict
from sortedcontainers import SortedSet

class TopologicalGraph:
    """
    多重辺・辺追加削除対応の有向グラフ。

    頂点は 0-indexed。
    """

    def __init__(self, n: int):
        self.n = n
        self.graph = [set() for _ in range(n)]
        self.edge_count = defaultdict(int)
        self.indegree = [0] * n

    def add_edge(self, u: int, v: int) -> None:
        key = (u, v)

        if self.edge_count[key] == 0:
            self.graph[u].add(v)
            self.indegree[v] += 1

        self.edge_count[key] += 1

    def remove_edge(self, u: int, v: int) -> bool:
        key = (u, v)

        if self.edge_count[key] == 0:
            return False

        self.edge_count[key] -= 1

        if self.edge_count[key] == 0:
            self.graph[u].remove(v)
            self.indegree[v] -= 1

        return True

    def add_path(self, path: list[int]) -> None:
        for u, v in zip(path, path[1:]):
            self.add_edge(u, v)

    def remove_path(self, path: list[int]) -> None:
        for u, v in zip(path, path[1:]):
            self.remove_edge(u, v)

    def has_edge(self, u: int, v: int) -> bool:
        return self.edge_count[(u, v)] > 0

    def edge_multiplicity(self, u: int, v: int) -> int:
        return self.edge_count[(u, v)]

    def topological_sort(self) -> list[int]:
        indegree = self.indegree.copy()
        queue = deque(
            v for v in range(self.n)
            if indegree[v] == 0
        )

        order = []

        while queue:
            v = queue.popleft()
            order.append(v)

            for nv in self.graph[v]:
                indegree[nv] -= 1

                if indegree[nv] == 0:
                    queue.append(nv)

        if len(order) != self.n:
            return []

        return order

    def is_dag(self) -> bool:
        return len(self.topological_sort()) == self.n


N, M = map(int, input().split())
g = TopologicalGraph(N)
Plist = defaultdict(list)
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
    res = g.topological_sort()
    if res:
        resultX.append(minX)
    else:
        while not res:
            minX = Wsort.pop(0)
            for P in Plist[minX]:
                K = len(P)
                for k in range(K-1):
                    g.remove_edge(P[k]-1, P[k+1]-1)
            res = g.topological_sort()
        resultX.append(minX)
print(*resultX)
print(*(r + 1 for r in res))
