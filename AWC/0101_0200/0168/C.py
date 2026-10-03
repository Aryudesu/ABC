from atcoder.dsu import DSU

N, K = map(int, input().split())
dsu = DSU(N)
count = 0
for _ in range(N):
    a, b = map(int, input().split())
    count += dsu.same(a-1, b-1)
    dsu.merge(a-1, b-1)
print("Yes" if count <= K else "No")
