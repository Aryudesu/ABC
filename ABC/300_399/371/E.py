from atcoder.segtree import SegTree


def op(a: set, b: set):
    return b + a

N = int(input())
A = [set(int(l)) for l in input().split()]
seg = SegTree(op, set(), A)
memo = set()
data = []

