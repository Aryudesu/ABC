from atcoder.segtree import SegTree
from typing import Tuple

Item = Tuple[int, int, int, int, int]

def op(b: Item, a: Item)->Item:
    Ares, Azero, Aone, Atwo = a
    Bres, Bzero, Bone, Btwo = b
    res = (Ares + Bres) + (Azero * (Bone + Btwo)) + (Aone * Btwo)
    return (res, Azero + Bzero, Aone + Bone, Atwo + Btwo)

def e()->Item:
    return (0, 0, 0, 0)

def makeItem(num: int)->Item:
    match num:
        case 0:
            return (0, 1, 0, 0)
        case 1:
            return (0, 0, 1, 0)
        case 2:
            return (0, 0, 0, 1)
        case _:
            raise ValueError()

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
