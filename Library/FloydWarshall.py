from collections import defaultdict
from typing import Tuple

class FloydWarshall:
    """ワーシャルフロイド法"""
    def __init__(self, N:int=0, edge:list[Tuple[int, int, int]] = [], inf: int = 10**18):
        """ワーシャルフロイド法データ初期化（ノード数Nを指定）"""
        self.INF = inf
        self.N = N
        self.dist = defaultdict(lambda:defaultdict(lambda:self.INF))
        for i in range(self.N):
            self.dist[i][i] = 0
        for s, d, w in edge:
            self.__addEdge(s, d, w)
        self.__calcDist()

    def __addEdge(self, src, dst, weight):
        """辺の追加（距離の更新は行わない）"""
        assert src < self.N
        assert dst < self.N
        self.dist[src][dst] = min(self.dist[src][dst], weight)

    def __calcDist(self):
        """距離の計算"""
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])

    def update(self, src, dst, weight):
        """辺の追加（距離の更新を行う）"""
        self.dist[src][dst] = min(self.dist[src][dst], weight)
        for i in range(self.N - 1):
            for j in range(self.N - 1):
                self.dist[i][j] = min(self.dist[i][j], self.dist[i][src] + weight + self.dist[dst][j])
    
    def getDist(self, src, dst):
        """距離"""
        return self.dist[src][dst]

N, M = [int(l) for l in input().split()]
edge = []
for m in range(M):
    a,b,c = [int(l) for l in input().split()]
    edge.append((a-1, b-1, c))
    edge.append((b-1, a-1, c))
K, T = [int(l) for l in input().split()]
D = [int(l) for l in input().split()]
for d in D:
    edge.append((d-1, N, T))
    edge.append((N, d-1, 0))
wf = FloydWarshall(N + 1, edge)
result = []
Q = int(input())
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        n, x, y, t = query
        wf.update(x-1, y-1, t)
        wf.update(y-1, x-1, t)
    elif query[0] == 2:
        n, x = query
        wf.update(x-1, N, T)
        wf.update(N, x-1, 0)
    elif query[0] == 3:
        res = 0
        for i in range(N):
            for j in range(N):
                if wf.getDist(i, j) < wf.INF:
                    res += wf.getDist(i, j)
        result.append(res)

for r in result:
    print(r)
