from atcoder.fenwicktree import FenwickTree

M, S = map(int, input().split())
B = list(map(int, input().split()))
for m in range(M):
    B[m] += S//M
for r in range(S%M):
    B[r] += 1
ft = FenwickTree(M)
for m in range(M):
    ft.add(m, B[m])

result = []
N = int(input())
for n in range(N):
    l, r = map(int, input().split())
    result.append(ft.sum(l-1, r))
for r in result:
    print(r)
