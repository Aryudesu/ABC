from atcoder.lazysegtree import LazySegTree

def op(a, b):
    return (a[0] + b[0], a[1] + b[1])
def mapping(a, b):
    return (b[0] + a*b[1], b[1])
def composition(a, b):
    return a + b

N, Q = map(int, input().split())
C = list(map(int, input().split()))
data = []
for c in C:
    data.append((c, 1))
st = LazySegTree(op, (0, 0), mapping, composition, 0, data)
result = []
for _ in range(Q):
    n, *query = list(map(int, input().split()))
    if n == 1:
        l, r, v = query
        st.apply(l-1, r, v)
    elif n == 2:
        l, r = query
        result.append(st.prod(l-1, r)[0])
    else:
        raise ValueError()
for r in result:
    print(r)

