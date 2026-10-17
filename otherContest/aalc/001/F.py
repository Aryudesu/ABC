from atcoder.segtree import SegTree
from typing import Tuple

Item = Tuple[int, int, int, int, int, int]
def op(a: Item, b: Item)->Item:
    Ares, Alen, LAitem, LAnum, RAitem, RAnum = a
    Bres, Blen, LBitem, LBnum, RBitem, RBnum = b
    # a bの順番？
    Mres = max(Ares, Bres)
    if RAitem == LBitem:
        Mres = max(RAnum + LBnum, Mres)
    if LAitem == RAitem == LBitem == RBitem and Alen == LAnum and Blen == LBnum:
        newNum = LAnum + RBnum
        return (max(Mres, newNum), Alen + Blen, LAitem, newNum, RBitem, newNum)
    if LAitem == RAitem == LBitem and Alen == LAnum:
        newNum = LAnum + LBnum
        return (max(Mres, newNum), Alen + Blen, LAitem, newNum, RBitem, RBnum)
    if RAitem == LBitem == RBitem and Blen == LBnum:
        newNum = RAnum + LBnum
        return (max(Mres, newNum), Alen + Blen, LAitem, LAnum, RBitem, newNum)
    return (Mres, Alen + Blen, LAitem, LAnum, RBitem, RBnum)

def e()->Item:
    return (0, 0, 0, 0, 0, 0)

def makeItem(num: int)->Item:
    return (1, 1, num, 1, num, 1)

N, Q = map(int, input().split())
A = list(map(int, input().split()))
data = []
for a in A:
    data.append(makeItem(a))
st = SegTree(op, e(), data)
result = []
for _ in range(Q):
    n, a, b = map(int, input().split())
    match n:
        case 1:
            i, x = a, b
            st.set(i-1, makeItem(x))
        case 2:
            l, r = a, b
            res = st.prod(l-1, r)
            result.append(res[0])
        case _:
            raise ValueError()
print(*result, sep="\n")
