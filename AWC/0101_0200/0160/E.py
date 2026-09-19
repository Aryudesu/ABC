from sortedcontainers import SortedSet
from sys import stdin
from bisect import bisect_left

class BitVector:
    """0/1 ビット列に対する rank 補助クラス"""

    __slots__ = ("block", "count", "zeros")

    W = 64

    def __init__(self, n: int):
        # i == n の rank にも対応するため +1 相当を確保
        m = (n >> 6) + 1
        self.block = [0] * m
        self.count = [0] * m
        self.zeros = 0

    def build(self) -> None:
        """各 block より前にある 1 の個数"""
        s = 0
        block = self.block
        count = self.count

        for i, b in enumerate(block):
            count[i] = s
            s += b.bit_count()

    def rank1(self, i: int) -> int:
        """[0, i) の 1 の数"""
        j = i >> 6
        k = i & 63
        return (
            self.count[j]
            + (self.block[j] & ((1 << k) - 1)).bit_count()
        )

    def rank0(self, i: int) -> int:
        """[0, i) の 0 の数"""
        return i - self.rank1(i)

    def get(self, i: int) -> int:
        return (self.block[i >> 6] >> (i & 63)) & 1


class WaveletMatrix:
    """
    静的整数列に対する Wavelet Matrix

    ・index は 0-origin
    ・区間は [l, r)
    ・内部では座標圧縮を行う
    """

    __slots__ = ("n", "a", "values", "lg", "bv")

    def __init__(self, a: list[int] | int):
        if isinstance(a, int):
            self.n = a
            self.a = [0] * a
            self.values = []
            self.lg = 0
            self.bv = []
        else:
            self.a = list(a)
            self.n = len(self.a)
            self.build()

    def build(self) -> None:
        n = self.n

        if n == 0:
            self.values = []
            self.lg = 0
            self.bv = []
            return

        # --------------------------------
        # 座標圧縮
        # --------------------------------
        values = sorted(set(self.a))
        self.values = values

        rank = {v: i for i, v in enumerate(values)}
        cur = [rank[v] for v in self.a]

        # 値そのものではなく distinct 数だけ見ればよい
        lg = max((len(values) - 1).bit_length(), 1)
        self.lg = lg

        bv = [None] * lg

        # --------------------------------
        # Wavelet Matrix 構築
        # --------------------------------
        for h in range(lg - 1, -1, -1):
            bvh = BitVector(n)
            block = bvh.block

            zero = []
            one = []

            append0 = zero.append
            append1 = one.append

            # bitvector 構築と stable partition を同時に行う
            for i, v in enumerate(cur):
                if (v >> h) & 1:
                    block[i >> 6] |= 1 << (i & 63)
                    append1(v)
                else:
                    append0(v)

            bvh.zeros = len(zero)
            bvh.build()

            zero.extend(one)
            cur = zero

            bv[h] = bvh

        self.bv = bv

    def rebuild(self) -> None:
        """サイズ指定モードで a を設定した後に呼ぶ"""
        self.build()

    def access(self, k: int) -> int:
        """
        元配列を保持しているので O(1)。

        Wavelet Matrix を辿る必要はない。
        """
        assert 0 <= k < self.n
        return self.a[k]

    # =========================================================
    # 内部用
    # =========================================================

    def _kthRank(self, l: int, r: int, k: int) -> int:
        """圧縮後の rank で k-th smallest"""
        res = 0
        bv = self.bv

        for h in range(self.lg - 1, -1, -1):
            bvh = bv[h]

            block = bvh.block
            count = bvh.count

            # rank1(l)
            lj = l >> 6
            lk = l & 63
            l1 = (
                count[lj]
                + (block[lj] & ((1 << lk) - 1)).bit_count()
            )

            # rank1(r)
            rj = r >> 6
            rk = r & 63
            r1 = (
                count[rj]
                + (block[rj] & ((1 << rk) - 1)).bit_count()
            )

            l0 = l - l1
            r0 = r - r1

            cnt0 = r0 - l0

            if k < cnt0:
                l = l0
                r = r0
            else:
                k -= cnt0
                res |= 1 << h

                z = bvh.zeros
                l = z + l1
                r = z + r1

        return res

    def _rangeFreqRank(
        self,
        l: int,
        r: int,
        upper: int,
    ) -> int:
        """
        圧縮後の rank について
        [l, r) 内で rank < upper の個数
        """

        if upper <= 0:
            return 0

        if upper >= len(self.values):
            return r - l

        cnt = 0
        bv = self.bv

        for h in range(self.lg - 1, -1, -1):
            bvh = bv[h]

            block = bvh.block
            count = bvh.count

            # rank1(l)
            lj = l >> 6
            lk = l & 63
            l1 = (
                count[lj]
                + (block[lj] & ((1 << lk) - 1)).bit_count()
            )

            # rank1(r)
            rj = r >> 6
            rk = r & 63
            r1 = (
                count[rj]
                + (block[rj] & ((1 << rk) - 1)).bit_count()
            )

            l0 = l - l1
            r0 = r - r1

            if (upper >> h) & 1:
                cnt += r0 - l0

                z = bvh.zeros
                l = z + l1
                r = z + r1
            else:
                l = l0
                r = r0

        return cnt

    # =========================================================
    # Public API
    # =========================================================

    def kthSmallest(
        self,
        l: int,
        r: int,
        k: int,
    ) -> int:
        """[l, r) の k 番目の最小値 (0-index)"""

        assert 0 <= l <= r <= self.n
        assert 0 <= k < r - l

        rank = self._kthRank(l, r, k)
        return self.values[rank]

    def kthLargest(
        self,
        l: int,
        r: int,
        k: int,
    ) -> int:
        """[l, r) の k 番目の最大値 (0-index)"""

        return self.kthSmallest(
            l,
            r,
            r - l - 1 - k,
        )

    def rangeFreq(
        self,
        l: int,
        r: int,
        upper: int,
    ) -> int:
        """[l, r) で x < upper の個数"""

        assert 0 <= l <= r <= self.n

        upperRank = bisect_left(self.values, upper)

        return self._rangeFreqRank(
            l,
            r,
            upperRank,
        )

    def rangeFreqRange(
        self,
        l: int,
        r: int,
        lower: int,
        upper: int,
    ) -> int:
        """[l, r) で lower <= x < upper の個数"""

        lowerRank = bisect_left(self.values, lower)
        upperRank = bisect_left(self.values, upper)

        return (
            self._rangeFreqRank(l, r, upperRank)
            - self._rangeFreqRank(l, r, lowerRank)
        )

    def prevValue(
        self,
        l: int,
        r: int,
        upper: int,
    ) -> int:
        """upper 未満の最大値"""

        upperRank = bisect_left(self.values, upper)
        cnt = self._rangeFreqRank(l, r, upperRank)

        if cnt == 0:
            return -1

        rank = self._kthRank(l, r, cnt - 1)
        return self.values[rank]

    def nextValue(
        self,
        l: int,
        r: int,
        lower: int,
    ) -> int:
        """lower 以上の最小値"""

        lowerRank = bisect_left(self.values, lower)
        cnt = self._rangeFreqRank(l, r, lowerRank)

        if cnt == r - l:
            return -1

        rank = self._kthRank(l, r, cnt)
        return self.values[rank]

readline = stdin.readline
N = int(readline())
C = []
HN = []
LR = [None] * N
for n in range(N):
    c, h = map(int, readline().split())
    C.append(c)
    HN.append((h, n))
HN.sort(reverse=True)
data = SortedSet()
data.add(-1)
data.add(N+1)
result = 0
wm = WaveletMatrix(C)
for h, n in HN:
    data.add(n)
    idx = data.index(n)
    l = data[idx-1]
    r = data[idx+1]
    lIdx = l if l > -1 else -1
    rIdx = N if N < r else r
    res = wm.rangeFreq(lIdx+1, rIdx, C[n]+1) - wm.rangeFreq(lIdx+1, rIdx, C[n]) - 1
    result += res
print(result)
