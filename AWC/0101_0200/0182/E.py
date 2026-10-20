# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary
class RangeZeroSumIter:
    """
    区間を 0 にする更新 + 区間和 セグ木
    - zero(l, r): A[l:r] = 0
    - sum(l, r): A[l:r] の総和
    - point_set(i, v): A[i] = v
    """
    __slots__ = ("n", "size", "log", "seg", "lazy")

    def __init__(self, n: int):
        self.n = n
        size = 1
        log = 0
        while size < n:
            size <<= 1
            log += 1
        self.size = size
        self.log = log
        self.seg = [0] * (2 * size)
        self.lazy = [False] * (2 * size)

    def _apply_zero(self, k: int):
        seg = self.seg
        lazy = self.lazy
        seg[k] = 0
        lazy[k] = True

    def _push_to_leaf(self, k: int):
        seg = self.seg
        lazy = self.lazy
        for h in range(self.log, 0, -1):
            p = k >> h
            if lazy[p]:
                c1 = p << 1
                c2 = c1 | 1
                seg[c1] = 0
                seg[c2] = 0
                lazy[c1] = True
                lazy[c2] = True
                lazy[p] = False

    def _recalc_from_leaf(self, k: int):
        seg = self.seg
        lazy = self.lazy
        k >>= 1
        while k:
            if not lazy[k]:
                seg[k] = seg[k << 1] + seg[(k << 1) | 1]
            k >>= 1

    def zero(self, l: int, r: int):
        """A[l:r] を 0 にする"""
        if l >= r:
            return
        size = self.size
        seg = self.seg
        lazy = self.lazy

        l += size
        r += size
        l0, r0 = l, r

        self._push_to_leaf(l0)
        self._push_to_leaf(r0 - 1)

        while l < r:
            if l & 1:
                seg[l] = 0
                lazy[l] = True
                l += 1
            if r & 1:
                r -= 1
                seg[r] = 0
                lazy[r] = True
            l >>= 1
            r >>= 1

        self._recalc_from_leaf(l0)
        self._recalc_from_leaf(r0 - 1)

    def sum(self, l: int, r: int) -> int:
        """A[l:r] の総和をとる"""
        if l >= r:
            return 0
        size = self.size
        seg = self.seg

        l += size
        r += size
        self._push_to_leaf(l)
        self._push_to_leaf(r - 1)

        res = 0
        while l < r:
            if l & 1:
                res += seg[l]
                l += 1
            if r & 1:
                r -= 1
                res += seg[r]
            l >>= 1
            r >>= 1
        return res

    def point_set(self, i: int, v: int):
        """A[i]にvを代入"""
        size = self.size
        k = i + size
        self._push_to_leaf(k)
        self.seg[k] = v
        self.lazy[k] = False
        self._recalc_from_leaf(k)


N, Q = map(int, input().split())
A = list(map(int, input().split()))
# 荷物個数
stNum = RangeZeroSumIter(N)
# 倉庫0に運ぶための費用
stCount = RangeZeroSumIter(N)
for n in range(N):
    a = A[n]
    stNum.point_set(n, a)
    stCount.point_set(n, a * n)

result = []
for _ in range(Q):
    res = 0
    l, r = map(int, input().split())
    mid = (l + r) // 2
    leftSum = stNum.sum(l, mid)
    leftCount = stCount.sum(l, mid)

    res += leftCount - leftSum * (l - 1)
    leftNum = stNum.sum(l-1, l) + leftSum
    stNum.point_set(l-1, leftNum)
    stCount.point_set(l-1, leftNum * (l-1))

    rightSum = stNum.sum(mid, r-1)
    rightCount = stCount.sum(mid, r-1)
    res += rightSum * (r - 1) - rightCount

    rightNum = stNum.sum(r-1, r) + rightSum
    stNum.point_set(r-1, rightNum)
    stCount.point_set(r-1, rightNum * (r-1))

    stNum.zero(l, r-1)
    stCount.zero(l, r-1)
    # debug1 = []
    # for idx in range(N):
    #     debug1.append(stNum.sum(idx,idx+1))
    # print(debug1)
    # debug2 = []
    # for idx in range(N):
    #     debug2.append(stCount.sum(idx,idx+1))
    # print(debug2)
    # print("===")
    result.append(res)
print(*result, sep="\n")
