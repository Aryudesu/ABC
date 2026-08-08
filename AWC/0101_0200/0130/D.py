from atcoder.dsu import DSU
from collections import defaultdict

class Imos2D:
    """0-indexed座標での2次元いもす法用ライブラリ"""
    def __init__(self, H: int, W: int)->None:
        self.data = [[0] * W for _ in range(H)]
        self.H = H
        self.W = W
        self._num = 0
        self.initialized = False

    def add(self, u: int, l: int, d: int, r: int, x: int = 1)->None:
        """(u, l)を左上，(d, r)を右下とする矩形にxを加算します"""
        assert not self.initialized
        u_ = max(0, u)
        l_ = max(0, l)
        d_ = min(d, self.H-1)
        r_ = min(r, self.W-1)
        if u_ > d_ or l_ > r_:
            return
        self.data[u_][l_] += x
        if r_ + 1 < self.W:
            self.data[u_][r_ + 1] -= x
        if d_ + 1 < self.H:
            self.data[d_+1][l_] -= x
        if d_ + 1 < self.H and r_ + 1 < self.W:
            self.data[d_+1][r_+1] += x
        self._num += 1

    def build(self)->None:
        """計算を行います"""
        assert not self.initialized
        for h in range(self.H):
            tmp = 0
            for w in range(self.W):
                tmp += self.data[h][w]
                self.data[h][w] = tmp
        for w in range(self.W):
            tmp = 0
            for h in range(self.H):
                tmp += self.data[h][w]
                self.data[h][w] = tmp
        self.initialized = True
    
    def get(self, h: int, w: int)->int:
        """
        (h, w)の座標の値を取得します．
        buildを行った後でないとExceptionがraiseされます
        """
        assert self.initialized
        assert 0 <= h < self.H
        assert 0 <= w < self.W
        return self.data[h][w]

    def getData(self)->list[list[int]]:
        """
        build後の生データ（内部参照）を取得します．
        buildを行った後でないとExceptionがraiseされます
        """
        assert self.initialized
        return self.data

    def cells(self):
        """
        グリッドに対してのループ処理を行います
        各マスに対して(h, w, value)をyieldします
        """
        assert self.initialized
        for h in range(self.H):
            row = self.data[h]
            for w in range(self.W):
                yield h, w, row[w]
    
    def rows(self):
        """H*Wの範囲についての各行のデータ（長さWのリスト）を順に返却します"""
        assert self.initialized
        for dat in self.data:
            yield dat

    @staticmethod
    def zipCells(a: "Imos2D", b: "Imos2D"):
        """
        2つのいもす法のグリッドに対してのループ処理を行います
        各マスに対して(h, w, value1, value2)をyieldします
        """
        assert a.initialized and b.initialized
        assert a.H == b.H and a.W == b.W
        H, W = a.H, a.W
        dataA = a.data
        dataB = b.data
        for h in range(H):
            rowA = dataA[h]
            rowB = dataB[h]
            for w in range(W):
                yield h, w, rowA[w], rowB[w]

    def __len__(self)->int:
        """グリッドに反映されたデータの個数を返却します"""
        return self._num
    
    def __getitem__(self, h: int)->int:
        assert self.initialized
        assert 0 <= h < self.H
        return self.data[h]
    
    def __iter__(self):
        assert self.initialized
        return iter(self.data)

def xy2num(H: int, W: int, h: int, w: int)->int:
    return W * h + w

H, W, N = map(int, input().split())
imos = Imos2D(H, W)
for n in range(N):
    a, b, c, d = map(int, input().split())
    imos.add(a-1, c-1, b-1, d-1)
imos.build()
field = imos.getData()

dsu = DSU(H * W)
for h in range(H):
    for w in range(W):
        d = field[h][w] % 2
        field[h][w] = d

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for h in range(H):
    for w in range(W):
        for dh, dw in dirs:
            nh, nw = h + dh, w + dw
            if not (0 <= nh < H):
                continue
            if not (0 <= nw < W):
                continue
            if field[h][w] == 1 and field[nh][nw] == 1:
                dsu.merge(xy2num(H, W, h, w), xy2num(H, W, nh, nw))
mapData = [[-1] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if field[h][w] == 1:
            l = dsu.leader(xy2num(H, W, h, w))
            mapData[h][w] = l

leaderMinW, leaderMinH, leaderMaxW, leaderMaxH = dict(), dict(), dict(), dict()
for h in range(H):
    for w in range(W):
        d = mapData[h][w]
        if d < 0:
            continue
        leaderMinH[d] = min(leaderMinH.get(d, H), h)
        leaderMinW[d] = min(leaderMinW.get(d, W), w)
        leaderMaxH[d] = max(leaderMaxH.get(d, 0), h)
        leaderMaxW[d] = max(leaderMaxW.get(d, 0), w)

upLeft, lowRight = [[] for _ in range(H * W)], [[] for _ in range(H * W)]
for key in leaderMaxW:
    lmnh = leaderMinH[key]
    lmnw = leaderMinW[key]
    lmxh = leaderMaxH[key]
    lmxw = leaderMaxW[key]
    upLeft[xy2num(H, W, lmnh, lmnw)].append(key)
    lowRight[xy2num(H, W, lmxh, lmxw)].append(key)

# print(upLeft)
# print(lowRight)
# for f in mapData:
#     print(f)

M = int(input())
for m in range(M):
    p, q, r, s = map(int, input().split())
    count = 0
    land = 0
    memo = [0] * (H * W)
    for h in range(p-1, q):
        for w in range(r-1, s):
            if field[h][w]:
                count += 1
            key = xy2num(H, W, h, w)
            for d in upLeft[key]:
                memo[d] += 1
            for d in lowRight[key]:
                memo[d] += 1
                if memo[d] == 2:
                    land += 1
    print(count, land)
