from atcoder.fenwicktree import FenwickTree

N, M = map(int, input().split())
S = list(map(int, input().split()))
ft = FenwickTree(N)
for i in range(N):
    ft.add(i, 1)
result = []
for i in range(M):
    pos = S[i] - 1
    ft.add(pos, -1)
    result.append(ft.sum(0, pos))
for r in result:
    print(r + 1)
