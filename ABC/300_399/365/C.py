import bisect
from collections.abc import Iterable
from typing import List, Optional


class BisectMapper:
    """
    bisect のマッパ
    self.data はソート済み前提
    """

    def __init__(self, data: Optional[Iterable[int]] = None, *, sort: bool = True) -> None:
        if data is None:
            self.data: List[int] = []
        else:
            self.data = list(data)
            if sort:
                self.data.sort()
        self.N = len(self.data)

    def _refresh_size(self) -> None:
        self.N = len(self.data)

    def set_data(self, data: Iterable[int], *, sort: bool = True) -> None:
        """データを入れ替える（必要ならソート）"""
        self.data = list(data)
        if sort:
            self.data.sort()
        self._refresh_size()

    # ------- インデックス -------

    def data_leq(self, x: int) -> int:
        """
        x 以下で最大の要素のインデックスを返す。
        該当要素がなければ -1。
        """
        i = bisect.bisect_right(self.data, x) - 1
        return i  # -1 ～ N-1

    def data_geq(self, x: int) -> int:
        """
        x 以上で最小の要素のインデックスを返す。
        該当要素がなければ N。
        """
        i = bisect.bisect_left(self.data, x)
        return i  # 0 ～ N

    def data_lt(self, x: int) -> int:
        """
        x 未満で最大の要素のインデックスを返す。
        該当要素がなければ -1。
        """
        i = bisect.bisect_left(self.data, x) - 1
        return i  # -1 ～ N-1

    def data_gt(self, x: int) -> int:
        """
        x 超過で最小の要素のインデックスを返す。
        該当要素がなければ N。
        """
        i = bisect.bisect_right(self.data, x)
        return i  # 0 ～ N

    data_l = data_lt
    data_g = data_gt

    # ------- 区間カウント -------

    def _count_between(self, a: int, b: int, left_closed: bool, right_closed: bool) -> int:
        """
        汎用: (left_closed ? [a : ) : (a : ) と、
              (right_closed ? : b] : : b) の間の要素数。
        """
        if a > b:
            return 0

        if left_closed:
            left = bisect.bisect_left(self.data, a)
        else:
            left = bisect.bisect_right(self.data, a)

        if right_closed:
            right = bisect.bisect_right(self.data, b)
        else:
            right = bisect.bisect_left(self.data, b)

        if right < left:
            return 0
        return right - left

    def between_c_c(self, a: int, b: int) -> int:
        """[a, b] に含まれる要素数"""
        return self._count_between(a, b, left_closed=True, right_closed=True)

    def between_c_o(self, a: int, b: int) -> int:
        """[a, b) に含まれる要素数"""
        return self._count_between(a, b, left_closed=True, right_closed=False)

    def between_o_c(self, a: int, b: int) -> int:
        """(a, b] に含まれる要素数"""
        return self._count_between(a, b, left_closed=False, right_closed=True)

    def between_o_o(self, a: int, b: int) -> int:
        """(a, b) に含まれる要素数"""
        return self._count_between(a, b, left_closed=False, right_closed=False)

def is_ok(mid, N, M, B, bm: BisectMapper):
    # 予算以上になる人の最小のindexを取得
    # mid以上の人込みで考える
    idx = bm.data_geq(mid)
    s = 0
    # 全員x未満である場合
    if idx == N:
        # 全員の総和がそれになる
        s += B[-1]
    else:
        if idx > 0:
            # x未満の人の総和
            s += B[idx - 1]
        # x以上の人はminで考える
        s += mid * (N - idx)
    return s <= M


def search_result(N, M, B, bm):
    """
    左側に対しての判定で二分探索実行
    ===
    return (条件を満たす中で最大, 条件を満たさない中で最小)
    """
    l = -1
    r = 10**9 + 1
    while r - l > 1:
        mid = (l + r) // 2
        if is_ok(mid, N, M, B, bm):
            l = mid
        else:
            r = mid
    return l, r

def calc(N, M, A):
    if sum(A) <= M:
        return "infinite"
    B = []
    s = 0
    for a in A:
        s += a
        B.append(s)
    bm = BisectMapper(A)
    l, r = search_result(N, M, B, bm)
    return l

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
print(calc(N, M, A))
