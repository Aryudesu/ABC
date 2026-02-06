from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
ft = FenwickTree(N + 1)
A = list(map(int, input().split()))
for i in range(N):
    ft.add(i, A[i])
result = []
for _ in range(Q):
    n, *query = map(int, input().split())
    if n == 1:
        x = query[0]
        a, b = A[x-1], A[x]
        ft.add(x-1, -a+b)
        ft.add(x, -b+a)
        A[x-1], A[x] = b, a
    elif n == 2:
        l, r = query
        result.append(ft.sum(l-1, r))
    else:
        raise Exception()
for r in result:
    print(r)
