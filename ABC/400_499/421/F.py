from atcoder.lazysegtree import LazySegTree

ID = None
e = (0, 0)

def op(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mapping(f, x):
    if f is ID:
        return x
    return (x[0], f*x[0])

def composition(f, g):
    if f is ID:
        return g
    else:
        return f

class InsertableList:
    """
    挿入可能な配列管理用クラス
    同じ要素が2度使われないことが保証されていること前提
    """

    def __init__(self, Data):
        """初期設定"""
        self.arrayData = dict()
        N = len(Data)
        assert N > 0
        self.stNum = Data[0]
        check = set(Data)
        assert len(check) == len(Data)
        for i in range(N):
            prev = None
            aft = None
            if i > 0:
                prev = Data[i-1]
            if i < N - 1:
                aft = Data[i + 1]
            self.arrayData[Data[i]] = (prev, aft)

    def insert(self, x, y):
        """xの後にyを挿入します"""
        assert x in self.arrayData
        assert self.arrayData.get(y) is None
        tmp = self.arrayData[x]
        aftNum = tmp[1]
        if not aftNum is None:
            adata = self.arrayData[aftNum]
            self.arrayData[aftNum] = (y, adata[1])
        self.arrayData[y] = (x, aftNum)
        self.arrayData[x] = (tmp[0], y)

    def delete(self, x):
        """要素を削除します"""
        assert x in self.arrayData
        tmp = self.arrayData[x]
        prev, aft = tmp
        if not prev is None:
            ptmp = self.arrayData[prev]
            self.arrayData[prev] = (ptmp[0], aft)
        else:
            self.stNum = aft
        if not aft is None:
            atmp = self.arrayData[aft]
            self.arrayData[aft] = (prev, atmp[1])
        self.arrayData[x] = None

    def getArray(self):
        """配列でデータを取得します"""
        result = []
        num = self.stNum
        while not num is None:
            result.append(num)
            tmp = self.arrayData[num]
            num = tmp[1]
        return result

il = InsertableList([0])
Q = int(input())
queryData = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        n, x = query
        queryData.append((n, x, 0))
        il.insert(x, i + 1)
    elif query[0] == 2:
        n, x, y = query
        queryData.append((n, x, y))
    else:
        raise Exception()

arrayData = il.getArray()
idxData = dict()
valData = dict()
for i in range(len(arrayData)):
    idxData[arrayData[i]] = i
    valData[i] = arrayData[i]
result = []
data = [(1, 0) for _ in range(len(arrayData))]
seg = LazySegTree(op, e, mapping, composition, ID, data)
for i in range(len(queryData)):
    n, x, y = queryData[i]
    if n == 1:
        idx = idxData.get(i + 1)
        seg.set(idx, (1, i + 1))
    elif n == 2:
        l = idxData.get(x)
        r = idxData.get(y)
        l, r = min(l, r), max(l, r)
        result.append(seg.prod(l+1, r))
        seg.apply(l+1, r, 0)
    else:
        raise Exception()
for r in result:
    print(r[1])
