from atcoder.segtree import SegTree
from sortedcontainers import SortedSet
from collections import defaultdict

N, Q, K = map(int, input().split())
A = list(map(int, input().split()))
data = defaultdict(SortedSet)
st = SegTree(max, 0, N-1)
for n in range(N-1):
    d = abs(A[n] - A[n+1])
    st.set(n, d)
    data[d].add(n)

result = []
for _ in range(Q):
    n, a, b = map(int, input().split())
    match n:
        case 1:
            p, v = a-1, b
            prev = A[p]
            A[p] = v
            if p+1 < N:
                pd = abs(prev - A[p+1])
                nd = abs(v - A[p+1])
                data[pd].discard(p)
                data[nd].add(p)
                st.set(p, nd)
            if p-1 >= 0:
                pd = abs(A[p-1] - prev)
                nd = abs(A[p-1] - v)
                data[pd].discard(p-1)
                data[nd].add(p-1)
                st.set(p-1, nd)
        case 2:
            l, r = a-1, b-1
            M1 = st.prod(l, r)
            if M1 <= K:
                result.append(M1)
            else:
                idx = data[M1].bisect_left(l)
                targetIdx = data[M1][idx]
                M2 = 0
                if l <= targetIdx:
                    M2 = st.prod(l, targetIdx)
                M3 = 0
                if targetIdx + 1 <= r:
                    M3 = st.prod(targetIdx+1, r)
                result.append(max(M2, M3))
        case _:
            raise ValueError()
print(*result, sep="\n")
