from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
ft = FenwickTree(N)
DAVN = []
for n in range(N):
    a, d, v = map(int, input().split())
    DAVN.append((d, a, v, n))
DAVN.sort(reverse=True)

query = []
for q in range(Q):
    l, r, t = map(int, input().split())
    query.append((t, l, r, q))
query.sort()

results = []
for qry in query:
    t, l, r, n = qry
    while DAVN and DAVN[-1][0] <= t:
        d, a, v, m = DAVN.pop()
        ft.add(m, v * a)
    results.append((n, ft.sum(l-1, r)))
results.sort()
for n, r in results:
    print(r)
