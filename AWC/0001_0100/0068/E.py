from sortedcontainers import SortedList

class PrefixSum2D:
    """0-indexed座標のグリッドに対する2次元累積和"""
    def __init__(self, H: int, W: int):
        self.H = H
        self.W = W
        # 元データ
        self.orig = [[0] * W for _ in range(H)]
        self.sums = [[0] * (W + 1) for _ in range(H + 1)]
        self.initialized = False
    
    def add(self, h: int, w: int, x: int) -> None:
        """(h, w)にxを加算します"""
        assert not self.initialized
        if 0 <= h < self.H and 0 <= w < self.W:
            self.orig[h][w] += x
    
    def set(self, h: int, w: int, x: int) -> None:
        """(h, w)にxを設定します"""
        assert not self.initialized
        if 0 <= h < self.H and 0 <= w < self.W:
            self.orig[h][w] = x
    
    def build(self) -> None:
        """2次元累積和の計算を行います"""
        assert not self.initialized
        for h in range(self.H):
            s = 0
            for w in range(self.W):
                s += self.orig[h][w]
                self.sums[h + 1][w + 1] = s + self.sums[h][w + 1]
        self.initialized = True
    
    def sum(self, u: int, l: int, d: int, r: int) -> int:
        """矩形 [u, d] * [l, r] の総和を返します"""
        assert self.initialized
        assert 0 <= u <= d < self.H
        assert 0 <= l <= r < self.W
        u1, l1, d1, r1 = u, l, d + 1, r + 1
        return self.sums[d1][r1] - self.sums[u1][r1] - self.sums[d1][l1] + self.sums[u1][l1]

    def getData(self) -> list[list[int]]:
        """元データを返却します"""
        return self.orig

    def getSumTable(self) -> list[list[int]]:
        """累積和テーブル（1-indexed）を返却します"""
        assert self.initialized
        return self.sums

    def __getitem__(self, h: int):
        return self.orig[h]

    @classmethod
    def makeData(cls, grid: list[list[int]]) -> "PrefixSum2D":
        """
        既存の2次元グリッドから累積和を構築します
        """
        H = len(grid)
        W = len(grid[0]) if H > 0 else 0
        obj = cls(H, W)
        for h in range(H):
            for w in range(W):
                obj.orig[h][w] = grid[h][w]
        obj.build()
        return obj

N, K = map(int, input().split())
A = []
for n in range(N):
    A.append(list(map(int, input().split())))
gridMax = [[0] * (N - K + 1) for _ in range(N)]
gridMax2 = [[0] * (N - K + 1) for _ in range(N - K + 1)]
for y in range(N):
    data = SortedList()
    for x in range(K):
        data.add(A[y][x])
    gridMax[y][0] = data[-1]
    for x in range(1, N - K + 1):
        data.add(A[y][x + K - 1])
        data.discard(A[y][x - 1])
        gridMax[y][x] = data[-1]

for x in range(N-K+1):
    data = SortedList()
    for y in range(K):
        data.add(gridMax[y][x])
    gridMax2[0][x] = data[-1]
    for y in range(1, N - K + 1):
        data.add(gridMax[y + K - 1][x])
        data.discard(gridMax[y - 1][x])
        gridMax2[y][x] = data[-1]
# for gm in gridMax2:
#     print(gm)

psd = PrefixSum2D(N, N)
for y in range(N):
    for x in range(N):
        psd.add(y, x, int(A[y][x]))
psd.build()
result = 0
for y in range(N-K+1):
    for x in range(N-K+1):
        s1 = psd.sum(y, x, y + K - 1, x + K - 1)
        s2 = gridMax2[y][x]
        result = max(result, s1-s2)
print(result)
