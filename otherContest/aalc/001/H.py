from atcoder.segtree import SegTree
from typing import Tuple

Item = Tuple[int, int, int]

def makeItem(num: int)->Item:
    return (num, 0, 0)

def op(a: Item, b: Item)->Item:
    aNum, aMod, aSum = a
    bNum, bMod, bSum = b
    if bNum == 0:
        return ()

N, Q = map(int, input().split())
A = list(map(int, input().split()))
data = [makeItem(a) for a in A]


for _ in range(Q):
    n, *query = map(int, input().split())
    match n:
        case 1:
            i, x = query

        case 2:
            l, r, x = query
        case _:
            raise ValueError()
