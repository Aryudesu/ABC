from typing import Tuple

class FloydWarshall:
    """ワーシャルフロイド法"""
    def __init__(self, N:int=0, inf: int = 10**18):
        """ワーシャルフロイド法データ初期化（ノード数Nを指定）"""
        self.INF = inf
        self.N = N
        self.dist = [[inf] * N for _ in range(N)]
        self.cashe = None
        self.isUpdate = True
        self.isInitCalc = False

    def addEdge(self, src, dst, weight):
        """辺の追加（距離の更新は行わない）"""
        assert src < self.N
        assert dst < self.N
        self.dist[src][dst] = min(self.dist[src][dst], weight)

    def calcDist(self):
        """距離の計算"""
        for k in range(self.N):
            self.dist[k][k] = 0
            for i in range(self.N):
                for j in range(self.N):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])
        self.isInitCalc = True

    def update(self, src, dst, weight):
        """辺の追加（距離の更新を行う）"""
        assert src < self.N
        assert dst < self.N
        self.dist[src][dst] = min(self.dist[src][dst], weight)
        for i in range(self.N):
            for j in range(self.N):
                self.dist[i][j] = min(self.dist[i][j], self.dist[i][src] + weight + self.dist[dst][j])
        self.isUpdate = True
    
    def updateMutual(self, src, dst, weight):
        """辺の追加（距離の更新を行う）"""
        assert src < self.N
        assert dst < self.N
        self.dist[src][dst] = min(self.dist[src][dst], weight)
        self.dist[dst][src] = min(self.dist[dst][src], weight)
        for i in range(self.N):
            for j in range(self.N):
                self.dist[i][j] = min(self.dist[i][j], self.dist[i][src] + weight + self.dist[dst][j])
                self.dist[i][j] = min(self.dist[i][j], self.dist[i][dst] + weight + self.dist[src][j])
        self.isUpdate = True

    def updateMutual2(self, src, dst, weight):
        """辺の追加（距離の更新を行う）戻りは0"""
        assert src < self.N
        assert dst < self.N
        self.dist[src][dst] = min(self.dist[src][dst], weight)
        self.dist[dst][src] = min(self.dist[dst][src], 0)
        for i in range(self.N):
            for j in range(self.N):
                self.dist[i][j] = min(self.dist[i][j], self.dist[i][src] + weight + self.dist[dst][j])
                self.dist[i][j] = min(self.dist[i][j], self.dist[i][dst] + self.dist[src][j])
        self.isUpdate = True

    def getResult(self):
        """答え取得"""
        assert self.isInitCalc
        if not self.isUpdate:
            return self.cashe
        self.cashe = 0
        for i in range(self.N-1):
            for j in range(self.N-1):
                if self.dist[i][j] < self.INF:
                    self.cashe += self.dist[i][j]
        self.isUpdate = False
        return self.cashe

N, M = [int(l) for l in input().split()]
wf = FloydWarshall(N + 1)
for m in range(M):
    a,b,c = [int(l) for l in input().split()]
    wf.addEdge(a-1, b-1, c)
    wf.addEdge(b-1, a-1, c)
K, T = [int(l) for l in input().split()]
D = [int(l) for l in input().split()]
for d in D:
    wf.addEdge(d-1, N, T)
    wf.addEdge(N, d-1, 0)
wf.calcDist()
Q = int(input())
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        n, x, y, t = query
        wf.updateMutual(x-1, y-1, t)
    elif query[0] == 2:
        n, x = query
        wf.updateMutual2(x-1, N, T)
    elif query[0] == 3:
        print(wf.getResult())
