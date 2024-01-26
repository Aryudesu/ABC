class LieGroup:
    """行列"""

    def __init__(self, H, W) -> None:
        """H行W列の零行列を生成します"""
        self.W = W
        self.H = H
        self.T = False
        self.data = []
        for h in range(H):
            tmp = [0] * W
            self.data.append(tmp)

    def setArray(self, arr):
        """行列を設定します"""
        assert len(arr) == self.H
        for h in range(self.H):
            assert len(self.data[h]) == len(arr[h])
            for w in range(self.W):
                self.data[h][w] = arr[h][w]

    def setData(self, h, w, x):
        """h行w列に値xを設定します"""
        assert 0 <= h < self.H
        assert 0 <= w < self.W
        self.data[h][w] = x

    def getElem(self, h, w):
        """h行w列の要素を取得します"""
        return self.data[h][w]

    def dot(self, dat):
        """行列同士の積を計算します"""
        result = []
        if not self.T and not dat.T:
            return self.dotNN(dat)
        if self.T and not dat.T:
            return self.dotTN(dat)
        if not self.T and dat.T:
            return self.dotNT(dat)
        if self.T and dat.T:
            return self.dotTT(dat)
        raise Exception()

    def dotNN(self, a):
        assert self.W == a.H
        assert not self.T and not a.T
        result = LieGroup(self.H, a.W)
        for h in range(self.H):
            for w in range(a.W):
                tmp = 0
                for t in range(self.W):
                    tmp += self.data[h][t] * a.data[t][w]
                result.setData(h, w, tmp)
        return result

    def dotTN(self, a):
        assert self.H == a.H
        assert self.T and not a.T
        result = LieGroup(self.W, a.W)
        for h in range(self.W):
            for w in range(a.W):
                tmp = 0
                for t in range(self.H):
                    tmp += self.data[t][h] * a.data[t][w]
                result.setData(h, w, tmp)
        return result

    def dotNT(self, a):
        assert self.W == a.W
        assert not self.T and a.T
        result = LieGroup(self.H, a.H)
        for h in range(self.H):
            for w in range(a.H):
                tmp = 0
                for t in range(self.W):
                    tmp += self.data[h][t] * a.data[w][t]
                result.setData(h, w, tmp)
        return result

    def dotTT(self, a):
        assert self.H == a.W
        assert self.T and a.T
        result = LieGroup(self.W, a.H)
        for h in range(self.W):
            for w in range(a.H):
                tmp = 0
                for t in range(self.W):
                    tmp += self.data[t][h] * a.data[w][t]
                result.setData(h, w, tmp)
        return result

    def draw(self):
        """行列を描画します"""
        if self.T:
            self.drawT()
            return
        for dat in self.data:
            print(dat)

    def drawT(self):
        """転置行列を描画します"""
        for w in range(self.W):
            tmp = []
            for h in range(self.H):
                tmp.append(self.data[h][w])
            print(tmp)

    def deepCopy(self):
        """深いコピーを生成します"""
        result = LieGroup(self.H, self.W)
        result.setArray(self.data)
        return result

    def trans(self):
        """転置行列を計算します"""
        self.T = not self.T

    def __add__(self, a):
        """和を計算します"""
        assert self.H == a.H
        assert self.W == a.W
        result = LieGroup(self.H, self.W)
        for h in range(self.H):
            for w in range(self.W):
                result.data[h][w] = self.data[h][w] + a.data[h][w]
        return result

    def __sub__(self, a):
        """差を計算します"""
        assert self.H == a.H
        assert self.W == a.W
        result = LieGroup(self.H, self.W)
        for h in range(self.H):
            for w in range(self.W):
                result.data[h][w] = self.data[h][w] - a.data[h][w]
        return result

    def __mul__(self, a):
        """アダマール積を計算します"""
        assert self.H == a.H
        assert self.W == a.W
        result = LieGroup(self.H, self.W)
        for h in range(self.H):
            for w in range(self.W):
                result.data[h][w] = self.data[h][w] * a.data[h][w]
        return result

    def getI(self, N):
        """N*N単位行列を取得します"""
        result = LieGroup(N, N)
        for n in range(N):
            result.setData(n, n, 1)
        return result

    def __pow__(self, a):
        """a乗を計算します"""
        assert self.H == self.W
        tmpA = a
        tmp = self.deepCopy()
        result = self.getI(self.W)
        while tmpA:
            if tmpA & 1:
                result = result.dot(tmp)
            tmpA >>= 1
            tmp = tmp.dot(tmp)
        return result

lie1 = LieGroup(1, 5)
lie2 = LieGroup(1, 5)
dat1 = [[1, 2, 3, 4, 5]]
dat2 = [[1, 2, 3, 4, 5]]
lie1.setArray(dat1)
lie2.setArray(dat2)
lie2.trans()
res = lie1.dot(lie2)
res.draw()
