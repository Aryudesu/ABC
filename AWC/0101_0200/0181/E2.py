from atcoder.segtree import SegTree

# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary

def rangeArgMin(st: SegTree, l: int, r: int) -> tuple[int, int]:
    mn = st.prod(l, r)
    return mn, st.max_right(l, lambda x: x > mn)

N, M, T = map(int, input().split())
st = SegTree(min, 10 ** 18, [0] * N)
memo = [0] * N
result = [0] * N
for _ in range(M):
    s, l, r = map(int, input().split())
    mn, index = rangeArgMin(st, l-1, r)
    st.set(index, mn + 1)
    if T - s >= 100:
        continue
    result[index] += 100 - (T - s)
print(*result)
