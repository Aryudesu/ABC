from atcoder.segtree import SegTree

# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary
def calcIndex(mn: int, st: SegTree, left: int, right: int)->int:
    l = left - 1
    r = right + 1
    while r - l > 1:
        mid = (r + l) // 2
        if st.prod(left, mid + 1) <= mn:
            r = mid
        else:
            l = mid
    return r


N, M, T = map(int, input().split())
st = SegTree(min, 10 ** 18, [0] * N)
memo = [0] * N
result = [0] * N
for _ in range(M):
    s, l, r = map(int, input().split())
    mn = st.prod(l-1, r)
    index = calcIndex(mn, st, l-1, r-1)
    st.set(index, mn + 1)
    if T - s >= 100:
        continue
    result[index] += 100 - (T - s)
print(*result)
