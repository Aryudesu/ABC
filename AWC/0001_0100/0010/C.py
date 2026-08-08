from atcoder.dsu import DSU

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
dsu = DSU(N+1)
for i in range(1, N):
    if abs(A[i] - A[i-1]) <= K:
        dsu.merge(i + 1, i)
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    result.append("Yes" if dsu.same(l, r) else "No")
for r in result:
    print(r)
