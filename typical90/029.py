from atcoder.lazysegtree import LazySegTree


class LazySegBase:
    def __init__(self, lst):
        self.lst = LazySegTree(self.op, self.e(), self.mapping, self.composition, self.id(), lst)

    def set(self, p, x): self.lst.set(p, x)
    def get(self, p): return self.lst.get(p)
    def prod(self, l, r): return self.lst.prod(l, r)
    def all_prod(self): return self.lst.all_prod()
    def apply(self, l, r, f): self.lst.apply(l, r, f)

class LazySegChmax(LazySegBase):
    def op(self, a, b): return max(a, b)
    def mapping(self, f, x): return max(f, x)
    def composition(self, f, g): return max(f, g)
    def e(self): return -10**10
    def id(self): return -10**10

W, N = [int(l) for l in input().split()]
ls = [0] * W
lst = LazySegChmax(ls)
data = []
result = []
for n in range(N):
    l, r = [int(l) - 1 for l in input().split()]
    h = lst.prod(l, r+1)
    if h < 0:
        h = 0
    lst.apply(l, r+1, h + 1)
    result.append(h + 1)
for r in result:
    print(r)
