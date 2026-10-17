from atcoder.segtree import SegTree

def op(a: int, b: int)->int:
    return a + b

N, Q = map(int, input().split())
A = list(map(int, input().split()))
st = SegTree(op, 0, A)
result = []
for _ in range(Q):
    n, a, b = map(int, input().split())
    match n:
        case 1:
            i, x = a, b
            st.set(i-1, x)
        case 2:
            l, t = a, b
            tmp = st.prod(l-1, N)
            if tmp < t:
                result.append(N+1)
                continue
            result.append(st.max_right(l-1, lambda x:x < t) + 1)
        case 3:
            r, t = a, b
            tmp = st.prod(0, r)
            if tmp < t:
                result.append(0)
                continue
            result.append(st.min_left(r, lambda x:x < t))
        case _:
            raise ValueError()
print(*result, sep="\n")
