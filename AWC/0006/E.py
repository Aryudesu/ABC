from atcoder.fenwicktree import FenwickTree

# いらっしゃ～い
N, Q = map(int, input().split())
S = list(map(int, input().split()))
ft = FenwickTree(N + 3)
for n in range(N):
    ft.add(n, S[n])

result = []
for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        L, R = b, c
        result.append(ft.sum(L-1, R))
    elif a == 2:
        X, V = b, c
        tmp = S[X-1]
        S[X-1] = V
        ft.add(X-1, -tmp + V)
    else:
        raise ValueError()
for r in result:
    print(r)
