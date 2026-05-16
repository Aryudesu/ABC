from atcoder.dsu import DSU

INF = 10 ** 18
class Graph:
    """グラフデータの作成"""
    def __init__(self, N: int):
        self.N = N
        self.edges = dict()
    
    def addEdge(self, src: int, dst: int, weight: int=1)->None:
        """srcからdstまでコストweightの辺を追加します"""
        assert 0 <= src < self.N
        assert 0 <= dst < self.N
        assert 0 <= weight
        key = (src, dst)
        if key not in self.edges or self.edges[key] > weight:
            self.edges[key] = weight
    
    def __iter__(self):
        for (u, v), w in self.edges.items():
            yield u, v, w


class WarshallFloyd:
    """ワーシャルフロイド全最短経路探索を行います"""
    def __init__(self, graph: Graph):
        self.N = graph.N
        self.dist = [[INF] * self.N for _ in range(self.N)]
        self.next = [[-1] * self.N for _ in range(self.N)]
        self.bit = [[0] * self.N for _ in range(self.N)]
        for i in range(self.N):
            self.dist[i][i] = 0
            self.next[i][i] = i
            self.bit[i][i] = (1 << i) & 1

        for u, v, w in graph:
            self.dist[u][v] = w
            self.next[u][v] = v
            self.bit[u][v] = ((1 << u) | (1 << v)) & 1

        for k in range(self.N):
            for i in range(self.N):
                if self.dist[i][k] == INF:
                    continue
                for j in range(self.N):
                    if self.dist[k][j] == INF:
                        continue
                    nextDist = self.dist[i][k] + self.dist[k][j]
                    if self.dist[i][j] > nextDist:
                        self.dist[i][j] = nextDist
                        self.next[i][j] = self.next[i][k]
                        self.bit[i][j] = (self.bit[i][k] | self.bit[k][j]) & 1
    
    def getDist(self, src: int, dst: int) -> int:
        """srcからdstまでの最短距離を取得します"""
        assert 0 <= src < self.N
        assert 0 <= dst < self.N
        return self.dist[src][dst]

    def getPath(self, src: int, dst: int) -> list[int]:
        """srcからdstまでの最短経路のうち1本を取得します"""
        assert 0 <= src < self.N
        assert 0 <= dst < self.N
        if self.next[src][dst] == -1:
            return []
        result = [src]
        while src != dst:
            src = self.next[src][dst]
            result.append(src)
        return result
    
    def getBit(self, src: int, dst: int) -> int:
        """srcからdstまでの最短経路のうち1本の点集合をBit集合で返却します"""
        assert 0 <= src < self.N
        assert 0 <= dst < self.N
        return self.bit[src][dst]

N, M = map(int, input().split())
g = Graph(N)
S = list(map(int, input().split()))
for m in range(M):
    u, v, w = map(int, input().split())
    g.addEdge(u-1, v-1, w)
    g.addEdge(v-1, u-1, w)
wf = WarshallFloyd(g)
fumanCount = [0] * N
for i in range(N):
    for j in range(N):
        fumanCount[i] += wf.getDist(i, j) > S[i]
result = 0
for i in range(N):
    for j in range(i+1, N):
        d = wf.getDist(i, j)
        if d <= S[i] and d <= S[j] and fumanCount[i] == fumanCount[j]:
            result += 1
print(result)
