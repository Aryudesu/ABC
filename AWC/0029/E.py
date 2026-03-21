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
            self.next[i][i] = i\

        for u, v, w in graph:
            self.dist[u][v] = w
            self.next[u][v] = v\

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
                        self.next[i][j] = self.next[i][k]\
    
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


def calc(N: int, S: int, T: list[int], wf: WarshallFloyd)->int:
    K = len(T)
    goal = (1 << K) - 1
    result = INF
    dp = [[INF] * K for _ in range(1<<K)]

    # マスク: { 現在位置, 距離 }
    dp = dict()
    for idx in range(K):
        bit = 1 << idx
        dp[bit] = {idx: wf.getDist(S-1, T[idx]-1)}

    while dp:
        newDP = dict()
        for mask, inner in dp.items():
            for nowP, nowDist in inner.items():
                remain = goal ^ mask
                while remain:
                    b = remain & -remain
                    newP = b.bit_length() - 1
                    remain ^= b
                    d = wf.getDist(T[nowP]-1, T[newP]-1)
                    if d == INF:
                        continue

                    newMask = mask | (1 << newP)
                    newDist = nowDist + d
                    if newMask == goal:
                        back = wf.getDist(T[newP]-1, S-1)
                        if back != INF:
                            res = newDist + back
                            if result > res:
                                result = res
                    else:
                        if newMask not in newDP:
                            newDP[newMask] = {newP: newDist}
                        else:
                            old = newDP[newMask].get(newP)
                            if old is None or old > newDist:
                                newDP[newMask][newP] = newDist
        dp = newDP
    return result

N, M = map(int, input().split())
graph = Graph(N)
for m in range(M):
    u, v, w = map(int, input().split())
    graph.addEdge(u-1, v-1, w)
S, K = map(int, input().split())
T = list(map(int, input().split()))
revT = dict()
tSet = set(T)
distData = [[0] * K for _ in range(K)]
for idx in range(K):
    t = T[idx]
    revT[t] = idx

wf = WarshallFloyd(graph)
res = calc(N, S, T, wf)
print(res if res < INF else -1)
