from atcoder.segtree import SegTree

INF = 10**18
N = int(input())
H = list(map(int, input().split()))
result = 0
st = SegTree(min, INF, H)
data = [(INF, N)]
data.append((H[-1], N-1))
for idx in range(N-2, -1, -1):
    h = H[idx]
    while data[-1][0] <= h:
        data.pop()
    j = data[-1][1]
    if j < N:
        result += st.prod(idx, j+1)
    data.append((h, idx))
    # print(data)
print(result)
