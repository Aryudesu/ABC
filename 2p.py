class LieGroup:
    """行列プログラム Edited By Aryu"""

    def __init__(self, H=1, W=1) -> None:
        """H行W列の零行列を生成します"""
        self.W = W
        self.H = H
        self.T = False
        self.data = []
        for h in range(H):
            tmp = [0] * W
            self.data.append(tmp)

    def makeArray(self, a, H, W):
        """H*W配列を作成します"""
        return [[a] * W for _ in range(H)]

    def setArray(self, arr):
        """行列を設定します"""
        self.H = len(arr)
        self.W = len(arr[0])
        self.data = arr

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

    def modDot(self, dat, M):
        """行列同士の積をmod Mで計算します"""
        result = []
        if not self.T and not dat.T:
            return self.dotNN(dat, M)
        if self.T and not dat.T:
            return self.dotTN(dat, M)
        if not self.T and dat.T:
            return self.dotNT(dat, M)
        if self.T and dat.T:
            return self.dotTT(dat, M)
        raise Exception()

    def dotNN(self, a, M = None):
        assert self.W == a.H
        assert not self.T and not a.T
        result = LieGroup(self.H, a.W)
        for h in range(self.H):
            for w in range(a.W):
                tmp = 0
                for t in range(self.W):
                    tmp += self.data[h][t] * a.data[t][w]
                    if not M is None:
                        tmp = tmp % M
                result.setData(h, w, tmp)
        return result

    def dotTN(self, a, M = None):
        assert self.H == a.H
        assert self.T and not a.T
        result = LieGroup(self.W, a.W)
        for h in range(self.W):
            for w in range(a.W):
                tmp = 0
                for t in range(self.H):
                    tmp += self.data[t][h] * a.data[t][w]
                    if not M is None:
                        tmp = tmp % M
                result.setData(h, w, tmp)
        return result

    def dotNT(self, a, M = None):
        assert self.W == a.W
        assert not self.T and a.T
        result = LieGroup(self.H, a.H)
        for h in range(self.H):
            for w in range(a.H):
                tmp = 0
                for t in range(self.W):
                    tmp += self.data[h][t] * a.data[w][t]
                    if not M is None:
                        tmp = tmp % M
                result.setData(h, w, tmp)
        return result

    def dotTT(self, a, M = None):
        assert self.H == a.W
        assert self.T and a.T
        result = LieGroup(self.W, a.H)
        for h in range(self.W):
            for w in range(a.H):
                tmp = 0
                for t in range(self.W):
                    tmp += self.data[t][h] * a.data[w][t]
                    if not M is None:
                        tmp = tmp % M
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

    def pow(self, a):
        return self**a

    def modPow(self, a, M):
        """a乗をmod Mで計算します"""
        assert self.H == self.W
        tmpA = a
        tmp = self.deepCopy()
        result = self.getI(self.W)
        while tmpA:
            if tmpA & 1:
                result = result.modDot(tmp, M)
            tmpA >>= 1
            tmp = tmp.modDot(tmp, M)
        return result

    def Ydet(self, M):
        """余因子展開で行列式を計算します"""
        size = len(M)
        if size == 1:
            return M[0][0]
        T = self.makeArray(0, size - 1, size - 1)
        result = 0
        for i in range(size):
            for x in range(size-1):
                for y in range(size-1):
                    tmp = x + 1 if x >= i else x
                    T[y][x] = M[y+1][tmp]
            sign = 1 if i % 2 == 0 else -1
            result += M[0][i] * sign * self.Ydet(T)
        return result

    def det(self):
        """行列式計算"""
        assert self.H == self.W
        return self.Ydet(self.data)

    def inverse(self):
        assert self.H == self.W
        assert self.det() != 0
        N = self.H
        result = []
        for i in range(N):
            result.append([1 if i == j else 0 for j in range(N)])
        a = []
        for i in range(N):
            a.append([self.data[i][j] for j in range(N)])

        for i in range(N):
            buf = 1/a[i][i]
            for j in range(N):
                a[i][j] *= buf
                result[i][j] *= buf
            for j in range(N):
                if i != j:
                    buf = a[j][i]
                    for k in range(N):
                        a[j][k] -= a[i][k] * buf
                        result[j][k] -= result[i][k] * buf
        res = LieGroup(N, N)
        res.setArray(result)
        return res

def f(N, x, param):
    result = 0
    for n in range(N):
        result += param[n] * (x ** n)
    return result

def drawResult(N, param):
    res = []
    for n in range(N):
        res.append(str(param[n]) + f"x^{n}")
    print(" + ".join(res))


Data = [[7.60, 81], [6.92, 58], [6.59, 54], [5.76, 44], [4.48, 32], [4.19, 29]]
N = len(Data)
leftData = []
rightData = []
for n in range(N):
    x, y = Data[n]
    rightData.append([y])
    tmp = []
    for m in range(N):
        tmp.append(x ** m)
    leftData.append(tmp)
left = LieGroup(6, 6)
left.setArray(leftData)
right = LieGroup(6, 1)
right.setArray(rightData)
left_inv = left.inverse()
ans = left_inv.dot(right)
result = []
for n in range(N):
    result.append(ans.getElem(n, 0))
print(result)
for dat in Data:
    x, t = dat
    y = f(N, x, result)
    print(y, t)

drawResult(N, result)
