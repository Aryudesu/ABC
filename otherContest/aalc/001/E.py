from atcoder.segtree import SegTree
from typing import Tuple

Item = Tuple[int, int, int, int, int, int]
MOD = 998244353
def op(a: Item, b: Item)->Item:
    Argb, Ar, Ag, Ab, Arg, Agb = a
    Brgb, Br, Bg, Bb, Brg, Bgb = b
    rgb = ((Argb + Brgb) + (Ar * Bgb) + (Arg * Bb)) % MOD
    return (rgb, (Ar + Br)%MOD, (Ag + Bg)%MOD, (Ab + Bb)%MOD, (Arg + Brg + Ar * Bg)%MOD, (Agb + Bgb + Ag * Bb)%MOD)

def e()->Item:
    return (0, 0, 0, 0, 0, 0)

def makeItem(s: str, num: int)->Item:
    match s:
        case "R":
            return (0, num%MOD, 0, 0, 0, 0)
        case "G":
            return (0, 0, num%MOD, 0, 0, 0)
        case "B":
            return (0, 0, 0, num%MOD, 0, 0)
        case _:
            raise ValueError()

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = input()
data = []
for idx in range(N):
    data.append(makeItem(S[idx], A[idx]))
result = []
st = SegTree(op, e(), data)
for _ in range(Q):
    n, a, b = map(int, input().split())
    match n:
        case 1:
            i, x = a-1, b
            st.set(i, makeItem(S[i], x))
        case 2:
            l, r = a, b
            res = st.prod(l-1, r)
            result.append(res[0])
        case _:
            raise ValueError()
print(*result, sep="\n")
