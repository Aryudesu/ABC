from heapq import heappop, heappush
import sys

read = sys.stdin.buffer.readline
INF = 10**18

def dijkstra(
    graph: list[list[tuple[int, int]]],
    start: int,
) -> tuple[list[int], list[int]]:
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    prev = [-1] * n
    pq = [(0, start)]
    push = heappush
    pop = heappop
    while pq:
        d, u = pop(pq)
        if d != dist[u]:
            continue
        for v, weight in graph[u]:
            nd = d + weight
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                push(pq, (nd, v))
    return dist, prev

class CoordinateCompress:
    """座標圧縮用クラス"""
    def __init__(self):
        self.vals = []
        self.id = None
        self.inv = None
    
    def add(self, x)-> bool:
        """座標圧縮にデータを追加します"""
        self.vals.append(x)

    def build(self)-> None:
        """座標圧縮を行います"""
        self.inv = sorted(set(self.vals))
        self.id = {x: i for i, x in enumerate(self.inv)}

    def getId(self, data)-> int:
        """座標圧縮後のIDを取得します"""
        if data in self.id:
            return self.id[data]
        raise Exception()
    
    def getVal(self, id: int):
        """座標圧縮IDに対応するデータを取得します"""
        assert 0 <= id < len(self.inv)
        return self.inv[id]

    def __len__(self):
        return len(self.inv)


N, M, K, T = map(int, input().split())
graph = [[] for _ in range(N)]
for m in range(M):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))
distData = [[0] * N for _ in range(N)]
SData = []
PData = []
cc = CoordinateCompress()
cc.add(0)
for k in range(K):
    ABSS, *S, P = list(map(int, input().split()))
    SData.append(S)
    PData.append(P)
    for s in S:
        cc.add(s-1)
cc.build()
L = len(cc)
scores = [0] * (1 << L)
for k in range(K):
    S = SData[k]
    P = PData[k]
    mask = 0
    for s in S:
        id = cc.getId(s-1)
        mask |= 1 << id
    scores[mask] += P

print(scores)

nodes = cc.vals
for src in range(L):
    dist, _ = dijkstra(graph, nodes[src])
    for dst in range(src, L):
        distData[nodes[src]][nodes[dst]] = dist[nodes[dst]]
        distData[nodes[dst]][nodes[src]] = dist[nodes[dst]]

dpData = [(0, 0)] * (1 << L)
for mask in range(1 << L):
    pass
