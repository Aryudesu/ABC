from atcoder.segtree import SegTree

def op(a, b):
    return max(a, b)

MAX = 500003
N, D = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
st = SegTree(op, 0, MAX)
result = 0
for a in A:
    M = st.prod(max(0, a - D), min(MAX, a + D + 1))
    st.set(a, M + 1)
    result = max(result, M + 1)
print(result)
