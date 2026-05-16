from atcoder.segtree import SegTree

INF = 10 ** 18
N = int(input())
B = list(map(int, input().split()))
st = SegTree(min, INF, N)

s = B[0]
maIdx = 0
oneMax = B[0]
ruiseki = [0] * N
ruiseki[0] = B[0]
result = [B[0]]
st.set(0, B[0])
for i in range(1, N):
    s += B[i]
    ruiseki[i] = s
    if s > ruiseki[maIdx]:
        maIdx = i
    oneMax = max(oneMax, B[i])
    st.set(i, s)
    mi = 0
    if maIdx > 0:
        mi = min(0, st.prod(0, maIdx))
    result.append(max(ruiseki[maIdx] - mi, oneMax))
    # print(ruiseki)
for r in result:
    print(r)
