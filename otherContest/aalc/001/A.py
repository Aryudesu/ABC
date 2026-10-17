from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
st = SegTree(min, 10**18, A)
result = []
for _ in range(Q):
    n, a, b = map(int, input().split())
    match n:
        case 1:
            i, x = a, b
            st.set(i-1, x)
        case 2:
            l, r = a, b
            result.append(st.prod(l-1, r))
        case _:
            raise ValueError()
print(*result, sep="\n")
