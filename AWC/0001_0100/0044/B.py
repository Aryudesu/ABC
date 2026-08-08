from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
ft = FenwickTree(N)
for i in range(N):
    ft.add(i, A[i])

result = []
for _ in range(Q):
    l, r = map(int, input().split())
    result.append(ft.sum(l-1, r))

for r in result:
    print(r)
