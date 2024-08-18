import bisect


class bisectMapper:
    """bisectを個人的にわかりやすいようにしたかったやつ"""
    def __init__(self, A = [], sort=True) -> None:
        self.data = A
        if sort and len(A) > 0:
            self.data.sort()
        self.N = len(A)

    def set_data(self, A):
        """データをセットし直します"""
        self.data = A
        self.N = len(A)

    def data_leq(self, a):
        """
        a以下のデータの最大のインデックスを取得します．
        aがデータ内の最小値より小さければ-1を返却します．
        """
        tmp = bisect.bisect_right(self.data, a)
        if tmp == self.N:
            return self.N - 1
        return tmp if self.data[tmp] == a else tmp - 1

    def data_geq(self, a):
        """
        a以上のデータの最小のインデックスを取得します
        aがデータ内の最大値より大きければNを返却します．
        """
        tmp = bisect.bisect_left(self.data, a)
        if tmp == -1:
            return 0
        return bisect.bisect_left(self.data, a)

    def data_l(self, a):
        """
        a未満のデータの最大のインデックスを取得します．
        aがデータ内の最大値より大きければN，小さければ-1を返却します．
        """
        tmpl = self.data_leq(a)
        tmpr = self.data_geq(a)
        # 枠からはみ出た場合
        if tmpl == -1:
            return tmpl
        if tmpl == self.N:
            return self.N - 1
        # ちょうどのデータだった場合
        if self.data[tmpl] == a:
            return tmpr - 1
        return tmpl

    def data_g(self, a):
        """
        a超過のデータの最小のインデックスを取得します
        aがデータ内の最大値より大きければN，小さければ0を返却します．
        """
        tmpl = self.data_leq(a)
        tmpr = self.data_geq(a)
        # 枠からはみ出た場合
        if tmpr == self.N:
            return tmpr
        # ちょうどのデータだった場合
        if self.data[tmpr] == a:
            return tmpl + 1
        return tmpr

    def between_c_c(self, a, b):
        """a以上b以下のデータの個数を取得します"""
        # a以下となる最大のインデックス
        tmp = self.data_geq(a)
        # はみ出た結果の場合
        if tmp == -1:
            tmp = 0
        if tmp == self.N:
            tmp = self.N - 1
        if self.data[tmp] < a:
            tmp += 1
        tmpl = tmp
        # b以上となる最小のインデックス
        tmp = self.data_leq(b)
        if tmp == -1:
            tmp = 0
        if tmp == self.N:
            tmp = self.N - 1
        if self.data[tmp] > b:
            tmp -= 1
        tmpr = tmp
        return tmpr - tmpl + 1

    def between_c_o(self, a, b):
        """a以上b未満のデータの個数を取得します"""
        # a以下となる最大のインデックス
        tmp = self.data_geq(a)
        # はみ出た結果の場合
        if tmp == -1:
            tmp = 0
        if tmp == self.N:
            tmp = self.N - 1
        if self.data[tmp] < a:
            tmp += 1
        tmpl = tmp
        # b超過となる最小のインデックス
        tmp = self.data_l(b)
        if tmp == -1:
            tmp = 0
        if tmp == self.N:
            tmp = self.N - 1
        tmpr = tmp
        return tmpr - tmpl + 1

    def between_o_c(self, a, b):
        """a超過b以下のデータの個数を取得します"""
        # a超過となる最大のインデックス
        tmp = self.data_g(a)
        # はみ出た結果の場合
        if tmp == -1:
            tmp = 0
        if tmp == self.N:
            tmp = self.N - 1
        tmpl = tmp
        # b以上となる最小のインデックス
        tmp = self.data_geq(b)
        if tmp == -1:
            tmp = 0
        if tmp == self.N:
            tmp = self.N - 1
        if self.data[tmp] > b:
            tmp -= 1
        tmpr = tmp
        return tmpr - tmpl + 1

    def between_o_o(self, a, b):
        """a超過b未満のデータの個数を取得します"""
        # a以下となる最大のインデックス
        tmp = self.data_g(a)
        # はみ出た結果の場合
        if tmp == -1:
            tmp = 0
        if tmp == self.N:
            tmp = self.N - 1
        tmpl = tmp
        # b超過となる最小のインデックス
        tmp = self.data_l(b)
        if tmp == -1:
            tmp = 0
        if tmp == self.N:
            tmp = self.N - 1
        tmpr = tmp
        return tmpr - tmpl + 1

def is_ok(mid, N, M, B, bm: bisectMapper):
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
    bm = bisectMapper(A)
    l, r = search_result(N, M, B, bm)
    return l

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print(calc(N, M, A))
