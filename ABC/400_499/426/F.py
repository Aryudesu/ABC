from atcoder.lazysegtree import LazySegTree

class LazySegBase:
    def __init__(self, lst):
        self.lst = LazySegTree(self.op, self.e(), self.mapping, self.composition, self.id(), lst)

    def set(self, p, x): self.lst.set(p, x)
    def get(self, p): return self.lst.get(p)
    def prod(self, l, r): return self.lst.prod(l, r)
    def all_prod(self): return self.lst.all_prod()
    def apply(self, l, r, f): self.lst.apply(l, r, f)

class CustomLasySeg(LazySegBase):
    # (個数, 注文数)で管理？
    # 個数は全部足す．注文数も全部足す．
    def op(self, a, b):
        return (a[0] + b[0], a[1] + b[1])
    def mapping(self, f, x):
        return (max(0, x[0] - f), min(f, x[0]))
    def composition(self, a, b):
        return a + b
    def e(self):
        return (0, 0)
    def id(self):
        return 0

N = int(input())
A = [(int(l), 0) for l in input().split()]
lst = CustomLasySeg(A)
Q = int(input())
result = []
for q in range(Q):
    l, r, k = [int(i) - 1 for i in input().split()]
    lst.apply(l, r + 1, k + 1)
    result.append(lst.prod(l, r + 1))
for r in result:
    print(r)
