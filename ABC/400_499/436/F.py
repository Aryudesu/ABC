from atcoder.fenwicktree import FenwickTree

N = int(input())
B = list(map(int, input().split()))
data = dict()
for i in range(N):
    data[B[i]] = i
ft = FenwickTree(N)
for i in range(N):
    ft.add(i, 1)
result = 0
for i in range(N):
    idx = data[N - i]
    B[idx] = 0
    ft.add(idx, -1)
    l = ft.sum(0, idx)
    r = ft.sum(idx, N)
    result += l*r
result += (N*(N+1))//2
print(result)
