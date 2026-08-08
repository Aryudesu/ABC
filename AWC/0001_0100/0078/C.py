from atcoder.fenwicktree import FenwickTree

N = int(input())
L = list(map(int, input().split()))
ft = FenwickTree(N)
lData = []
for i in range(N):
    lData.append((L[i], i))
    ft.add(i, 1)
lData.sort(reverse=True)
result = []
for i in range(N):
    l, n = lData.pop()
    res = ft.sum(0, n + 1)
    ft.add(n, -1)
    result.append(res)
for r in result:
    print(r)
