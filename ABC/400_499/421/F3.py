import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

class RangeZeroSumIter:
    """
    区間を 0 にする更新 + 区間和 セグ木（非再帰・PyPy向け）
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
                # 子に 0 適用
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

        # 遅延伝播
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
        """A[l:r] の総和"""
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
        """A[i] = v"""
        size = self.size
        k = i + size
        self._push_to_leaf(k)
        self.seg[k] = v
        self.lazy[k] = False
        self._recalc_from_leaf(k)


def main():
    Q = int(input())

    # --- 連結リスト（配列版）で最終形の順序だけ先に決める ---
    # 値は 0..Q まで使い得る
    prev = [-1] * (Q + 1)
    nxt = [-1] * (Q + 1)
    head = 0  # 先頭の値
    # 0 の初期ノードはすでにあるとみなす（prev[0] = -1, nxt[0] 初期は -1）

    queryData = []  # (type, x, y) で保存

    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            _, x = q
            v = i + 1  # 挿入される値
            queryData.append((1, x, 0))
            # x の直後に v を挿入
            nx = nxt[x]
            nxt[x] = v
            prev[v] = x
            nxt[v] = nx
            if nx != -1:
                prev[nx] = v
        else:
            _, x, y = q
            queryData.append((2, x, y))

    # --- 最終的な並びを配列にする ---
    arrayData = []
    cur = head
    while cur != -1:
        arrayData.append(cur)
        cur = nxt[cur]

    n = len(arrayData)

    # 値 -> index
    idxData = [0] * (Q + 1)
    for i, v in enumerate(arrayData):
        idxData[v] = i

    # --- 区間ゼロセグ木でシミュレーション ---
    seg = RangeZeroSumIter(n)
    result = []
    append_res = result.append

    for i, (typ, x, y) in enumerate(queryData):
        if typ == 1:
            pos = idxData[i + 1]
            seg.point_set(pos, i + 1)
        else:
            l = idxData[x]
            r = idxData[y]
            if l > r:
                l, r = r, l
            s = seg.sum(l + 1, r)
            append_res(s)
            seg.zero(l + 1, r)

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
