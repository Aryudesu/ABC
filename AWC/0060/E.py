from typing import Tuple

class Doubling:
    def __init__(self, graph: list[Tuple[int, int]], MOD: int, maxPow: int = 30):
        """
        初期化
        graph: グラフ（次の遷移先）
        maxPow: 最大操作ビット数
        """
        self.N = len(graph)
        self.M = maxPow
        self.MOD = MOD
        self.data = self._makeData(graph)

    def _makeData(self, graph: list[Tuple[int]]) -> list[list[Tuple[int]]]:
        """事前データ作成"""
        result = [[graph[i] for i in range(self.N)]]
        b = 10
        for _ in range(1, self.M):
            result.append([((result[-1][result[-1][i][1]][0] * b + result[-1][result[-1][i][1]][0]) % self.MOD, result[-1][result[-1][i][1]][1]) for i in range(self.N)])
            b = (b * b) % self.MOD
        return result
    
    def jump(self, v: int, t: int) -> int:
        """vからt回操作後の値を取得"""
        res = self.data[0][v][0] if t & 1 else 0
        p = v
        b = 10
        for i in range(1, t.bit_length()):
            if t & (1 << i):
                res = (res * b + self.data[i][p][0]) % self.MOD
                p = self.data[i][p][1]
            b = (b * b) % self.MOD
        return res


N, Q, M = map(int, input().split())
graph = [None] * N
for n in range(N):
    d, p = map(int, input().split())
    graph[n] = (d, p-1)
dd = Doubling(graph, M, 60)
for _ in range(Q):
    s, k = map(int, input().split())
    print(dd.jump(s-1, k))

