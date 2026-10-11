from typing import Tuple
from atcoder.segtree import SegTree

def op(a: Tuple[int, int], b: Tuple[int, int])->Tuple[int, int]:
    a1, a2 = a
    b1, b2 = b
    if a1 > b1:
        return (a1, max(b1, a2))
    else:
        return (b1, max(a1, b2))

N, Q, K = map(int, input().split())
A = list(map(int, input().split()))
st = SegTree(op, (0, 0), N-1)
for n in range(N-1):
    d = abs(A[n] - A[n+1])
    st.set(n, (d, 0))

result = []
for _ in range(Q):
    n, a, b = map(int, input().split())
    match n:
        case 1:
            p, v = a-1, b
            A[p] = v
            if 0 <= p-1:
                d = abs(A[p-1] - A[p])
                st.set(p-1, (d, 0))
            if p+1 < N:
                d = abs(A[p] - A[p+1])
                st.set(p, (d, 0))
        case 2:
            l, r = a-1, b-1
            M1, M2 = st.prod(l, r)
            result.append(M1 if M1 <= K else M2)
        case _:
            raise ValueError()
print(*result, sep="\n")
