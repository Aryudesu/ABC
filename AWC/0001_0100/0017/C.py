from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
C = list(map(int, input().split()))
ft = FenwickTree(N-1)
# デバッグ用
data = []
for i in range(N-1):
    if C[i] == C[i+1]:
        ft.add(i, 1)
        data.append(1)
    else:
        ft.add(i, 0)
        data.append(0)
# print(data)
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    result.append(ft.sum(l-1, r-1))

for r in result:
    print(r)
