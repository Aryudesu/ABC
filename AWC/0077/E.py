from atcoder.maxflow import MFGraph

class FlowBipartiteMatching:
    """左側 N点, 右側 M点 の0-indexed二部グラフの最大マッチング用クラス"""
    def __init__(self, N: int, M: int):
        self.N = N
        self.M = M
        self.MBase = N
        self.mf = MFGraph(N + M + 2)
        self.s = N + M
        self.t = N + M + 1
        for n in range(N):
            self.mf.add_edge(self.s, n, 1)
        for m in range(M):
            self.mf.add_edge(self.MBase + m, self.t, 1)

    def addEdge(self, src: int, dst: int)->None:
        """左側の点から右側の点に辺を張ります"""
        assert 0 <= src < self.N
        assert 0 <= dst < self.M
        self.mf.add_edge(src, self.MBase + dst, 1)
    
    def maxMatching(self)->int:
        """最大マッチングの結果を計算します"""
        return self.mf.flow(self.s, self.t)

N, M = map(int, input().split())
B = list(map(int, input().split()))

CData = []
CCount = [0] * M
isOver = [False] * M
for n in range(N):
    k, *C = list(map(int, input().split()))
    CData.append(C)
    for c in C:
        if CCount[c-1] == B[c-1]:
            isOver[c-1] = True
        CCount[c-1] = min(CCount[c-1] + 1, B[c-1])
SB = sum(CCount)
bm = FlowBipartiteMatching(N, SB)

# えーーー二分マッチング問題だと思ってるのに・・・
# 500 * 250000... びみょいのか…
idxData = [0]
for c in CCount:
    idxData.append(idxData[-1] + c)
idxData.pop()
idxCount = [0] * M
for n in range(N):
    for c in CData[n]:
        if isOver[c-1]:
            for m in range(CCount[c - 1]):
                bm.addEdge(n, idxData[c - 1] + m)
                idxCount[c-1] += 1
        else:
            bm.addEdge(n, idxData[c - 1] + idxCount[c-1])
            idxCount[c-1] += 1

res = bm.maxMatching()
print(res)
