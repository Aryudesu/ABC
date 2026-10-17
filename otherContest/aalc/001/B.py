from atcoder.lazysegtree import LazySegTree


class LazySegBase:
    def __init__(self, lst):
        self.lst = LazySegTree(
            self.op, self.e(), self.mapping, self.composition, self.id(), lst
        )

    def set(self, p, x):
        self.lst.set(p, x)

    def get(self, p):
        return self.lst.get(p)

    def prod(self, l, r):
        return self.lst.prod(l, r)

    def all_prod(self):
        return self.lst.all_prod()

    def apply(self, l, r, f):
        self.lst.apply(l, r, f)


class LazySegChmin(LazySegBase):
    """
    ACL LazySegTree 用設定:

    * op(a, b): セグメント木に乗る要素の二項演算
        例：min(a, b), max(a, b), a + b など
    * mapping(f, x): 遅延評価値 f を値 x に適用
        ex: "加算": f + x, "chmax": max(f, x), "代入": f
    * composition(f, g): 遅延値同士の合成（f を先に適用）
        ex: "加算": f + g, "代入": f（g を無視）
    * e(): 本体データの単位元
    * id(): 遅延データの単位元（影響を与えない値）
    """

    def op(self, a, b):
        return min(a, b)

    def mapping(self, f, x):
        return f + x

    def composition(self, f, g):
        return f + g

    def e(self):
        return (10**18)

    def id(self):
        return 0

N, Q = map(int, input().split())
A = list(map(int, input().split()))
st = LazySegChmin(A)
result = []
for _ in range(Q):
    n, *query = map(int, input().split())
    match n:
        case 1:
            l, r, x = query
            st.apply(l-1, r, x)
        case 2:
            l, r = query
            result.append(st.prod(l-1, r))
        case _:
            raise ValueError()
print(*result, sep="\n")
