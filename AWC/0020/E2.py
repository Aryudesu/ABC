from atcoder.segtree import SegTree

N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))
st = SegTree(max, -1, C)
result = 0
for w in W:
    idx = st.max_right(0, lambda x: x < w)
    if idx == M:
        continue
    st.set(idx, -1)
    result += 1
print(result)
