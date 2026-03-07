from atcoder.segtree import SegTree

def getMaxMinIdx(M: int, num: int, st: SegTree):
    if st.all_prod() < num:
        return M
    l = -1
    r = M-1
    while r - l > 1:
        m = (l + r) // 2
        tmp = st.prod(0, m + 1)
        if tmp < num:
            l = m
        else:
            r = m
    return r

N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))
st = SegTree(max, -1, C)
result = 0
for w in W:
    idx = getMaxMinIdx(M, w, st)
    if idx == M:
        continue
    st.set(idx, -1)
    result += 1
print(result)
