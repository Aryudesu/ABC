from atcoder.lazysegtree import LazySegTree


class LSTTemplate:
    # 区間に対する最大値の単位元
    e = -(10**10)
    # 区間に対する変更の単位元
    id = -(10**10)

    # 区間に対する演算
    def op(self, ele1, ele2):
        return max(ele1, ele2)

    # 区間の遅延評価
    # data[p] = mapping(data[p], ele2)
    def mapping(self, data, ele2):
        return max(data, ele2)

    # 区間同士の遅延評価同士の計算
    def composition(self, f, g):
        return max(f, g)

    # data[p] = x
    def set(self, p, x):
        self.lst.set(p, x)

    # return data[p]
    def get(self, p):
        return self.lst.get(p)

    # op(data[l], data[l+1], ..., data[r-1])
    def prod(self, l, r):
        return self.lst.prod(l, r)

    # op(data[0], ..., data[n-1])
    def all_prod(self):
        return self.lst.all_prod()

    # data[l] ～ data[r-1]に対しmapping(data[i], p)を計算
    def apply(self, l, r, p):
        self.lst.apply(l, r, p)

    def __init__(self, lst):
        self.lst = LazySegTree(self.op, self.e, self.mapping, self.composition, self.id, lst)

H, W, N = [int(l) for l in input().split()]
ls = [0] * W
lst = LSTTemplate(ls)
data = []
for n in range(N):
    tmp = [int(l) for l in input().split()]
    tmp[1] -= 1
    tmp.append(n)
    data.append(tmp)
data.sort(reverse=True)
result = []
for dat in data:
    y, x, l, num = dat
    h = lst.prod(x, x + l)
    lst.apply(x, x + l, h + 1)
    result.append([num, H - h])
result.sort()
for r in result:
    print(r[1])
