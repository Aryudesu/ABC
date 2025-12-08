import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(1_000_000)

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

class RangeZeroSum:
    """
    区間を 0 にする更新 + 区間和セグ木
    - zero(l, r): A[l:r] を 0 にする
    - sum(l, r): A[l:r] の総和
    - 点更新: point_set(i, v)
    """
    __slots__ = ("n", "size", "seg", "lazy")

    def __init__(self, n: int, init: list[int] | None = None) -> None:
        self.n = n
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.seg = [0] * (2 * size)
        self.lazy = [False] * (2 * size)  # True なら「この区間は全部 0」

        if init is not None:
            assert len(init) == n
            for i, v in enumerate(init):
                self.seg[size + i] = v
            for k in range(size - 1, 0, -1):
                self.seg[k] = self.seg[k * 2] + self.seg[k * 2 + 1]

    # 内部用: ノード k（[l, r)）を全部 0 にする
    def _apply_zero(self, k: int, l: int, r: int) -> None:
        self.seg[k] = 0
        self.lazy[k] = True

    # 内部用: lazy を子へ
    def _push(self, k: int, l: int, r: int) -> None:
        if not self.lazy[k] or r - l == 1:
            return
        m = (l + r) // 2
        self._apply_zero(k * 2, l, m)
        self._apply_zero(k * 2 + 1, m, r)
        self.lazy[k] = False

    # 内部用: 区間 [a, b) を 0 にする
    def _range_zero(self, a: int, b: int, k: int, l: int, r: int) -> None:
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self._apply_zero(k, l, r)
            return
        self._push(k, l, r)
        m = (l + r) // 2
        self._range_zero(a, b, k * 2, l, m)
        self._range_zero(a, b, k * 2 + 1, m, r)
        self.seg[k] = self.seg[k * 2] + self.seg[k * 2 + 1]

    def zero(self, l: int, r: int) -> None:
        """
        A[l:r] を 0 にする（0 <= l <= r <= n）
        """
        self._range_zero(l, r, 1, 0, self.size)

    # 内部用: 区間 [a, b) の和
    def _range_sum(self, a: int, b: int, k: int, l: int, r: int) -> int:
        if b <= l or r <= a:
            return 0
        if a <= l and r <= b:
            return self.seg[k]
        self._push(k, l, r)
        m = (l + r) // 2
        return (self._range_sum(a, b, k * 2, l, m)
                + self._range_sum(a, b, k * 2 + 1, m, r))

    def sum(self, l: int, r: int) -> int:
        """
        A[l:r] の総和
        """
        return self._range_sum(l, r, 1, 0, self.size)

    # 点更新（消したあとに復活させる用途など）
    def _point_set(self, i: int, val: int, k: int, l: int, r: int) -> None:
        if r - l == 1:
            self.seg[k] = val
            self.lazy[k] = False
            return
        self._push(k, l, r)
        m = (l + r) // 2
        if i < m:
            self._point_set(i, val, k * 2, l, m)
        else:
            self._point_set(i, val, k * 2 + 1, m, r)
        self.seg[k] = self.seg[k * 2] + self.seg[k * 2 + 1]

    def point_set(self, i: int, val: int) -> None:
        """
        A[i] = val にする
        """
        self._point_set(i, val, 1, 0, self.size)

    def get(self, i: int) -> int:
        return self.sum(i, i + 1)


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
for i in range(len(arrayData)):
    idxData[arrayData[i]] = i
result = []
seg = RangeZeroSum(len(arrayData))
for i in range(len(queryData)):
    n, x, y = queryData[i]
    if n == 1:
        idx = idxData.get(i + 1)
        seg.point_set(idx, i + 1)
    elif n == 2:
        l = idxData.get(x)
        r = idxData.get(y)
        l, r = min(l, r), max(l, r)
        result.append(seg.sum(l+1, r))
        seg.zero(l+1, r)
    else:
        raise Exception()
for r in result:
    print(r)
